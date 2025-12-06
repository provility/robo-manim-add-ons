### Coordinate Extraction
```python
x(obj) -> float
# Extract x-coordinate. obj can be: Manim object with get_center() (Dot, VMobject),
# np.array [x,y,z], or list [x,y,z]

y(obj) -> float
# Extract y-coordinate. obj can be: Manim object with get_center() (Dot, VMobject),
# np.array [x,y,z], or list [x,y,z]

st(obj) -> Dot
# Get start point as Dot. obj can be: Manim object with get_start() (Line, Arc),
# np.array [x,y,z], or list [x,y,z]

ed(obj) -> Dot
# Get end point as Dot. obj can be: Manim object with get_end() (Line, Arc),
# np.array [x,y,z], or list [x,y,z]

mid(obj) -> Dot
# Get midpoint as Dot. obj must be: Manim object with get_center() (Line, Circle, VMobject)
```

### Vector Operations
```python
mag(obj) -> float
# Get magnitude/length. obj can be: Manim object with get_length() (Line, Arc),
# np.array (calculates norm), or list (converts to array then norm)

mag(pt1, pt2) -> float
# Distance between two points. pt1, pt2 can each be: Dot, np.array, or list

uv(obj) -> np.ndarray
# Get unit vector. obj can be: Manim object with get_unit_vector() (Line, Vector),
# np.array (normalizes), or list (converts then normalizes)

vec(obj) -> np.ndarray
# Get vector. obj can be: Manim object with get_vector() (Line - returns end-start),
# np.array (returned as-is), or list (converted to np.array)

ang(obj) -> float
# Get angle in radians. obj can be: Manim object with get_angle() (Line),
# np.array (calculates arctan2(y,x)), or list (converts then arctan2)

slope(obj) -> float
# Get slope (y/x). obj can be: Manim object with get_slope() (Line),
# np.array (y/x), or list (converts then y/x)

val(obj) -> float
# Get value. obj can be: Manim object with get_value() (ValueTracker, Variable),
# or numeric value (int/float - returned as float)
```

### Point Creation
```python
pt(x, y, z=0) -> Dot
# Create Dot at coordinates (x, y, z). x, y, z are numeric values

m2v(axes, x, y) -> Dot
# Model to view coordinates. Converts axes coordinates (x,y) to screen point as Dot

v2m(axes, x, y) -> Dot
# View to model coordinates. Converts screen point (x,y) to axes coordinates as Dot

x2v(axes, graph, x) -> Dot
# Point on graph at x-value. Wrapper for axes.i2gp(x, graph), returns Dot on graph

r2p(obj, proportion) -> Dot
# Point at proportion along object. obj must have point_from_proportion() (Line, Arc, VMobject).
# proportion: 0=start, 1=end
```

### Line/Arrow Creation
```python
vl(x, y1=-20, y2=20) -> Line
# Vertical line at x from y1 to y2

hl(y, x1=-20, x2=20) -> Line
# Horizontal line at y from x1 to x2

lra(radius, angle, from_x=0, from_y=0) -> Line
# Line using polar coords (angle in DEGREES). From (from_x, from_y) with given radius and angle

vra(radius, angle, from_x=0, from_y=0) -> Arrow
# Arrow using polar coords (angle in DEGREES). From (from_x, from_y) with given radius and angle

ln(*args) -> Line
# Flexible red Line. Args: (pt, pt) | (x,y, x,y) | (pt, x,y) | (x,y, pt)
# pt can be: Dot, VMobject with get_center(), or np.array

vt(*args) -> Arrow
# Flexible red Arrow. Same args as ln(): (pt, pt) | (x,y, x,y) | (pt, x,y) | (x,y, pt)
# pt can be: Dot, VMobject with get_center(), or np.array
```

### Shape Creation
```python
tri(p1, p2, p3) -> Polygon
# Red triangle from three points. p1, p2, p3 can each be: Dot, VMobject with get_center(), or np.array

sss(a, b=None, c=None) -> Polygon
# Red triangle using SSS construction. (a) = equilateral, (a,b,c) = scalene/isosceles

sas(a, angle_deg, b) -> Polygon
# Red triangle using SAS construction. angle_deg in DEGREES between sides a and b

ssa(a, b, angle_deg) -> Polygon
# Red triangle using SSA construction (ambiguous case). Returns first valid solution

rect(*args) -> Rectangle
# Rectangle. Args: (width, height) | (left_bottom, top_right) | (lb, lt, rt, rb)
# Points can be: np.array, list, or Dot

cr(*args) -> Circle
# Circle. Args: (line) center at line.get_center(), diameter=line.length |
# (center, radius) where center is Dot/np.array | (pt1, pt2) midpoint=center, distance=diameter

aa(*args, radius=0.5, dash=True) -> ArcArrow
# Angle arc visualization. Args: (line1, line2) | (p1, vertex, p3) where vertex is angle vertex.
# dash=True for dashed arc, dash=False for solid. Points can be: Dot, VMobject, or np.array

aa2(*args, radius=0.5, **kwargs) -> Angle
# Manim Angle with quadrant control. Args: (line1, line2) | (line1, line2, quadrant) |
# (p1, vertex, p3) | (p1, vertex, p3, quadrant). quadrant: 1/-1 for CCW/CW, True/False for reflex
```

