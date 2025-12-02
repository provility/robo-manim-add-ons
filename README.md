# Robo Manim Add-ons

A collection of geometry utilities for [Manim Community Edition](https://www.manim.community/).

## Installation

### For Users

Install from PyPI (once published):

```bash
pip install robo-manim-add-ons
```

### For Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/robo-manim-add-ons.git
cd robo-manim-add-ons
```

2. Create and activate a virtual environment:
```bash
# Create venv
python -m venv venv

# Activate on macOS/Linux
source venv/bin/activate

# Activate on Windows
# venv\Scripts\activate
```

3. Install manim and development dependencies:
```bash
pip install -e .
pip install -e ".[dev]"
```

Or install from requirements files:
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Documentation

Full documentation with examples, images, and demo videos:
- **[https://provility.github.io/robo-manim-add-ons/](https://provility.github.io/robo-manim-add-ons/)**

## Quick Start

```python
from manim import *
from robo_manim_add_ons import perp, parallel

class GeometryDemo(Scene):
    def construct(self):
        # Create reference line
        line = Line(LEFT * 2, RIGHT * 2)
        dot = Dot(ORIGIN)

        # Create perpendicular line
        perp_line = perp(line, dot, length=3.0)

        # Create parallel line at different position
        dot2 = Dot(UP)
        parallel_line = parallel(line, dot2, length=2.0)

        self.add(line, dot, dot2, perp_line, parallel_line)
        self.wait()
```

Get help in Python:
```python
import robo_manim_add_ons
robo_manim_add_ons.show_usage()
```

## Running Examples

```bash
# Make sure your venv is activated
source venv/bin/activate

# Run geometry demos
manim -pql examples/geometry_demo.py PerpDemo
manim -pql examples/geometry_demo.py ParallelDemo
manim -pql examples/geometry_demo.py PlacementDemo
```

## Running Tests

```bash
# Make sure your venv is activated
source venv/bin/activate

# Run all tests
pytest

# Run with coverage
pytest --cov=robo_manim_add_ons
```

## Project Structure

```
robo-manim-add-ons/
├── pyproject.toml              # Package configuration
├── setup.py                    # Setup file
├── README.md                   # This file
├── LICENSE                     # MIT License
├── requirements.txt            # Production dependencies
├── requirements-dev.txt        # Development dependencies
├── robo_manim_add_ons/        # Main package
│   ├── __init__.py
│   └── ...
├── tests/                      # Test suite
│   └── test_*.py
└── examples/                   # Usage examples
    └── demo.py
```

## Development Workflow

1. Create and activate venv (see above)
2. Install in editable mode: `pip install -e ".[dev]"`
3. Make your changes
4. Run tests: `pytest`
5. Run examples to verify: `python examples/demo.py`

## Building and Publishing

### Build the package:
```bash
pip install build twine
python -m build
```

### Publish to PyPI:
```bash
twine upload dist/*
```

### Publish to TestPyPI (for testing):
```bash
twine upload --repository testpypi dist/*
```

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
