import os
import sys
import json
import shutil
from datetime import datetime

def purge_interface():
    # Detect vault directory path
    vault_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    cold_dir = os.path.join(vault_dir, '_Cold_Storage')
    os.makedirs(cold_dir, exist_ok=True)
    
    # 1. VISUAL QUARANTINE (Sidebar Purge)
    # Folders/files to keep at the root of DiegoOS_Vault
    keep_list = {
        '01_Peripheral_Layer',
        '02_Inner_Layer',
        '03_Outer_Layer',
        '_Cold_Storage',
        'system',
        '.obsidian',
        '.git',
        '.gitignore'
    }
    
    print("[*] Starting visual layout sidebar purge...")
    moved_items = []
    
    for item in os.listdir(vault_dir):
        if item in keep_list:
            continue
            
        src_path = os.path.join(vault_dir, item)
        dest_path = os.path.join(cold_dir, item)
        
        try:
            # Overwrite if dest exists to prevent crash
            if os.path.exists(dest_path):
                if os.path.isdir(dest_path):
                    shutil.rmtree(dest_path)
                else:
                    os.remove(dest_path)
                    
            shutil.move(src_path, dest_path)
            moved_items.append(item)
            print(f"[➔] Moved legacy item: {item} -> _Cold_Storage/")
        except Exception as e:
            print(f"[!] Failed to quarantine {item}: {e}")
            
    # 2. OBSIDIAN WORKSPACE CONFIGURATION INJECTION
    obsidian_dir = os.path.join(vault_dir, '.obsidian')
    os.makedirs(obsidian_dir, exist_ok=True)
    
    # Sub-Routine A: Excluded Files Configuration
    app_json_path = os.path.join(obsidian_dir, 'app.json')
    app_config = {}
    if os.path.exists(app_json_path):
        try:
            with open(app_json_path, 'r', encoding='utf-8') as f:
                app_config = json.load(f)
        except Exception as e:
            print(f"[!] Warning: failed to parse existing app.json, initializing new. {e}")
            
    # Guarantee userExcludedFilenames list exists
    if 'userExcludedFilenames' not in app_config:
        app_config['userExcludedFilenames'] = []
        
    # Inject system/ and _Cold_Storage/ into exclusions
    exclusions = ["system/", "_Cold_Storage/"]
    for path in exclusions:
        if path not in app_config['userExcludedFilenames']:
            app_config['userExcludedFilenames'].append(path)
            print(f"[+] Appended Obsidian Exclusion: {path}")
            
    with open(app_json_path, 'w', encoding='utf-8') as f:
        json.dump(app_config, f, indent=4)
    print("[+] app.json exclusion properties updated successfully.")
    
    # Sub-Routine B: Homepage Command Center Enforcement
    homepage_dir = os.path.join(obsidian_dir, 'plugins', 'homepage')
    os.makedirs(homepage_dir, exist_ok=True)
    homepage_json_path = os.path.join(homepage_dir, 'data.json')
    
    homepage_config = {
        "homepage": "03_Outer_Layer/Dashboards/Active_Dashboard.md",
        "homeNote": "03_Outer_Layer/Dashboards/Active_Dashboard.md",
        "autoOpen": True,
        "openOnStartup": "always",
        "refreshOnOpen": True,
        "useBookmark": False,
        "hasSystemOpen": True
    }
    
    # Write default startup homepage config
    with open(homepage_json_path, 'w', encoding='utf-8') as f:
        json.dump(homepage_config, f, indent=4)
    print(f"[+] Homepage default startup view hardcoded: {homepage_json_path}")
    
    # 3. TELEMETRY & VERIFICATION
    # Check if a critical logistical item is currently logged in the dashboard
    dash_path = os.path.join(vault_dir, '03_Outer_Layer', 'Dashboards', 'Active_Dashboard.md')
    has_critical = False
    if os.path.exists(dash_path):
        with open(dash_path, 'r', encoding='utf-8') as f:
            dash_content = f.read()
        if "!!! URGENT ACTION REQUIRED !!!" in dash_content:
            has_critical = True
            
    # Append structured success row to diagnostics ledger
    diag_path = os.path.join(vault_dir, '01_Peripheral_Layer', 'System_Diagnostics.md')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    category = "Interface Optimization"
    details = f"Sidebar Purge complete. Moved {len(moved_items)} legacy items to _Cold_Storage. Exclusions injected. Homepage locked to Active_Dashboard.md. Critical task active = {has_critical}."
    
    entry = f"| {timestamp} | [Sidebar Visual Purge] | {category} | {details} |\n"
    
    if os.path.exists(diag_path):
        with open(diag_path, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        content = "# System Diagnostics Telemetry Ledger\n\n| Timestamp | Project Target | Friction Category | Observed Drift / System Failure |\n| --- | --- | --- | --- |\n"
        
    content = content.rstrip() + "\n" + entry
    with open(diag_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("[+] Interface Optimization telemetry logged successfully.")

if __name__ == '__main__':
    purge_interface()
