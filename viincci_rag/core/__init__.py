"""Core compatibility package for viincci_rag

This package re-exports core modules from the legacy `V4` package so
imports like `from viincci_rag.core.rag_system import RAGSystem` continue
to work.
"""

from .rag_system import RAGSystem
from .spider import UniversalResearchSpider
from .config import ConfigManager
from .article_generator import UniversalArticleGenerator
from .api_monitor import SerpAPIMonitor

__all__ = [
    "RAGSystem",
    "UniversalResearchSpider",
    "ConfigManager",
    "UniversalArticleGenerator",
    "SerpAPIMonitor",
]
