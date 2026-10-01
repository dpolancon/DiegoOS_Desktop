#!/usr/bin/env python3
import os
import sys
import re
import argparse
from datetime import datetime, date

def is_vault_root(path):
    """
    Returns True when a directory looks like the DiegoOS vault root.
    """
    required_dirs = [
        '01_Peripheral_Layer',
        '02_Inner_Layer',
        '03_Outer_Layer',
        'system',
    ]
    return all(os.path.isdir(os.path.join(path, name)) for name in required_dirs)

def find_default_vault_dir():
    """
    Resolve the vault root from this script's location.

    The script lives at system/scripts/vault_automation.py, so the normal vault
    root is two levels up. If the script is moved, walk upward to find the first
    directory with the active DiegoOS vault layer folders.
    """
    script_dir = os.path.abspath(os.path.dirname(__file__))
    expected_root = os.path.abspath(os.path.join(script_dir, '..', '..'))
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

def parse_frontmatter(content):
    """
    Parses a markdown file's YAML frontmatter.
    Returns (metadata_dict, body_text).
    """
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return {}, content
    
    yaml_text = match.group(1)
    body = content[match.end():]
    
    data = {}
    stack = [data]
    indents = [-1]
    
    for line in yaml_text.split('\n'):
        if not line.strip() or line.strip().startswith('#'):
            continue
        
        leading_spaces = len(line) - len(line.lstrip())
        stripped = line.strip()
        
        if ':' not in stripped:
            continue
            
        key, val = stripped.split(':', 1)
        key = key.strip()
        val = val.strip()
        
        # Remove surrounding quotes
        if val.startswith('"') and val.endswith('"'):
            val = val[1:-1]
        elif val.startswith("'") and val.endswith("'"):
            val = val[1:-1]
            
        while indents and leading_spaces <= indents[-1]:
            stack.pop()
            indents.pop()
            
        current_dict = stack[-1]
        if val == "":
            new_dict = {}
            current_dict[key] = new_dict
            stack.append(new_dict)
            indents.append(leading_spaces)
        else:
            current_dict[key] = val
            
    return data, body

def strip_machine_prose(text):
    """
    Strips common AI conversational smoothing prefixes/suffixes and summaries,
    leaving only the raw conceptual human core.
    """
    lines = text.split('\n')
    cleaned_lines = []
    in_intro = True
    
    conversational_intros = [
        r"^here\s+is\s+the\s+.*",
        r"^certainly.*",
        r"^sure,\s+here.*",
        r"^i\s+can\s+help\s+with\s+.*",
        r"^i\s+have\s+.*",
        r"^as\s+requested.*",
        r"^here's\s+the.*",
        r"^ok,\s+here.*",
        r"^sure,\s+i've\s+.*"
    ]
    
    conversational_outros = [
        r"^let\s+me\s+know\s+if\s+.*",
        r"^hope\s+this\s+helps.*",
        r"^if\s+you\s+need\s+.*",
        r"^this\s+completes\s+.*",
        r"^let\s+me\s+know\s+how\s+.*",
        r"^feel\s+free\s+to\s+.*",
        r"^in\s+summary.*",
        r"^to\s+summarize.*"
    ]
    
    for line in lines:
        stripped = line.strip().lower()
        if not stripped:
            if not cleaned_lines:
                continue
            cleaned_lines.append(line)
            continue
            
        is_intro = False
        if in_intro:
            for pattern in conversational_intros:
                if re.match(pattern, stripped):
                    is_intro = True
                    break
            if is_intro:
                continue
            else:
                in_intro = False
                
        is_outro = False
        for pattern in conversational_outros:
            if re.match(pattern, stripped):
                is_outro = True
                break
        if is_outro:
            continue
            
        cleaned_lines.append(line)
        
    while cleaned_lines and not cleaned_lines[-1].strip():
        cleaned_lines.pop()
        
    return '\n'.join(cleaned_lines)

