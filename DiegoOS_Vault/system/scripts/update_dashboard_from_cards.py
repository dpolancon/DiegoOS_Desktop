#!/usr/bin/env python3
import argparse
import csv
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta

try:
    import yaml
except ImportError:
    yaml = None


FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
INACTIVE_STATUSES = {
    "test",
    "archived",
    "archive",
    "inactive",
    "parked",
    "done",
    "closed",
    "rejected",
}
STABLE_STATUSES = {"stabilized", "submitted", "done", "closed"}
PRIORITY_RANK = {"critical": 0, "high": 1, "standard": 2, "low": 3}


@dataclass
class CardRecord:
    path: str
    rel_path: str
    metadata: dict = field(default_factory=dict)
    parse_error: str = ""
    card_class: str = "unknown"
    card_id: str = ""
    project_id: str = ""
    card_type: str = ""
    status: str = ""
    state: str = ""
    priority: str = "standard"
    dashboard_visible: bool = True
    lane: str = ""
    institution: str = ""
    role: str = ""
    materials_status: str = ""
    conceptual_anchor: str = ""
    portal_deadline: date | None = None
    freeze_date: date | None = None
    next_action: str = "N/A"
    next_action_date: str = ""
    action_status: str = ""
    included: bool = False
    skipped: bool = False
    skip_reason: str = ""
    repair_needed: bool = False
    problems: list[str] = field(default_factory=list)
    suggested_fixes: list[str] = field(default_factory=list)
    is_test: bool = False


def is_vault_root(path):
    required_dirs = [
        "01_Peripheral_Layer",
        "02_Inner_Layer",
        "03_Outer_Layer",
        "system",
    ]
    return all(os.path.isdir(os.path.join(path, name)) for name in required_dirs)


def find_default_vault_dir():
    script_dir = os.path.abspath(os.path.dirname(__file__))
    expected_root = os.path.abspath(os.path.join(script_dir, "..", ".."))
    if is_vault_root(expected_root):
        return expected_root

    current = script_dir
    while True:
        if is_vault_root(current):
            return current
        parent = os.path.dirname(current)
        if parent == current:
            return expected_root
        current = parent


def parse_bool(value, default=True):
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    normalized = str(value).strip().lower()
    if normalized in {"false", "no", "0", "off"}:
        return False
    if normalized in {"true", "yes", "1", "on"}:
        return True
    return default


def normalize_date(value):
    if value is None or value == "":
        return None, "missing"
    if isinstance(value, datetime):
        return value.date(), ""
    if isinstance(value, date):
        return value, ""

    text = str(value).strip().strip('"').strip("'")
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y"):
        try:
            return datetime.strptime(text, fmt).date(), ""
        except ValueError:
            pass

    text_without_ordinals = re.sub(r"(\d+)(st|nd|rd|th)\b", r"\1", text, flags=re.IGNORECASE)
    for fmt in ("%d %B %Y", "%d %b %Y"):
        try:
            return datetime.strptime(text_without_ordinals, fmt).date(), ""
        except ValueError:
            pass

    return None, f"unparseable date: {value}"


def date_text(value):
    return value.isoformat() if isinstance(value, date) else ""


def get_nested(metadata, dotted_key):
    current = metadata
    for part in dotted_key.split("."):
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            return None
    return current


