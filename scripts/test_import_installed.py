#!/usr/bin/env python3
"""
Test import behavior for viincci_rag vs legacy V4.

This script performs two checks:
  1. Import `viincci_rag` as available in the current workspace and report which
     underlying module provides the core classes (file paths).
  2. Simulate an "installed wheel" that still exposes `viincci_rag` but whose
     `__init__` re-exports from `V4` (legacy). We create a temporary fake
     site-packages directory containing such a package, insert it early in
     sys.path, and import `viincci_rag` again to demonstrate the behavior.

Run locally in Codespaces; this does not install anything to global site-packages
and avoids downloading large models.
"""
import importlib
import sys
import types
import tempfile
import os
import shutil
import inspect


def report_loaded_symbols(module_name: str, symbols: list):
    try:
        m = importlib.import_module(module_name)
    except Exception as e:
        print(f"Failed to import {module_name}: {e}")
        return

    print(f"Imported package: {module_name} (path={getattr(m, '__file__', None)})")
    for s in symbols:
        obj = getattr(m, s, None)
        if obj is None:
            print(f"  {s}: <not found>")
            continue
        # If it's a class or function, try to locate its defining file
        try:
            src = inspect.getsourcefile(obj) or inspect.getfile(obj)
        except TypeError:
            src = getattr(obj, '__file__', None)
        print(f"  {s}: {obj} (defined in: {src})")


def import_workspace_then_report():
    # Ensure workspace package is imported (prefer local files)
    for mod in list(sys.modules.keys()):
        if mod.startswith('viincci_rag'):
            del sys.modules[mod]
    print('\n=== Importing viincci_rag from workspace environment ===')
    report_loaded_symbols('viincci_rag', [
        'ConfigManager', 'RAGSystem', 'UniversalResearchSpider', 'UniversalArticleGenerator'
    ])


def simulate_installed_wheel_and_report():
    print('\n=== Simulating installed wheel that re-exports V4 (legacy) ===')
    tmpdir = tempfile.mkdtemp(prefix='fake_sitepkg_')
    pkgdir = os.path.join(tmpdir, 'viincci_rag')
    os.makedirs(pkgdir)

    # Create a minimal __init__ that re-exports from V4 (old behavior)
    init_py = '''# Simulated installed viincci_rag that delegates to legacy V4
try:
    from V4 import ConfigManager, RAGSystem, UniversalResearchSpider, UniversalArticleGenerator
except Exception:
    ConfigManager = None
    RAGSystem = None
    UniversalResearchSpider = None
    UniversalArticleGenerator = None
__all__ = ["ConfigManager", "RAGSystem", "UniversalResearchSpider", "UniversalArticleGenerator"]
'''

    with open(os.path.join(pkgdir, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write(init_py)

    # Insert the fake site-packages dir at the front of sys.path and re-import
    sys.path.insert(0, tmpdir)

    # Remove any previously loaded viincci_rag modules
    for mod in list(sys.modules.keys()):
        if mod.startswith('viincci_rag'):
            del sys.modules[mod]

    try:
        report_loaded_symbols('viincci_rag', [
            'ConfigManager', 'RAGSystem', 'UniversalResearchSpider', 'UniversalArticleGenerator'
        ])
    finally:
        # Clean up: remove the fake path and delete tmpdir
        try:
            sys.path.remove(tmpdir)
        except ValueError:
            pass
        shutil.rmtree(tmpdir)


def main():
    import_workspace_then_report()
    simulate_installed_wheel_and_report()


if __name__ == '__main__':
    main()
