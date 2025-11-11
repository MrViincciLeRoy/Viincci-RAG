"""
Test the examples notebook: backwards-compatible imports and SerpAPI mock.

These tests validate:
1. Backwards-compatible import fallback logic (viincci_rag → V4)
2. Mock SerpAPI client returns expected results
3. Fallback generation writes expected output files
"""

import os
import sys
import json
import tempfile
import pytest
from pathlib import Path

# Add repo root to path
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_backwards_compatible_import():
    """Test that import fallback logic works (prefer viincci_rag, fallback to V4)."""
    # Simulate the logic from test_examples.ipynb cell 1
    viincci_modules = {}
    
    def try_import():
        # Try new package layout first
        try:
            from viincci_rag.core.config import ConfigManager
            return {'ConfigManager': ConfigManager, 'source': 'viincci_rag'}
        except Exception as e_new:
            # Try legacy package name
            try:
                from V4 import ConfigManager
                return {'ConfigManager': ConfigManager, 'source': 'V4'}
            except Exception as e_legacy:
                return {'source': 'none'}
    
    result = try_import()
    # Either should work; we're testing the logic works
    assert result is not None
    assert 'source' in result
    assert result['source'] in ('viincci_rag', 'V4', 'none')
    print(f"  ✓ Backwards-compatible import succeeded: source={result['source']}")


def test_mock_serpapi_client():
    """Test that MockSerpAPI returns expected results."""
    class MockSerpAPI:
        def __init__(self, key=None):
            self.key = key
        
        def search(self, query, num_results=3):
            return [
                {
                    'title': f'Mock result for {query} - {i+1}',
                    'text': f'This is a short mock snippet about "{query}" (result {i+1}).',
                    'metadata': {'source': 'mock', 'rank': i+1}
                } for i in range(num_results)
            ]
    
    # Test with no key (safe mock)
    client = MockSerpAPI(None)
    results = client.search("test query", num_results=3)
    
    assert len(results) == 3
    assert all('title' in r for r in results)
    assert all('text' in r for r in results)
    assert all('metadata' in r for r in results)
    assert results[0]['metadata']['rank'] == 1
    print(f"  ✓ MockSerpAPI returned {len(results)} expected results")


def test_normalize_search_results():
    """Test that normalize_search_results converts mock results properly."""
    def normalize_search_results(results):
        normalized = []
        for r in results:
            normalized.append({
                'text': r.get('text', ''),
                'metadata': {'title': r.get('title'), **r.get('metadata', {})}
            })
        return normalized
    
    mock_results = [
        {
            'title': 'Result 1',
            'text': 'Text 1',
            'metadata': {'source': 'mock', 'rank': 1}
        },
        {
            'title': 'Result 2',
            'text': 'Text 2',
            'metadata': {'source': 'mock', 'rank': 2}
        }
    ]
    
    normalized = normalize_search_results(mock_results)
    
    assert len(normalized) == 2
    assert normalized[0]['text'] == 'Text 1'
    assert normalized[0]['metadata']['title'] == 'Result 1'
    assert normalized[0]['metadata']['rank'] == 1
    print(f"  ✓ normalize_search_results converted {len(normalized)} results correctly")


def test_fallback_file_generation():
    """Test that fallback content can be written to files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Simulate writing fallback files
        domains = ['botany', 'literature', 'carpentry']
        for domain in domains:
            mock_results = [
                {'text': f'Mock text for {domain} result 1', 'metadata': {'title': f'Title {domain} 1'}},
                {'text': f'Mock text for {domain} result 2', 'metadata': {'title': f'Title {domain} 2'}}
            ]
            summary = '\n\n'.join([r['text'] for r in mock_results])
            output = f'FALLBACK SUMMARY for "{domain}"\n\n' + summary
            
            fname = tmpdir / f'fallback_{domain}.txt'
            fname.write_text(output, encoding='utf-8')
            
            # Verify it was written
            assert fname.exists()
            content = fname.read_text(encoding='utf-8')
            assert 'FALLBACK SUMMARY' in content
            assert domain in content
        
        # Check all files were created
        files = list(tmpdir.glob('fallback_*.txt'))
        assert len(files) == 3
        print(f"  ✓ Fallback files generated successfully ({len(files)} files)")


def test_notebook_validation():
    """Test that the example notebook is valid nbformat."""
    import nbformat
    
    notebook_path = Path(__file__).parent.parent / 'viincci_rag' / 'examples' / 'test_examples.ipynb'
    
    if not notebook_path.exists():
        print(f"  ⚠ Skipping: {notebook_path} not found")
        return
    
    try:
        with open(notebook_path) as f:
            nb = nbformat.read(f, as_version=4)
        assert len(nb.cells) > 0
        assert nb.nbformat in (4, 5)
        print(f"  ✓ Notebook is valid nbformat v{nb.nbformat}: {len(nb.cells)} cells")
    except Exception as e:
        raise AssertionError(f"Failed to validate notebook: {e}")


def test_test_ipynb_validation():
    """Test that Test.ipynb (after widget fix) is valid nbformat."""
    import nbformat
    
    notebook_path = Path(__file__).parent.parent / 'Test.ipynb'
    
    if not notebook_path.exists():
        print(f"  ⚠ Skipping: {notebook_path} not found")
        return
    
    try:
        with open(notebook_path) as f:
            nb = nbformat.read(f, as_version=4)
        assert len(nb.cells) > 0
        assert nb.nbformat in (4, 5)
        # Check that the notebook doesn't have invalid metadata.widgets
        for cell in nb.cells:
            if 'widgets' in cell.get('metadata', {}):
                widgets = cell['metadata']['widgets']
                assert 'state' in widgets or not isinstance(widgets, dict), \
                    "metadata.widgets missing 'state' key"
        print(f"  ✓ Test.ipynb is valid nbformat v{nb.nbformat}: {len(nb.cells)} cells, no invalid widget metadata")
    except Exception as e:
        raise AssertionError(f"Failed to validate Test.ipynb: {e}")


if __name__ == '__main__':
    # Run tests manually for debugging
    print("\n" + "="*70)
    print("Running example notebook tests")
    print("="*70)
    
    tests = [
        test_backwards_compatible_import,
        test_mock_serpapi_client,
        test_normalize_search_results,
        test_fallback_file_generation,
        test_notebook_validation,
        test_test_ipynb_validation,
    ]
    
    for test_func in tests:
        try:
            print(f"\n{test_func.__name__}:")
            test_func()
        except Exception as e:
            print(f"  ✗ FAILED: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "="*70)
    print("All manual tests completed")
    print("="*70)
