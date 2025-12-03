# Geometry Utilities

Demonstrations of `perp()` and `parallel()` functions.

---

## PerpDemo
**Basic perpendicular line construction**

```python
from robo_manim_add_ons import perp

ref_line = Line(LEFT * 3, RIGHT * 3, color=BLUE)
dot = Dot(ORIGIN, color=RED)
perp_line = perp(ref_line, dot, length=4.0, placement="mid").set_color(GREEN)

self.play(Create(ref_line))
self.play(Create(dot))
self.play(Create(perp_line))
```

![PerpDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/PerpDemo_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/PerpDemo.mp4)**

---

## ParallelDemo
**Basic parallel line construction**

```python
from robo_manim_add_ons import parallel

ref_line = Line(LEFT + DOWN, RIGHT + UP, color=BLUE)
dot = Dot(UP * 2, color=RED)
parallel_line = parallel(ref_line, dot, length=3.0, placement="mid").set_color(YELLOW)

self.play(Create(ref_line))
self.play(Create(dot))
self.play(Create(parallel_line))
```

![ParallelDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/ParallelDemo_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/ParallelDemo.mp4)**

---

## PlacementDemo
**Placement options: start, mid, end**

```python
ref_line = Line(LEFT * 4, RIGHT * 4, color=BLUE)

dot_mid = Dot(ORIGIN, color=RED)
dot_start = Dot(UP * 2, color=GREEN)
dot_end = Dot(DOWN * 2, color=YELLOW)

perp_mid = perp(ref_line, dot_mid, 2.0, placement="mid").set_color(RED)
perp_start = perp(ref_line, dot_start, 2.0, placement="start").set_color(GREEN)
perp_end = perp(ref_line, dot_end, 2.0, placement="end").set_color(YELLOW)
```

![PlacementDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/PlacementDemo_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/PlacementDemo.mp4)**

---

## GeometryComboDemo
**Combining perpendicular and parallel**

```python
ref_line = Line(LEFT * 2 + DOWN, RIGHT * 2 + UP, color=BLUE)
dot = Dot(ORIGIN, color=RED)
perp_line = perp(ref_line, dot, 3.0, placement="mid").set_color(GREEN)

dot2 = Dot(UP * 2 + LEFT, color=ORANGE)
parallel_line = parallel(ref_line, dot2, 2.5, placement="mid").set_color(YELLOW)
```

![GeometryComboDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/GeometryComboDemo_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/GeometryComboDemo.mp4)**

---

## DynamicPerpExample
**Dynamic perpendicular with always_redraw()**

```python
base_line = Line(LEFT * 2, RIGHT * 2, color=BLUE)
center_dot = Dot(ORIGIN, color=YELLOW)

perp_line = always_redraw(
    lambda: perp(base_line, center_dot, length=3, placement="mid").set_color(RED)
)

self.play(Create(base_line))
self.play(FadeIn(center_dot))
self.play(Create(perp_line))

self.play(Rotate(base_line, angle=PI/3, about_point=ORIGIN), run_time=3)
self.play(Rotate(base_line, angle=-PI/3, about_point=ORIGIN), run_time=3)
```

![DynamicPerpExample](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/DynamicPerpExample_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/DynamicPerpExample.mp4)**

---

## DynamicParallelExample
**Dynamic parallel line following reference line**

```python
base_line = Line(LEFT * 3, RIGHT * 3, color=BLUE)
following_dot = Dot(UP * 1.5, color=YELLOW)

parallel_line = always_redraw(
    lambda: parallel(base_line, following_dot, length=4, placement="mid").set_color(GREEN)
)

self.play(Create(base_line))
self.play(FadeIn(following_dot), Create(parallel_line))

# Rotate base line - parallel line follows
self.play(Rotate(base_line, angle=PI/4, about_point=ORIGIN), run_time=3)
```

![DynamicParallelExample](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/DynamicParallelExample_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/DynamicParallelExample.mp4)**

---

## InteractivePerpUpdater
**Perpendicular line following a moving point**

```python
ref_line = Line(LEFT * 3, RIGHT * 3, color=BLUE).shift(DOWN)
moving_dot = Dot(ORIGIN, color=RED)

perp_line = always_redraw(
    lambda: perp(ref_line, moving_dot, length=3.0, placement="mid").set_color(GREEN)
)

self.play(Create(ref_line))
self.add(moving_dot, perp_line)

# Move dot along path - perpendicular updates
self.play(moving_dot.animate.shift(RIGHT * 2 + UP), run_time=2)
self.play(moving_dot.animate.shift(LEFT * 4), run_time=3)
```

![InteractivePerpUpdater](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/InteractivePerpUpdater_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/InteractivePerpUpdater.mp4)**

---

## MultiplePerpendicularUpdaters
**Multiple perpendiculars at different positions**

```python
ref_line = Line(LEFT * 3, RIGHT * 3, color=BLUE)

# Create three dots at different positions
dots = [
    Dot(LEFT * 2, color=RED),
    Dot(ORIGIN, color=GREEN),
    Dot(RIGHT * 2, color=YELLOW)
]

# Create perpendiculars with updaters
perps = [
    always_redraw(lambda d=dot: perp(ref_line, d, 2.0, placement="mid").set_color(dot.get_color()))
    for dot in dots
]

# Rotate reference line - all perpendiculars update
self.play(Rotate(ref_line, angle=PI/3, about_point=ORIGIN), run_time=3)
```

![MultiplePerpendicularUpdaters](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/MultiplePerpendicularUpdaters_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/MultiplePerpendicularUpdaters.mp4)**

---

## ParallelLinesGrid
**Grid of parallel lines with dynamic updates**

```python
ref_line = Line(LEFT * 3, RIGHT * 3, color=BLUE).rotate(PI/6)

# Create grid of dots
grid_dots = VGroup(*[
    Dot(LEFT * 2 + UP * i) for i in range(-2, 3)
])

# Create parallel lines for each dot
parallel_lines = VGroup(*[
    always_redraw(lambda d=dot: parallel(ref_line, d, 4.0, placement="mid").set_color(GREEN))
    for dot in grid_dots
])

# Rotate reference line - all parallels update
self.play(Rotate(ref_line, angle=PI/4, about_point=ORIGIN), run_time=4)
```

![ParallelLinesGrid](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/ParallelLinesGrid_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/ParallelLinesGrid.mp4)**

---

## ParallelogramUpdater
**Dynamic parallelogram construction**

```python
base = Line(LEFT * 2 + DOWN, RIGHT * 2 + DOWN, color=BLUE)
top_left_dot = Dot(LEFT * 1.5 + UP, color=YELLOW)

side = always_redraw(
    lambda: Line(base.get_start(), top_left_dot.get_center(), color=BLUE)
)

top = always_redraw(
    lambda: parallel(
        base, top_left_dot,
        length=base.get_length(),
        placement="start"
    ).set_color(GREEN)
)

top_right_dot = always_redraw(lambda: Dot(top.get_end(), color=YELLOW))

right_side = always_redraw(
    lambda: parallel(
        side, top_right_dot,
        length=side.get_length(),
        placement="end"
    ).set_color(GREEN)
)

self.play(top_left_dot.animate.move_to(LEFT * 2.5 + UP * 2), run_time=3)
```

![ParallelogramUpdater](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/ParallelogramUpdater_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/ParallelogramUpdater.mp4)**
