"""Research V4 package initialization"""

from .ConfigManager import ConfigManager
from .FloraDatabase import FloraDatabase
from .Spider import UniversalResearchSpider, research
from .RagSys import RAGSystem
from .ArtGenSys import EnhancedPlantArticleGenerator
from .UniversalArticleGenerator import UniversalArticleGenerator
from .ApiMonitor import SerpAPIMonitor, check_api_credits, can_start_research

__all__ = [
    'ConfigManager',
    'FloraDatabase',
    'UniversalResearchSpider',
    'research',
    'RAGSystem',
    'EnhancedPlantArticleGenerator',
    'UniversalArticleGenerator',
    'SerpAPIMonitor',
    'check_api_credits',
    'can_start_research'
]

__version__ = '4.0.0'
