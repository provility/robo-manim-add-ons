# Annotation Utilities

Demonstrations of `distance_marker()` function for geometric annotations.

---

## BasicDistanceMarker
**Triangle with distance markers**

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/annotation/BasicDistanceMarker.mp4" controls width="100%"></video>

```python
from robo_manim_add_ons import distance_marker

triangle = Polygon([-2, -1, 0], [2, -1, 0], [0, 2, 0], color=WHITE)

# Add distance marker on each side
marker_a = distance_marker(
    [-2, -1, 0], [2, -1, 0],
    label_text="a",
    color=BLUE,
    label_offset=0.4  # Distance from line to label
)
```

---

## DistanceMarkerRectangle
**Annotating rectangle dimensions**

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/annotation/DistanceMarkerRectangle.mp4" controls width="100%"></video>

```python
rect = Rectangle(width=4, height=2.5, color=WHITE)
corners = rect.get_vertices()  # [top_right, top_left, bottom_left, bottom_right]

# Width marker
width_marker = distance_marker(
    corners[2], corners[3],  # bottom_left to bottom_right
    label_text="4",
    label_offset=-0.5  # Place below
)

# Height marker
height_marker = distance_marker(
    corners[3], corners[0],  # bottom_right to top_right
    label_text="2.5",
    label_offset=0.5   # Place to the right
)
```

---

## DistanceMarkerWithDots
**Using Dot objects with markers**

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/annotation/DistanceMarkerWithDots.mp4" controls width="100%"></video>

```python
# Create Dot objects
dot_a = Dot([-2, -1, 0], color=BLUE)
dot_b = Dot([2, -1, 0], color=RED)
dot_c = Dot([0, 2, 0], color=GREEN)

# Markers automatically extract positions from Dots
marker_ab = distance_marker(
    dot_a, dot_b,  # Pass Dots directly
    label_text="d_{AB}",
    label_offset=-0.5,
    marker_offset=0  # Optional: offset entire marker perpendicular to line
)

marker_bc = distance_marker(dot_b, dot_c, label_text="d_{BC}")
marker_ca = distance_marker(dot_c, dot_a, label_text="d_{CA}")
```

---

## PythagoreanTheorem
**Right triangle with Pythagorean theorem**

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/annotation/PythagoreanTheorem.mp4" controls width="100%"></video>

```python
triangle = Polygon(
    [-2, -1.5, 0], [2, -1.5, 0], [2, 1.5, 0],
    color=WHITE
)

a_marker = distance_marker(
    [-2, -1.5, 0], [2, -1.5, 0],
    label_text="a = 4",
    color=BLUE,
    label_offset=-0.4
)

b_marker = distance_marker(
    [2, -1.5, 0], [2, 1.5, 0],
    label_text="b = 3",
    color=RED,
    label_offset=0.4
)

c_marker = distance_marker(
    [2, 1.5, 0], [-2, -1.5, 0],
    label_text="c = 5",
    color=GREEN,
    label_offset=0.4
)

formula = MathTex(r"a^2 + b^2 = c^2")
```
