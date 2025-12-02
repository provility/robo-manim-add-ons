# Geometry Utilities

Demonstrations of `perp()` and `parallel()` functions.

---

## PerpDemo
**Basic perpendicular line construction**

```python
from robo_manim_add_ons import perp

ref_line = Line(LEFT * 3, RIGHT * 3, color=BLUE)
dot = Dot(ORIGIN, color=RED)

# Create perpendicular line through dot
perp_line = perp(ref_line, dot, length=4.0, placement="mid")
perp_line.set_color(GREEN)
```

![PerpDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/PerpDemo_ManimCE_v0.19.0.png)

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/PerpDemo.mp4" controls width="100%"></video>

---

## ParallelDemo
**Basic parallel line construction**

```python
from robo_manim_add_ons import parallel

ref_line = Line(LEFT + DOWN, RIGHT + UP, color=BLUE)
dot = Dot(UP * 2, color=RED)

# Create parallel line through dot
parallel_line = parallel(ref_line, dot, length=3.0, placement="mid")
parallel_line.set_color(YELLOW)
```

![ParallelDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/ParallelDemo_ManimCE_v0.19.0.png)

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/ParallelDemo.mp4" controls width="100%"></video>

---

## PlacementDemo
**Placement options: start, mid, end**

```python
ref_line = Line(LEFT * 4, RIGHT * 4, color=BLUE)

dot_mid = Dot(ORIGIN)
dot_start = Dot(UP * 2)
dot_end = Dot(DOWN * 2)

# Three placement options
perp_mid = perp(ref_line, dot_mid, 2.0, placement="mid")      # centered on dot
perp_start = perp(ref_line, dot_start, 2.0, placement="start")  # starts at dot
perp_end = perp(ref_line, dot_end, 2.0, placement="end")       # ends at dot
```

![PlacementDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/PlacementDemo_ManimCE_v0.19.0.png)

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/PlacementDemo.mp4" controls width="100%"></video>

---

## GeometryComboDemo
**Combining perpendicular and parallel**

```python
ref_line = Line(LEFT * 2 + DOWN, RIGHT * 2 + UP, color=BLUE)

# Perpendicular to ref_line
dot1 = Dot(ORIGIN, color=RED)
perp_line = perp(ref_line, dot1, 3.0, placement="mid").set_color(GREEN)

# Parallel to ref_line
dot2 = Dot(UP * 2 + LEFT, color=ORANGE)
parallel_line = parallel(ref_line, dot2, 2.5, placement="mid").set_color(YELLOW)
```

![GeometryComboDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/GeometryComboDemo_ManimCE_v0.19.0.png)

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/GeometryComboDemo.mp4" controls width="100%"></video>

---

## DynamicPerpExample
**Dynamic perpendicular with always_redraw()**

```python
base_line = Line(LEFT * 2, RIGHT * 2, color=BLUE)
center_dot = Dot(ORIGIN, color=YELLOW)

# Perpendicular updates automatically as base_line rotates
perp_line = always_redraw(
    lambda: perp(base_line, center_dot, length=3, placement="mid")
        .set_color(RED)
)

self.play(Rotate(base_line, angle=PI/3, about_point=ORIGIN))
```

![DynamicPerpExample](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/DynamicPerpExample_ManimCE_v0.19.0.png)

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/DynamicPerpExample.mp4" controls width="100%"></video>

---

## ParallelogramUpdater
**Dynamic parallelogram construction**

```python
base = Line(LEFT * 2 + DOWN, RIGHT * 2 + DOWN, color=BLUE)
top_left_dot = Dot(LEFT * 1.5 + UP, color=YELLOW)

# Side from base to dot
side = always_redraw(
    lambda: Line(base.get_start(), top_left_dot.get_center(), color=BLUE)
)

# Top edge parallel to base
top = always_redraw(
    lambda: parallel(base, top_left_dot, length=base.get_length(), placement="start")
        .set_color(GREEN)
)

# Right side parallel to left side
top_right_dot = always_redraw(lambda: Dot(top.get_end(), color=YELLOW))
right_side = always_redraw(
    lambda: parallel(side, top_right_dot, length=side.get_length(), placement="end")
        .set_color(GREEN)
)
```

![ParallelogramUpdater](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/ParallelogramUpdater_ManimCE_v0.19.0.png)

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/ParallelogramUpdater.mp4" controls width="100%"></video>