### Geometry Operations
```python
perp(line, dot, length, placement="mid") -> Line
# Perpendicular line to 'line' passing through 'dot'. placement: "start"|"mid"|"end"

pll(line, dot, length, placement="mid") -> Line
# Parallel line to 'line' passing through 'dot'. placement: "start"|"mid"|"end"
# Alias: parallel()

project(line, point) -> Dot
# Project point onto line (extended infinitely). point can be: Dot or np.array

reflect(line, point) -> Dot
# Reflect point across line (extended infinitely). point can be: Dot or np.array

xl(line, proportion, length) -> Line
# Extend line at proportion (0=start, 1=end) by length. Alias: extended_line()
```

### Intersection Operations
```python
ill(line1, line2) -> Union[Dot, VGroup]
# Line-line intersection. Returns: Dot (if intersect) or empty VGroup (if parallel)
# Alias: intersect_lines()

ilc(line, circle) -> VGroup
# Line-circle intersection. Returns: VGroup of 0, 1, or 2 Dots depending on intersection
# Alias: intersect_line_circle()
```

### Annotation
```python
dm(pt1, pt2=None, **kwargs) -> VGroup
# Distance marker. Args: (line) | (pt1, pt2) where pt1, pt2 can be: Dot, np.array, or list
# Key params: text="", color="#1e40af", stroke_width=2, tick_size=0.25, label_offset=0.3
# Alias: distance_marker()

label(latex_text, pt1, pt2, buff=0.5, alpha=0.5, auto_rotate=True) -> MathTex
# MathTex label between two points with perpendicular offset
# pt1, pt2 can each be: Dot, np.array, list, or VMobject with get_center()

hatch(axes, vertices, **kwargs) -> VGroup
# Hatched region visualization. vertices: list of (x,y) tuples in axes coordinates
# Key params: spacing=0.2, direction="/"|"\"|"-"|"|", color="#808080", stroke_width=2
# Alias: hatched_region()
```

### Style Operations (Chainable)
```python
stroke(obj, color) -> VMobject
# Set stroke color. obj: any VMobject. Returns obj for chaining

fill(obj, color) -> VMobject
# Set fill color. obj: any VMobject. Returns obj for chaining

sopacity(obj, opacity) -> VMobject
# Set stroke opacity (0-1). obj: any VMobject. Returns obj for chaining

fopacity(obj, opacity) -> VMobject
# Set fill opacity (0-1). obj: any VMobject. Returns obj for chaining

sw(obj, width) -> VMobject
# Set stroke width. obj: any VMobject. Returns obj for chaining

style(obj) -> Style
# Get Style wrapper for method chaining. All above methods available
```

**Style Chaining:**
```python
style(circle).fill(BLUE).stroke(RED).sw(3).fopacity(0.5).sopacity(1)
```

### Transform Operations
```python
translated(obj, dx, dy) -> Mobject
# Copy obj and translate by (dx, dy). Returns new copy, original unchanged

rotated(obj, angle_deg, about=None) -> Mobject
# Copy obj and rotate by angle_deg (DEGREES). about: rotation point (default: obj center)

scaled(obj, scale_factor, about=None) -> Mobject
# Copy obj and scale by factor. about: scaling point (default: obj center)
```

### Graph Operations
```python
graph(*args, x_range=[-5, 5], y_range=[-5, 5], axes=None, x_ticks=None, y_ticks=None,
      coords=True, **kwargs) -> Tuple[Axes, object]
# Create graph with flexible equation input
# Args: (equation_str) for explicit/implicit | (x_expr, y_expr) for parametric
# equation_str examples: "y=x**2", "x**2+y**2=1", "r=2*cos(theta)" (polar)
# Returns: (axes, plot) - the Axes object and plotted function
# GraphUtils.graph(...) - Class method version with same signature
```

---

