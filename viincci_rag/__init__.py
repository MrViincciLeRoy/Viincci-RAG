"""
Viincci-RAG: Universal Research & Article Generation System

A professional Python package for multi-domain research, retrieval-augmented
generation (RAG), and article generation.

Usage:
    from viincci_rag import ConfigManager, RAGSystem, UniversalResearchSpider
    
    config = ConfigManager(domain="botany")
    rag = RAGSystem(config)
    spider = UniversalResearchSpider(config)

Or import all:
    from viincci_rag import *
"""

__version__ = "4.0.0"
__author__ = "Viincci Team"
__license__ = "MIT"

# Core classes and utilities (re-exported from V4 for backward compatibility)
try:
    from V4 import (
        ConfigManager,
        FloraDatabase,
        RAGSystem,
        UniversalArticleGenerator,
        UniversalResearchSpider,
        SerpAPIMonitor,
        EnhancedPlantArticleGenerator,
        FloraWikipediaScraper,
    )
except Exception:
    # Fallback stubs if V4 imports fail
    ConfigManager = None
    FloraDatabase = None
    RAGSystem = None
    UniversalArticleGenerator = None
    UniversalResearchSpider = None
    SerpAPIMonitor = None
    EnhancedPlantArticleGenerator = None
    FloraWikipediaScraper = None

__all__ = [
    # Version info
    "__version__",
    "__author__",
    "__license__",
    # Core classes
    "ConfigManager",
    "RAGSystem",
    "UniversalResearchSpider",
    "UniversalArticleGenerator",
    "SerpAPIMonitor",
    # Database and utilities
    "FloraDatabase",
    "EnhancedPlantArticleGenerator",
    "FloraWikipediaScraper",
]
