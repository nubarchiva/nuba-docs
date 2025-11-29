#!/usr/bin/env python3
"""
Script para añadir front matter con status a todos los archivos .md
Uso: python scripts/add-frontmatter.py
"""
import os
from pathlib import Path

DOCS_DIR = Path(__file__).parent.parent / 'docs'

# Archivos que deben marcarse como published (contenido listo)
PUBLISHED_FILES = {
    'index.md',
    'installation/index.md',
    'installation/requirements.md',
    'installation/deployment/docker.md',
    'installation/deployment/bare-metal.md',
    'installation/database/postgresql.md',
    'installation/upgrade/index.md',
    'getting-started/index.md',
    'user-guide/index.md',
    'admin-guide/index.md',
    'customization/index.md',
    'changelog/index.md',
    'community.md',
}

def add_frontmatter(filepath: Path, status: str):
    """Añade o actualiza front matter con status."""
    content = filepath.read_text(encoding='utf-8')

    # Si ya tiene front matter, verificar si tiene status
    if content.startswith('---'):
        end = content.find('---', 3)
        if end != -1:
            fm_content = content[3:end]
            if 'status:' in fm_content:
                print(f"  [SKIP] {filepath.relative_to(DOCS_DIR)} - ya tiene status")
                return
            # Añadir status al front matter existente
            new_fm = f"---\nstatus: {status}\n{fm_content.strip()}\n---"
            new_content = new_fm + content[end+3:]
            filepath.write_text(new_content, encoding='utf-8')
            print(f"  [UPDATE] {filepath.relative_to(DOCS_DIR)} -> {status}")
            return

    # No tiene front matter, añadir nuevo
    new_content = f"---\nstatus: {status}\n---\n\n{content}"
    filepath.write_text(new_content, encoding='utf-8')
    print(f"  [ADD] {filepath.relative_to(DOCS_DIR)} -> {status}")

def main():
    print("Añadiendo front matter a archivos .md...\n")

    published_count = 0
    draft_count = 0

    for md_file in DOCS_DIR.rglob('*.md'):
        rel_path = str(md_file.relative_to(DOCS_DIR))

        if rel_path in PUBLISHED_FILES:
            add_frontmatter(md_file, 'published')
            published_count += 1
        else:
            add_frontmatter(md_file, 'draft')
            draft_count += 1

    print(f"\n✅ Completado:")
    print(f"   - {published_count} archivos marcados como 'published'")
    print(f"   - {draft_count} archivos marcados como 'draft'")

if __name__ == '__main__':
    main()
