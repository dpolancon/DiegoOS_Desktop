#!/usr/bin/env python3
import argparse
import csv
import os
import re
import shutil
import sys
from collections import OrderedDict
from copy import deepcopy
from datetime import date, datetime, timedelta

try:
    import yaml
except ImportError:
    yaml = None


FRONTMATTER_RE = re.compile(
    r"\A---[ \t]*\r?\n(?P<yaml>.*?)(?P<closing>\r?\n---[ \t]*)(?P<after>\r?\n|\Z)(?P<body>.*)\Z",
    re.DOTALL,
)
ACTIVE_STATUSES = {"active", "pipeline_eval", "stabilized", "submitted"}
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


def date_string(value):
    parsed = normalize_date(value)
    return parsed.isoformat() if parsed else ""


def get_nested(data, dotted_key):
    current = data
    for part in dotted_key.split("."):
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            return None
    return current


def parse_bool(value, default=True):
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() not in {"false", "no", "0", "off"}


def extract_snapshot_field(body, label):
    pattern = re.compile(rf"^\s*[-*]\s+\*\*{re.escape(label)}:\*\*\s*(.+?)\s*$", re.IGNORECASE | re.MULTILINE)
    match = pattern.search(body)
    if not match:
        return ""
    return re.sub(r"\s+", " ", match.group(1).strip()).rstrip(".")


def clean_materials(value):
    if not value:
        return "unknown"
    text = str(value).strip()
    text = re.sub(r"[^A-Za-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_").lower()
    return text or "unknown"


def infer_materials_status(body):
    lowered = body.lower()
    if "covering letter" in lowered or "cover letter" in lowered:
        if "cv" in lowered:
            return "cv_and_cover_letter"
    if "personal statement" in lowered:
        if "cv" in lowered:
            return "cv_and_personal_statement"
    return "unknown"


def detect_test(rel_path, metadata):
    filename = os.path.basename(rel_path).lower()
    id_text = f"{metadata.get('id', '')} {metadata.get('project_id', '')}".lower()
    return "test" in filename or "test" in id_text or filename.startswith("_")


def classify_card(rel_path, metadata, body):
    if not metadata:
        return "malformed card"
    if detect_test(rel_path, metadata):
        return "test card"
    status = str(metadata.get("status") or "").strip().lower()
    if status in INACTIVE_STATUSES:
        return "inactive/archived card"
    position = extract_snapshot_field(body, "Position")
    application_signals = [position, str(metadata.get("output_target") or ""), rel_path]
    if status in ACTIVE_STATUSES and any(signal for signal in application_signals):
        return "active application card"
    if status in ACTIVE_STATUSES:
        return "active mission card"
    return "unknown"


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


def change_summary(before, after, prefix=""):
    changes = []
    keys = sorted(set(before.keys()) | set(after.keys()))
    for key in keys:
        left = before.get(key, "<missing>")
        right = after.get(key, "<missing>")
        if left != right:
            changes.append((f"{prefix}{key}", left, right))
    return changes


def summarize_metadata_changes(before, after):
    changes = []
    for key in [
        "type",
        "priority",
        "lane",
        "institution",
        "role",
        "materials_status",
        "dashboard_visible",
        "deadline",
        "t_minus_1_freeze",
        "last_reviewed",
    ]:
        left = before.get(key, "<missing>")
        right = after.get(key, "<missing>")
        if left != right:
            changes.append((key, left, right))
    changes.extend(change_summary(before.get("deadlines", {}) or {}, after.get("deadlines", {}) or {}, "deadlines."))
    return changes


