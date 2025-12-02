# Quick Setup Guide

This guide will help you set up your development environment with a virtual environment (venv) and install Manim for testing.

## Step 1: Create Virtual Environment

```bash
# Create venv
python3 -m venv venv

# Activate venv (macOS/Linux)
source venv/bin/activate

# Your prompt should now show (venv)
```

## Step 2: Upgrade pip

```bash
pip install --upgrade pip
```

## Step 3: Install Manim and Dependencies

Install Manim Community Edition along with your package in development mode:

```bash
# Install your package in editable mode with all dependencies
pip install -e .

# Or install from requirements files
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Step 4: Verify Installation

Test that everything is installed correctly:

```bash
# Check manim version
manim --version

# Check that your package is importable
python -c "from robo_manim_add_ons import CustomCircle; print('Import successful!')"

# Run tests
pytest
```

## Step 5: Run the Demo

```bash
# Run the demo scene (preview quality, low resolution)
manim -pql examples/demo.py DemoScene

# Or high quality
manim -pqh examples/demo.py DemoScene
```

## Quality Flags Explained

- `-p`: Preview (open video after rendering)
- `-q`: Quality flag
  - `l`: Low quality (480p, 15fps) - fast for testing
  - `m`: Medium quality (720p, 30fps)
  - `h`: High quality (1080p, 60fps)
  - `k`: 4K quality (2160p, 60fps)

## Common Commands

```bash
# Activate venv
source venv/bin/activate

# Deactivate venv
deactivate

# Run tests
pytest

# Run tests with coverage
pytest --cov=robo_manim_add_ons

# Format code with black
black robo_manim_add_ons/ tests/

# Check code style
flake8 robo_manim_add_ons/ tests/

# Build package
python -m build
```

## Troubleshooting

### Manim system dependencies

If Manim fails to install, you may need to install system dependencies first:

**macOS:**
```bash
brew install cairo ffmpeg pango pkg-config scipy
```

**Ubuntu/Debian:**
```bash
sudo apt-get install build-essential python3-dev libcairo2-dev libpango1.0-dev ffmpeg
```

**Windows:**
Follow the Manim installation guide at https://docs.manim.community/en/stable/installation/windows.html

### Virtual environment not activating

Make sure you're in the project root directory and use the correct activation command for your OS.

### Import errors

Make sure:
1. Your venv is activated (you should see `(venv)` in your prompt)
2. You've installed the package with `pip install -e .`
3. You're running Python from within the venv

## Next Steps

1. Modify `robo_manim_add_ons/custom_mobjects.py` to add your own custom Manim objects
2. Add new modules to the `robo_manim_add_ons/` directory
3. Write tests in the `tests/` directory
4. Create examples in the `examples/` directory
5. Update the README.md with information about your add-ons

Happy animating!
