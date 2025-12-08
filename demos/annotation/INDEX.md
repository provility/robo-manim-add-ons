# Annotation Utilities

Demonstrations of `label()`, `hatch()`, and `dm()` for geometric annotations.

**Short aliases:** `dm` (distance_marker), `hatch` (hatched_region)

---

## BasicLabelDemo
**Simple label between two points**

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/annotation/BasicLabelDemo.mp4)**

```python
from robo_manim_add_ons import label

# Two dots
dot_a = Dot([-2, 0, 0], color=BLUE)
dot_b = Dot([2, 0, 0], color=RED)

# Create label positioned above the line
ab_label = label("AB", dot_a, dot_b, buff=0.5)
```

---

## DiagonalHatchDemo
**Diagonal hatching pattern on a rectangle**

```python
from robo_manim_add_ons import hatch

axes = Axes(x_range=[0, 10, 1], y_range=[0, 8, 1])
vertices = [(2, 2), (8, 2), (8, 6), (2, 6)]

# Create hatched region with diagonal lines
hatched, boundary = hatch(
    axes, vertices,
    spacing=0.2,
    direction="/",    # Diagonal hatching
    color=BLUE,
    stroke_width=1.5
)

self.add(axes, boundary, hatched)
```

![DiagonalHatchDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/annotation/DiagonalHatchDemo_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/annotation/DiagonalHatchDemo.mp4)**

---

## TriangleHatchDemo
**Backslash hatching pattern on a triangle**

```python
from robo_manim_add_ons import hatch

axes = Axes(x_range=[0, 10, 1], y_range=[0, 8, 1])
vertices = [(2, 2), (8, 2), (5, 6)]  # Triangle

# Create hatched region with backslash pattern
hatched, boundary = hatch(
    axes, vertices,
    spacing=0.25,
    direction="\\",   # Backslash hatching
    color=RED,
    stroke_width=1.5
)

self.add(axes, boundary, hatched)
```

![TriangleHatchDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/annotation/TriangleHatchDemo_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/annotation/TriangleHatchDemo.mp4)**

---

## BasicDistanceMarker
**Triangle with distance markers**

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/annotation/BasicDistanceMarker.mp4)**

```python
from robo_manim_add_ons import dm

triangle = Polygon([-2, -1, 0], [2, -1, 0], [0, 2, 0], color=WHITE)

# Add distance marker on each side (using two points)
marker_a = dm(
    [-2, -1, 0], [2, -1, 0],
    text="a",
    color=BLUE,
    label_offset=0.4  # Distance from line to label
)
```

---

## LineObjectDemo
**Using Line objects directly with distance markers**

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/annotation/LineObjectDemo.mp4)**

```python
from robo_manim_add_ons import dm

# Create line objects
line1 = Line([-3, 1.5, 0], [3, 1.5, 0], color=BLUE)
line2 = Arrow([-2, 0, 0], [2, 0, 0], color=RED, buff=0)

# Pass line objects directly to dm
marker1 = dm(line1, text="Line", marker_offset=0.5)
marker2 = dm(line2, text="Arrow", marker_offset=0.5)

# Both signatures work:
# dm(line_object, **kwargs)           # Line/Arrow object
# dm(point1, point2, **kwargs)        # Two points (Dots, arrays, or lists)
```

---

## DistanceMarkerRectangle
**Annotating rectangle dimensions**

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/annotation/DistanceMarkerRectangle.mp4)**

```python
rect = Rectangle(width=4, height=2.5, color=WHITE)
corners = rect.get_vertices()  # [top_right, top_left, bottom_left, bottom_right]

# Width marker
width_marker = dm(
    corners[2], corners[3],  # bottom_left to bottom_right
    label_text="4",
    label_offset=-0.5  # Place below
)

# Height marker
height_marker = dm(
    corners[3], corners[0],  # bottom_right to top_right
    label_text="2.5",
    label_offset=0.5   # Place to the right
)
```

---

## DistanceMarkerWithDots
**Using Dot objects with markers**

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/annotation/DistanceMarkerWithDots.mp4)**

```python
# Create Dot objects
dot_a = Dot([-2, -1, 0], color=BLUE)
dot_b = Dot([2, -1, 0], color=RED)
dot_c = Dot([0, 2, 0], color=GREEN)

# Markers automatically extract positions from Dots
marker_ab = dm(
    dot_a, dot_b,  # Pass Dots directly
    label_text="d_{AB}",
    label_offset=-0.5,
    marker_offset=0  # Optional: offset entire marker perpendicular to line
)

marker_bc = dm(dot_b, dot_c, label_text="d_{BC}")
marker_ca = dm(dot_c, dot_a, label_text="d_{CA}")
```

---

## PythagoreanTheorem
**Right triangle with Pythagorean theorem**

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/annotation/PythagoreanTheorem.mp4)**

```python
triangle = Polygon(
    [-2, -1.5, 0], [2, -1.5, 0], [2, 1.5, 0],
    color=WHITE
)

a_marker = dm(
    [-2, -1.5, 0], [2, -1.5, 0],
    label_text="a = 4",
    color=BLUE,
    label_offset=-0.4
)

b_marker = dm(
    [2, -1.5, 0], [2, 1.5, 0],
    label_text="b = 3",
    color=RED,
    label_offset=0.4
)

c_marker = dm(
    [2, 1.5, 0], [-2, -1.5, 0],
    label_text="c = 5",
    color=GREEN,
    label_offset=0.4
)

formula = MathTex(r"a^2 + b^2 = c^2")
```
