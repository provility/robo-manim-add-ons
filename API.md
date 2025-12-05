# Robo Manim Add-ons API Reference

Compact API listing for quick reference. All utilities organized in one place.

---

## Core Expression Utils

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
val(obj) -> float                            # Get value from ValueTracker/number
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
lra(radius, angle, from_x=0, from_y=0) -> Line       # Line using polar coords (degrees)
vra(radius, angle, from_x=0, from_y=0) -> Arrow     # Arrow using polar coords (degrees)
ln(*args) -> Line                            # Flexible Line (red): (pt,pt) | (x,y,x,y) | (pt,x,y)
vt(*args) -> Arrow                           # Flexible Arrow (red): same as ln
```

### Shape Creation
```python
tri(p1, p2, p3) -> Polygon                   # Triangle from three points (red)
rect(*args) -> Rectangle                     # Rectangle: (w,h) | (lb,tr) | (lb,lt,rt,rb)
cr(*args) -> Circle                          # Circle: (line) | (center,radius) | (pt,pt)
aa(*args, radius=0.5, dash=True) -> ArcArrow         # Angle arc (dashed): (l1,l2) | (p1,vertex,p3)
aa2(*args, radius=0.5) -> Angle              # Manim Angle: supports quadrant control
```

### Geometry Operations
```python
perp(line, dot, length, placement="mid") -> Line    # Perpendicular line
pll(line, dot, length, placement="mid") -> Line     # Parallel line (alias: parallel)
project(line, point) -> Dot                  # Project point onto line (infinite)
reflect(line, point) -> Dot                  # Reflect point across line (infinite)
xl(line, proportion, length) -> Line         # Extend line (alias: extended_line)
```

### Intersection Operations
```python
ill(line1, line2) -> Union[Dot, VGroup]      # Line-line intersection (alias: intersect_lines)
ilc(line, circle) -> VGroup                  # Line-circle intersection (alias: intersect_line_circle)
```

### Annotation
```python
dm(pt1, pt2=None, **kwargs)                  # Distance marker (alias: distance_marker)
# Key params: text="", color="#1e40af", stroke_width=2, tick_size=0.25, label_offset=0.3, marker_offset=0
label(latex_text, pt1, pt2, buff=0.5, alpha=0.5, auto_rotate=True) -> MathTex
hatch(axes, vertices, **kwargs)              # Hatched region (alias: hatched_region)
# Key params: spacing=0.2, direction="/", color="#808080", stroke_width=2
```

### Style Operations (Chainable)
```python
stroke(obj, color) -> VMobject               # Set stroke color
fill(obj, color) -> VMobject                 # Set fill color
sopacity(obj, opacity) -> VMobject           # Set stroke opacity
fopacity(obj, opacity) -> VMobject           # Set fill opacity
sw(obj, width) -> VMobject                   # Set stroke width
style(obj) -> Style                          # Get Style wrapper for chaining
```

**Style Chaining:**
```python
style(circle).fill(BLUE).stroke(RED).sw(3).fopacity(0.5).sopacity(1)
```

### Transform Operations
```python
translated(obj, dx, dy) -> Mobject           # Copy and translate
rotated(obj, angle_deg, about=None) -> Mobject          # Copy and rotate
scaled(obj, scale_factor, about=None) -> Mobject        # Copy and scale
```

### Graph Operations
```python
graph(axes, func, x_range=None, **kwargs) -> ParametricFunction
GraphUtils.graph(axes, func, x_range=None, **kwargs)    # Class method version
```

---

## Vector Utils (VectorUtils Class)

```python
VectorUtils.forward(source, distance) -> Mobject        # Copy forward by distance
VectorUtils.fw(source, distance) -> Mobject             # Alias
VectorUtils.backward(source, distance) -> Mobject       # Copy backward by distance
VectorUtils.bw(source, distance) -> Mobject             # Alias
VectorUtils.perp_move(source, distance) -> Mobject      # Copy perpendicular by distance
VectorUtils.pm(source, distance) -> Mobject             # Alias
VectorUtils.copy_at(source, position) -> Mobject        # Copy at position
VectorUtils.reverse_at(source, position) -> Mobject     # Copy reversed at position
```

---

## Label Utils

```python
vertex_labels(graph, labels, font_size=24, buff=0.2, **kwargs) -> VGroup
edge_labels(graph, labels, font_size=20, buff=0.1, **kwargs) -> VGroup
```

---

## Arrow Utils (ArrowUtil Class)

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

**Examples:**
```python
self.fadeIn(obj1, obj2, 2)                   # Fade in 2 objects over 2 seconds
self.fadeOut(obj1)                           # Fade out 1 object
self.amo(obj1, pos1, obj2, pos2, 1.5)        # Move 2 objects over 1.5 seconds
self.tf(obj1, target1, True, 2)              # Transform with copy over 2 seconds
```

---

## Exp Class (Alternative Interface)

All expression utilities available as static methods:

```python
Exp.x(obj)       Exp.y(obj)        Exp.st(obj)       Exp.ed(obj)       Exp.mid(obj)
Exp.mag(obj)     Exp.uv(obj)       Exp.vec(obj)      Exp.ang(obj)      Exp.slope(obj)
Exp.val(obj)     Exp.pt(x,y,z)     Exp.m2v(...)      Exp.v2m(...)      Exp.x2v(...)
Exp.vl(...)      Exp.hl(...)       Exp.lra(...)      Exp.vra(...)      Exp.r2p(...)
Exp.ln(...)      Exp.vt(...)       Exp.tri(...)      Exp.rect(...)     Exp.aa(...)
Exp.aa2(...)     Exp.cr(...)       Exp.graph(...)
```

---

## Import Examples

```python
# Minimal imports
from robo_manim_add_ons import x, y, pt, ln, dm, style

# All expression utils
from robo_manim_add_ons import (
    # Coords & vectors
    x, y, st, ed, mid, mag, uv, vec, ang, slope, val,
    # Points
    pt, m2v, v2m, x2v, r2p,
    # Lines & shapes
    vl, hl, lra, vra, ln, vt, tri, rect, aa, aa2, cr,
    # Geometry
    perp, pll, project, reflect, xl,
    # Intersection
    ill, ilc,
    # Annotation
    dm, label, hatch,
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

## Quick Reference by Category

**Getters:** `x` `y` `st` `ed` `mid` `mag` `uv` `vec` `ang` `slope` `val`
**Creators:** `pt` `m2v` `v2m` `x2v` `r2p` `vl` `hl` `lra` `vra` `ln` `vt` `tri` `rect` `cr` `aa` `aa2`
**Geometry:** `perp` `pll` `project` `reflect` `xl` `ill` `ilc`
**Annotation:** `dm` `label` `hatch`
**Style:** `stroke` `fill` `sopacity` `fopacity` `sw` `style`
**Transform:** `translated` `rotated` `scaled`

---

**Notes:**
- All 2-letter functions are aliases for longer names
- Functions with `*args` accept flexible arguments (see individual docs)
- Chainable functions return the object for method chaining
- Angles in degrees for `lra`/`vra`, radians for `ang`/`rotated`
- Points can be: Dot, np.array, [x,y,z], or any object with `get_center()`
