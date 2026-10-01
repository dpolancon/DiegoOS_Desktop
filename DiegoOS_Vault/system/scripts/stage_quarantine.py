import os
import shutil

def stage_files():
    vault_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    cold_dir = os.path.join(vault_dir, '_Cold_Storage')
    os.makedirs(cold_dir, exist_ok=True)
    
    # 1. Gather legacy cards
    legacy_dir = os.path.join(vault_dir, '02_AREAS', 'Application_Pipeline', 'legacy')
    if os.path.exists(legacy_dir):
        for f in os.listdir(legacy_dir):
            src = os.path.join(legacy_dir, f)
            if os.path.isfile(src) and f.endswith('.md'):
                shutil.move(src, os.path.join(cold_dir, f))
                print(f"[Staged] Legacy: {f} -> _Cold_Storage/")
                
    # 2. Gather Cards
    cards_dir = os.path.join(vault_dir, '02_AREAS', 'Application_Pipeline', 'Cards')
    if os.path.exists(cards_dir):
        for f in os.listdir(cards_dir):
            src = os.path.join(cards_dir, f)
            if os.path.isfile(src) and f.endswith('.md'):
                shutil.move(src, os.path.join(cold_dir, f))
                print(f"[Staged] Card: {f} -> _Cold_Storage/")
                
    # 3. Gather historical logs from 05_ACTIONS/
    actions_dir = os.path.join(vault_dir, '05_ACTIONS')
    if os.path.exists(actions_dir):
        for f in os.listdir(actions_dir):
            # Move only specific daily files and recovery registries, not the folder templates or base configs
            if f.endswith('.md') and (
                any(c.isdigit() for c in f) or 
                "log" in f.lower() or 
                "registry" in f.lower() or
                f == "Today.md"
            ):
                src = os.path.join(actions_dir, f)
                shutil.move(src, os.path.join(cold_dir, f))
                print(f"[Staged] Action/Log: {f} -> _Cold_Storage/")

if __name__ == '__main__':
    stage_files()
