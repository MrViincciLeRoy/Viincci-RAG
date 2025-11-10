#!/usr/bin/env python3
"""
research_cli.py - Command Line Interface for Universal Research System V4
Easily perform research in any domain with API monitoring
"""

import argparse
import sys
from pathlib import Path

try:
    from v4.ConfigManager import ConfigManager
    from v4.EnhancedSpider import UniversalResearchSpider, research
    from v4.ApiMonitor import SerpAPIMonitor, check_api_credits
    from FlaskApp.services.v4.RagSys import RAGSystem
except ImportError:
    print("❌ Error: Could not import required modules")
    print("Please ensure the FlaskApp package is properly installed")
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
        print(f"   Keywords: {', '.join(info.get('keywords', [])[:5])}")
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


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Universal Research System V4 - Multi-Domain Research with API Monitoring",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # List available domains
  python research_cli.py --list-domains
  
  # Check API credits
  python research_cli.py --check-credits
  
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
        '--check-credits',
        action='store_true',
        help='Check SerpAPI credit status'
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
    config = ConfigManager(
        config_dir=args.config_dir,
        domain=args.domain,
        verbose=args.verbose
    )
    
    # Handle commands
    if args.list_domains:
        list_domains(config)
        return
    
    if args.check_credits:
        check_credits(config)
        return
    
    if not args.query:
        parser.print_help()
        print("\n❌ Error: Please provide a query with -q/--query")
        sys.exit(1)
    
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