```python
# Vector positioning (use short aliases)
VectorUtils.fw(source, distance) -> Arrow
# Forward: copy Arrow 'source' moved forward by distance. source must be Arrow

VectorUtils.bw(source, distance) -> Arrow
# Backward: copy Arrow 'source' moved backward by distance. source must be Arrow

VectorUtils.pm(source, distance) -> Arrow
# Perp move: copy Arrow 'source' moved perpendicular by distance. source must be Arrow

VectorUtils.cp(source, start_point, **kwargs) -> Arrow
# Copy at: copy Arrow with same direction at new start_point. start_point: np.array or Dot

VectorUtils.rv(source, start_point, **kwargs) -> Arrow
# Reverse at: copy Arrow reversed at new start_point. start_point: np.array or Dot

VectorUtils.tt(vec_a, vec_b) -> Arrow
# Tail at tip: position vec_b's tail at vec_a's tip. Both must be Arrows

VectorUtils.sa(vec_target, vec_source) -> np.ndarray
# Shift amount: calculate shift vector to move vec_source to vec_target position

# Vector arithmetic (standalone functions)
addv(vec_a, vec_b, start_point=None, **kwargs) -> Arrow
# Vector addition a + b. vec_a, vec_b must be Arrows. Returns new Arrow for sum

subv(vec_a, vec_b, start_point=None, **kwargs) -> Arrow
# Vector subtraction a - b. vec_a, vec_b must be Arrows. Returns new Arrow for difference

sclv(vector, scalar, start_point=None, **kwargs) -> Arrow
# Scalar multiplication. vector must be Arrow, scalar is numeric. Returns scaled Arrow

# Vector decomposition & projection (use short aliases)
VectorUtils.po(vec, target, **kwargs) -> Arrow
# Project onto: project Arrow 'vec' onto Arrow 'target'. Returns projection Arrow

VectorUtils.dc(source, ref, perp=False, **kwargs) -> Arrow
# Decompose: get parallel (perp=False) or perpendicular (perp=True) component of 'source' to 'ref'

VectorUtils.projection_line(vec, target, **kwargs) -> Line
# Perpendicular line from vec tip to projection on target

VectorUtils.projection_region(vec, target, **kwargs) -> Polygon
# Triangle region showing projection visualization
```

---

```python
addp(point, vector, **dot_kwargs) -> Dot
# Displace point by vector. point: Dot or np.array, vector: Arrow or np.array
# Returns new Dot at displaced position
# PointUtils.addp(...) - Class method version with same signature
```

---

```python
text(scene, mathtext, *indices) -> MathTex
# Extract parts from MathTex. mathtext: string (creates MathTex) or MathTex object
# indices: int or "1:2" slice strings. Chainable: eq[1][2] same as (eq, 1, 2)
# Silently fails on invalid indices, returns empty VMobject

text2(scene, mathtext, *indices) -> MathTex
# Debug version: extracts parts + highlights with BLUE color and ORANGE box
# Same params as text(). Use for visual debugging of MathTex structure

# TextUtils.text(...), TextUtils.text2(...) - Class method versions with same signatures
```

---

```python
vertex_labels(polygon, labels, scale=0.7, color=WHITE, buff=0.3) -> list
# Create labels at polygon vertices. labels: list of strings for each vertex
# Returns list of MathTex objects positioned at vertices

edge_labels(polygon, labels, scale=0.6, color=YELLOW, buff=0.2) -> list
# Create labels at polygon edge midpoints. labels: list of strings for each edge
# Returns list of MathTex objects positioned at edge midpoints
```

---

```python
ArrowUtil.arrow(start, end, buff=0, dashed=False, bidirectional=False,
                tip_angle=20*DEGREES, tip_length=0.3, **kwargs) -> VMobject
# Advanced arrow. start, end: np.array or Dot. buff: perpendicular offset distance
# dashed: dashed line, bidirectional: tips on both ends

ArrowUtil.curved_arrow(start, end, angle=45*DEGREES, tip_angle=20*DEGREES,
                      tip_length=0.3, **kwargs) -> VMobject
# Curved arrow along circular arc. start, end: np.array or Dot, angle: arc curvature

ArrowUtil.perpendicular_offset(start, end, distance) -> np.ndarray
# Calculate perpendicular offset vector. start, end: np.array, distance: offset amount

ArrowUtil.label(arrow, tex, buff=0.2) -> VMobject
# Position MathTex label relative to arrow with perpendicular offset

ArrowUtil.marker(point, direction, tip_angle=20*DEGREES, tip_length=0.3, **kwargs) -> VGroup
# Directional marker (arrow tip only). point, direction: np.array
```

---

Convenient scene class extending MovingCameraScene with utility methods:

