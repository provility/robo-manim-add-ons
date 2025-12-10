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

mid(*args) -> Dot
# Flexible function with two forms:
#   mid(obj) - midpoint of obj (Line/Circle/VMobject with get_center())
#   mid(pt1, pt2) - midpoint between two points (Dot/np.array/list)
```

### Vector Operations
```python
mag(*args) -> float
# Single function with flexible args:
#   mag(obj) - magnitude/length of obj (Line/Arc/np.array/list)
#   mag(pt1, pt2) - distance between two points (Dot/np.array/list)

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

a2p(circle, angle_degrees) -> Dot
# Point on circle at angle (degrees). 0=right, 90=top, 180=left, 270=bottom
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

rangle(line1, line2, length=0.3, quadrant=(1,1)) -> RightAngle
# Right angle marker (L-shape) at intersection of two lines
# quadrant: (1,1)=upper-right, (1,-1)=lower-right, (-1,1)=upper-left, (-1,-1)=lower-left
```

### Circle Utilities (angles in degrees)
```python
tangentc(circle, angle, length=3) -> TangentLine
# Tangent line at angle (degrees) or point. Wraps Manim's TangentLine with degree conversion
# angle: degrees (0°=right, CCW) or Dot/np.array point on circle

chord(circle, angle1, angle2) -> Line
# Chord (line) between two angles on circle. When |angle2-angle1|=180, creates diameter

normal(circle, angle, length=3, placement="mid") -> Line
# Normal/radius line extended. placement: "start"|"mid"|"end" for point position on line

sector(circle, start, end, **kwargs) -> Sector
# Filled sector (pie slice) between start and end angles. Wraps Manim's Sector
```

### Triangle Centers & Altitude
```python
centroid(A, B, C) -> Dot
# Centroid: intersection of medians, (A+B+C)/3. A,B,C: Dot/np.array/list

circumcenter(A, B, C) -> Dot
# Circumcenter: center of circumscribed circle (perpendicular bisector intersection)

orthocenter(A, B, C) -> Dot
# Orthocenter: intersection of altitudes

incenter(A, B, C) -> Dot
# Incenter: center of inscribed circle (angle bisector intersection)

altitude(vertex, *args) -> Line
# Altitude from vertex perpendicular to opposite side
# Args: (vertex, line) | (vertex, p1, p2) where line or p1,p2 define the opposite side
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

icc(c1, c2) -> VGroup
# Circle-circle intersection. c1, c2: Circle objects
# Returns: VGroup of 0, 1, or 2 Dots (0=no intersection, 1=tangent, 2=intersecting)

ilp(line, polygon) -> VGroup
# Line-polygon intersection. line: Line (treated as infinite), polygon: Polygon
# Returns: VGroup of Dots at all intersection points with polygon edges
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
graph(*args, x_range=[-5, 5], y_range=[-5, 5], axes=None, x_ticks=None, y_ticks=None, coords=True, **kwargs) -> Tuple[Axes, object]
# Returns: (axes, plot) - the Axes object and plotted function
# x_ticks/y_ticks: None (auto), "pi", "pi/2", "2pi", or False (regular numbers)
# coords: True adds coordinate numbers (default), False hides them
GraphUtils.graph(...)    # Class method version (same signature)
```

**Examples:**
```python
# Explicit plot (1 string, no "=")
axes, plot = graph("x**2")                      # Parabola
axes, plot = graph("sin(x)")                    # Auto π ticks on x-axis
axes, plot = graph("y = 2*x + 1")               # "y=" prefix stripped

# Implicit plot (1 string with "=")
axes, plot = graph("x**2 + y**2 = 4")           # Circle radius 2
axes, plot = graph("x*y = 1")                   # Hyperbola

# Parametric plot (2 strings)
axes, plot = graph("cos(t)", "sin(t)")          # Unit circle
axes, plot = graph("t*cos(t)", "t*sin(t)")      # Spiral

# Custom ranges
axes, plot = graph("sin(x)", x_range=[0, 2*PI], y_range=[-1.5, 1.5])

# Manual π tick control
axes, plot = graph("sin(x)", x_ticks="pi/2")    # Finer π/2 ticks
axes, plot = graph("tan(x)", x_ticks="pi", y_range=[-10, 10])

# Disable auto features
axes, plot = graph("sin(x)", x_ticks=False)     # No π ticks, use numbers
axes, plot = graph("x**2", coords=False)        # No coordinate numbers

# Styling
axes, plot = graph("x**2", color=RED, stroke_width=4)
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

scalev(vector, scalar, start_point=None, **kwargs) -> Arrow
# Scalar multiplication. vector must be Arrow, scalar is numeric. Returns scaled Arrow

# Vector decomposition & projection (use short aliases)
VectorUtils.prov(vec, target, **kwargs) -> Arrow
# Project onto: project Arrow 'vec' onto Arrow 'target'. Returns projection Arrow

