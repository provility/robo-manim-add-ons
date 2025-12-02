#!/bin/bash

# Build and Upload to PyPI
# This script builds the package and uploads it to PyPI

set -e  # Exit on error

echo "🧹 Cleaning old build artifacts..."
rm -rf dist/ build/ *.egg-info

echo "🔨 Building package..."
python -m build

echo "📦 Uploading to PyPI..."
source .env
twine upload dist/* --username __token__ --password "$PYPI_TOKEN"

echo "✅ Done! Package uploaded to PyPI"
echo "View at: https://pypi.org/project/robo-manim-add-ons/"