def read_card(path, vault_dir):
    rel_path = os.path.relpath(path, vault_dir)
    record = CardRecord(path=path, rel_path=rel_path)
    filename = os.path.basename(path)
    lowered_filename = filename.lower()
    rel_parts = [part.lower() for part in rel_path.split(os.sep)]
    record.is_test = (
        "test" in lowered_filename
        or "_tests" in rel_parts
        or filename.startswith("_")
    )

    try:
        with open(path, "r", encoding="utf-8", errors="replace") as handle:
            content = handle.read()
    except OSError as exc:
        record.parse_error = str(exc)
        record.repair_needed = True
        record.problems.append("Unable to read card")
        record.suggested_fixes.append("Check file permissions and encoding.")
        return record

    match = FRONTMATTER_RE.match(content)
    if not match:
        record.card_class = "malformed card"
        record.repair_needed = True
        record.problems.append("Missing frontmatter")
        record.suggested_fixes.append("Add YAML frontmatter with id/project_id, status, and deadlines.portal_submission.")
        return record

    try:
        metadata = yaml.safe_load(match.group(1)) if match.group(1).strip() else {}
    except Exception as exc:
        record.card_class = "malformed card"
        record.parse_error = str(exc)
        record.repair_needed = True
        record.problems.append("Invalid frontmatter")
        record.suggested_fixes.append("Fix YAML syntax in the card frontmatter.")
        return record

    if metadata is None:
        metadata = {}
    if not isinstance(metadata, dict):
        record.card_class = "malformed card"
        record.repair_needed = True
        record.problems.append("Invalid frontmatter")
        record.suggested_fixes.append("Frontmatter root must be a YAML mapping.")
        return record

    record.metadata = metadata
    record.card_id = str(metadata.get("id") or "").strip()
    record.project_id = str(metadata.get("project_id") or "").strip()
    record.card_type = str(metadata.get("type") or "").strip()
    record.status = str(metadata.get("status") or "").strip()
    record.state = str(metadata.get("state") or "").strip()
    record.priority = str(metadata.get("priority") or "standard").strip() or "standard"
    record.dashboard_visible = parse_bool(metadata.get("dashboard_visible"), default=True)
    record.lane = str(metadata.get("lane") or "").strip()
    record.institution = str(metadata.get("institution") or metadata.get("target") or "").strip()
    record.role = str(metadata.get("role") or metadata.get("object") or "").strip()
    record.materials_status = str(metadata.get("materials_status") or metadata.get("output_target") or "").strip()
    record.conceptual_anchor = str(metadata.get("conceptual_anchor") or "").strip()
    record.next_action = str(metadata.get("next_action") or "N/A").strip() or "N/A"
    record.next_action_date = str(metadata.get("next_action_date") or "").strip()
    record.action_status = str(metadata.get("action_status") or "").strip()

    if record.is_test:
        record.card_class = "test card"
    elif record.status.lower() in INACTIVE_STATUSES:
        record.card_class = "archived/inactive card"
    elif record.card_type in {"mission_card", "application_card"} or record.status:
        record.card_class = "active mission/application card"
    else:
        record.card_class = "unknown"

    if not (record.card_id or record.project_id):
        record.repair_needed = True
        record.problems.append("Missing id/project_id")
        record.suggested_fixes.append("Add id or project_id to frontmatter.")

    if not record.status:
        record.repair_needed = True
        record.problems.append("Missing required status")
        record.suggested_fixes.append("Add status to frontmatter.")

    portal_raw = (
        get_nested(metadata, "deadlines.portal_submission")
        or metadata.get("portal_submission")
        or metadata.get("deadline")
    )
    portal_date, portal_error = normalize_date(portal_raw)
    if portal_date is None:
        record.repair_needed = True
        if portal_error == "missing":
            record.problems.append("Missing portal submission deadline")
            record.suggested_fixes.append("Add deadlines.portal_submission: YYYY-MM-DD.")
        else:
            record.problems.append("Unparseable deadline")
            record.suggested_fixes.append("Use ISO date format under deadlines.portal_submission.")
    else:
        record.portal_deadline = portal_date

    freeze_raw = get_nested(metadata, "deadlines.t_minus_1_freeze") or metadata.get("t_minus_1_freeze")
    freeze_date, freeze_error = normalize_date(freeze_raw)
    if freeze_date is not None:
        record.freeze_date = freeze_date
    elif freeze_error == "missing" and portal_date is not None:
        record.freeze_date = portal_date - timedelta(days=1)
    elif freeze_error != "missing":
        record.repair_needed = True
        record.problems.append("Unparseable T-1 freeze")
        record.suggested_fixes.append("Use ISO date format under deadlines.t_minus_1_freeze or remove it so it can be derived.")

    return record


def iter_card_paths(vault_dir):
    missions_dir = os.path.join(vault_dir, "03_Outer_Layer", "Active_Missions")
    if not os.path.isdir(missions_dir):
        return []

    paths = []
    for root, _, files in os.walk(missions_dir):
        for filename in files:
            if filename.endswith(".md"):
                paths.append(os.path.join(root, filename))
    return sorted(paths, key=lambda path: os.path.relpath(path, missions_dir).lower())


def classify_cards(vault_dir, include_tests=False):
    cards = [read_card(path, vault_dir) for path in iter_card_paths(vault_dir)]

    for card in cards:
        status = card.status.lower()
        rel_parts = [part.lower() for part in card.rel_path.split(os.sep)]
        filename = os.path.basename(card.path)
        id_text = f"{card.card_id} {card.project_id} {filename}".lower()

        if card.repair_needed:
            card.skipped = True
            card.skip_reason = "metadata repair needed"
            continue

        if "archive" in rel_parts:
            card.skipped = True
            card.skip_reason = "inside archive folder"
            continue

        is_test_by_id = "test" in id_text
        if (card.is_test or is_test_by_id or status == "test") and not include_tests:
            card.skipped = True
            card.skip_reason = "test card excluded"
            continue

        if status in INACTIVE_STATUSES and not (include_tests and status == "test"):
            card.skipped = True
            card.skip_reason = f"status {status} excluded"
            continue

        if not card.dashboard_visible:
            card.skipped = True
            card.skip_reason = "dashboard_visible is false"
            continue

        card.included = True

    return cards


