# Robo Manim Add-ons Documentation

Welcome to the official documentation for **Robo Manim Add-ons** - a collection of geometry utilities for [Manim Community Edition](https://www.manim.community/).

## Quick Start

### Installation

```bash
pip install robo-manim-add-ons
```

### Basic Usage

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

## Documentation

- **[API Reference](api/)** - Complete API documentation with examples
- **[Examples](examples/)** - Example scenes and usage patterns
- **[GitHub Repository](https://github.com/provility/robo-manim-add-ons)** - Source code and issues

## Features

- Geometry utilities for perpendicular and parallel lines
- Flexible placement options (start, mid, end)
- Easy-to-use API
- Fully documented with examples and demo videos

## Help & Support

- **View API Help in Python:**
  ```python
  import robo_manim_add_ons
  robo_manim_add_ons.show_usage()
  ```

- **PyPI Package:** [robo-manim-add-ons](https://pypi.org/project/robo-manim-add-ons/)
- **Issues:** [GitHub Issues](https://github.com/provility/robo-manim-add-ons/issues)

## License

MIT License - see [LICENSE](https://github.com/provility/robo-manim-add-ons/blob/main/LICENSE) file for details.