```python
class RogebraScene(MovingCameraScene):
    # Animation shortcuts
    fadeIn(*args)
    # Fade in objects. Args: (obj1, obj2, ..., run_time) where last numeric arg is run_time

    fadeOut(*args)
    # Fade out objects. Args: (obj1, obj2, ..., run_time) where last numeric arg is run_time

    amo(*args)
    # Animate move_to. Args: (obj1, pos1, obj2, pos2, ..., run_time)
    # Pairs of object-position, last numeric arg is run_time

    tf(*args)
    # Transform. Args: (source1, target1, source2, target2, ..., run_time)
    # Pairs of source-target, last numeric arg is run_time

    rtf(*args)
    # ReplacementTransform. Args: (source1, target1, source2, target2, ..., run_time)
    # Pairs of source-target, last numeric arg is run_time

    # Camera utilities
    zoom(obj, wait_time=0.3, width_factor=1.2)
    # Zoom camera to object, wait, then restore. obj: any Mobject

    # MathTex utilities (same as TextUtils)
    text(mathtext, *indices) -> MathTex
    # Extract MathTex parts. mathtext: string or MathTex, indices: int or slice strings

    text2(mathtext, *indices) -> MathTex
    # Debug version with BLUE + ORANGE highlight
```

**Examples:**
```python
# Animation shortcuts
self.fadeIn(obj1, obj2, 2)                   # Fade in 2 objects over 2 seconds
self.fadeOut(obj1)                           # Fade out 1 object
self.amo(obj1, pos1, obj2, pos2, 1.5)        # Move 2 objects over 1.5 seconds
self.tf(obj1, target1, True, 2)              # Transform with copy over 2 seconds

# Camera zoom
self.zoom(equation)                          # Quick zoom to equation
self.zoom(text, 1.0, 1.5)                    # Zoom for 1s with 1.5x width

# MathTex extraction
eq = self.text("x^2 + y^2 = r^2")            # Create MathTex
part = self.text(eq, 0)                      # Extract eq[0]
self.text2(eq, 1, "2:4")                     # Show eq[1][2:4] with highlight
```

---

All expression utilities available as static methods:

```python
Exp.x(obj)       Exp.y(obj)        Exp.st(obj)       Exp.ed(obj)       Exp.mid(obj)
Exp.mag(obj)     Exp.uv(obj)       Exp.vec(obj)      Exp.ang(obj)      Exp.slope(obj)
Exp.val(obj)     Exp.pt(x,y,z)     Exp.m2v(...)      Exp.v2m(...)      Exp.x2v(...)
Exp.vl(...)      Exp.hl(...)       Exp.lra(...)      Exp.vra(...)      Exp.r2p(...)
Exp.ln(...)      Exp.vt(...)       Exp.tri(...)      Exp.sss(...)      Exp.sas(...)
Exp.ssa(...)     Exp.rect(...)     Exp.aa(...)       Exp.aa2(...)      Exp.cr(...)
Exp.graph(...)
```

---

```python
# Minimal imports
from robo_manim_add_ons import x, y, pt, ln, dm, style

# All expression utils
from robo_manim_add_ons import (
    # Coords & vectors
    x, y, st, ed, mid, mag, uv, vec, ang, slope, val,
    # Points
    pt, m2v, v2m, x2v, r2p, addp,
    # Lines & shapes
    vl, hl, lra, vra, ln, vt, tri, sss, sas, ssa, rect, aa, aa2, cr,
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
    # Vector operations
    addv, subv, sclv,
    # Text utilities
    text, text2,
    # Scene
    RogebraScene
)

# Class-based interface
from robo_manim_add_ons import Exp, VectorUtils, PointUtils, TextUtils, ArrowUtil, GraphUtils, Style

# Note: ArcArrow and ArcDashedVMobject are internal - use aa() and aa2() instead
```

---

**Getters:** `x` `y` `st` `ed` `mid` `mag` `uv` `vec` `ang` `slope` `val`
**Creators:** `pt` `m2v` `v2m` `x2v` `r2p` `vl` `hl` `lra` `vra` `ln` `vt` `tri` `sss` `sas` `ssa` `rect` `cr` `aa` `aa2`
**Geometry:** `perp` `pll` `project` `reflect` `xl` `ill` `ilc`
**Annotation:** `dm` `label` `hatch`
**Style:** `stroke` `fill` `sopacity` `fopacity` `sw` `style`
**Transform:** `translated` `rotated` `scaled`
**Vector Ops:** `addv` `subv` `sclv` `VectorUtils`
**Point Ops:** `addp` `PointUtils`
**Text Ops:** `text` `text2` `TextUtils`
**Scene Utils:** `RogebraScene` (fadeIn, fadeOut, amo, tf, rtf, zoom, text, text2)

---

**Notes:**
- All 2-letter functions are aliases for longer names
- Functions with `*args` accept flexible arguments (see individual docs)
- Chainable functions return the object for method chaining
- Angles in degrees for `lra`/`vra`, radians for `ang`/`rotated`
- Points can be: Dot, np.array, [x,y,z], or any object with `get_center()`
