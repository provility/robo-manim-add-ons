# Robo Manim Add-ons API Reference

Compact API listing for quick reference. For detailed documentation, see individual module docs.

---

## Expression Utils (`exp_utils`)

### Coordinate Extraction
```python
x(obj) -> float                              # Extract x-coordinate
y(obj) -> float                              # Extract y-coordinate
st(obj) -> Dot                               # Get start point as Dot
ed(obj) -> Dot                               # Get end point as Dot
mid(obj) -> Dot                              # Get midpoint as Dot
```

### Vector Operations
```python
mag(obj) -> float                            # Get magnitude/length
mag(pt1, pt2) -> float                       # Distance between two points
uv(obj) -> np.ndarray                        # Get unit vector
vec(obj) -> np.ndarray                       # Get vector
ang(obj) -> float                            # Get angle in radians
slope(obj) -> float                          # Get slope (y/x)
val(obj) -> float                            # Get value from ValueTracker or number
```

### Point Creation
```python
pt(x, y, z=0) -> Dot                         # Create Dot at (x, y, z)
m2v(axes, x, y) -> Dot                       # Model to view coordinates
v2m(axes, x, y) -> Dot                       # View to model coordinates
x2v(axes, graph, x) -> Dot                   # Point on graph at x-value
r2p(obj, proportion) -> Dot                  # Point at proportion along object
```

### Line/Arrow Creation
```python
vl(x, y1=-20, y2=20) -> Line                 # Vertical line at x
hl(y, x1=-20, x2=20) -> Line                 # Horizontal line at y
lra(radius, angle, from_x=0, from_y=0) -> Line       # Line using polar coords
vra(radius, angle, from_x=0, from_y=0) -> Arrow     # Arrow using polar coords
ln(*args) -> Line                            # Flexible Line creation (red)
vt(*args) -> Arrow                           # Flexible Arrow creation (red)
```

### Shape Creation
```python
tri(p1, p2, p3) -> Polygon                   # Triangle from three points (red)
cr(*args) -> Circle                          # Circle (flexible arguments)
aa(*args, radius=0.5, dash=True) -> ArcArrow         # Angle arc (dashed)
aa2(*args, radius=0.5) -> Angle              # Angle using Manim's Angle class
```

---

## Annotation Utils (`annotation_utils`)

```python
distance_marker(pt1, pt2=None, color="#1e40af", stroke_width=2, tick_size=0.25, text="", label_offset=0.3, marker_offset=0)
dm(pt1, pt2=None, **kwargs)                  # Alias for distance_marker
label(latex_text, pt1, pt2, buff=0.5, alpha=0.5, auto_rotate=True) -> MathTex
hatched_region(axes, vertices, spacing=0.2, direction="/", color="#808080", stroke_width=2)
hatch(axes, vertices, **kwargs)              # Alias for hatched_region
```

---

## Geometry Utils (`geometry_utils`)

```python
perp(line, dot, length, placement="mid") -> Line      # Perpendicular line
parallel(line, dot, length, placement="mid") -> Line  # Parallel line
pll(line, dot, length, placement="mid") -> Line       # Alias for parallel
project(line, point) -> Dot                  # Project point onto line
reflect(line, point) -> Dot                  # Reflect point across line
extended_line(line, proportion, length) -> Line       # Extend line
xl(line, proportion, length) -> Line         # Alias for extended_line
```

---

## Intersection Utils (`intersection_utils`)

```python
intersect_lines(line1, line2) -> Union[Dot, VGroup]         # Line-line intersection
ill(line1, line2) -> Union[Dot, VGroup]                     # Alias for intersect_lines
intersect_line_circle(line, circle) -> VGroup               # Line-circle intersection
ilc(line, circle) -> VGroup                                 # Alias for intersect_line_circle
```

---

## Style Utils (`style_utils`)

```python
stroke(obj, color) -> VMobject               # Set stroke color (chainable)
fill(obj, color) -> VMobject                 # Set fill color (chainable)
sopacity(obj, opacity) -> VMobject           # Set stroke opacity (chainable)
fopacity(obj, opacity) -> VMobject           # Set fill opacity (chainable)
sw(obj, width) -> VMobject                   # Set stroke width (chainable)
style(obj) -> Style                          # Get Style object for chaining
```

### Style Chaining
```python
style(circle).fill(BLUE).stroke(RED).sw(3).fopacity(0.5).sopacity(1)
```

---

## Transform Utils (`transform_utils`)

```python
translated(obj, dx, dy) -> Mobject           # Copy and translate
rotated(obj, angle_deg, about=None) -> Mobject          # Copy and rotate
scaled(obj, scale_factor, about=None) -> Mobject        # Copy and scale
```

