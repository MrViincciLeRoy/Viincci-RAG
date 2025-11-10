#!/usr/bin/env python3
"""
research_cli.py - Command Line Interface for Universal Research System V4
Easily perform research in any domain with API monitoring
"""

import argparse
import sys
from pathlib import Path

try:
    from V4.ConfigManager import ConfigManager
    from V4.Spider import UniversalResearchSpider, research
    from V4.ApiMonitor import SerpAPIMonitor, check_api_credits
    from V4.RagSys import RAGSystem
except ImportError as e:
    print(f"❌ Error: Could not import required modules: {e}")
    print("Please ensure the V4 package is properly installed")
    sys.exit(1)


def list_domains(config: ConfigManager):
    """List available research domains."""
    print("\n" + "="*70)
    print("🌐 Available Research Domains")
    print("="*70 + "\n")
    
    for domain in config.get_available_domains():
        info = config.get_domain_info(domain)
        current = " ⭐ (CURRENT)" if domain == config.get_current_domain() else ""
        
        print(f"🔹 {domain}{current}")
        print(f"   {info.get('description', 'No description')}")
        keywords = info.get('keywords', [])
        if keywords:
            print(f"   Keywords: {', '.join(keywords[:5])}")
        print()


def check_credits(config: ConfigManager):
    """Check SerpAPI credits."""
    monitor = SerpAPIMonitor(config)
    status = monitor.check_credits(verbose=True)
    return status['can_proceed']


def perform_research(query: str, domain: str, config: ConfigManager, use_rag: bool = False):
    """Perform research with optional RAG analysis."""
    print(f"\n🔍 Starting research...")
    print(f"   Query: {query}")
    print(f"   Domain: {domain}\n")
    
    # Switch to requested domain
    config.switch_domain(domain)
    
    # Perform research
    spider = UniversalResearchSpider(config, check_credits=True)
    sources = spider.research(query, estimate_first=True)
    
    if not sources:
        print("\n❌ No sources found or insufficient API credits")
        return
    
    print(f"\n✅ Research complete! Found {len(sources)} sources")
    
    # RAG Analysis (optional)
    if use_rag and len(sources) > 0:
        print("\n🤖 Performing RAG analysis...")
        
        try:
            rag = RAGSystem(config)
            
            # Build index from sources
            texts = [s['text'] for s in sources]
            metadata = [s['metadata'] for s in sources]
            
            rag.build_index(texts, metadata)
            
            # Load LLM
            print("   Loading LLM model (this may take a moment)...")
            rag.load_llm()
            
            # Get domain questions
            questions = config.get_domain_questions()[:3]  # Top 3 questions
            
            print("\n📝 AI Insights:\n")
            
            for i, question in enumerate(questions, 1):
                full_question = f"{query} - {question}"
                print(f"{i}. {question}")
                print("   " + "-"*60)
                
                result = rag.query(full_question, k=5, max_new_tokens=300)
                answer = result['answer'][:500]  # Limit output
                
                print(f"   {answer}")
                print()
            
            print("✅ RAG analysis complete")
            
        except Exception as e:
            print(f"\n⚠️  RAG analysis failed: {str(e)}")
            print("   Research results still saved to file")


def show_domain_info(domain: str, config: ConfigManager):
    """Show detailed information about a specific domain."""
    if domain not in config.get_available_domains():
        print(f"\n❌ Domain '{domain}' not found")
        return
    
    info = config.get_domain_info(domain)
    
    print("\n" + "="*70)
    print(f"🔬 Domain: {domain.upper()}")
    print("="*70)
    print(f"\nName: {info.get('name', 'N/A')}")
    print(f"Description: {info.get('description', 'N/A')}")
    
    print("\n📚 Primary Sources:")
    for source in info.get('primary_sources', []):
        print(f"  • {source.replace('_', ' ').title()}")
    
    print("\n❓ Research Questions:")
    for i, question in enumerate(info.get('questions', []), 1):
        print(f"  {i}. {question}")
    
    print("\n🔑 Keywords:")
    keywords = info.get('keywords', [])
    if keywords:
        print(f"  {', '.join(keywords)}")
    else:
        print("  No keywords defined")
    
    print("\n" + "="*70 + "\n")


