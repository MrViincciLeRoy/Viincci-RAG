"""
Viincci-RAG Root Package Initialization

This file allows importing directly from the repository root:
    from . import ConfigManager, RAGSystem
    import Viincci_RAG as viincci_rag

It prefers viincci_rag imports but falls back to V4 for backward compatibility.
"""

__version__ = "4.0.0"
__author__ = "Viincci Team"
__license__ = "MIT"

# Try to import from viincci_rag first (preferred)
try:
    from viincci_rag import (
        ConfigManager,
        RAGSystem,
        UniversalResearchSpider,
        UniversalArticleGenerator,
        SerpAPIMonitor,
        FloraDatabase,
    )
except Exception as e_viincci:
    # Fallback to V4 for backward compatibility
    try:
        from V4 import (
            ConfigManager,
            RAGSystem,
            UniversalResearchSpider,
            UniversalArticleGenerator,
            SerpAPIMonitor,
            FloraDatabase,
        )
    except Exception as e_v4:
        ConfigManager = None
        RAGSystem = None
        UniversalResearchSpider = None
        UniversalArticleGenerator = None
        SerpAPIMonitor = None
        FloraDatabase = None

__all__ = [
    "__version__",
    "__author__",
    "__license__",
    "ConfigManager",
    "RAGSystem",
    "UniversalResearchSpider",
    "UniversalArticleGenerator",
    "SerpAPIMonitor",
    "FloraDatabase",
]
