#!/usr/bin/env python3
"""
Obsidian Note Splitter & AI Processor
Generalizable utility to ingest a note, split by headers, optionally process with AI,
and output new notes to a target directory (e.g., 08_INBOX).
"""
import os
import re
import argparse
from pathlib import Path
from typing import List, Tuple, Optional
import json

# Optional AI integration
try:
    import openai
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False

class NoteProcessor:
    def __init__(self, vault_root: str, target_dir: str = "08_INBOX", ai_model: Optional[str] = None):
        self.vault_root = Path(vault_root)
        self.target_path = self.vault_root / target_dir
        self.target_path.mkdir(parents=True, exist_ok=True)
        self.ai_model = ai_model
        self.client = openai.OpenAI() if HAS_OPENAI and ai_model else None

    def split_by_headers(self, content: str, header_level: int = 2) -> List[Tuple[str, str]]:
        """Split markdown content by specified header level."""
        pattern = rf'^(#{"#" * header_level} .+)$'
        parts = re.split(pattern, content, flags=re.MULTILINE)
        sections = []
        for i in range(1, len(parts), 2):
            header = parts[i].strip()
            body = parts[i+1].strip() if i+1 < len(parts) else ""
            sections.append((header, body))
        return sections

    def sanitize_filename(self, header: str) -> str:
        """Convert header to safe filename."""
        name = header.lstrip("#").strip()
        name = re.sub(r'[^\w\s-]', '', name).strip()
        name = re.sub(r'[\s]+', '_', name)
        return f"{name}.md"

    def ai_transform(self, header: str, body: str, prompt_template: str) -> str:
        """Optional AI processing step."""
        if not self.client:
            return body
        prompt = prompt_template.format(header=header, content=body)
        try:
            response = self.client.chat.completions.create(
                model=self.ai_model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"⚠️ AI processing failed: {e}")
            return body

    def process_note(self, source_path: str, ai_prompt: Optional[str] = None, dry_run: bool = False) -> List[Path]:
        """Main processing pipeline."""
        source = Path(source_path)
        if not source.exists():
            raise FileNotFoundError(f"Source note not found: {source}")

        content = source.read_text(encoding="utf-8")
        sections = self.split_by_headers(content)
        created = []

        for header, body in sections:
            filename = self.sanitize_filename(header)
            output_path = self.target_path / filename

            final_content = f"{header}\n\n{body}\n"
            if ai_prompt:
                final_content = self.ai_transform(header, body, ai_prompt)

            if not dry_run:
                output_path.write_text(final_content, encoding="utf-8")
            created.append(output_path)

        return created

def main():
    parser = argparse.ArgumentParser(description="Split Obsidian notes by headers and optionally process with AI.")
    parser.add_argument("source", help="Path to source note (relative to vault root)")
    parser.add_argument("--vault", default=".", help="Path to Obsidian vault root")
    parser.add_argument("--target", default="08_INBOX", help="Target directory for output notes")
    parser.add_argument("--ai-model", help="OpenAI model to use (e.g., gpt-4o-mini)")
    parser.add_argument("--prompt-file", help="Path to JSON file containing AI prompt template")
    parser.add_argument("--dry-run", action="store_true", help="Preview output without writing files")
    args = parser.parse_args()

    # Load AI prompt if provided
    ai_prompt = None
    if args.prompt_file:
        with open(args.prompt_file, "r", encoding="utf-8") as f:
            ai_prompt = json.load(f).get("prompt", "")

    processor = NoteProcessor(vault_root=args.vault, target_dir=args.target, ai_model=args.ai_model)
    created = processor.process_note(args.source, ai_prompt=ai_prompt, dry_run=args.dry_run)

    print(f"✅ Processed {len(created)} sections from {args.source}")
    for p in created:
        print(f"   → {p.relative_to(args.vault)}")

if __name__ == "__main__":
    main()