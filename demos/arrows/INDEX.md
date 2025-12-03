# Arrow Utilities

Demonstrations of `ArrowUtil` class for creating advanced arrows with dashing, curves, perpendicular offsets, and markers.

---

## BasicArrowDemo
**Simple arrow with textbook-style tips**

![BasicArrowDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/arrows/BasicArrowDemo_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/arrows/BasicArrowDemo.mp4)**

```python
from robo_manim_add_ons import ArrowUtil

# Basic arrow with simple two-line tip (textbook style)
arrow = ArrowUtil.arrow(LEFT * 2, RIGHT * 2, color=BLUE)
```

---

## DashedArrowDemo
**Arrow with dashed line**

![DashedArrowDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/arrows/DashedArrowDemo_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/arrows/DashedArrowDemo.mp4)**

```python
from robo_manim_add_ons import ArrowUtil

# Dashed arrow
arrow = ArrowUtil.arrow(LEFT * 2, RIGHT * 2, dashed=True, color=RED)
```

---

## PerpendicularBufferDemo
**Arrows with perpendicular offset**

![PerpendicularBufferDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/arrows/PerpendicularBufferDemo_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/arrows/PerpendicularBufferDemo.mp4)**

```python
from robo_manim_add_ons import ArrowUtil

# Reference line
ref_line = Line(LEFT * 3, RIGHT * 3, color=GRAY)

# Arrow with positive buffer (shifted upward)
arrow1 = ArrowUtil.arrow(LEFT * 2.5, RIGHT * 2.5, buff=0.5, color=BLUE)

# Arrow with negative buffer (shifted downward)
arrow2 = ArrowUtil.arrow(LEFT * 2.5, RIGHT * 2.5, buff=-0.5, color=RED)
```

---

## BidirectionalArrowDemo
**Arrow with tips on both ends**

![BidirectionalArrowDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/arrows/BidirectionalArrowDemo_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/arrows/BidirectionalArrowDemo.mp4)**

```python
from robo_manim_add_ons import ArrowUtil

# Bidirectional arrow (tips on both ends)
arrow = ArrowUtil.arrow(
    LEFT * 2, RIGHT * 2,
    bidirectional=True,
    color=GREEN
)
```

---

## CurvedArrowDemo
**Arrows along circular arcs with different angles**

![CurvedArrowDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/arrows/CurvedArrowDemo_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/arrows/CurvedArrowDemo.mp4)**

```python
from robo_manim_add_ons import ArrowUtil

start = LEFT * 2 + DOWN
end = RIGHT * 2 + DOWN

# Curved arrow with 30 degree arc
arrow1 = ArrowUtil.curved_arrow(
    start, end,
    angle=30 * DEGREES,
    color=BLUE
)

# Curved arrow with 60 degree arc
arrow2 = ArrowUtil.curved_arrow(
    start, end,
    angle=60 * DEGREES,
    color=RED
)

# Curved arrow with 90 degree arc (more pronounced curve)
arrow3 = ArrowUtil.curved_arrow(
    start, end,
    angle=90 * DEGREES,
    color=GREEN
)
```

---

## LabelPositioningDemo
**Automatic label positioning with perpendicular offset**

![LabelPositioningDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/arrows/LabelPositioningDemo_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/arrows/LabelPositioningDemo.mp4)**

```python
from robo_manim_add_ons import ArrowUtil

# Horizontal arrow with label
arrow1 = ArrowUtil.arrow(LEFT * 2 + UP, RIGHT * 2 + UP, buff=0.2, color=BLUE)
label1 = ArrowUtil.label(arrow1, MathTex("L_1"), buff=0.3)

# Diagonal arrow with label
arrow2 = ArrowUtil.arrow(LEFT * 2 + DOWN, RIGHT * 1 + DOWN * 2, buff=0.2, color=RED)
label2 = ArrowUtil.label(arrow2, MathTex("L_2"), buff=0.3)
```

---

## MarkerDemo
**Directional markers at specific points**

![MarkerDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/arrows/MarkerDemo_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/arrows/MarkerDemo.mp4)**

```python
from robo_manim_add_ons import ArrowUtil

# Create a circle
circle = Circle(radius=2, color=GRAY)

# Add markers at different positions around the circle
for i in range(8):
    proportion = i / 8
    point = circle.point_from_proportion(proportion)

    # Calculate tangent direction
    next_point = circle.point_from_proportion((proportion + 0.01) % 1)
    direction = next_point - point

    # Create marker at point
    marker = ArrowUtil.marker(
        point, direction,
        tip_length=0.4,
        color=BLUE
    )
```

---

## CombinedFeaturesDemo
**Combining multiple features: dashed lines with labels**

![CombinedFeaturesDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/arrows/CombinedFeaturesDemo_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/arrows/CombinedFeaturesDemo.mp4)**

```python
from robo_manim_add_ons import ArrowUtil

# Square with labeled sides
square = Square(side_length=3, color=GRAY)
v1, v2, v3, v4 = square.get_vertices()

# Top side - dashed with label
arrow_top = ArrowUtil.arrow(
    v1, v2,
    dashed=True,
    buff=-0.3,
    color=BLUE
)
label_top = ArrowUtil.label(arrow_top, MathTex("a"), buff=-0.3)

# Right side - solid bidirectional with label
arrow_right = ArrowUtil.arrow(
    v2, v3,
    bidirectional=True,
    buff=-0.3,
    color=RED
)
label_right = ArrowUtil.label(arrow_right, MathTex("b"), buff=-0.3)
```

---

## ArrowUtil Methods

### `arrow()`
Create enhanced straight arrows with dashing, buffer, and bidirectional tips.

**Parameters:**
- `start` - Starting point
- `end` - Ending point
- `buff` - Perpendicular offset (positive = counterclockwise, negative = clockwise)
- `dashed` - If True, creates dashed line
- `bidirectional` - If True, adds tips on both ends
- `tip_angle` - Angle of tip lines (default: 20 degrees)
- `tip_length` - Length of tip lines (default: 0.3)

### `curved_arrow()`
Create arrows along circular arcs.

**Parameters:**
- `start` - Starting point
- `end` - Ending point
- `angle` - Arc angle controlling curvature
- `tip_angle` - Angle of tip lines (default: 20 degrees)
- `tip_length` - Length of tip lines (default: 0.3)

### `perpendicular_offset()`
Calculate perpendicular offset vector for a line segment.

**Parameters:**
- `start` - Starting point
- `end` - Ending point
- `distance` - Offset distance

**Returns:** numpy.ndarray offset vector

### `label()`
Position a label relative to an arrow with perpendicular offset.

**Parameters:**
- `arrow` - The arrow to label
- `tex` - Label mobject (MathTex, Text, etc.)
- `buff` - Perpendicular offset from arrow center

**Returns:** Positioned label mobject

### `marker()`
Create a directional marker (arrow tip) at a specific point.

**Parameters:**
- `point` - Point where marker should be placed
- `direction` - Direction vector for the marker
- `tip_angle` - Angle of marker lines (default: 20 degrees)
- `tip_length` - Length of marker lines (default: 0.3)

**Returns:** VGroup of marker lines
