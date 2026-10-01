#!/usr/bin/env python3
import argparse
import csv
import os
import re
import shutil
import sys
from collections import OrderedDict
from copy import deepcopy
from datetime import date, datetime

try:
    import yaml
except ImportError:
    yaml = None


FRONTMATTER_RE = re.compile(
    r"\A---[ \t]*\r?\n(?P<yaml>.*?)(?P<closing>\r?\n---[ \t]*)(?P<after>\r?\n|\Z)(?P<body>.*)\Z",
    re.DOTALL,
)
ACTION_STATUSES = {
    "current",
    "needs_next_action",
    "stale_needs_review",
    "blocked",
    "waiting",
    "parked_visible",
    "submitted",
    "closed",
}
INACTIVE_STATUSES = {"archived", "archive", "inactive", "parked", "done", "closed", "rejected"}
FIELD_ORDER = [
    "type",
    "system_layer",
    "id",
    "project_id",
    "status",
    "state",
    "priority",
    "lane",
    "institution",
    "role",
    "materials_status",
    "dashboard_visible",
    "deadlines",
    "deadline_time_uk",
    "deadline_status",
    "output_target",
    "next_action",
    "next_action_date",
    "action_status",
    "last_action_reviewed",
    "last_reviewed",
    "ai_engagement",
    "conceptual_anchor",
]


class QuotedString(str):
    pass


class OrderedDumper(yaml.SafeDumper if yaml else object):
    pass


class FrontmatterLoader(yaml.BaseLoader if yaml else object):
    pass


if yaml:
    def _dict_representer(dumper, data):
        return dumper.represent_mapping("tag:yaml.org,2002:map", data.items())

    def _quoted_string_representer(dumper, data):
        return dumper.represent_scalar("tag:yaml.org,2002:str", str(data), style='"')

    OrderedDumper.add_representer(OrderedDict, _dict_representer)
    OrderedDumper.add_representer(QuotedString, _quoted_string_representer)


def is_vault_root(path):
    required_dirs = ["01_Peripheral_Layer", "02_Inner_Layer", "03_Outer_Layer", "system"]
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


def normalize_date(value):
    if value is None or value == "":
        return None
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    text = str(value).strip().strip('"').strip("'")
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y"):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            pass
    text = re.sub(r"(\d+)(st|nd|rd|th)\b", r"\1", text, flags=re.IGNORECASE)
    for fmt in ("%d %B %Y", "%d %b %Y"):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            pass
    return None


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


def get_nested(data, dotted_key):
    current = data
    for part in dotted_key.split("."):
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            return None
    return current


def is_test_card(rel_path, metadata):
    filename = os.path.basename(rel_path).lower()
    id_text = f"{metadata.get('id', '')} {metadata.get('project_id', '')}".lower()
    return "test" in filename or "test" in id_text or filename.startswith("_")


def is_visible(metadata, rel_path, include_tests=False):
    status = str(metadata.get("status") or "").strip().lower()
    rel_parts = [part.lower() for part in rel_path.split(os.sep)]
    if is_test_card(rel_path, metadata) and not include_tests:
        return False, "test card excluded"
    if "archive" in rel_parts:
        return False, "inside archive folder"
    if status in INACTIVE_STATUSES:
        return False, f"status {status} excluded"
    if not parse_bool(metadata.get("dashboard_visible"), default=True):
        return False, "dashboard_visible is false"
    return True, ""


def extract_body_next_action(body):
    pattern = re.compile(r"^\s*[-*]\s+\*\*Next action:\*\*\s*(.+?)\s*$", re.IGNORECASE | re.MULTILINE)
    match = pattern.search(body)
    if not match:
        return ""
    return re.sub(r"\s+", " ", match.group(1).strip()).rstrip(".")


def is_blank_action(value):
    return not value or str(value).strip().upper() == "N/A"


def stale_action(value, current_date):
    text = str(value or "").lower()
    if "before review starts on may 4" in text and current_date >= date(2026, 5, 23):
        return True
    if "2026-05-04" in text and current_date > date(2026, 5, 4):
        return True
    return False


def ordered_frontmatter(metadata):
    ordered = OrderedDict()
    for key in FIELD_ORDER:
        if key in metadata:
            ordered[key] = metadata[key]
    for key, value in metadata.items():
        if key not in ordered:
            ordered[key] = value
    return ordered


