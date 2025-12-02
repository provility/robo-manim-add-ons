# Examples

This page contains example scenes demonstrating the usage of Robo Manim Add-ons geometry utilities.

## Perpendicular Line Example

```python
from manim import *
from robo_manim_add_ons import perp

class PerpExample(Scene):
    def construct(self):
        # Create a horizontal reference line
        ref_line = Line(LEFT * 3, RIGHT * 3, color=BLUE)
        ref_line_label = Text("Reference Line", font_size=24).next_to(ref_line, DOWN)

        # Create a dot at origin
        dot = Dot(ORIGIN, color=RED)
        dot_label = Text("Dot", font_size=20).next_to(dot, UP, buff=0.2)

        # Create perpendicular line with mid placement
        perp_line = perp(ref_line, dot, length=4.0, placement="mid")
        perp_line.set_color(GREEN)
        perp_label = Text("Perpendicular Line", font_size=24).next_to(perp_line, RIGHT)

        # Animate
        self.play(Create(ref_line), Write(ref_line_label))
        self.wait(0.5)
        self.play(Create(dot), Write(dot_label))
        self.wait(0.5)
        self.play(Create(perp_line), Write(perp_label))
        self.wait(2)
```

**Output:**

<video width="640" height="480" controls>
  <source src="../videos/perp_example.mp4" type="video/mp4">
</video>

---

## Parallel Line Example

```python
from manim import *
from robo_manim_add_ons import parallel

class ParallelExample(Scene):
    def construct(self):
        # Create a diagonal reference line
        ref_line = Line(LEFT + DOWN, RIGHT + UP, color=BLUE)
        ref_line_label = Text("Reference Line", font_size=24).next_to(ref_line, LEFT, buff=0.3)

        # Create a dot above the line
        dot = Dot(UP * 2, color=RED)
        dot_label = Text("Dot", font_size=20).next_to(dot, UP, buff=0.2)

        # Create parallel line with mid placement
        parallel_line = parallel(ref_line, dot, length=3.0, placement="mid")
        parallel_line.set_color(YELLOW)
        parallel_label = Text("Parallel Line", font_size=24).next_to(parallel_line, RIGHT, buff=0.3)

        # Animate
        self.play(Create(ref_line), Write(ref_line_label))
        self.wait(0.5)
        self.play(Create(dot), Write(dot_label))
        self.wait(0.5)
        self.play(Create(parallel_line), Write(parallel_label))
        self.wait(2)
```

**Output:**

<video width="640" height="480" controls>
  <source src="../videos/parallel_example.mp4" type="video/mp4">
</video>

---

## Placement Options Example

```python
from manim import *
from robo_manim_add_ons import perp

class PlacementExample(Scene):
    def construct(self):
        # Create horizontal reference line
        ref_line = Line(LEFT * 4, RIGHT * 4, color=BLUE)
        ref_label = Text("Reference", font_size=20).next_to(ref_line, DOWN, buff=0.3)

        # Create three dots at different heights
        dot_mid = Dot(ORIGIN, color=RED)
        dot_start = Dot(UP * 2, color=GREEN)
        dot_end = Dot(DOWN * 2, color=YELLOW)

        # Labels for dots
        label_mid = Text('placement="mid"', font_size=18).next_to(dot_mid, LEFT, buff=0.5)
        label_start = Text('placement="start"', font_size=18).next_to(dot_start, LEFT, buff=0.5)
        label_end = Text('placement="end"', font_size=18).next_to(dot_end, LEFT, buff=0.5)

        # Create perpendicular lines with different placements
        perp_mid = perp(ref_line, dot_mid, 2.0, placement="mid").set_color(RED)
        perp_start = perp(ref_line, dot_start, 2.0, placement="start").set_color(GREEN)
        perp_end = perp(ref_line, dot_end, 2.0, placement="end").set_color(YELLOW)

        # Show all elements
        self.play(Create(ref_line), Write(ref_label))
        self.wait(0.5)

        self.play(Create(dot_mid), Write(label_mid))
        self.play(Create(perp_mid))
        self.wait(1)

        self.play(Create(dot_start), Write(label_start))
        self.play(Create(perp_start))
        self.wait(1)

        self.play(Create(dot_end), Write(label_end))
        self.play(Create(perp_end))
        self.wait(2)
```

**Output:**

<video width="640" height="480" controls>
  <source src="../videos/placement_example.mp4" type="video/mp4">
</video>

---

## Combined Example

```python
from manim import *
from robo_manim_add_ons import perp, parallel

class GeometryComboExample(Scene):
    def construct(self):
        # Create a diagonal line
        ref_line = Line(LEFT * 2 + DOWN, RIGHT * 2 + UP, color=BLUE)

        # Create perpendicular line
        dot = Dot(ORIGIN, color=RED)
        perp_line = perp(ref_line, dot, 3.0, placement="mid")
        perp_line.set_color(GREEN)

        # Create parallel line at a different position
        dot2 = Dot(UP * 2 + LEFT, color=ORANGE)
        parallel_line = parallel(ref_line, dot2, 2.5, placement="mid")
        parallel_line.set_color(YELLOW)

        # Labels
        ref_label = Text("Reference", font_size=20, color=BLUE).next_to(ref_line, DOWN)
        perp_label = Text("Perpendicular", font_size=20, color=GREEN).next_to(perp_line, RIGHT)
        parallel_label = Text("Parallel", font_size=20, color=YELLOW).next_to(parallel_line, UP)

        # Animate
        self.play(Create(ref_line), Write(ref_label))
        self.wait(0.5)

        self.play(Create(dot))
        self.play(Create(perp_line), Write(perp_label))
        self.wait(1)

        self.play(Create(dot2))
        self.play(Create(parallel_line), Write(parallel_label))
        self.wait(2)
```

**Output:**

<video width="640" height="480" controls>
  <source src="../videos/geometry_combo.mp4" type="video/mp4">
</video>

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

## Back to [Documentation Home](../)
