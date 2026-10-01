#!/usr/bin/env python3
import os
import re
import shutil
import yaml
from datetime import datetime

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

class DiegoOSCardTidier:
    def __init__(self, vault_root=None):
        self.vault_root = os.path.abspath(vault_root or find_default_vault_dir())
        self.active_dir = os.path.join(self.vault_root, "03_Outer_Layer", "Active_Missions")
        self.storage_dir = os.path.join(self.vault_root, "_Cold_Storage", "02_AREAS", "Application_Pipeline", "legacy")
        self.log_file = os.path.join(self.vault_root, "01_Peripheral_Layer", "System_Diagnostics.md")
        
    def _parse_date(self, date_str):
        if not date_str:
            return None
        # Clean ordinal suffixes (st, nd, rd, th)
        cleaned = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', str(date_str).strip())
        
        # Hierarchical parsing rules
        for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d %B %Y"):
            try:
                return datetime.strptime(cleaned, fmt).date()
            except ValueError:
                continue
        return None

    def tidy_and_quarantine(self, reference_date_str="2026-05-23"):
        ref_date = datetime.strptime(reference_date_str, "%Y-%m-%d").date()
        os.makedirs(self.storage_dir, exist_ok=True)
        
        if not os.path.exists(self.active_dir):
            print(f"[-] Active directory not found: {self.active_dir}")
            return

        for filename in os.listdir(self.active_dir):
            if not filename.endswith(".md") or "Test" in filename:
                continue
                
            file_path = os.path.join(self.active_dir, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Match frontmatter YAML block
            yaml_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
            if not yaml_match:
                continue
                
            try:
                metadata = yaml.safe_load(yaml_match.group(1))
            except Exception:
                continue
                
            deadline_raw = metadata.get("deadline") if metadata else None
            deadline_date = self._parse_date(deadline_raw)
            
            if deadline_date and deadline_date < ref_date:
                # Target is past its portal validation limit -> Quarantine Execution
                dest_path = os.path.join(self.storage_dir, filename)
                shutil.move(file_path, dest_path)
                self._log_telemetry(filename, reference_date_str, "Pipeline Evacuation", f"Deadline {deadline_raw} surpassed.")
                print(f"[➔] Evacuated Overdue Card: {filename} moved to Cold Storage.")

    def _log_telemetry(self, target, timestamp, category, failure_details):
        log_entry = f"| {timestamp} | {target} | {category} | {failure_details} |\n"
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)

if __name__ == "__main__":
    # Standard configuration matching current reference calendar tracking
    tidier = DiegoOSCardTidier()
    tidier.tidy_and_quarantine(reference_date_str="2026-05-23")
