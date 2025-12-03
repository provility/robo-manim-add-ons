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

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/PerpDemo.mp4" controls width="100%"></video>

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

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/ParallelDemo.mp4" controls width="100%"></video>

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

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/PlacementDemo.mp4" controls width="100%"></video>

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

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/GeometryComboDemo.mp4" controls width="100%"></video>

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

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/DynamicPerpExample.mp4" controls width="100%"></video>

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

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/ParallelogramUpdater.mp4" controls width="100%"></video>

---

## ReverseAtDemo
**Vector reversal for subtraction visualization**

```python
from robo_manim_add_ons.vector_utils import VectorUtils

origin = Dot(ORIGIN, color=YELLOW)
vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE)
vector_b = Arrow(ORIGIN, UP * 2, buff=0, color=RED)

# Create -b at origin
neg_b_at_origin = VectorUtils.reverse_at(vector_b, ORIGIN, color=PURPLE)
self.play(Create(neg_b_at_origin))

# Move -b to tip of a
neg_b_at_tip = VectorUtils.reverse_at(vector_b, vector_a.get_end(), color=PURPLE)
self.play(Transform(neg_b_at_origin, neg_b_at_tip))

# Show result vector (a - b)
vec_a_dir = vector_a.get_end() - vector_a.get_start()
vec_b_dir = vector_b.get_end() - vector_b.get_start()
result_vector = Arrow(ORIGIN, ORIGIN + vec_a_dir - vec_b_dir, buff=0, color=GREEN)
self.play(GrowArrow(result_vector))
```

![ReverseAtDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/ReverseAtDemo_ManimCE_v0.19.0.png)

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/ReverseAtDemo.mp4" controls width="100%"></video>

---

## ProjectionDemo
**Vector projection with dynamic rotation**

```python
from robo_manim_add_ons.vector_utils import VectorUtils

vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0)
vector_b = Arrow(ORIGIN, RIGHT * 2 + UP * 1.5, buff=0)

# Projection visualizations with updaters
projection = always_redraw(
    lambda: VectorUtils.project_onto(vector_b, vector_a)
)

proj_line = always_redraw(
    lambda: VectorUtils.projection_line(vector_b, vector_a)
)

proj_region = always_redraw(
    lambda: VectorUtils.projection_region(vector_b, vector_a, fill_opacity=0.3)
)

# Rotate vector_b - projections update dynamically
self.play(Rotate(vector_b, angle=PI, about_point=ORIGIN))
```

![ProjectionDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/ProjectionDemo_ManimCE_v0.19.0.png)

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/ProjectionDemo.mp4" controls width="100%"></video>

---

## ProjectionScalingDemo
**Projection scaling with vector magnitude**

```python
from robo_manim_add_ons.vector_utils import VectorUtils

vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0)
vector_b = Arrow(ORIGIN, RIGHT * 1 + UP * 1, buff=0)

# Projection with always_redraw
projection = always_redraw(
    lambda: VectorUtils.project_onto(vector_b, vector_a)
)

proj_line = always_redraw(
    lambda: VectorUtils.projection_line(vector_b, vector_a)
)

proj_region = always_redraw(
    lambda: VectorUtils.projection_region(vector_b, vector_a, fill_opacity=0.3)
)

# Scale vector_b - projection scales proportionally
new_end = RIGHT * 2.5 + UP * 2.5
self.play(vector_b.animate.put_start_and_end_on(ORIGIN, new_end))
```

![ProjectionScalingDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/ProjectionScalingDemo_ManimCE_v0.19.0.png)

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/geometry/ProjectionScalingDemo.mp4" controls width="100%"></video>
