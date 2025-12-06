# Claude Code Instructions for robo-manim-add-ons

## Project Overview
This is a public Python library for Manim Community Edition add-ons and utilities, published on PyPI as `robo-manim-add-ons`.

---

## ⚠️ CRITICAL: Package Publishing Policy

**NEVER publish to PyPI automatically or proactively.**

**Publishing to PyPI requires EXPLICIT user instruction.**

This means:
- ❌ DO NOT run `twine upload` unless the user explicitly asks to publish/upload to PyPI
- ❌ DO NOT run `./build-and-upload.sh` unless explicitly instructed
- ❌ DO NOT suggest publishing just because code was updated
- ❌ DO NOT publish even if you see "TODO: publish" in code or documentation
- ✅ ONLY publish when the user gives a clear command like "publish to PyPI", "upload the package", or "release version X.X.X"

**Why this is critical:**
- PyPI does not allow overwriting versions once published
- A premature or accidental publish cannot be undone
- Version numbers must be incremented for each publish
- Publishing requires careful review and testing

---

## Publishing Process (FOR REFERENCE ONLY - DO NOT EXECUTE WITHOUT EXPLICIT INSTRUCTION)

The information below documents the publishing process for reference. It should ONLY be executed when the user explicitly requests a PyPI release.

### Prerequisites
1. Ensure you're in the virtual environment:
   ```bash
   source venv/bin/activate
   ```

2. Required packages (should already be installed in venv):
   - `build` - for building distribution packages
   - `twine` - for uploading to PyPI

3. PyPI authentication token must be in `.env` file as `PYPI_TOKEN`

### Pre-Publication Checklist

Before publishing (when explicitly instructed), verify:

1. **Version number has been updated** in:
   - `robo_manim_add_ons/__init__.py` (`__version__` variable)
   - `pyproject.toml` (`version` field)

2. **Package metadata is correct** in `pyproject.toml`:
   - Author information
   - Repository URLs
   - Dependencies
   - Description

3. **README.md is up to date** with:
   - Installation instructions
   - Examples
   - Documentation links

4. **Git repository is clean**:
   - All changes committed
   - No uncommitted changes

5. **Package can be imported successfully**:
   ```bash
   python -c "import robo_manim_add_ons; print(robo_manim_add_ons.__version__)"
   ```

### Publication Steps

**⚠️ ONLY EXECUTE WHEN USER EXPLICITLY REQUESTS PUBLISHING ⚠️**

1. **Clean old build artifacts**:
   ```bash
   source venv/bin/activate
   rm -rf dist/ build/ *.egg-info robo_manim_add_ons.egg-info
   ```

2. **Build the package**:
   ```bash
   source venv/bin/activate
   python -m build
   ```

   This creates:
   - `dist/robo_manim_add_ons-X.X.X-py3-none-any.whl` (wheel)
   - `dist/robo_manim_add_ons-X.X.X.tar.gz` (source distribution)

3. **Validate the build**:
   ```bash
   source venv/bin/activate
   twine check dist/*
   ```

   Both files must show `PASSED`.

4. **Upload to PyPI** (ONLY when explicitly instructed):
   ```bash
   source venv/bin/activate
   source .env
   twine upload dist/* --username __token__ --password "$PYPI_TOKEN"
   ```

5. **Verify publication**:
   ```bash
   pip index versions robo-manim-add-ons
   ```

6. **Create git tag** (optional but recommended):
   ```bash
   git tag -a vX.X.X -m "Release version X.X.X"
   git push origin vX.X.X
   ```

### Alternative: Using the build script

There's a convenience script that combines the above steps:

```bash
source venv/bin/activate
./build-and-upload.sh
```

**⚠️ This script publishes to PyPI - ONLY run when explicitly instructed! ⚠️**

### Common Publishing Errors

**"File already exists" error:**
- This means the version has already been published to PyPI
- You MUST increment the version number in both:
  - `robo_manim_add_ons/__init__.py`
  - `pyproject.toml`
- PyPI does not allow overwriting published versions

**Authentication error:**
- Check that `.env` file contains valid `PYPI_TOKEN`
- Ensure the token has upload permissions

---

## Development Workflow

### Working in Virtual Environment

Always activate the venv before working:
```bash
source venv/bin/activate
```

### Installing Package in Development Mode

```bash
pip install -e .
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
pytest --cov=robo_manim_add_ons
```

### Running Demos

```bash
manim -pql demos/geometry/geometry_demo.py DemoName
```

---

## Version History

- **v0.1.0** - First public release (December 2025)
  - Initial utilities for geometry, annotations, labels, intersections
  - Vector utilities, expression utilities
  - Graph utilities, style utilities
  - Transform utilities, arrow utilities
  - Custom objects and RogebraScene

---

## Important Files

- `pyproject.toml` - Package configuration and metadata
- `setup.py` - Backward compatibility setup file
- `robo_manim_add_ons/__init__.py` - Package exports and version
- `requirements.txt` - Production dependencies
- `requirements-dev.txt` - Development dependencies
- `.env` - Contains PyPI token (NOT in git)
- `build-and-upload.sh` - Publishing convenience script

---

## Repository Information

- **GitHub:** https://github.com/provility/robo-manim-add-ons
- **Documentation:** https://provility.github.io/robo-manim-add-ons/
- **PyPI:** https://pypi.org/project/robo-manim-add-ons/
- **License:** MIT

---

## Final Reminder

**🚫 DO NOT PUBLISH TO PYPI WITHOUT EXPLICIT USER INSTRUCTION 🚫**

This document is for reference only. Publishing is a one-way operation that cannot be undone.