def log_telemetry(vault_dir, target_file, friction_category, failure_details):
    r"""
    Appends a structured violation/drift entry to C:\...\01_Peripheral_Layer\System_Diagnostics.md.
    """
    diag_path = os.path.join(vault_dir, '01_Peripheral_Layer', 'System_Diagnostics.md')
    os.makedirs(os.path.dirname(diag_path), exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Make relative path for cleaner display
    rel_target = os.path.relpath(target_file, vault_dir) if os.path.isabs(target_file) else target_file
    
    entry = f"| {timestamp} | {rel_target} | {friction_category} | {failure_details} |\n"
    
    # Read/Create Diagnostics file
    if os.path.exists(diag_path):
        with open(diag_path, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        content = "# System Diagnostics Telemetry Ledger\n\n| Timestamp | Project Target | Friction Category | Observed Drift / System Failure |\n| --- | --- | --- | --- |\n"
        
    # Check if table headers exist, if not, append them
    if "| Timestamp |" not in content:
        content += "\n| Timestamp | Project Target | Friction Category | Observed Drift / System Failure |\n| --- | --- | --- | --- |\n"
        
    content = content.rstrip() + "\n" + entry
    
    with open(diag_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"[-] Telemetry appended: {friction_category} -> {rel_target}")

def get_nested_key(data, path_str):
    """ Helper to get nested value like 'deadlines.t_minus_1_freeze' """
    parts = path_str.split('.')
    curr = data
    for part in parts:
        if isinstance(curr, dict) and part in curr:
            curr = curr[part]
        else:
            return None
    return curr

def parse_standard_date(date_str):
    """
    Parses date string strictly using hierarchical order:
    1. YYYY-MM-DD (ISO standard)
    2. DD/MM/YYYY (UK/Latin American standard)
    3. Word-based boundaries like "DD Month YYYY" or "D Month YYYY"
    Returns a datetime.date object, or None if parsing fails.
    """
    if not date_str:
        return None
    date_str = str(date_str).strip()
    
    # Strip ordinal suffixes like 15th -> 15, 22nd -> 22
    date_str = re.sub(r'(\d+)(st|nd|rd|th)\b', r'\1', date_str)
    
    # Try YYYY-MM-DD
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        pass
        
    # Try DD/MM/YYYY (de-prioritising US MM/DD/YYYY)
    try:
        return datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        pass
        
    # Try DD-MM-YYYY
    try:
        return datetime.strptime(date_str, "%d-%m-%Y").date()
    except ValueError:
        pass
        
    # Try textual "DD Month YYYY" e.g., "01 June 2026"
    try:
        return datetime.strptime(date_str, "%d %B %Y").date()
    except ValueError:
        pass

    # Try textual "D Month YYYY" e.g., "1 June 2026" or "12 June 2026"
    try:
        # On Windows, %e is not always supported, so we parse manually
        parts = date_str.split()
        if len(parts) == 3:
            day = int(parts[0])
            month_str = parts[1]
            year = int(parts[2])
            # Construct a temp string with zero-padded day
            temp_str = f"{day:02d} {month_str} {year}"
            return datetime.strptime(temp_str, "%d %B %Y").date()
    except Exception:
        pass
        
    return None

def get_mission_deadlines(metadata):
    """
    Robustly extracts portal_submission and t_minus_1_freeze dates from metadata.
    If t_minus_1_freeze is missing, dynamically offsets portal_submission by -1 day.
    Returns (parsed_deadline, parsed_freeze) as datetime.date objects or (None, None).
    """
    deadline_str = (
        get_nested_key(metadata, 'deadlines.portal_submission') or
        metadata.get('portal_submission') or
        metadata.get('deadline') or
        "2026-06-30"
    )
    t_minus_1_str = (
        get_nested_key(metadata, 'deadlines.t_minus_1_freeze') or
        metadata.get('t_minus_1_freeze')
    )
    
    parsed_deadline = parse_standard_date(deadline_str)
    
    if t_minus_1_str:
        parsed_freeze = parse_standard_date(t_minus_1_str)
    else:
        if parsed_deadline:
            import datetime as dt_mod
            parsed_freeze = parsed_deadline - dt_mod.timedelta(days=1)
        else:
            parsed_freeze = None
            
    return parsed_deadline, parsed_freeze

def run_validate_gates(args):
    """
    Executes Gate A, B, and C validations on all active missions.
    """
    vault_dir = args.vault_dir
    missions_dir = os.path.join(vault_dir, '03_Outer_Layer', 'Active_Missions')
    
    if not os.path.exists(missions_dir):
        print(f"[!] Active Missions directory does not exist: {missions_dir}")
        return 0
        
    current_dt = parse_standard_date(args.current_date) if args.current_date else date.today()
    print(f"[*] Starting Logic Gate validation (Target Date: {current_dt})...")
    
    violations_found = False
    
    for filename in os.listdir(missions_dir):
        if not filename.endswith('.md'):
            continue
            
        file_path = os.path.join(missions_dir, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        metadata, body = parse_frontmatter(content)
        
        # GATE A: T-1 Finalization Validator
        parsed_deadline, parsed_freeze = get_mission_deadlines(metadata)
        status = metadata.get('status', 'active')
        
        if parsed_freeze:
            if current_dt >= parsed_freeze and status != 'stabilized':
                violations_found = True
                details = f"System date {current_dt} matches or exceeds freeze timestamp {parsed_freeze} while status is '{status}'."
                print(f"[!] GATE A VIOLATION: {filename} is frozen. Prose modifications are locked.")
                log_telemetry(vault_dir, file_path, "Gate A Violation", details)
        else:
            violations_found = True
            details = f"Could not determine or parse t_minus_1_freeze for {filename}."
            print(f"[!] INVALID FRONTMATTER DATE: {filename}")
            log_telemetry(vault_dir, file_path, "Invalid Metadata", details)
                
        # GATE B: Conceptual Anchor Enforcement
        anchor_link = metadata.get('conceptual_anchor')
        if not anchor_link:
            violations_found = True
            details = "Missing 'conceptual_anchor' link in frontmatter."
            print(f"[!] GATE B VIOLATION: {filename} lacks a conceptual anchor.")
            log_telemetry(vault_dir, file_path, "Gate B Violation", details)
        else:
            # Anchor can be relative path like "02_Inner_Layer/Conceptual_Notes/Anchor.md"
            # or obsidian style [[Anchor]]
            cleaned_anchor = anchor_link.replace('[[', '').replace(']]', '').strip()
            anchor_path = os.path.join(vault_dir, cleaned_anchor)
            
            # Check standard path and check inner layer directories recursively
            anchor_exists = os.path.exists(anchor_path) and os.path.isfile(anchor_path)
            
            if not anchor_exists:
                # Search inside 02_Inner_Layer recursively
                inner_dir = os.path.join(vault_dir, '02_Inner_Layer')
                basename = os.path.basename(cleaned_anchor)
                found = False
                if os.path.exists(inner_dir):
                    for root, _, files in os.walk(inner_dir):
                        if basename in files:
                            found = True
                            break
                anchor_exists = found
                
            if not anchor_exists:
                violations_found = True
                details = f"Conceptual anchor link '{anchor_link}' points to an invalid/non-existent file."
                print(f"[!] GATE B VIOLATION: {filename} points to invalid anchor.")
                log_telemetry(vault_dir, file_path, "Gate B Violation", details)
                
    if violations_found:
        print("[!] Validation finished with errors. Telemetry logged.")
        return 1
    else:
        print("[+] All Active Missions conform to Logic Gates A & B.")
        return 0

def run_migrate_cold_storage(args):
    """
    Routinely sorts files from _Cold_Storage/ into active system layers.
    """
    vault_dir = args.vault_dir
    cold_dir = os.path.join(vault_dir, '_Cold_Storage')
    
    if not os.path.exists(cold_dir):
        print(f"[!] Cold Storage directory does not exist: {cold_dir}")
        return 0
        
    files = [f for f in os.listdir(cold_dir) if os.path.isfile(os.path.join(cold_dir, f)) and f != '.gitkeep']
    if not files:
        print("[*] _Cold_Storage is empty. No files to migrate.")
        return 0
        
    print(f"[*] Ingesting and routing {len(files)} files from Cold Storage...")
    
    route_a_count = 0
    route_b_count = 0
    route_c_count = 0
    anomalies_count = 0
    
    for filename in files:
        file_path = os.path.join(cold_dir, filename)
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            print(f"[!] Failed to read {filename}: {e}")
            anomalies_count += 1
            continue
            
        low_name = filename.lower()
        low_content = content.lower()
        
        # Exact Routing Matrix Rules
        is_log = ("log" in low_name or "todo" in low_name or "diary" in low_name or 
                  "event" in low_name or "task" in low_name or "registry" in low_name or 
                  re.search(r'\d{2}-\d{2}-\d{4}', filename) or "weekly" in low_name or 
                  "weekend" in low_name or filename == "Today.md")
                  
        is_mission = ("proposal" in low_name or "mission" in low_name or "submission" in low_name or 
                      "draft" in low_name or "prompt" in low_name or "rule" in low_name or 
                      "postdoc" in low_name or "fellow" in low_name or "analyst" in low_name or 
                      "officer" in low_name or "assistant" in low_name or "associate" in low_name or
                      "package checklist" in low_content or "output_target:" in low_content or
                      "cgd" in low_name or "lse" in low_name)
        
        # Override logs if it contains source summaries or academic reading logs
        if "source" in low_name or "research" in low_name or "literature" in low_name:
            is_log = False
            
        # ROUTE C: The Logistical Ingestion Layer
        if is_log:
            dest_dir = os.path.join(vault_dir, '01_Peripheral_Layer', 'A_Daily_Logs')
            os.makedirs(dest_dir, exist_ok=True)
            dest_path = os.path.join(dest_dir, filename)
            
            with open(dest_path, 'w', encoding='utf-8') as f_out:
                f_out.write(content)
            print(f"[➔] Daily Log (Route C): {filename} routed to 01_Peripheral_Layer/A_Daily_Logs/")
            route_c_count += 1
            
        # ROUTE B: The Execution Engine Layer
        elif is_mission:
            dest_dir = os.path.join(vault_dir, '03_Outer_Layer', 'Active_Missions')
            os.makedirs(dest_dir, exist_ok=True)
            dest_path = os.path.join(dest_dir, filename)
            
            # Format project ID
            proj_match = re.match(r'^(\d{4})_(.*)', filename)
            proj_id = filename.split('.')[0]
            if proj_match:
                proj_id = f"{proj_match.group(1)}_{proj_match.group(2).split('.')[0]}"
            else:
                proj_id = f"{datetime.now().year}_{proj_id}"
                
            # Strip standard Obsidian/Windows symbols from project ID
            proj_id = proj_id.replace(' — ', '_').replace(' ', '_').replace('-', '_')
            
            # Parse existing frontmatter to preserve existing metadata if any
            metadata, body = parse_frontmatter(content)
            
            # Extract deadlines if existing, else use standard placeholders
            raw_portal = get_nested_key(metadata, 'deadlines.portal_submission') or metadata.get('deadline')
            
            # If not in frontmatter, search body text for deadline clues (e.g. Closes: 15th June 2026)
            if not raw_portal:
                deadline_match = re.search(r'(?:deadline|closes):\s*\*?\|?\s*(\d{1,2}(?:st|nd|rd|th)?\s+[a-zA-Z]+\s+\d{4}|\d{1,2}/\d{1,2}/\d{4}|\d{4}-\d{2}-\d{2})', content, re.IGNORECASE)
                if deadline_match:
                    raw_portal = deadline_match.group(1).strip()
                    
            parsed_portal = parse_standard_date(raw_portal)
            if parsed_portal:
                portal_deadline = parsed_portal.strftime("%Y-%m-%d")
                import datetime as dt_mod
                t_minus_1_deadline = (parsed_portal - dt_mod.timedelta(days=1)).strftime("%Y-%m-%d")
            else:
                portal_deadline = "2026-06-30"
                t_minus_1_deadline = "2026-06-29"
                
            yaml_header = f"""---
system_layer: 03_Outer
project_id: "{proj_id}"
status: active
deadlines:
  portal_submission: {portal_deadline}
  t_minus_1_freeze: {t_minus_1_deadline}
ai_engagement:
  allowance: restricted
  gatekeeper_prompt: "03_Outer_Layer/System_Prompts.md"
conceptual_anchor: "02_Inner_Layer/Conceptual_Notes/Anchor_Note.md"
---
"""
            with open(dest_path, 'w', encoding='utf-8') as f_out:
                f_out.write(yaml_header + body.lstrip())
            print(f"[➔] Active Mission (Route B): {filename} routed to 03_Outer_Layer/Active_Missions/ (YAML Prepend)")
            route_b_count += 1
            
        # ROUTE A: The Sovereign Inner Layer
        else:
            if "literature" in low_name or "source" in low_name or "anatomy" in low_name:
                dest_dir = os.path.join(vault_dir, '02_Inner_Layer', 'Literature')
            else:
                dest_dir = os.path.join(vault_dir, '02_Inner_Layer', 'Conceptual_Notes')
                
            os.makedirs(dest_dir, exist_ok=True)
            dest_path = os.path.join(dest_dir, filename)
            
            # Core Ingestion Rule: Strip machine-generated prose signatures
            cleaned_content = strip_machine_prose(content)
            
            with open(dest_path, 'w', encoding='utf-8') as f_out:
                f_out.write(cleaned_content)
            print(f"[➔] Sovereign Note (Route A): {filename} routed to {os.path.relpath(dest_dir, vault_dir)}/ (Prose Stripped)")
            route_a_count += 1
            
        # Remove successfully migrated file
        os.remove(file_path)
        
    print("[+] Migration sub-routine routing loop completed successfully.")
    
    # 2. Post-Migration Actions
    # Dashboard compilation
    run_compile_dashboard(args)
    
    # Telemetry logging row
    diag_path = os.path.join(vault_dir, '01_Peripheral_Layer', 'System_Diagnostics.md')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    friction_category = "System Ingestion"
    total_processed = len(files)
    metrics_str = f"Total files processed: {total_processed}. Route A (Inner)={route_a_count}, Route B (Outer)={route_b_count}, Route C (Logistical)={route_c_count}. Anomalies={anomalies_count}."
    
    # Append structured telemetry row
    entry = f"| {timestamp} | [System Ingestion Run] | {friction_category} | {metrics_str} |\n"
    if os.path.exists(diag_path):
        with open(diag_path, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        content = "# System Diagnostics Telemetry Ledger\n\n| Timestamp | Project Target | Friction Category | Observed Drift / System Failure |\n| --- | --- | --- | --- |\n"
    
    content = content.rstrip() + "\n" + entry
    with open(diag_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[+] Post-migration telemetry appended successfully to {os.path.basename(diag_path)}.")
    
    return 0

def run_compile_dashboard(args):
    """
    Aggregates active missions metadata to generate/update Active_Dashboard.md.
    """
    try:
        from update_dashboard_from_cards import compile_dashboard as compile_cards_dashboard
        from update_dashboard_from_cards import write_audit_csv
    except ImportError as e:
        print(f"[!] Failed to load card dashboard compiler: {e}")
        return 1

    vault_dir = args.vault_dir
    dash_path = os.path.join(vault_dir, '03_Outer_Layer', 'Dashboards', 'Active_Dashboard.md')
    current_dt = parse_standard_date(args.current_date) if args.current_date else date.today()

    try:
        cards, dash_content = compile_cards_dashboard(vault_dir, current_date=current_dt, include_tests=False)
    except RuntimeError as e:
        print(f"[!] {e}")
        return 1

    os.makedirs(os.path.dirname(dash_path), exist_ok=True)
    with open(dash_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(dash_content)

    audit_path = write_audit_csv(vault_dir, cards)
    parsed_count = len(cards)
    included_count = sum(1 for card in cards if card.included)
    repair_count = sum(1 for card in cards if card.repair_needed)
    skipped_count = parsed_count - included_count

    print(f"Dashboard written to: {dash_path}")
    print(f"Audit written to: {audit_path}")
    print(f"Cards parsed: {parsed_count}")
    print(f"Cards included: {included_count}")
    print(f"Cards skipped: {skipped_count}")
    print(f"Metadata repair items: {repair_count}")
    return 0

    missions_dir = os.path.join(vault_dir, '03_Outer_Layer', 'Active_Missions')
    logs_dir = os.path.join(vault_dir, '01_Peripheral_Layer', 'A_Daily_Logs')
        
    dash_path = os.path.join(vault_dir, '03_Outer_Layer', 'Dashboards', 'Active_Dashboard.md')
    
    os.makedirs(os.path.dirname(dash_path), exist_ok=True)
    current_dt = parse_standard_date(args.current_date) if args.current_date else date.today()
    
    print(f"[*] Compiling Dashboard table (Reference Date: {current_dt})...")
    
    # 1. Parse daily logs for checklist tasks and urgency triggers
    critical_items = []
    high_items = []
    standard_items = []
    
    if os.path.exists(logs_dir):
        for filename in os.listdir(logs_dir):
            if not filename.endswith('.md') or filename == 'Daily_Log_Template.md':
                continue
                
            log_file_path = os.path.join(logs_dir, filename)
            try:
                with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    log_lines = f.readlines()
            except Exception as e:
                print(f"[!] Failed to read log {filename}: {e}")
                continue
                
            for line in log_lines:
                m = re.search(r'^[-\*]\s*\[\s*\]\s*\[?([^\]:]+)\]?:\s*(.*?)\|\s*\[\s*Urgency:\s*(Critical|High|Standard)\s*\]', line, re.IGNORECASE)
                if m:
                    task_name = m.group(1).strip()
                    description = m.group(2).strip()
                    urgency = m.group(3).strip().capitalize()
                    
                    task_info = {
                        'task_name': task_name,
                        'description': description,
                        'source': filename,
                        'path': log_file_path
                    }
                    
                    if urgency == 'Critical':
                        critical_items.append(task_info)
                        
                        # Diagnostic logging for new Critical items
                        diag_path = os.path.join(vault_dir, '01_Peripheral_Layer', 'System_Diagnostics.md')
                        already_logged = False
                        if os.path.exists(diag_path):
                            with open(diag_path, 'r', encoding='utf-8') as f_diag:
                                diag_content = f_diag.read()
                            if f"Critical logistical task '{task_name}'" in diag_content:
                                already_logged = True
                                
                        if not already_logged:
                            log_telemetry(vault_dir, log_file_path, "Systemic Urgency", f"Critical logistical task '{task_name}' captured. Description: {description}")
                            
                    elif urgency == 'High':
                        high_items.append(task_info)
                    else:
                        standard_items.append(task_info)
    
    # 2. Compile Active Mission list from 03_Outer_Layer/Active_Missions/
    rows = []
    if os.path.exists(missions_dir):
        for filename in os.listdir(missions_dir):
            if not filename.endswith('.md') or filename == '.gitkeep':
                continue
                
            file_path = os.path.join(missions_dir, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                print(f"[!] Failed to read mission {filename}: {e}")
                continue
                
            metadata, _ = parse_frontmatter(content)
            
            proj_id = metadata.get('project_id') or metadata.get('id') or filename.split('.')[0]
            status = metadata.get('status', 'active')
            priority = metadata.get('priority', 'standard')
            next_action = metadata.get('next_action') or "N/A"
            
            # Format and parse deadlines
            parsed_deadline, parsed_freeze = get_mission_deadlines(metadata)
            
            portal_deadline = parsed_deadline.strftime("%Y-%m-%d") if parsed_deadline else "2026-06-30"
            t_minus_1_str = parsed_freeze.strftime("%Y-%m-%d") if parsed_freeze else "2026-06-29"
            
            # Sort date key
            sort_date = parsed_deadline or date(2999, 12, 31)
            
            # Determine visual priority elevation
            is_overdue = parsed_freeze and current_dt >= parsed_freeze
            
            if is_overdue:
                mission_id_cell = f"**`{proj_id}` ⚠️**"
                status_cell = f"**`{status}`**"
                priority_cell = f"**`{priority}`**"
                deadline_cell = f"**{portal_deadline}**"
                freeze_cell = f"**`{t_minus_1_str}`**"
                action_cell = f"**{next_action}**"
            else:
                mission_id_cell = f"`{proj_id}`"
                status_cell = f"`{status}`"
                priority_cell = f"`{priority}`"
                deadline_cell = f"**{portal_deadline}**"
                freeze_cell = f"`{t_minus_1_str}`"
                action_cell = next_action
                
            rows.append((sort_date, mission_id_cell, status_cell, priority_cell, deadline_cell, freeze_cell, action_cell))
            
    # Sort active missions ledger chronologically by upcoming deadline
    rows.sort(key=lambda x: x[0])
    
    # 3. Generate Dashboard Content
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dash_content = ""
    
    # Force bold critical warning block at the top if any Critical task is found
    if critical_items:
        dash_content += "# !!! URGENT ACTION REQUIRED !!!\n\n"
        dash_content += "The following Critical logistical items require immediate attention:\n\n"
        for item in critical_items:
            dash_content += f"*   **{item['task_name']}**: {item['description']} *(Source: [{item['source']}](../../01_Peripheral_Layer/A_Daily_Logs/{item['source']}))*\n"
        dash_content += "\n---\n\n"
        
    dash_content += f"# 3-Layer System Master Dashboard\n\n"
    dash_content += f"*Last Compiled: {timestamp} (Reference Date: {current_dt})*\n\n"
    
    # Execution Engine Active Dashboard Matrix
    dash_content += "## Active Mission Tracking Ledger\n\n"
    dash_content += "| Mission ID | Status | Priority | Submission Deadline | T-1 Lockout Freeze | Next Action |\n"
    dash_content += "| :--- | :--- | :--- | :--- | :--- | :--- |\n"
    for _, mission_id, status, priority, deadline, freeze, action in rows:
        dash_content += f"| {mission_id} | {status} | {priority} | {deadline} | {freeze} | {action} |\n"
    dash_content += "\n"
    
    # Logistical items table
    dash_content += "## Pending Logistics Ledger\n\n"
    dash_content += "| Urgency | Task | Description | Source Log |\n"
    dash_content += "| --- | --- | --- | --- |\n"
    
    # High priority items first
    for item in high_items:
        dash_content += f"| **High** | {item['task_name']} | {item['description']} | [{item['source']}](../../01_Peripheral_Layer/A_Daily_Logs/{item['source']}) |\n"
        
    # Standard priority items below
    for item in standard_items:
        dash_content += f"| Standard | {item['task_name']} | {item['description']} | [{item['source']}](../../01_Peripheral_Layer/A_Daily_Logs/{item['source']}) |\n"
        
    with open(dash_path, 'w', encoding='utf-8') as f:
        f.write(dash_content)
        
    print(f"[+] Master dashboard successfully written to: {dash_path}")
    return 0

def normalize_text_dates(content):
    """
    Parses any date in format DD-MM-YYYY, DD/MM/YYYY, MM/DD/YYYY,
    or textual date (like 15th June 2026) and translates it to ISO-8601 standard YYYY-MM-DD.
    """
    # 1. Match DD-MM-YYYY or DD/MM/YYYY
    def repl_iso(m):
        d, m_val, y = m.group(1), m.group(2), m.group(3)
        if len(y) == 4 and len(d) == 2 and len(m_val) == 2:
            return f"{y}-{m_val}-{d}"
        return m.group(0)
    content = re.sub(r'\b(\d{2})[-/](\d{2})[-/](\d{4})\b', repl_iso, content)
    
    # 2. Match word-based dates like "15th June 2026" or "15 June 2026"
    def repl_word(m):
        day = m.group(1)
        month_name = m.group(2)
        year = m.group(3)
        # Clean ordinals
        day = re.sub(r'(st|nd|rd|th)', '', day)
        day_num = int(day)
        try:
            dt = datetime.strptime(f"{day_num:02d} {month_name} {year}", "%d %B %Y")
            return dt.strftime("%Y-%m-%d")
        except Exception:
            return m.group(0)
            
    content = re.sub(r'\b(\d{1,2}(?:st|nd|rd|th)?)\s+([a-zA-Z]+)\s+(\d{4})\b', repl_word, content)
    return content

def extract_friction(log_content, filename):
    """
    Parses the daily and weekly logs for roadblock, bottleneck, and friction entries.
    """
    # Find section ## Soft friction capture
    match = re.search(r'## Soft friction capture.*?\n(.*?)\n(?:---|##|$)', log_content, re.DOTALL | re.IGNORECASE)
    if not match:
        return None
        
    section_text = match.group(1).strip()
    # Clean standard markdown comments or prompt instructions
    section_text = re.sub(r'only if blocked\.?', '', section_text, flags=re.IGNORECASE).strip()
    
    if not section_text or "___" in section_text or len(section_text) < 15:
        return None
        
    intended = ""
    but_instead = ""
    because = ""
    
    # Try regex matching bullet points
    m_bullet = re.search(r'(?:intended to:?)\s*(.*?)(?:\n\+?\s*but instead:?|\n\+?\s*because:?|$)', section_text, re.DOTALL | re.IGNORECASE)
    if m_bullet:
        intended = m_bullet.group(1).strip()
        
    m_instead = re.search(r'(?:but instead:?)\s*(.*?)(?:\n\+?\s*because:?|$)', section_text, re.DOTALL | re.IGNORECASE)
    if m_instead:
        but_instead = m_instead.group(1).strip()
        
    m_because = re.search(r'(?:because:?)\s*(.*?)$', section_text, re.DOTALL | re.IGNORECASE)
    if m_because:
        because = m_because.group(1).strip()
        
    origin_title = filename.split('.')[0]
    
    if not but_instead:
        core_issue = section_text
        intended_str = "N/A"
        mitigation = "Standardize work boundary sequencing and protect focus blocks from secondary projects."
    else:
        core_issue = f"Intended to {intended.lower()} but instead {but_instead.lower()} because {because.lower()}"
        
        # Actionable Mitigations based on common patterns:
        if "too much" in core_issue or "balance" in core_issue or "multitasking" in core_issue:
            mitigation = "Enforce a strict single-deliverable focus limit per day. Avoid parallel multi-front execution sprints."
        elif "procrastinated" in core_issue or "chatting" in core_issue or "distraction" in core_issue:
            mitigation = "Isolate deep-focus workspace from social/communication channels during designated work blocks."
        elif "time-consuming" in core_issue or "judgment" in core_issue or "polishing" in core_issue:
            mitigation = "De-prioritize secondary paper reviews or empirical coding; allocate dedicated, high-friction human concentration blocks for critical thesis editing."
        elif "uneven" in core_issue or "naps" in core_issue or "recovery" in core_issue or "burnout" in core_issue:
            mitigation = "Redesign weekends strictly as low-velocity cognitive recovery zones instead of high-pace sprints."
        else:
            mitigation = "Set rigid task-completion boundaries and park overflow items immediately in the capacity pool."
            
    # Generate short name
    short_name = origin_title + " Roadblock"
    if "southern voice" in core_issue.lower():
        short_name = "Application Overhead & Social Procrastination"
    elif "editing" in core_issue.lower() or "serious editing" in core_issue.lower():
        short_name = "Thesis Editing Human Judgment Bottleneck"
    elif "uneven blocks" in core_issue.lower() or "recovery" in core_issue.lower():
        short_name = "High-Output Cognitive Fatigue Recovery"
        
    return {
        'short_name': short_name,
        'origin_title': origin_title,
        'core_issue': core_issue,
        'mitigation': mitigation
    }

def run_harmonize_logs(args):
    """
    Normalizes log file names and formats, and consolidates frictions log ledger.
    """
    import shutil
    vault_dir = args.vault_dir
    logs_dir = os.path.join(vault_dir, '01_Peripheral_Layer')
    
    # Rename B_Wekly_Logs to B_Weekly_Logs if present
    wekly_path = os.path.join(logs_dir, 'B_Wekly_Logs')
    weekly_path = os.path.join(logs_dir, 'B_Weekly_Logs')
    if os.path.exists(wekly_path) and not os.path.exists(weekly_path):
        try:
            os.rename(wekly_path, weekly_path)
            print("[+] Standardized directory: B_Wekly_Logs renamed to B_Weekly_Logs")
        except Exception as e:
            print(f"[!] Warning: failed to rename folder B_Wekly_Logs: {e}")
            weekly_path = wekly_path
            
    daily_dir = os.path.join(logs_dir, 'A_Daily_Logs')
    frictions_dir = os.path.join(logs_dir, 'C_Frictions_Logs')
    os.makedirs(frictions_dir, exist_ok=True)
    
    frictions_extracted = []
    
    for folder_dir in [daily_dir, weekly_path]:
        if not os.path.exists(folder_dir):
            continue
            
        for filename in os.listdir(folder_dir):
            file_path = os.path.join(folder_dir, filename)
            if os.path.isdir(file_path):
                continue
                
            # Rename if extension is missing, lowercase .markdown, or malformed
            base, ext = os.path.splitext(filename)
            new_filename = filename
            if ext.lower() in ['.markdown', '.txt', ''] or ext == "":
                new_filename = base + ".md"
                new_file_path = os.path.join(folder_dir, new_filename)
                try:
                    shutil.move(file_path, new_file_path)
                    file_path = new_file_path
                    filename = new_filename
                    print(f"[+] Extension Normalized: {filename} -> strict .md")
                except Exception as e:
                    print(f"[!] Failed to rename file {filename}: {e}")
                
            if not filename.endswith('.md') or filename == '.gitkeep':
                continue
                
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
            except Exception as e:
                print(f"[!] Failed to read log file {filename}: {e}")
                continue
                
            # 1. Normalize dates in content
            normalized_content = normalize_text_dates(content)
            if normalized_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(normalized_content)
                print(f"[+] Date standardisation locked inside {filename}")
                content = normalized_content
                
            # 2. Extract Roadblocks/Frictions
            f_data = extract_friction(content, filename)
            if f_data:
                frictions_extracted.append(f_data)
                
    # 3. Consolidate and write to C_Frictions_Logs/Frictions_Ledger.md
    if frictions_extracted:
        ledger_path = os.path.join(frictions_dir, 'Frictions_Ledger.md')
        ledger_content = "# Tri-Layer System Consolidated Frictions Ledger\n\n"
        ledger_content += "This ledger aggregates roadblocks, process bottlenecks, and cognitive friction logs captured across Peripheral Daily and Weekly logs.\n\n"
        
        for f in frictions_extracted:
            ledger_content += f"> ### Friction: {f['short_name']}\n"
            ledger_content += f"> - **Source File:** `[[{f['origin_title']}]]`\n"
            ledger_content += f"> - **Core Issue:** {f['core_issue']}\n"
            ledger_content += f"> - **Actionable Mitigation:** {f['mitigation']}\n\n"
            
        with open(ledger_path, 'w', encoding='utf-8') as f:
            f.write(ledger_content)
        print(f"[+] Unified friction ledger written with {len(frictions_extracted)} roadblock profiles.")
    else:
        print("[*] No active frictions found in daily or weekly logs.")
        
    # Append confirmation row to diagnostic log
    log_telemetry(vault_dir, "01_Peripheral_Layer/C_Frictions_Logs/Frictions_Ledger.md", "Log Harmonisation", f"Harmonised daily and weekly logs. Compiled {len(frictions_extracted)} frictions.")
    
    return 0

def main():
    default_vault = find_default_vault_dir()
    
    parser = argparse.ArgumentParser(description="DiegoOS Vault 3-Layer Architecture Automation Engine")
    parser.add_argument('--vault-dir', default=default_vault, help="Path to the Vault root directory")
    parser.add_argument('--current-date', help="Simulated current date (YYYY-MM-DD) for logic gate testing")
    
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Command: validate-gates
    subparsers.add_parser('validate-gates', help="Execute logic gate validations (A & B)")
    
    # Command: migrate-cold-storage
    subparsers.add_parser('migrate-cold-storage', help="Sort files from _Cold_Storage/ into correct layers")
    
    # Command: compile-dashboard
    subparsers.add_parser('compile-dashboard', help="Compile Active_Dashboard.md from active missions metadata")
    
    # Command: harmonize-logs
    subparsers.add_parser('harmonize-logs', help="Harmonize logs and extract roadblocks/frictions")
    
    args = parser.parse_args()
    args.vault_dir = os.path.abspath(os.path.expanduser(args.vault_dir))
    
    if not os.path.exists(args.vault_dir):
        print(f"[!] Specified Vault directory does not exist: {args.vault_dir}")
        sys.exit(1)
        
    if args.command == 'validate-gates':
        sys.exit(run_validate_gates(args))
    elif args.command == 'migrate-cold-storage':
        sys.exit(run_migrate_cold_storage(args))
    elif args.command == 'compile-dashboard':
        sys.exit(run_compile_dashboard(args))
    elif args.command == 'harmonize-logs':
        sys.exit(run_harmonize_logs(args))

if __name__ == '__main__':
    main()
