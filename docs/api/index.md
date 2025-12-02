# API Reference

Complete API reference for Robo Manim Add-ons.

## Geometry Utilities

### perp

Create a perpendicular line to a given line, passing through a dot.

**Function Signature:**
```python
from robo_manim_add_ons import perp

perp(line: Line, dot: Dot, length: float, placement: str = "mid") -> Line
```

**Parameters:**
- `line` (Line): The reference Line object
- `dot` (Dot): The Dot object through which the perpendicular line passes
- `length` (float): The length of the perpendicular line
- `placement` (str): Where the dot is positioned on the new line. Options: `"start"`, `"mid"` (default), `"end"`

**Returns:**
- `Line`: A new Line object perpendicular to the input line

**Example:**
```python
from manim import *
from robo_manim_add_ons import perp

class PerpExample(Scene):
    def construct(self):
        # Create a horizontal line
        line = Line(LEFT * 2, RIGHT * 2)
        dot = Dot(ORIGIN)

        # Create perpendicular line (vertical) centered at dot
        perp_line = perp(line, dot, length=3.0, placement="mid")

        # Display
        self.add(line, dot, perp_line)
        self.wait()
```

**See Also:**
- [Full examples in examples/geometry/](../../examples/geometry/)
- [Dynamic geometry demos](../../examples/geometry/dynamic_geometry_demo.py)

---

### parallel

Create a parallel line to a given line, passing through a dot.

**Function Signature:**
```python
from robo_manim_add_ons import parallel

parallel(line: Line, dot: Dot, length: float, placement: str = "mid") -> Line
```

**Parameters:**
- `line` (Line): The reference Line object
- `dot` (Dot): The Dot object through which the parallel line passes
- `length` (float): The length of the parallel line
- `placement` (str): Where the dot is positioned on the new line. Options: `"start"`, `"mid"` (default), `"end"`

**Returns:**
- `Line`: A new Line object parallel to the input line

**Example:**
```python
from manim import *
from robo_manim_add_ons import parallel

class ParallelExample(Scene):
    def construct(self):
        # Create a diagonal line
        line = Line(LEFT + DOWN, RIGHT + UP)
        dot = Dot(UP * 2)

        # Create parallel line starting at dot
        parallel_line = parallel(line, dot, length=4.0, placement="start")

        # Display
        self.add(line, dot, parallel_line)
        self.wait()
```

**See Also:**
- [Full examples in examples/geometry/](../../examples/geometry/)
- [Dynamic geometry demos](../../examples/geometry/dynamic_geometry_demo.py)

---

### Placement Options

The `placement` parameter controls where the dot is positioned on the newly created line:

- **`"mid"`** (default): The dot is at the midpoint of the line
- **`"start"`**: The dot is at the start of the line
- **`"end"`**: The dot is at the end of the line

**Visual Example:**
```python
from manim import *
from robo_manim_add_ons import perp

class PlacementExample(Scene):
    def construct(self):
        line = Line(LEFT * 2, RIGHT * 2)

        # Three dots at different positions
        dot_mid = Dot(ORIGIN)
        dot_start = Dot(UP * 2)
        dot_end = Dot(DOWN * 2)

        # Create perpendicular lines with different placements
        perp_mid = perp(line, dot_mid, 2.0, placement="mid")
        perp_start = perp(line, dot_start, 2.0, placement="start")
        perp_end = perp(line, dot_end, 2.0, placement="end")

        self.add(line, dot_mid, dot_start, dot_end)
        self.add(perp_mid, perp_start, perp_end)
        self.wait()
```

---

### project

Project a point onto a line (extended infinitely).

**Function Signature:**
```python
from robo_manim_add_ons import project

project(line: Line, point: Union[np.ndarray, Dot]) -> Dot
```

**Parameters:**
- `line` (Line): The reference Line object
- `point` (Dot or numpy array): The point to project

**Returns:**
- `Dot`: Dot at the projected position on the line (extended infinitely)

**Example:**
```python
from manim import *
from robo_manim_add_ons import project

class ProjectExample(Scene):
    def construct(self):
        # Create a horizontal line
        line = Line(LEFT * 2, RIGHT * 2, color=BLUE)

        # Create a point above the line
        point = Dot(UP * 2, color=RED)

        # Project point onto line
        projection = project(line, point)
        projection.set_color(GREEN)

        # Show connection
        connection = Line(point.get_center(), projection.get_center(), color=GRAY)

        self.add(line, point, projection, connection)
        self.wait()
```

**See Also:**
- [Geometry examples](../../examples/geometry/)

---

### reflect

Reflect a point across a line (extended infinitely).

**Function Signature:**
```python
from robo_manim_add_ons import reflect

reflect(line: Line, point: Union[np.ndarray, Dot]) -> Dot
```

**Parameters:**
- `line` (Line): The reference Line object
- `point` (Dot or numpy array): The point to reflect

**Returns:**
- `Dot`: Dot at the reflected position

**Example:**
```python
from manim import *
from robo_manim_add_ons import reflect

class ReflectExample(Scene):
    def construct(self):
        # Create a horizontal line (mirror)
        line = Line(LEFT * 3, RIGHT * 3, color=BLUE)

        # Create a point above the line
        point = Dot(UP * 2 + LEFT, color=RED)

        # Reflect point across line
        reflected = reflect(line, point)
        reflected.set_color(YELLOW)

        # Show connection
        connection = Line(point.get_center(), reflected.get_center(), color=GRAY)

        self.add(line, point, reflected, connection)
        self.wait()
```

**See Also:**
- [Geometry examples](../../examples/geometry/)

---

## Complete Example

Here's a comprehensive example demonstrating all geometry utilities:

```python
from manim import *
from robo_manim_add_ons import perp, parallel, project, reflect

class GeometryUtilsDemo(Scene):
    def construct(self):
        # Create a diagonal reference line
        ref_line = Line(LEFT * 2 + DOWN, RIGHT * 2 + UP, color=BLUE)

        # Create perpendicular line at origin
        dot1 = Dot(ORIGIN, color=RED)
        perp_line = perp(ref_line, dot1, length=3.0, placement="mid")
        perp_line.set_color(GREEN)

        # Create parallel line at different position
        dot2 = Dot(UP * 2 + LEFT, color=ORANGE)
        parallel_line = parallel(ref_line, dot2, length=2.5, placement="mid")
        parallel_line.set_color(YELLOW)

        # Project and reflect a point
        point = Dot(UP * 3, color=RED)
        projection = project(ref_line, point).set_color(GREEN)
        reflection = reflect(ref_line, point).set_color(PURPLE)

        # Animate
        self.play(Create(ref_line))
        self.play(Create(dot1), Create(perp_line))
        self.play(Create(dot2), Create(parallel_line))
        self.play(Create(point), Create(projection), Create(reflection))
        self.wait()
```

**See Also:**
- [View all geometry examples](../../examples/geometry/)
- [Dynamic geometry demonstrations](../../examples/geometry/dynamic_geometry_demo.py)

---

## Back to [Documentation Home](../)