def yaml_ready(value):
    if isinstance(value, dict):
        ready = OrderedDict()
        for key, item in value.items():
            ready[key] = yaml_ready(item)
        return ready
    if isinstance(value, list):
        return [yaml_ready(item) for item in value]
    if isinstance(value, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return QuotedString(value)
    return value


def emit_frontmatter(metadata):
    ready = yaml_ready(ordered_frontmatter(metadata))
    return yaml.dump(
        ready,
        Dumper=OrderedDumper,
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
        width=120,
    ).strip()


def read_markdown(path, vault_dir):
    rel_path = os.path.relpath(path, vault_dir)
    with open(path, "r", encoding="utf-8", errors="replace", newline="") as handle:
        content = handle.read()
    match = FRONTMATTER_RE.match(content)
    if not match:
        return rel_path, None, "", content, content
    metadata = yaml.load(match.group("yaml"), Loader=FrontmatterLoader) if match.group("yaml").strip() else {}
    if metadata is None:
        metadata = {}
    return rel_path, metadata, match.group("after"), match.group("body"), content


def build_new_content(metadata, after_fence, body):
    return "---\n" + emit_frontmatter(metadata) + "\n---" + after_fence + body


def backup_path_for(vault_dir, source_path, current_date):
    backup_dir = os.path.join(vault_dir, "system", "backups", "next_action_hygiene", current_date.isoformat())
    os.makedirs(backup_dir, exist_ok=True)
    base_path = os.path.join(backup_dir, os.path.basename(source_path) + ".bak.md")
    if not os.path.exists(base_path):
        return base_path
    counter = 1
    while True:
        candidate = os.path.join(backup_dir, os.path.basename(source_path) + f".bak.{counter}.md")
        if not os.path.exists(candidate):
            return candidate
        counter += 1


def iter_cards(vault_dir):
    missions_dir = os.path.join(vault_dir, "03_Outer_Layer", "Active_Missions")
    for root, _, files in os.walk(missions_dir):
        for filename in sorted(files):
            if filename.endswith(".md"):
                yield os.path.join(root, filename)


def normalize_card(rel_path, metadata, body, current_date, include_tests=False):
    before = deepcopy(metadata)
    after = deepcopy(metadata)
    warnings = []
    skipped = False
    visible, skip_reason = is_visible(metadata, rel_path, include_tests=include_tests)

    if is_test_card(rel_path, metadata):
        if not include_tests:
            return after, [], ["test card skipped"], True, False, skip_reason
        after["dashboard_visible"] = "false"
        skipped = False

    if not visible and not include_tests:
        return after, [], [skip_reason or "card skipped"], True, False, skip_reason

    status = str(after.get("status") or "").strip().lower()
    state = str(after.get("state") or "").strip().lower()
    next_action_before = str(after.get("next_action") or "").strip()
    body_action = extract_body_next_action(body)
    stale_flag = False

    if status == "submitted":
        action_status = "submitted"
    elif status == "closed":
        action_status = "closed"
    elif stale_action(next_action_before, current_date):
        action_status = "stale_needs_review"
        stale_flag = True
        warnings.append("stale action")
        if state == "parked":
            warnings.append("parked-visible ambiguity preserved")
    elif is_blank_action(next_action_before):
        if body_action:
            after["next_action"] = body_action
            action_status = "current"
            warnings.append("next_action promoted from explicit body text")
        elif state == "parked":
            action_status = "parked_visible"
        else:
            action_status = "needs_next_action"
            warnings.append("missing current next action")
    elif state == "parked":
        action_status = "parked_visible"
    else:
        action_status = "current"

    after["action_status"] = action_status
    after["last_action_reviewed"] = current_date.isoformat()

    changes = []
    for key in ["next_action", "next_action_date", "action_status", "last_action_reviewed", "dashboard_visible"]:
        if before.get(key, "") != after.get(key, ""):
            changes.append((key, before.get(key, "<missing>"), after.get(key, "<missing>")))

    return after, changes, warnings, skipped, stale_flag, skip_reason


def print_summary(rel_path, changes, warnings, skipped):
    print(f"File: {rel_path}")
    if skipped:
        print("Changes proposed: skipped")
    elif changes:
        print("Changes proposed:")
        for field, before, after in changes:
            print(f"* {field}: {before} -> {after}")
    else:
        print("Changes proposed: none")
    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"* {warning}")
    print("")


def audit_row(rel_path, before, after, skipped, stale_flag, changed, warnings):
    return {
        "file": rel_path,
        "id": after.get("id", ""),
        "project_id": after.get("project_id", ""),
        "status": after.get("status", ""),
        "state": after.get("state", ""),
        "dashboard_visible": after.get("dashboard_visible", ""),
        "next_action_before": before.get("next_action", ""),
        "next_action_after": after.get("next_action", ""),
        "next_action_date_before": before.get("next_action_date", ""),
        "next_action_date_after": after.get("next_action_date", ""),
        "action_status_before": before.get("action_status", ""),
        "action_status_after": after.get("action_status", ""),
        "last_action_reviewed": after.get("last_action_reviewed", ""),
        "stale_flag": stale_flag,
        "changed": changed,
        "warning": "; ".join(warnings),
    }