def urgency_rank(urgency):
    return {"Critical": 0, "High": 1, "Standard": 2}.get(urgency, 3)


def parse_pending_logistics(vault_dir):
    logs_dir = os.path.join(vault_dir, "01_Peripheral_Layer", "A_Daily_Logs")
    if not os.path.isdir(logs_dir):
        return []

    pattern = re.compile(
        r"^[-*]\s*\[\s*\]\s*(?:\[([^\]]+)\]|([^:]+)):\s*(.*?)\s*\|\s*\[\s*Urgency:\s*(Critical|High|Standard)\s*\]",
        re.IGNORECASE,
    )
    items = []
    for filename in sorted(os.listdir(logs_dir)):
        if not filename.endswith(".md"):
            continue
        path = os.path.join(logs_dir, filename)
        with open(path, "r", encoding="utf-8", errors="replace") as handle:
            for line in handle:
                match = pattern.search(line.strip())
                if not match:
                    continue
                task = (match.group(1) or match.group(2) or "").strip()
                description = match.group(3).strip()
                urgency = match.group(4).strip().capitalize()
                items.append({
                    "task": task,
                    "description": description,
                    "urgency": urgency,
                    "source": filename,
                })
    return sorted(items, key=lambda item: (urgency_rank(item["urgency"]), item["source"], item["task"]))


def table_cell(value):
    text = str(value or "N/A")
    return text.replace("\n", " ").replace("|", "\\|")


def display_id(card, include_tests=False):
    base = card.project_id or card.card_id or os.path.splitext(os.path.basename(card.path))[0]
    if include_tests and ("test" in base.lower() or card.is_test):
        return f"TEST `{base}`"
    return f"`{base}`"


def render_dashboard(vault_dir, cards, current_date, include_tests=False):
    included_cards = [card for card in cards if card.included]
    repair_cards = [card for card in cards if card.repair_needed]
    logistics = parse_pending_logistics(vault_dir)

    included_cards.sort(key=lambda card: (
        card.portal_deadline or date.max,
        PRIORITY_RANK.get(card.priority.lower(), 2),
        (card.project_id or card.card_id or card.rel_path).lower(),
    ))

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "# 3-Layer System Master Dashboard",
        "",
        f"*Last Compiled: {timestamp} (Reference Date: {current_date.isoformat()})*",
        "",
        "## Active Mission Tracking Ledger",
        "",
        "| Mission ID | Lane | Status | State | Priority | Institution / Target | Role / Object | Submission Deadline | T-1 Lockout Freeze | Materials | Action Status | Next Action Date | Next Action |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]

    if included_cards:
        for card in included_cards:
            frozen = (
                card.freeze_date
                and current_date >= card.freeze_date
                and card.status.lower() not in STABLE_STATUSES
            )
            values = [
                display_id(card, include_tests=include_tests),
                table_cell(card.lane),
                f"`{table_cell(card.status)}`",
                f"`{table_cell(card.state)}`",
                f"`{table_cell(card.priority)}`",
                table_cell(card.institution),
                table_cell(card.role),
                date_text(card.portal_deadline),
                f"`{date_text(card.freeze_date)}`",
                table_cell(card.materials_status),
                f"`{table_cell(card.action_status)}`",
                table_cell(card.next_action_date),
                table_cell(card.next_action),
            ]
            if card.action_status == "stale_needs_review":
                values[10] = "**`stale_needs_review`**"
            elif card.action_status == "parked_visible":
                values[3] = "**`parked`**"
                values[10] = "**`parked_visible`**"
            if frozen:
                values = [f"**{value}**" for value in values]
                values[0] = values[0].replace("`", "`") + " ⚠️"
            lines.append("| " + " | ".join(values) + " |")
    else:
        lines.append("| No active dashboard cards parsed. | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |")

    if repair_cards:
        lines.extend([
            "",
            "## Cards Needing Metadata Repair",
            "",
            "| File | Problem | Suggested Fix |",
            "| --- | --- | --- |",
        ])
        for card in sorted(repair_cards, key=lambda item: item.rel_path.lower()):
            problem = "; ".join(card.problems) or "Unknown metadata problem"
            fix = "; ".join(card.suggested_fixes) or "Inspect card frontmatter."
            lines.append(f"| {table_cell(card.rel_path)} | {table_cell(problem)} | {table_cell(fix)} |")

    lines.extend([
        "",
        "## Pending Logistics Ledger",
        "",
    ])

    if logistics:
        lines.extend([
            "| Urgency | Task | Description | Source Log |",
            "| --- | --- | --- | --- |",
        ])
        for item in logistics:
            source_link = f"[{item['source']}](../../01_Peripheral_Layer/A_Daily_Logs/{item['source']})"
            urgency = f"**{item['urgency']}**" if item["urgency"] in {"Critical", "High"} else item["urgency"]
            lines.append(f"| {urgency} | {table_cell(item['task'])} | {table_cell(item['description'])} | {source_link} |")
    else:
        lines.append("No pending logistics parsed from active daily logs.")

    return "\n".join(lines).rstrip() + "\n"


