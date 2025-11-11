#!/usr/bin/env python3
"""
test_v4.py - Backward Compatibility Wrapper
This file maintains compatibility with direct script execution.
The actual implementation is in V4.test_v4 module.
"""

import sys
import warnings

# Warn about deprecation (optional)
warnings.warn(
    "Direct execution of test_v4.py is deprecated. "
    "Please use 'viincci-test' command after installation, "
    "or import from V4.test_v4 module.",
    DeprecationWarning,
    stacklevel=2
)

# Import and delegate to the real implementation
try:
    from V4.test_v4 import main
except ImportError as e:
    print(f"Error: Could not import V4.test_v4 module: {e}")
    print("\nPlease ensure the package is properly installed:")
    print("  pip install -e .")
    sys.exit(1)

if __name__ == "__main__":
    sys.exit(main())