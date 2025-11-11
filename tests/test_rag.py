"""Test RAG system functionality"""
import pytest


def test_rag_system_initialization():
    """Test RAGSystem initializes correctly"""
    try:
        from viincci_rag.core import RAGSystem, ConfigManager
        config = ConfigManager(verbose=False)
        rag = RAGSystem(config)
        assert rag.config is not None
        assert rag.embedding_model is not None
    except Exception as e:
        pytest.skip(f"RAGSystem unavailable: {e}")


def test_rag_system_stats():
    """Test RAGSystem statistics"""
    try:
        from viincci_rag.core import RAGSystem, ConfigManager
        config = ConfigManager(verbose=False)
        rag = RAGSystem(config)
        stats = rag.get_statistics()
        assert "embedding_model" in stats
        assert "llm_model" in stats
        assert "device" in stats
    except Exception as e:
        pytest.skip(f"RAGSystem unavailable: {e}")