def resolve_output_path(vault_dir, output_arg):
    if output_arg:
        return os.path.abspath(os.path.expanduser(output_arg)), True
    return os.path.join(vault_dir, "03_Outer_Layer", "Dashboards", "Active_Dashboard.md"), False


def ensure_safe_output(vault_dir, output_path, explicit_output):
    vault_real = os.path.realpath(vault_dir)
    output_real = os.path.realpath(output_path)
    if not explicit_output and not (output_real == vault_real or output_real.startswith(vault_real + os.sep)):
        raise ValueError(f"Refusing to write outside vault: {output_path}")


def write_audit_csv(vault_dir, cards):
    audit_path = os.path.join(vault_dir, "DASHBOARD_CARD_AUDIT.csv")
    fieldnames = [
        "file",
        "id",
        "project_id",
        "type",
        "status",
        "priority",
        "state",
        "dashboard_visible",
        "deadline",
        "freeze",
        "lane",
        "included_in_dashboard",
        "repair_needed",
        "problem",
    ]
    with open(audit_path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for card in sorted(cards, key=lambda item: item.rel_path.lower()):
            writer.writerow({
                "file": card.rel_path,
                "id": card.card_id,
                "project_id": card.project_id,
                "type": card.card_type,
                "status": card.status,
                "priority": card.priority,
                "state": card.state,
                "dashboard_visible": card.dashboard_visible,
                "deadline": date_text(card.portal_deadline),
                "freeze": date_text(card.freeze_date),
                "lane": card.lane,
                "included_in_dashboard": card.included,
                "repair_needed": card.repair_needed,
                "problem": "; ".join(card.problems or ([card.skip_reason] if card.skip_reason else [])),
            })
    return audit_path


def compile_dashboard(vault_dir, current_date=None, include_tests=False):
    if yaml is None:
        raise RuntimeError("PyYAML is required for dashboard card parsing. Install it or run inside the configured environment.")

    current_date = current_date or date.today()
    cards = classify_cards(vault_dir, include_tests=include_tests)
    content = render_dashboard(vault_dir, cards, current_date, include_tests=include_tests)
    return cards, content


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Compile DiegoOS active dashboard from mission/application card frontmatter.")
    parser.add_argument("--vault-dir", default=find_default_vault_dir(), help="Path to the vault root directory")
    parser.add_argument("--current-date", help="Reference date for freeze/overdue rendering, YYYY-MM-DD")
    parser.add_argument("--dry-run", action="store_true", help="Print generated dashboard content without writing files")
    parser.add_argument("--include-tests", action="store_true", help="Include test cards and mark them as TEST")
    parser.add_argument("--output", help="Custom markdown output path")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    vault_dir = os.path.abspath(os.path.expanduser(args.vault_dir))
    if not os.path.isdir(vault_dir):
        print(f"[!] Vault directory does not exist: {vault_dir}")
        return 2

    current_date = date.today()
    if args.current_date:
        parsed_date, error = normalize_date(args.current_date)
        if parsed_date is None:
            print(f"[!] Invalid --current-date: {error}")
            return 2
        current_date = parsed_date

    try:
        cards, dashboard = compile_dashboard(vault_dir, current_date=current_date, include_tests=args.include_tests)
    except RuntimeError as exc:
        print(f"[!] {exc}")
        return 2

    output_path, explicit_output = resolve_output_path(vault_dir, args.output)
    parsed_count = len(cards)
    included_count = sum(1 for card in cards if card.included)
    repair_count = sum(1 for card in cards if card.repair_needed)
    skipped_count = parsed_count - included_count

    if args.dry_run:
        print(f"Dry run: dashboard would be written to: {output_path}")
        print(f"Cards parsed: {parsed_count}")
        print(f"Cards included: {included_count}")
        print(f"Cards skipped: {skipped_count}")
        print(f"Metadata repair items: {repair_count}")
        print("")
        print(dashboard, end="")
        return 0

    try:
        ensure_safe_output(vault_dir, output_path, explicit_output)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(dashboard)
        audit_path = write_audit_csv(vault_dir, cards)
    except (OSError, ValueError) as exc:
        print(f"[!] Failed to write dashboard: {exc}")
        return 1

    print(f"Dashboard written to: {output_path}")
    print(f"Audit written to: {audit_path}")
    print(f"Cards parsed: {parsed_count}")
    print(f"Cards included: {included_count}")
    print(f"Cards skipped: {skipped_count}")
    print(f"Metadata repair items: {repair_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