---

## Vector Utils (`vector_utils`)

### VectorUtils Class Methods
```python
VectorUtils.forward(source, distance) -> Mobject        # Copy forward by distance
VectorUtils.fw(source, distance) -> Mobject             # Alias for forward
VectorUtils.backward(source, distance) -> Mobject       # Copy backward by distance
VectorUtils.bw(source, distance) -> Mobject             # Alias for backward
VectorUtils.perp_move(source, distance) -> Mobject      # Copy perpendicular by distance
VectorUtils.pm(source, distance) -> Mobject             # Alias for perp_move
VectorUtils.copy_at(source, position) -> Mobject        # Copy at position
VectorUtils.reverse_at(source, position) -> Mobject     # Copy reversed at position
```

---

## Graph Utils (`graph_utils`)

```python
GraphUtils.graph(axes, func, x_range=None, **kwargs) -> ParametricFunction
graph(axes, func, x_range=None, **kwargs) -> ParametricFunction    # Function alias
```

---

## Label Utils (`label_utils`)

```python
vertex_labels(graph, labels, font_size=24, buff=0.2, **kwargs) -> VGroup
edge_labels(graph, labels, font_size=20, buff=0.1, **kwargs) -> VGroup
```

---

## Arrow Utils (`arrow_utils`)

### ArrowUtil Static Methods
```python
ArrowUtil.arc_arrow(arc, color=WHITE, stroke_width=2, tip_length=0.2, buff=0)
ArrowUtil.smooth_arc_arrow(start, end, angle=PI/2, color=WHITE, stroke_width=2, tip_length=0.2, buff=0)
ArrowUtil.perpendicular_offset(start, end, distance) -> np.ndarray
```

---

## Custom Objects

```python
ArcArrow(arc, color=WHITE, stroke_width=2, tip_length=0.2, buff=0)
ArcDashedVMobject(*args, num_dashes=15, **kwargs)
```

---

## RogebraScene

Convenient scene class with utility methods:

```python
class RogebraScene(Scene):
    fadeIn(*args)                            # Fade in objects (last arg = run_time)
    fadeOut(*args)                           # Fade out objects (last arg = run_time)
    amo(*args)                               # Animate move_to (pairs of obj,pos)
    tf(*args)                                # Transform (pairs of source,target)
    rtf(*args)                               # ReplacementTransform (pairs of source,target)
```

### Usage Examples
```python
self.fadeIn(obj1, obj2, 2)                   # Fade in 2 objects over 2 seconds
self.fadeOut(obj1)                           # Fade out 1 object
self.amo(obj1, pos1, obj2, pos2, 1.5)        # Move 2 objects over 1.5 seconds
self.tf(obj1, target1, True, 2)              # Transform with copy over 2 seconds
```

---

## Exp Class (Alternative Interface)

All `exp_utils` functions also available as static methods:

```python
Exp.x(obj)       Exp.y(obj)        Exp.st(obj)       Exp.ed(obj)
Exp.mid(obj)     Exp.mag(obj)      Exp.uv(obj)       Exp.vec(obj)
Exp.ang(obj)     Exp.slope(obj)    Exp.val(obj)      Exp.pt(x,y,z)
Exp.m2v(...)     Exp.v2m(...)      Exp.x2v(...)      Exp.vl(...)
Exp.hl(...)      Exp.lra(...)      Exp.vra(...)      Exp.r2p(...)
Exp.ln(...)      Exp.vt(...)       Exp.tri(...)      Exp.aa(...)
Exp.aa2(...)     Exp.cr(...)       Exp.graph(...)
```

---

## Import Examples

```python
# Individual imports
from robo_manim_add_ons import x, y, pt, ln, dm, style

# Category imports
from robo_manim_add_ons import (
    # Exp utils
    x, y, st, ed, mid, mag, uv, vec, ang, slope, val,
    pt, m2v, v2m, x2v, vl, hl, lra, vra, r2p,
    ln, vt, tri, aa, aa2, cr,
    # Annotation
    dm, label, hatch,
    # Geometry
    perp, pll, project, reflect, xl,
    # Intersection
    ill, ilc,
    # Style
    stroke, fill, sopacity, fopacity, sw, style,
    # Transform
    translated, rotated, scaled,
    # Scene
    RogebraScene
)

# Class-based interface
from robo_manim_add_ons import Exp, VectorUtils, ArrowUtil, GraphUtils, Style
```

---

**Legend:**
- Functions with `->` show return types
- Functions with `*args` accept flexible arguments (see individual docs)
- Functions with `**kwargs` accept additional keyword arguments
- Chainable functions return the object for method chaining
- Aliases are short names for longer function names