def normalize_metadata(rel_path, metadata, body, current_date, include_tests=False):
    before = deepcopy(metadata)
    after = deepcopy(metadata)
    warnings = []
    classification = classify_card(rel_path, metadata, body)

    if classification == "test card" and not include_tests:
        return classification, after, [], ["test card skipped"], True

    if classification in {"malformed card", "unknown"}:
        return classification, after, [], ["card not normalized because classification is not active/test"], True

    if classification == "inactive/archived card":
        return classification, after, [], ["inactive/archived card skipped"], True

    if classification == "test card":
        after.setdefault("dashboard_visible", False)
        after.setdefault("type", "test_card")
        warnings.append("test card normalized only when --include-tests is passed")
    else:
        after.setdefault("type", "application_card")
        after.setdefault("dashboard_visible", True)

    if after.get("type") == "application_card":
        after.setdefault("lane", "applications")

    after.setdefault("priority", "standard")
    after["last_reviewed"] = current_date.isoformat()

    institution = after.get("institution")
    role = after.get("role")
    inferred_institution = extract_snapshot_field(body, "Institution")
    inferred_role = extract_snapshot_field(body, "Position")
    if not institution:
        after["institution"] = inferred_institution or "TODO"
        if not inferred_institution:
            warnings.append("uncertain institution")
    if not role:
        after["role"] = inferred_role or "TODO"
        if not inferred_role:
            warnings.append("uncertain role")

    if not after.get("materials_status") or after.get("materials_status") == "unknown":
        after["materials_status"] = clean_materials(after.get("output_target"))
        if after["materials_status"] == "unknown":
            after["materials_status"] = infer_materials_status(body)

    portal_raw = get_nested(after, "deadlines.portal_submission") or after.get("portal_submission") or after.get("deadline")
    portal_date = normalize_date(portal_raw)
    if portal_date:
        deadlines = deepcopy(after.get("deadlines") or {})
        deadlines["portal_submission"] = portal_date.isoformat()
        freeze_raw = deadlines.get("t_minus_1_freeze") or after.get("t_minus_1_freeze")
        freeze_date = normalize_date(freeze_raw) or (portal_date - timedelta(days=1))
        deadlines["t_minus_1_freeze"] = freeze_date.isoformat()
        after["deadlines"] = deadlines
        if "deadline" in after:
            after.pop("deadline")
            warnings.append("legacy deadline converted")
        if "t_minus_1_freeze" in after:
            after.pop("t_minus_1_freeze")
            warnings.append("legacy t_minus_1_freeze converted")
        if "portal_submission" in after:
            after.pop("portal_submission")
            warnings.append("legacy portal_submission converted")
    else:
        warnings.append("missing or unparseable deadline")

    next_action = str(after.get("next_action") or "")
    if "may 4" in next_action.lower() and current_date >= date(2026, 5, 23):
        warnings.append("stale next_action possible")

    changes = summarize_metadata_changes(before, after)
    return classification, after, changes, warnings, False


def read_markdown(path, vault_dir):
    rel_path = os.path.relpath(path, vault_dir)
    with open(path, "r", encoding="utf-8", errors="replace", newline="") as handle:
        content = handle.read()
    match = FRONTMATTER_RE.match(content)
    if not match:
        return rel_path, None, "", content, ""
    metadata = yaml.load(match.group("yaml"), Loader=FrontmatterLoader) if match.group("yaml").strip() else {}
    if metadata is None:
        metadata = {}
    return rel_path, metadata, match.group("after"), match.group("body"), content


def iter_cards(vault_dir):
    missions_dir = os.path.join(vault_dir, "03_Outer_Layer", "Active_Missions")
    for root, _, files in os.walk(missions_dir):
        for filename in sorted(files):
            if filename.endswith(".md"):
                yield os.path.join(root, filename)


def backup_path_for(vault_dir, source_path, current_date):
    backup_dir = os.path.join(vault_dir, "system", "backups", "card_frontmatter", current_date.isoformat())
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


def build_new_content(metadata, after_fence, body):
    return "---\n" + emit_frontmatter(metadata) + "\n---" + after_fence + body


def run(vault_dir, current_date, apply=False, include_tests=False):
    if yaml is None:
        raise RuntimeError("PyYAML is required for card frontmatter normalization. Install it or run inside the configured environment.")

    rows = []
    for path in iter_cards(vault_dir):
        rel_path, metadata, after_fence, body, original = read_markdown(path, vault_dir)
        if metadata is None:
            row = {
                "file": rel_path,
                "classification": "malformed card",
                "changed": False,
                "skipped": True,
                "warnings": "missing frontmatter",
            }
            rows.append(row)
            print_card_summary(rel_path, "malformed card", [], ["missing frontmatter"], skipped=True)
            continue

        classification, updated, changes, warnings, skipped = normalize_metadata(
            rel_path,
            metadata,
            body,
            current_date,
            include_tests=include_tests,
        )
        changed = bool(changes)
        new_content = build_new_content(updated, after_fence, body) if changed else original

        print_card_summary(rel_path, classification, changes, warnings, skipped=skipped)

        if apply and changed and not skipped:
            backup_path = backup_path_for(vault_dir, path, current_date)
            shutil.copy2(path, backup_path)
            with open(path, "w", encoding="utf-8", newline="") as handle:
                handle.write(new_content)
            print(f"Changed: {rel_path}")
            print(f"Backup: {os.path.relpath(backup_path, vault_dir)}")
        elif apply and skipped:
            print(f"Skipped: {rel_path}")
        elif apply and not changed:
            print(f"Unchanged: {rel_path}")

        rows.append(audit_row(rel_path, classification, metadata, updated, changes, warnings, skipped))

    return rows


