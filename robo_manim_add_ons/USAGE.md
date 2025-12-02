# Robo Manim Add-ons

A collection of geometry utilities for Manim Community Edition.

## Installation

```bash
pip install robo-manim-add-ons
```

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

## Geometry Utilities

```python
from robo_manim_add_ons import perp, parallel, project, reflect

# Create perpendicular line
perp_line = perp(line, dot, length=2.0, placement="mid")

# Create parallel line
parallel_line = parallel(line, dot, length=3.0, placement="start")

# Project point onto line
projection_dot = project(line, point)

# Reflect point across line
reflected_dot = reflect(line, point)
```

**Functions:**
- **perp(line, dot, length, placement="mid")** - Create perpendicular line
- **parallel(line, dot, length, placement="mid")** - Create parallel line
- **project(line, point)** - Project point onto line (returns Dot)
- **reflect(line, point)** - Reflect point across line (returns Dot)

**Placement options:** `"start"`, `"mid"` (default), `"end"`

**Note:** `point` parameter can be a Dot or numpy array

## Full Documentation

For complete API reference with examples, images, and demo videos, visit:

**https://provility.github.io/robo-manim-add-ons/**

## Resources

- **Documentation**: https://provility.github.io/robo-manim-add-ons/
- **GitHub**: https://github.com/provility/robo-manim-add-ons
- **PyPI**: https://pypi.org/project/robo-manim-add-ons/
- **Issues**: https://github.com/provility/robo-manim-add-ons/issues

---

Version: 0.1.0 | License: MIT