VectorUtils.dcv(source, ref, perp=False, **kwargs) -> Arrow
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
# These are methods on RogebraScene (no scene argument needed)

part(mathtext, *indices) -> MathTex
# Extract parts from MathTex and color RED. mathtext: string (creates MathTex) or MathTex object
# indices: int or "1:2" slice strings. Chainable: eq[1][2] same as (eq, 1, 2)
# Silently fails on invalid indices, returns empty VMobject

part2(mathtext, *indices) -> MathTex
# Debug version: extracts parts + highlights with RED color and ORANGE box
# Same params as part(). Use for visual debugging of MathTex structure

textdg(tex, scale=2, lscale=0.3, buff=0.05, color_tex=True) -> VGroup
# Debug utility: show index labels below each MathTex character
# tex: string (creates MathTex) or MathTex object
# scale: scale factor for MathTex, lscale: scale for labels, buff: label spacing
# Returns VGroup with MathTex and colored index labels (word,char format)
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

    # MathTex utilities
    part(mathtext, *indices) -> MathTex
    # Extract MathTex parts and color RED. mathtext: string or MathTex, indices: int or slice strings

    part2(mathtext, *indices) -> MathTex
    # Debug version with RED + ORANGE highlight

    textdg(tex, scale=2, lscale=0.3, buff=0.05, color_tex=True) -> VGroup
    # Show index labels (word,char) below each character with cycling colors
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
eq = self.part("x^2 + y^2 = r^2")            # Create MathTex
p = self.part(eq, 0)                         # Extract eq[0]
self.part2(eq, 1, "2:4")                     # Show eq[1][2:4] with highlight

# Debug MathTex indices
self.textdg(r"\sin(x) = \frac{a}{b}")        # Show with colored index labels
```

---

All expression utilities available as static methods:

```python
Exp.x(obj)       Exp.y(obj)        Exp.st(obj)       Exp.ed(obj)       Exp.mid(obj)
Exp.mag(obj)     Exp.uv(obj)       Exp.vec(obj)      Exp.ang(obj)      Exp.slope(obj)
Exp.val(obj)     Exp.pt(x,y,z)     Exp.m2v(...)      Exp.v2m(...)      Exp.x2v(...)
Exp.vl(...)      Exp.hl(...)       Exp.lra(...)      Exp.vra(...)      Exp.r2p(...)      Exp.a2p(...)
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
    pt, m2v, v2m, x2v, r2p, a2p, addp,
    # Lines & shapes
    vl, hl, lra, vra, ln, vt, tri, sss, sas, ssa, rect, aa, aa2, rangle, cr,
    # Circle utilities
    tangentc, chord, normal, sector,
    # Triangle utilities
    centroid, circumcenter, orthocenter, incenter, altitude,
    # Geometry
    perp, pll, project, reflect, xl,
    # Intersection
    ill, ilc, icc, ilp,
    # Annotation
    dm, label, hatch,
    # Style
    stroke, fill, sopacity, fopacity, sw, style,
    # Transform
    translated, rotated, scaled,
    # Vector operations
    addv, subv, scalev,
    # MathTex utilities (standalone, require scene arg)
    part, part2,
    # Scene
    RogebraScene
)

# Class-based interface
from robo_manim_add_ons import Exp, VectorUtils, PointUtils, TextUtils, ArrowUtil, GraphUtils, Style

# Note: ArcArrow and ArcDashedVMobject are internal - use aa() and aa2() instead
```

---

**Getters:** `x` `y` `st` `ed` `mid` `mag` `uv` `vec` `ang` `slope` `val`
**Creators:** `pt` `m2v` `v2m` `x2v` `r2p` `a2p` `vl` `hl` `lra` `vra` `ln` `vt` `tri` `sss` `sas` `ssa` `rect` `cr` `aa` `aa2` `rangle`
**Circle:** `tangentc` `chord` `normal` `sector`
**Triangle:** `centroid` `circumcenter` `orthocenter` `incenter` `altitude`
**Geometry:** `perp` `pll` `project` `reflect` `xl` `ill` `ilc` `icc` `ilp`
**Annotation:** `dm` `label` `hatch`
**Style:** `stroke` `fill` `sopacity` `fopacity` `sw` `style`
**Transform:** `translated` `rotated` `scaled`
**Vector Ops:** `addv` `subv` `scalev` `VectorUtils`
**Point Ops:** `addp` `PointUtils`
**MathTex Ops:** `part` `part2` `textdg`
**Scene Utils:** `RogebraScene` (fadeIn, fadeOut, amo, tf, rtf, zoom, part, part2, textdg)

---

**Notes:**
- All 2-letter functions are aliases for longer names
- Functions with `*args` accept flexible arguments (see individual docs)
- Chainable functions return the object for method chaining
- Angles in degrees for `lra`/`vra`, radians for `ang`/`rotated`
- Points can be: Dot, np.array, [x,y,z], or any object with `get_center()`
