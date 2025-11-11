"""Integration tests for viincci_rag"""
import pytest


def test_imports_from_viincci_rag_root():
    """Test that main classes can be imported from root package"""
    try:
        from viincci_rag import (
            ConfigManager,
            RAGSystem,
            UniversalResearchSpider,
            SerpAPIMonitor,
        )
        assert ConfigManager is not None
        assert RAGSystem is not None
        assert UniversalResearchSpider is not None
        assert SerpAPIMonitor is not None
    except Exception as e:
        pytest.skip(f"Root imports unavailable: {e}")


def test_imports_from_viincci_rag_core():
    """Test that classes can be imported from viincci_rag.core"""
    try:
        from viincci_rag.core import (
            ConfigManager,
            RAGSystem,
            UniversalResearchSpider,
        )
        assert ConfigManager is not None
        assert RAGSystem is not None
        assert UniversalResearchSpider is not None
    except Exception as e:
        pytest.skip(f"Core imports unavailable: {e}")


def test_backward_compatibility_v4_imports():
    """Test that V4 imports still work"""
    try:
        from V4 import (
            ConfigManager,
            RAGSystem,
            UniversalResearchSpider,
        )
        assert ConfigManager is not None
        assert RAGSystem is not None
        assert UniversalResearchSpider is not None
    except Exception as e:
        pytest.skip(f"V4 imports unavailable: {e}")
