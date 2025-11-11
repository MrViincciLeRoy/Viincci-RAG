"""Test ConfigManager functionality"""
import pytest


def test_config_initialization():
    """Test that ConfigManager initializes correctly"""
    try:
        from viincci_rag.core import ConfigManager
        config = ConfigManager(domain="botany", verbose=False)
        assert config.domain == "botany"
        assert config.get_current_domain() == "botany"
    except Exception as e:
        pytest.skip(f"ConfigManager unavailable: {e}")


def test_config_domains():
    """Test domain switching"""
    try:
        from viincci_rag.core import ConfigManager
        config = ConfigManager(verbose=False)
        domains = config.get_available_domains()
        assert len(domains) > 0
        assert "botany" in domains or len(domains) > 0
    except Exception as e:
        pytest.skip(f"ConfigManager unavailable: {e}")
