#!/usr/bin/env python3
"""
main.py - Viincci-RAG Root Entry Point

This module serves as the canonical entry point for Viincci-RAG.
It provides easy access to all core modules and tries to import from the
new viincci_rag package first, then falls back to V4 for backward compatibility.

Usage:
    python main.py
    from main import ConfigManager, RAGSystem
    import main as viincci_rag
"""

import sys
import warnings

# Import and re-export core modules (prefer viincci_rag, fallback to V4)
__version__ = "4.0.0"
__author__ = "Viincci Team"
__license__ = "MIT"

try:
    # Try new viincci_rag package first
    from viincci_rag import (
        ConfigManager,
        RAGSystem,
        UniversalResearchSpider,
        UniversalArticleGenerator,
        SerpAPIMonitor,
        FloraDatabase,
    )
    print("✓ Loaded core modules from viincci_rag (new layout)")
except ImportError as e_viincci:
    try:
        # Fallback to legacy V4 package
        from V4 import (
            ConfigManager,
            RAGSystem,
            UniversalResearchSpider,
            UniversalArticleGenerator,
            SerpAPIMonitor,
            FloraDatabase,
        )
        print("✓ Loaded core modules from V4 (legacy layout - backward compatible)")
    except ImportError as e_v4:
        print(f"Error: Could not import from viincci_rag ({e_viincci}) or V4 ({e_v4})")
        print("\nPlease ensure the package is properly installed:")
        print("  pip install -e .")
        sys.exit(1)

# Import main function from the actual implementation
try:
    from V4.main import main
except ImportError as e:
    print(f"Error: Could not import V4.main module: {e}")
    sys.exit(1)

if __name__ == "__main__":
    main()
