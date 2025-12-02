# Examples

This page provides quick examples to get started with Robo Manim Add-ons.

## Complete Demos Index

For a **comprehensive catalog of all 24+ demonstration scenes** with full code snippets, reference images, and video links, see:

**[COMPLETE DEMOS INDEX](../../DEMOS_INDEX.md)**

The complete index includes all demos organized by category:
- **Geometry Demos:** perp, parallel, placement, dynamic geometry (6 demos)
- **Annotation Demos:** distance markers, labels, hatched regions (7 demos)
- **Labels Demos:** vertex labels, edge labels, dynamic labels (5 demos)
- **Intersection Demos:** line-line and line-circle intersections (6 demos)

---

## Quick Start Examples

### Perpendicular Line Example

```python
from manim import *
from robo_manim_add_ons import perp

class PerpExample(Scene):
    def construct(self):
        # Create a horizontal reference line
        ref_line = Line(LEFT * 3, RIGHT * 3, color=BLUE)

        # Create a dot at origin
        dot = Dot(ORIGIN, color=RED)

        # Create perpendicular line with mid placement
        perp_line = perp(ref_line, dot, length=4.0, placement="mid")
        perp_line.set_color(GREEN)

        # Animate
        self.play(Create(ref_line))
        self.play(Create(dot))
        self.play(Create(perp_line))
        self.wait(2)
```

---

### Parallel Line Example

```python
from manim import *
from robo_manim_add_ons import parallel

class ParallelExample(Scene):
    def construct(self):
        # Create a diagonal reference line
        ref_line = Line(LEFT + DOWN, RIGHT + UP, color=BLUE)

        # Create a dot above the line
        dot = Dot(UP * 2, color=RED)

        # Create parallel line with mid placement
        parallel_line = parallel(ref_line, dot, length=3.0, placement="mid")
        parallel_line.set_color(YELLOW)

        # Animate
        self.play(Create(ref_line))
        self.play(Create(dot))
        self.play(Create(parallel_line))
        self.wait(2)
```

---

### Distance Marker Example

```python
from manim import *
from robo_manim_add_ons import distance_marker

class DistanceExample(Scene):
    def construct(self):
        # Create a triangle
        triangle = Polygon([-2, -1, 0], [2, -1, 0], [0, 2, 0], color=WHITE)

        # Add distance markers on each side
        marker_a = distance_marker(
            [-2, -1, 0], [2, -1, 0],
            label_text="a", color=BLUE, label_offset=0.4
        )

        self.play(Create(triangle))
        self.play(Create(marker_a))
        self.wait(2)
```

---

### Vertex Labels Example

```python
from manim import *
from robo_manim_add_ons import vertex_labels

class VertexLabelsExample(Scene):
    def construct(self):
        # Create a triangle
        triangle = Polygon([-2, -1, 0], [2, -1, 0], [0, 2, 0], color=BLUE)

        # Create vertex labels using always_redraw
        labels = always_redraw(
            lambda: VGroup(*vertex_labels(
                triangle, labels=["A", "B", "C"],
                scale=0.8, color=WHITE, buff=0.3
            ))
        )

        self.play(Create(triangle))
        self.play(FadeIn(labels))

        # Scale the triangle - labels follow!
        self.play(triangle.animate.scale(1.5), run_time=2)
        self.wait()
```

---

### Line Intersection Example

```python
from manim import *
from robo_manim_add_ons import intersect_lines

class IntersectionExample(Scene):
    def construct(self):
        # Create two intersecting lines
        line1 = Line(LEFT * 3, RIGHT * 3, color=BLUE)
        line2 = Line(DOWN * 2, UP * 2, color=GREEN)

        # Find intersection
        intersection_dot = intersect_lines(line1, line2)
        intersection_dot.set_color(RED).scale(1.5)

        self.play(Create(line1))
        self.play(Create(line2))
        self.play(FadeIn(intersection_dot, scale=0.5))
        self.wait(2)
```

---

## Running These Examples

1. Save any example to a file (e.g., `example.py`)
2. Run with Manim:
   ```bash
   manim -pql example.py SceneName
   ```

Quality flags:
- `-pql`: Preview, low quality (fast)
- `-pqm`: Preview, medium quality
- `-pqh`: Preview, high quality

---

## More Resources

- **[Complete Demos Index](../../DEMOS_INDEX.md)** - All 24+ demos with full code, images, and videos
- **[Examples Directory](../../examples/)** - Browse all example files by category
- **[API Documentation](../api/index.md)** - Function reference and parameters
- **[Documentation Home](../)** - Back to main documentation

---