def print_card_summary(rel_path, classification, changes, warnings, skipped=False):
    print(f"File: {rel_path}")
    print(f"Classification: {classification}")
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


def audit_row(rel_path, classification, before, after, changes, warnings, skipped):
    before_deadlines = before.get("deadlines") or {}
    after_deadlines = after.get("deadlines") or {}
    return {
        "file": rel_path,
        "classification": classification,
        "changed": bool(changes) and not skipped,
        "skipped": skipped,
        "id": after.get("id", ""),
        "project_id": after.get("project_id", ""),
        "type_before": before.get("type", ""),
        "type_after": after.get("type", ""),
        "status": after.get("status", ""),
        "priority": after.get("priority", ""),
        "lane_before": before.get("lane", ""),
        "lane_after": after.get("lane", ""),
        "institution_before": before.get("institution", ""),
        "institution_after": after.get("institution", ""),
        "role_before": before.get("role", ""),
        "role_after": after.get("role", ""),
        "deadline_before": before_deadlines.get("portal_submission", before.get("deadline", "")),
        "deadline_after": after_deadlines.get("portal_submission", ""),
        "freeze_before": before_deadlines.get("t_minus_1_freeze", before.get("t_minus_1_freeze", "")),
        "freeze_after": after_deadlines.get("t_minus_1_freeze", ""),
        "materials_before": before.get("materials_status", before.get("output_target", "")),
        "materials_after": after.get("materials_status", ""),
        "dashboard_visible": after.get("dashboard_visible", ""),
        "last_reviewed": after.get("last_reviewed", ""),
        "warnings": "; ".join(warnings),
    }


def write_audit(vault_dir, rows):
    path = os.path.join(vault_dir, "CARD_SCHEMA_NORMALIZATION_AUDIT.csv")
    fields = [
        "file",
        "classification",
        "changed",
        "skipped",
        "id",
        "project_id",
        "type_before",
        "type_after",
        "status",
        "priority",
        "lane_before",
        "lane_after",
        "institution_before",
        "institution_after",
        "role_before",
        "role_after",
        "deadline_before",
        "deadline_after",
        "freeze_before",
        "freeze_after",
        "materials_before",
        "materials_after",
        "dashboard_visible",
        "last_reviewed",
        "warnings",
    ]
    with open(path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fields)
        writer.writeheader()
        writer.writerows(rows)
    return path


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Normalize DiegoOS mission/application card frontmatter.")
    parser.add_argument("--vault-dir", default=find_default_vault_dir(), help="Path to the vault root directory")
    parser.add_argument("--dry-run", action="store_true", help="Report proposed frontmatter changes without writing files")
    parser.add_argument("--apply", action="store_true", help="Apply frontmatter changes after creating backups")
    parser.add_argument("--include-tests", action="store_true", help="Normalize test cards while keeping dashboard_visible false")
    parser.add_argument("--current-date", default=date.today().isoformat(), help="Date used for last_reviewed, YYYY-MM-DD")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    if args.apply and args.dry_run:
        print("[!] Use either --dry-run or --apply, not both.")
        return 2

    apply_changes = args.apply
    mode = "apply" if apply_changes else "dry-run"

    current_date = normalize_date(args.current_date)
    if current_date is None:
        print(f"[!] Invalid --current-date: {args.current_date}")
        return 2

    vault_dir = os.path.abspath(os.path.expanduser(args.vault_dir))
    if not os.path.isdir(vault_dir):
        print(f"[!] Vault directory does not exist: {vault_dir}")
        return 2

    try:
        print(f"Mode: {mode}")
        print(f"Vault: {vault_dir}")
        print(f"Reference date: {current_date.isoformat()}")
        print("")
        rows = run(vault_dir, current_date, apply=apply_changes, include_tests=args.include_tests)
        if apply_changes:
            audit_path = write_audit(vault_dir, rows)
            print(f"Audit written to: {audit_path}")
        print(f"Cards inspected: {len(rows)}")
        print(f"Cards modified: {sum(1 for row in rows if row['changed'])}")
        print(f"Cards skipped: {sum(1 for row in rows if row['skipped'])}")
        return 0
    except RuntimeError as exc:
        print(f"[!] {exc}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
