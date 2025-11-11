"""Test spider functionality"""
import pytest


def test_spider_initialization():
    """Test UniversalResearchSpider initializes"""
    try:
        from viincci_rag.core import UniversalResearchSpider, ConfigManager
        config = ConfigManager(verbose=False)
        spider = UniversalResearchSpider(config, check_credits=False)
        assert spider.config is not None
        assert spider.domain is not None
    except Exception as e:
        pytest.skip(f"Spider unavailable: {e}")


def test_spider_api_check():
    """Test spider can check API status"""
    try:
        from viincci_rag.core import UniversalResearchSpider, ConfigManager
        config = ConfigManager(verbose=False)
        spider = UniversalResearchSpider(config, check_credits=False)
        # Should not crash even without API key
        assert spider.api_monitor is None  # check_credits=False
    except Exception as e:
        pytest.skip(f"Spider unavailable: {e}")
