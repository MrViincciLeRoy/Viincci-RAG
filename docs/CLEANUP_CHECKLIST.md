# 🧹 Cleanup Checklist - Post-Restructuring

After verifying that the new `viincci_rag` package structure is working correctly and all tests pass, use this checklist to clean up legacy files.

## ⚠️ Before You Start

**IMPORTANT**: 
- ✅ Run all tests first: `pytest tests/`
- ✅ Verify imports work: `python -c "from viincci_rag import *; print('OK')"`
- ✅ Commit your changes to git: `git add . && git commit -m 'Restructuring complete'`
- ✅ Have a backup or clean git history in case rollback is needed

## 📋 Cleanup Steps

### Phase 1: Verify Nothing is Broken (MUST DO)

```bash
# Run all tests
pytest tests/ -v

# Test all import methods
python -c "from V4 import *; from viincci_rag import *; print('✅ All imports work')"

# Verify package can be installed
pip install -e .

# Verify standard import
python -c "from viincci_rag import ConfigManager, RAGSystem; print('✅ Package imports work')"
```

**Status**: All tests passing? → Continue to Phase 2
**Status**: Tests failing? → STOP! Do NOT proceed. Fix tests first.

### Phase 2: Delete Legacy Test Files

Once you're confident the new tests in `tests/` are comprehensive:

```bash
# Delete old V4 test files
rm V4/test_v4.py
rm test_v4.py

# Verify tests still pass with new test suite
pytest tests/ -v
```

**Safe to Delete**:
- ✅ `V4/test_v4.py` - Moved to `tests/`
- ✅ `test_v4.py` - Moved to `tests/`

### Phase 3: Delete Legacy Setup/Config Files

These are superseded by `pyproject.toml`:

```bash
# Delete old setup files (already covered by pyproject.toml)
rm setup_py.py
```

**Safe to Delete**:
- ✅ `setup_py.py` - Superseded by `pyproject.toml` with proper packaging
- ⚠️ `setup.py` - Only if you're using `pyproject.toml` exclusively
  - Check: `cat pyproject.toml | grep "build-system"` → If modern, can delete

### Phase 4: Delete Legacy Reference/Research Files

These were original planning documents:

```bash
# Delete the old restructuring guides (now in docs/)
# They have been moved to docs/ so originals are no longer needed

# These were planning/reference documents
rm htmlcov/ -rf  # Old test coverage report

# Only if old, no longer needed:
rm main.py  # Was this used? Verify first!
rm research_cli.py  # Check if replaced by CLI entry points
```

**Evaluate Before Deleting**:
- ⚠️ `main.py` - Was this an entry point? Check git history
- ⚠️ `research_cli.py` - Is this replaced by CLI entry points in pyproject.toml?
- ✅ `htmlcov/` - Old coverage reports (can regenerate with `pytest --cov`)

### Phase 5: Verify V4 Backward Compatibility Files

Keep these - they're essential for backward compatibility:

```bash
# KEEP THESE - They're your backward compatibility layer
# V4/ (entire directory)
# viincci_rag/ (your new package)
# viincci_rag/core/ (wrappers)
```

**DO NOT DELETE**:
- ❌ `V4/` - Needed for backward compatibility
- ❌ `viincci_rag/` - Your new package structure
- ❌ `V4/__init__.py` - Re-exports everything

### Phase 6: Clean Up Documentation

Documentation is now in `docs/` - the root only needs README.md:

```bash
# These have been moved to docs/, so if they're still in root, delete them
# (You already moved them, so verify they're gone from root)

ls -la *.md  # Should only show: README.md

# If any old .md files are still in root (shouldn't be), delete:
# rm RESTRUCTURING_COMPLETE.md (already moved to docs/)
# rm MIGRATION.md (already moved to docs/)
# etc.
```

**Safe to Delete from Root**:
- ✅ All `.md` files except `README.md` (moved to `docs/`)
- ✅ Old documentation should be in `docs/` folder

## 📊 Full Cleanup Command Sequence

Once all checks pass:

```bash
# Step 1: Run comprehensive tests
pytest tests/ -v --cov=viincci_rag

# Step 2: Verify imports
python << 'EOF'
from viincci_rag import ConfigManager, RAGSystem, UniversalResearchSpider
from V4 import ConfigManager as CM2
print("✅ All imports work correctly")
EOF

# Step 3: Delete legacy test files
rm V4/test_v4.py test_v4.py

# Step 4: Delete old setup/config files  
rm setup_py.py

# Step 5: Clean old reports/artifacts
rm -rf htmlcov/ __pycache__ .pytest_cache

# Step 6: Verify structure is clean
ls -la | grep -E "\.py|\.toml|\.txt|\.md" | head -20

# Step 7: Final git commit
git add -A
git commit -m "Cleanup: Removed legacy files after restructuring"
```

## ✅ Final Verification Checklist

After cleanup, verify everything still works:

```bash
# ✅ Tests still pass
pytest tests/

# ✅ Can install package
pip install -e .

# ✅ Imports work (V4)
python -c "from V4 import *"

# ✅ Imports work (new)
python -c "from viincci_rag import *"

# ✅ Import all works
python -c "from viincci_rag import *; print(ConfigManager)"

# ✅ Git is clean
git status
```

## 📁 Post-Cleanup Structure

After cleanup, your root should look like:

```
.
├── README.md                    # ✅ Main documentation (KEEP)
├── LICENSE                      # ✅ License (KEEP)
├── pyproject.toml              # ✅ Project config (KEEP)
├── requirements.txt            # ✅ Dependencies (KEEP)
│
├── viincci_rag/                # ✅ New package (KEEP)
├── V4/                         # ✅ Old package (KEEP for compatibility)
├── tests/                      # ✅ Test suite (KEEP)
├── docs/                       # ✅ Documentation (KEEP)
│
├── .gitignore                  # ✅ Git config (KEEP)
├── .github/                    # ✅ GitHub workflows (KEEP)
│
# Deleted in Phase 2:
# ✅ V4/test_v4.py (DELETED)
# ✅ test_v4.py (DELETED)
#
# Deleted in Phase 3:
# ✅ setup_py.py (DELETED)
#
# Deleted in Phase 4:
# ✅ htmlcov/ (DELETED)
```

## 🔄 Rollback Plan

If something breaks after cleanup:

```bash
# Restore from git
git reset --hard HEAD~1

# Or restore specific files
git checkout HEAD -- V4/test_v4.py test_v4.py setup_py.py

# Reinstall
pip install -e .

# Retest
pytest tests/
```

## 🚀 After Cleanup

Your project is now:
- ✅ **Streamlined**: Only necessary files in root
- ✅ **Professional**: Clean structure following Python best practices
- ✅ **Maintainable**: Clear separation of concerns
- ✅ **Backward Compatible**: All old imports still work
- ✅ **Future-Ready**: Can publish to PyPI

### Next Steps:
1. Consider releasing v4.0.0 after major restructuring
2. Update CI/CD pipelines if needed
3. Document breaking changes (if any) in CHANGELOG
4. Plan Phase 2 migration (moving logic from V4 to viincci_rag)

## 📞 Questions?

See `docs/MIGRATION.md` for detailed information about the restructuring.

---

**Remember**: This checklist is provided as guidance. Always test thoroughly before deleting anything!