def write_audit(vault_dir, rows):
    path = os.path.join(vault_dir, "NEXT_ACTION_HYGIENE_AUDIT.csv")
    fields = [
        "file",
        "id",
        "project_id",
        "status",
        "state",
        "dashboard_visible",
        "next_action_before",
        "next_action_after",
        "next_action_date_before",
        "next_action_date_after",
        "action_status_before",
        "action_status_after",
        "last_action_reviewed",
        "stale_flag",
        "changed",
        "warning",
    ]
    with open(path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fields)
        writer.writeheader()
        writer.writerows(rows)
    return path


def body_from_content(text):
    match = FRONTMATTER_RE.match(text)
    if match:
        return match.group("body")
    fallback = re.match(r"\A---[ \t]*\r?\n.*?\r?\n---[ \t]*(?:\r?\n|\Z)(.*)\Z", text, re.DOTALL)
    return fallback.group(1) if fallback else text


def run(vault_dir, current_date, apply=False, include_tests=False):
    if yaml is None:
        raise RuntimeError("PyYAML is required for next-action hygiene normalization. Install it or run inside the configured environment.")

    rows = []
    modified = 0
    skipped_count = 0
    for path in iter_cards(vault_dir):
        rel_path, metadata, after_fence, body, original = read_markdown(path, vault_dir)
        if metadata is None:
            print_summary(rel_path, [], ["missing frontmatter"], skipped=True)
            rows.append(audit_row(rel_path, {}, {}, True, False, False, ["missing frontmatter"]))
            skipped_count += 1
            continue

        before = deepcopy(metadata)
        updated, changes, warnings, skipped, stale_flag, _ = normalize_card(
            rel_path, metadata, body, current_date, include_tests=include_tests
        )
        changed = bool(changes) and not skipped
        print_summary(rel_path, changes, warnings, skipped)

        if apply and changed:
            backup_path = backup_path_for(vault_dir, path, current_date)
            shutil.copy2(path, backup_path)
            new_content = build_new_content(updated, after_fence, body)
            with open(path, "w", encoding="utf-8", newline="") as handle:
                handle.write(new_content)
            with open(backup_path, "r", encoding="utf-8", errors="replace") as backup_handle:
                backup_content = backup_handle.read()
            if body_from_content(backup_content) != body:
                raise RuntimeError(f"Body preservation check failed for {rel_path}")
            print(f"Changed: {rel_path}")
            print(f"Backup: {os.path.relpath(backup_path, vault_dir)}")
            modified += 1
        elif apply and skipped:
            print(f"Skipped: {rel_path}")
        elif apply:
            print(f"Unchanged: {rel_path}")

        if skipped:
            skipped_count += 1
        rows.append(audit_row(rel_path, before, updated, skipped, stale_flag, changed, warnings))

    return rows, modified, skipped_count


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Normalize next-action governance fields on DiegoOS cards.")
    parser.add_argument("--vault-dir", default=find_default_vault_dir(), help="Path to the vault root directory")
    parser.add_argument("--dry-run", action="store_true", help="Report proposed changes without writing files")
    parser.add_argument("--apply", action="store_true", help="Apply frontmatter-only changes with backups")
    parser.add_argument("--include-tests", action="store_true", help="Inspect/normalize test cards while keeping them hidden")
    parser.add_argument("--current-date", default=date.today().isoformat(), help="Reference date, YYYY-MM-DD")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    if args.apply and args.dry_run:
        print("[!] Use either --dry-run or --apply, not both.")
        return 2

    current_date = normalize_date(args.current_date)
    if current_date is None:
        print(f"[!] Invalid --current-date: {args.current_date}")
        return 2

    vault_dir = os.path.abspath(os.path.expanduser(args.vault_dir))
    if not os.path.isdir(vault_dir):
        print(f"[!] Vault directory does not exist: {vault_dir}")
        return 2

    apply_changes = args.apply
    mode = "apply" if apply_changes else "dry-run"
    print(f"Mode: {mode}")
    print(f"Vault: {vault_dir}")
    print(f"Reference date: {current_date.isoformat()}")
    print("")

    try:
        rows, modified, skipped = run(vault_dir, current_date, apply=apply_changes, include_tests=args.include_tests)
        if apply_changes:
            audit_path = write_audit(vault_dir, rows)
            print(f"Audit written to: {audit_path}")
        print(f"Cards inspected: {len(rows)}")
        print(f"Cards modified: {modified if apply_changes else sum(str(row['changed']) == 'True' for row in rows)}")
        print(f"Cards skipped: {skipped}")
        return 0
    except RuntimeError as exc:
        print(f"[!] {exc}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
