# Intersection Utilities

Demonstrations of `intersect_lines()` and `intersect_line_circle()` functions.

---

## BasicIntersectionDemo
**Basic line-line intersection**

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/intersection/BasicIntersectionDemo.mp4" controls width="100%"></video>

```python
from robo_manim_add_ons import intersect_lines

line1 = Line(LEFT * 3, RIGHT * 3, color=BLUE)
line2 = Line(DOWN * 2, UP * 2, color=GREEN)

# Returns a Dot at intersection point
intersection_dot = intersect_lines(line1, line2)
intersection_dot.set_color(RED).scale(1.5)
```

---

## ParallelLinesDemo
**Parallel lines return empty VGroup**

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/intersection/ParallelLinesDemo.mp4" controls width="100%"></video>

```python
line1 = Line(LEFT * 3, RIGHT * 3).shift(UP)
line2 = Line(LEFT * 3, RIGHT * 3).shift(DOWN)

result = intersect_lines(line1, line2)

# Check if parallel (no intersection)
if len(result) == 0:
    # Lines are parallel
    pass
```

---

## DynamicIntersectionDemo
**Intersection follows rotating line using always_redraw()**

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/intersection/DynamicIntersectionDemo.mp4" controls width="100%"></video>

```python
fixed_line = Line(LEFT * 3, RIGHT * 3, color=BLUE)
rotating_line = Line(DOWN * 2, UP * 2, color=GREEN)

# Intersection updates automatically as line rotates
intersection_dot = always_redraw(
    lambda: intersect_lines(fixed_line, rotating_line)
        .set_color(RED).scale(1.5)
)

self.play(Rotate(rotating_line, angle=PI/3, about_point=ORIGIN))
```

---

## BasicLineCircleIntersection
**Line through circle (2 intersection points)**

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/intersection/BasicLineCircleIntersection.mp4" controls width="100%"></video>

```python
from robo_manim_add_ons import intersect_line_circle

circle = Circle(radius=2, color=BLUE)
line = Line(LEFT * 3, RIGHT * 3, color=GREEN)

# Returns VGroup containing 0, 1, or 2 Dots
intersections = intersect_line_circle(line, circle)

for dot in intersections:
    dot.set_color(RED).scale(1.5)
```

---

## TangentLineDemo
**Tangent line (1 intersection point)**

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/intersection/TangentLineDemo.mp4" controls width="100%"></video>

```python
circle = Circle(radius=2, color=BLUE)
line = Line(LEFT * 3 + UP * 2, RIGHT * 3 + UP * 2, color=GREEN)

intersections = intersect_line_circle(line, circle)

# Tangent line produces 1 intersection point
print(f"Found {len(intersections)} intersection(s)")
```

---

## DynamicLineCircleIntersection
**Dynamic intersection with rotating line**

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/intersection/DynamicLineCircleIntersection.mp4" controls width="100%"></video>

```python
circle = Circle(radius=2, color=BLUE)
line = Line(LEFT * 3, RIGHT * 3, color=GREEN)

# Intersections update automatically with always_redraw
intersections = always_redraw(
    lambda: VGroup(*[
        dot.set_color(RED).scale(1.5)
        for dot in intersect_line_circle(line, circle)
    ])
)

self.play(Rotate(line, angle=PI/4, about_point=ORIGIN))
```
