#!/usr/bin/env python3
"""
Fix notebooks that have `metadata.widgets` entries missing the `state` key.

Usage:
  python scripts/fix_notebook_widgets.py [--remove-widgets] [paths...]

If --remove-widgets is set, the script removes the `metadata.widgets` key entirely.
Otherwise it ensures `metadata.widgets['state']` exists (set to an empty dict by default).

It will modify files in-place and print a short summary.
"""
import sys
import json
from pathlib import Path
import argparse


def fix_notebook(path: Path, remove_widgets: bool = False) -> bool:
    changed = False
    with path.open('r', encoding='utf-8') as f:
        try:
            doc = json.load(f)
        except Exception as e:
            print(f"ERROR: could not parse {path}: {e}")
            return False
    meta = doc.get('metadata', {})
    if 'widgets' in meta:
        widgets = meta.get('widgets')
        if remove_widgets:
            del meta['widgets']
            doc['metadata'] = meta
            changed = True
        else:
            # Ensure widgets is a dict and has 'state'
            if not isinstance(widgets, dict):
                print(f"NOTE: metadata.widgets in {path} is not a dict; replacing with {{'state':{{}}}}")
                meta['widgets'] = {'state': {}}
                doc['metadata'] = meta
                changed = True
            else:
                if 'state' not in widgets:
                    widgets['state'] = {}
                    meta['widgets'] = widgets
                    doc['metadata'] = meta
                    changed = True
    # Also walk through cells and ensure widget metadata (rare)
    for cell in doc.get('cells', []):
        cell_meta = cell.get('metadata', {})
        if 'widgets' in cell_meta:
            widgets = cell_meta.get('widgets')
            if remove_widgets:
                del cell_meta['widgets']
                cell['metadata'] = cell_meta
                changed = True
            else:
                if not isinstance(widgets, dict):
                    cell_meta['widgets'] = {'state': {}}
                    cell['metadata'] = cell_meta
                    changed = True
                else:
                    if 'state' not in widgets:
                        widgets['state'] = {}
                        cell_meta['widgets'] = widgets
                        cell['metadata'] = cell_meta
                        changed = True
    if changed:
        # Write back safely
        with path.open('w', encoding='utf-8') as f:
            json.dump(doc, f, indent=2, ensure_ascii=False)
    return changed


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--remove-widgets', action='store_true', help='Remove metadata.widgets entries instead of adding state')
    parser.add_argument('paths', nargs='*', help='Files or directories to process (defaults to current repo root)')
    args = parser.parse_args(argv)
    paths = args.paths or ['.']
    p = Path('.')
    files = []
    for path in paths:
        pathp = Path(path)
        if pathp.is_dir():
            files.extend(sorted(pathp.rglob('*.ipynb')))
        elif pathp.is_file() and pathp.suffix == '.ipynb':
            files.append(pathp)
    if not files:
        print('No .ipynb files found to process.')
        return 0
    total = 0
    fixed = 0
    for fpath in files:
        total += 1
        try:
            if fix_notebook(fpath, remove_widgets=args.remove_widgets):
                print(f'Fixed: {fpath}')
                fixed += 1
        except Exception as e:
            print(f'Error processing {fpath}: {e}')
    print(f'Processed {total} .ipynb files, fixed: {fixed}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