def test_system(config: ConfigManager):
    """Run system tests to verify everything is working."""
    print("\n" + "="*70)
    print("🧪 System Test - Universal Research System V4")
    print("="*70 + "\n")
    
    tests_passed = 0
    tests_failed = 0
    
    # Test 1: Configuration
    print("1. Testing Configuration...")
    try:
        domains = config.get_available_domains()
        assert len(domains) > 0, "No domains available"
        print(f"   ✅ Found {len(domains)} domains")
        tests_passed += 1
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        tests_failed += 1
    
    # Test 2: Domain Switching
    print("\n2. Testing Domain Switching...")
    try:
        original_domain = config.get_current_domain()
        test_domain = 'medical' if original_domain != 'medical' else 'botany'
        
        config.switch_domain(test_domain)
        assert config.get_current_domain() == test_domain
        config.switch_domain(original_domain)
        
        print(f"   ✅ Successfully switched domains")
        tests_passed += 1
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        tests_failed += 1
    
    # Test 3: API Monitor
    print("\n3. Testing API Monitor...")
    try:
        monitor = SerpAPIMonitor(config)
        assert monitor.warning_threshold == 100
        assert monitor.critical_threshold == 20
        print(f"   ✅ API Monitor initialized correctly")
        tests_passed += 1
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        tests_failed += 1
    
    # Test 4: RAG System
    print("\n4. Testing RAG System...")
    try:
        rag = RAGSystem(config)
        assert rag.embedding_model is not None
        
        # Test index building
        test_texts = ["Test document 1", "Test document 2"]
        test_metadata = [{"source": "test1"}, {"source": "test2"}]
        rag.build_index(test_texts, test_metadata)
        
        assert rag.index.ntotal == 2
        print(f"   ✅ RAG System working correctly")
        tests_passed += 1
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        tests_failed += 1
    
    # Test 5: Article Generator
    print("\n5. Testing Article Generator...")
    try:
        from V4.UniversalArticleGenerator import UniversalArticleGenerator
        generator = UniversalArticleGenerator(config, fetch_images=False)
        assert generator is not None
        
        sections = generator.get_domain_sections("Test Topic")
        assert len(sections) > 0
        print(f"   ✅ Article Generator initialized")
        tests_passed += 1
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        tests_failed += 1
    
    # Summary
    print("\n" + "="*70)
    print(f"Test Results: {tests_passed} passed, {tests_failed} failed")
    print("="*70 + "\n")
    
    if tests_failed == 0:
        print("✅ All systems operational!\n")
        return True
    else:
        print("⚠️  Some tests failed. Check the output above.\n")
        return False


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Universal Research System V4 - Multi-Domain Research with API Monitoring",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # List available domains
  python research_cli.py --list-domains
  
  # Show information about a domain
  python research_cli.py --domain-info medical
  
  # Check API credits
  python research_cli.py --check-credits
  
  # Test the system
  python research_cli.py --test
  
  # Research in botany domain
  python research_cli.py -q "Rosa rubiginosa" -d botany
  
  # Research in medical domain with RAG analysis
  python research_cli.py -q "diabetes mellitus" -d medical --rag
  
  # Research in mathematics domain
  python research_cli.py -q "Pythagorean theorem" -d mathematics
  
  # Research in carpentry domain
  python research_cli.py -q "dovetail joints" -d carpentry
        """
    )
    
    parser.add_argument(
        '-q', '--query',
        type=str,
        help='Research query/topic'
    )
    
    parser.add_argument(
        '-d', '--domain',
        type=str,
        default='botany',
        help='Research domain (default: botany)'
    )
    
    parser.add_argument(
        '--list-domains',
        action='store_true',
        help='List all available research domains'
    )
    
    parser.add_argument(
        '--domain-info',
        type=str,
        metavar='DOMAIN',
        help='Show detailed information about a specific domain'
    )
    
    parser.add_argument(
        '--check-credits',
        action='store_true',
        help='Check SerpAPI credit status'
    )
    
    parser.add_argument(
        '--test',
        action='store_true',
        help='Run system tests to verify everything is working'
    )
    
    parser.add_argument(
        '--rag',
        action='store_true',
        help='Perform RAG analysis with LiquidAI (requires GPU/powerful CPU)'
    )
    
    parser.add_argument(
        '--no-credit-check',
        action='store_true',
        help='Skip API credit checking (not recommended)'
    )
    
    parser.add_argument(
        '--config-dir',
        type=str,
        help='Custom configuration directory'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Verbose output'
    )
    
    args = parser.parse_args()
    
    # Initialize config
    try:
        config = ConfigManager(
            config_dir=args.config_dir,
            domain=args.domain,
            verbose=args.verbose
        )
    except Exception as e:
        print(f"❌ Error initializing configuration: {e}")
        sys.exit(1)
    
    # Handle commands
    if args.list_domains:
        list_domains(config)
        return
    
    if args.domain_info:
        show_domain_info(args.domain_info, config)
        return
    
    if args.check_credits:
        can_proceed = check_credits(config)
        sys.exit(0 if can_proceed else 1)
    
    if args.test:
        success = test_system(config)
        sys.exit(0 if success else 1)
    
    if not args.query:
        parser.print_help()
        print("\n💡 Tip: Use --test to verify your system is working correctly")
        print("💡 Tip: Use --list-domains to see available research domains")
        sys.exit(0)
    
    # Validate domain
    if args.domain not in config.get_available_domains():
        print(f"\n❌ Error: Unknown domain '{args.domain}'")
        print("\nAvailable domains:")
        for d in config.get_available_domains():
            print(f"  • {d}")
        sys.exit(1)
    
    # Check credits unless disabled
    if not args.no_credit_check:
        if not check_credits(config):
            print("\n⚠️  Insufficient API credits. Use --no-credit-check to override (not recommended)")
            sys.exit(1)
    
    # Perform research
    try:
        perform_research(args.query, args.domain, config, use_rag=args.rag)
    except KeyboardInterrupt:
        print("\n\n⚠️  Research interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
