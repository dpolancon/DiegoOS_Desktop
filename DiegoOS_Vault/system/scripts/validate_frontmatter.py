#!/usr/bin/env python3
import argparse
import os
import re
import sys

try:
    import yaml
except ImportError:
    yaml = None


FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)


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


def iter_markdown_files(vault_dir):
    excluded_roots = {
        os.path.join(vault_dir, "_Cold_Storage"),
        os.path.join(vault_dir, ".git"),
        os.path.join(vault_dir, ".obsidian", "plugins"),
        os.path.join(vault_dir, ".obsidian", "themes"),
    }

    for root, dirs, files in os.walk(vault_dir):
        root_abs = os.path.abspath(root)
        dirs[:] = [
            d for d in dirs
            if os.path.abspath(os.path.join(root_abs, d)) not in excluded_roots
        ]
        if any(root_abs == excluded or root_abs.startswith(excluded + os.sep) for excluded in excluded_roots):
            continue

        for filename in files:
            if filename.endswith(".md"):
                yield os.path.join(root_abs, filename)


def validate_file(path, vault_dir):
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        content = handle.read()

    match = FRONTMATTER_RE.match(content)
    if not match:
        return None

    yaml_text = match.group(1)
    try:
        parsed = yaml.safe_load(yaml_text) if yaml_text.strip() else {}
    except Exception as exc:
        return f"{os.path.relpath(path, vault_dir)}: {exc}"

    if parsed is not None and not isinstance(parsed, dict):
        return f"{os.path.relpath(path, vault_dir)}: frontmatter root is {type(parsed).__name__}, expected mapping"

    return None


def main():
    parser = argparse.ArgumentParser(description="Validate YAML frontmatter in active DiegoOS vault markdown files.")
    parser.add_argument("--vault-dir", default=find_default_vault_dir(), help="Path to the vault root directory")
    args = parser.parse_args()
    args.vault_dir = os.path.abspath(os.path.expanduser(args.vault_dir))

    if yaml is None:
        print("[!] PyYAML is not available; cannot validate with a normal YAML parser.")
        return 2

    if not os.path.isdir(args.vault_dir):
        print(f"[!] Vault directory does not exist: {args.vault_dir}")
        return 2

    errors = []
    checked = 0
    with_frontmatter = 0
    for path in iter_markdown_files(args.vault_dir):
        checked += 1
        result = validate_file(path, args.vault_dir)
        if result is not None:
            errors.append(result)
        else:
            with open(path, "r", encoding="utf-8", errors="replace") as handle:
                if FRONTMATTER_RE.match(handle.read()):
                    with_frontmatter += 1

    if errors:
        print(f"[!] Frontmatter validation failed: {len(errors)} error(s)")
        for error in errors:
            print(f" - {error}")
        return 1

    print(f"[+] Frontmatter validation passed: {with_frontmatter} frontmatter block(s), {checked} active markdown file(s) checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
