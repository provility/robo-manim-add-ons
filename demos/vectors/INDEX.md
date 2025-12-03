# Vector Utilities

Demonstrations of vector operations using `VectorUtils`.

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

![ReverseAtDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/ReverseAtDemo_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/ReverseAtDemo.mp4)**

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

![ProjectionDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/ProjectionDemo_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/ProjectionDemo.mp4)**

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

![ProjectionScalingDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/ProjectionScalingDemo_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/ProjectionScalingDemo.mp4)**

---

## BasicDecompositionDemo
**Vector decomposition into parallel and perpendicular components**

```python
from robo_manim_add_ons.vector_utils import VectorUtils

# Reference vector (horizontal)
vector_b = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE)

# Vector to decompose
vector_a = Arrow(ORIGIN, RIGHT * 2 + UP * 1.5, buff=0, color=RED)

# Create decomposition components
parallel = VectorUtils.decompose_parallel(vector_a, vector_b, color=GREEN)
perp = VectorUtils.decompose_perp(vector_a, vector_b, color=ORANGE)

self.play(GrowArrow(parallel))
self.play(GrowArrow(perp))

# Add dashed line to complete the decomposition triangle
dashed = DashedLine(vector_a.get_end(), parallel.get_end(), color=GRAY)
self.play(Create(dashed))
```

![BasicDecompositionDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/BasicDecompositionDemo_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/BasicDecompositionDemo.mp4)**

---

## RotatingVectorDecomposition
**Decomposition updates as vector rotates**

```python
from robo_manim_add_ons.vector_utils import VectorUtils

# Fixed reference vector
vector_b = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE)

# Rotating vector
vector_a = Arrow(ORIGIN, RIGHT * 2 + UP * 1, buff=0, color=RED)

# Create dynamic decomposition with always_redraw
parallel = always_redraw(
    lambda: VectorUtils.decompose_parallel(vector_a, vector_b, color=GREEN)
)

perp = always_redraw(
    lambda: VectorUtils.decompose_perp(vector_a, vector_b, color=ORANGE)
)

dashed = always_redraw(
    lambda: DashedLine(vector_a.get_end(), parallel.get_end(), color=GRAY)
)

# Rotate vector_a - watch decomposition change
self.play(Rotate(vector_a, angle=PI, about_point=ORIGIN), run_time=4)
```

![RotatingVectorDecomposition](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/RotatingVectorDecomposition_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/RotatingVectorDecomposition.mp4)**

---

## RotatingReferenceDecomposition
**Decomposition updates as reference vector rotates**

```python
from robo_manim_add_ons.vector_utils import VectorUtils

# Vector to decompose (fixed)
vector_a = Arrow(ORIGIN, RIGHT * 2.5 + UP * 1.5, buff=0, color=RED)

# Rotating reference vector
vector_b = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE)

# Create dynamic decomposition
parallel = always_redraw(
    lambda: VectorUtils.decompose_parallel(vector_a, vector_b, color=GREEN)
)

perp = always_redraw(
    lambda: VectorUtils.decompose_perp(vector_a, vector_b, color=ORANGE)
)

# Rotate reference vector - decomposition changes
self.play(Rotate(vector_b, angle=PI/2, about_point=ORIGIN), run_time=3)
```

![RotatingReferenceDecomposition](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/RotatingReferenceDecomposition_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/RotatingReferenceDecomposition.mp4)**

---

## ScalingVectorDecomposition
**Decomposition with vector magnitude changes**

```python
from robo_manim_add_ons.vector_utils import VectorUtils

# Fixed reference vector
vector_b = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE)

# Vector that will scale
vector_a = Arrow(ORIGIN, RIGHT * 1 + UP * 1, buff=0, color=RED)

# Create dynamic decomposition
parallel = always_redraw(
    lambda: VectorUtils.decompose_parallel(vector_a, vector_b, color=GREEN)
)

perp = always_redraw(
    lambda: VectorUtils.decompose_perp(vector_a, vector_b, color=ORANGE)
)

# Scale up - decomposition components scale proportionally
self.play(
    vector_a.animate.put_start_and_end_on(ORIGIN, RIGHT * 2.5 + UP * 2.5),
    run_time=3
)
```

![ScalingVectorDecomposition](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/ScalingVectorDecomposition_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/ScalingVectorDecomposition.mp4)**

---

## InclinedPlaneForceDecomposition
**Practical example: Force decomposition on inclined plane**

```python
from robo_manim_add_ons.vector_utils import VectorUtils

# Create inclined plane (line)
angle = PI/6  # 30 degrees
plane = Line(LEFT * 3, RIGHT * 3, color=GRAY).rotate(angle, about_point=ORIGIN)

# Gravity force vector (pointing down)
gravity = Arrow(ORIGIN, DOWN * 2, buff=0, color=RED)

# Create slope direction (parallel to plane)
slope_direction = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE).rotate(angle, about_point=ORIGIN)

# Decompose gravity into parallel (down slope) and perpendicular (into plane)
parallel_force = VectorUtils.decompose_parallel(gravity, slope_direction, color=GREEN)
perp_force = VectorUtils.decompose_perp(gravity, slope_direction, color=ORANGE)

self.play(GrowArrow(parallel_force))
self.play(GrowArrow(perp_force))
```

![InclinedPlaneForceDecomposition](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/InclinedPlaneForceDecomposition_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/InclinedPlaneForceDecomposition.mp4)**

---

## MultipleDecompositions
**Multiple simultaneous decompositions with updaters**

```python
from robo_manim_add_ons.vector_utils import VectorUtils

# Central reference vector
ref_vector = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE)

# Multiple vectors at different angles
angles = [PI/6, PI/3, PI/2, 2*PI/3, 5*PI/6]
vectors = VGroup()

for angle in angles:
    vec = Arrow(ORIGIN, RIGHT * 2, buff=0, color=RED).rotate(angle, about_point=ORIGIN)
    vectors.add(vec)

    # Create decomposition components
    parallel = always_redraw(
        lambda v=vec: VectorUtils.decompose_parallel(v, ref_vector, color=GREEN)
    )

    perp = always_redraw(
        lambda v=vec: VectorUtils.decompose_perp(v, ref_vector, color=ORANGE)
    )

# Rotate reference vector - all decompositions update
self.play(Rotate(ref_vector, angle=PI/3, about_point=ORIGIN), run_time=4)
```

![MultipleDecompositions](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/MultipleDecompositions_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/MultipleDecompositions.mp4)**

---

## OppositeDirectionDecomposition
**Decomposition when vectors point in opposite directions**

```python
from robo_manim_add_ons.vector_utils import VectorUtils

# Reference vector (pointing right)
vector_b = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE)

# Vector pointing opposite direction (starts pointing left)
vector_a = Arrow(ORIGIN, LEFT * 2 + UP * 0.5, buff=0, color=RED)

# Create dynamic decomposition
parallel = always_redraw(
    lambda: VectorUtils.decompose_parallel(vector_a, vector_b, color=GREEN)
)

perp = always_redraw(
    lambda: VectorUtils.decompose_perp(vector_a, vector_b, color=ORANGE)
)

# Rotate vector_a to show parallel component changing sign
self.play(Rotate(vector_a, angle=PI, about_point=ORIGIN), run_time=4)
```

![OppositeDirectionDecomposition](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/OppositeDirectionDecomposition_ManimCE_v0.19.0.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/OppositeDirectionDecomposition.mp4)**

---

## DotProductProjectionDemo
**Vector projection with step-by-step visualization**

```python
from robo_manim_add_ons.vector_utils import VectorUtils

vector_a = Arrow(ORIGIN, RIGHT * 3.5, buff=0, color=BLUE)
vector_b = Arrow(ORIGIN, RIGHT * 2.5 + UP * 1.5, buff=0, color=RED)

# Show angle between vectors
angle_sector = Sector(radius=0.5, angle=angle, start_angle=0, color=YELLOW, fill_opacity=0.3)
self.play(FadeIn(angle_sector))

# Show projection line
proj_line = VectorUtils.projection_line(vector_b, vector_a, color=GRAY)
proj_line_dashed = DashedLine(proj_line.get_start(), proj_line.get_end(), color=GRAY)
self.play(Create(proj_line_dashed))

# Show right angle indicator
right_angle = RightAngle(Line(proj_point, vector_a.get_end()),
                         Line(proj_point, vector_b.get_end()))
self.play(Create(right_angle))

# Show projection vector
proj_vector = VectorUtils.project_onto(vector_b, vector_a, color=GREEN)
self.play(GrowArrow(proj_vector))
```

![DotProductProjectionDemo](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/DotProductProjectionDemo.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/DotProductProjectionDemo.mp4)**

---

## ProjectionWithFormula
**Projection with mathematical formula display**

```python
from robo_manim_add_ons.vector_utils import VectorUtils

# Formula at top
formula = MathTex(r"\text{proj}_{\vec{a}} \vec{b} = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}|^2} \vec{a}")
self.play(Write(formula))

# Vectors
vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE)
vector_b = Arrow(ORIGIN, RIGHT * 2 + UP * 1.5, buff=0, color=RED)

# Show projection
proj_vector = VectorUtils.project_onto(vector_b, vector_a, color=GREEN)
proj_line = DashedLine(proj_vector.get_end(), vector_b.get_end(), color=GRAY)

self.play(GrowArrow(proj_vector))
self.play(Create(proj_line))
```

![ProjectionWithFormula](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/ProjectionWithFormula.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/ProjectionWithFormula.mp4)**

---

## DynamicProjection
**Interactive projection that updates with vector rotation**

```python
from robo_manim_add_ons.vector_utils import VectorUtils

vector_a = Arrow(ORIGIN, RIGHT * 3.5, buff=0, color=BLUE)
vector_b = Arrow(ORIGIN, RIGHT * 2 + UP * 1.5, buff=0, color=RED)

# Dynamic projection using always_redraw
proj_vector = always_redraw(
    lambda: VectorUtils.project_onto(vector_b, vector_a, color=GREEN)
)

proj_line = always_redraw(
    lambda: DashedLine(proj_vector.get_end(), vector_b.get_end(), color=GRAY)
)

right_angle = always_redraw(
    lambda: RightAngle(Line(proj_vector.get_end(), vector_a.get_end()),
                       Line(proj_vector.get_end(), vector_b.get_end()))
)

# Rotate vector b - projection updates automatically
self.play(Rotate(vector_b, angle=PI, about_point=ORIGIN), run_time=4)
```

![DynamicProjection](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/DynamicProjection.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/DynamicProjection.mp4)**

---

## ProjectionWithRegion
**Projection with shaded triangular region**

```python
from robo_manim_add_ons.vector_utils import VectorUtils

vector_a = Arrow(ORIGIN, RIGHT * 3.5, buff=0, color=BLUE)
vector_b = Arrow(ORIGIN, RIGHT * 2.5 + UP * 1.5, buff=0, color=RED)

# Show shaded region
region = VectorUtils.projection_region(vector_b, vector_a, fill_opacity=0.3, color=YELLOW)
self.play(FadeIn(region))

# Show projection vector
proj_vector = VectorUtils.project_onto(vector_b, vector_a, color=GREEN)
self.play(GrowArrow(proj_vector))

# Show perpendicular line
proj_line = DashedLine(proj_vector.get_end(), vector_b.get_end(), color=GRAY)
self.play(Create(proj_line))
```

![ProjectionWithRegion](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/ProjectionWithRegion.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/ProjectionWithRegion.mp4)**

---

## ProjectionCases
**Different projection cases: acute, right, and obtuse angles**

```python
from robo_manim_add_ons.vector_utils import VectorUtils

# Case 1: Acute angle (positive projection)
vec_a1 = Arrow(LEFT * 5, LEFT * 5 + RIGHT * 2, buff=0, color=BLUE)
vec_b1 = Arrow(LEFT * 5, LEFT * 5 + RIGHT * 1.5 + UP * 0.8, buff=0, color=RED)
proj1 = VectorUtils.project_onto(vec_b1, vec_a1, color=GREEN)
line1 = DashedLine(proj1.get_end(), vec_b1.get_end(), color=GRAY)

# Case 2: Right angle (zero projection)
vec_a2 = Arrow(LEFT * 1, LEFT * 1 + RIGHT * 2, buff=0, color=BLUE)
vec_b2 = Arrow(LEFT * 1, LEFT * 1 + UP * 1.5, buff=0, color=RED)
proj2 = VectorUtils.project_onto(vec_b2, vec_a2, color=GREEN)

# Case 3: Obtuse angle (negative projection)
vec_a3 = Arrow(RIGHT * 3, RIGHT * 3 + RIGHT * 2, buff=0, color=BLUE)
vec_b3 = Arrow(RIGHT * 3, RIGHT * 3 + LEFT * 0.8 + UP * 1.2, buff=0, color=RED)
proj3 = VectorUtils.project_onto(vec_b3, vec_a3, color=GREEN)
```

![ProjectionCases](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/ProjectionCases.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/ProjectionCases.mp4)**

---

## ProjectionDecomposition
**Decompose vector into parallel and perpendicular components**

```python
from robo_manim_add_ons.vector_utils import VectorUtils

# Title formula
title = MathTex(r"\vec{b} = \vec{b}_\parallel + \vec{b}_\perp")

vector_a = Arrow(ORIGIN, RIGHT * 3.5, buff=0, color=BLUE)
vector_b = Arrow(ORIGIN, RIGHT * 2.5 + UP * 1.8, buff=0, color=RED)

# Parallel component (projection)
parallel = VectorUtils.decompose_parallel(vector_b, vector_a, color=GREEN)
self.play(GrowArrow(parallel))

# Perpendicular component
perp = VectorUtils.decompose_perp(vector_b, vector_a, color=ORANGE)
self.play(GrowArrow(perp))

# Dashed line completing triangle
dashed = DashedLine(vector_b.get_end(), parallel.get_end(), color=GRAY)
self.play(Create(dashed))
```

![ProjectionDecomposition](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/ProjectionDecomposition.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/ProjectionDecomposition.mp4)**

---

## ProjectionScaling
**Projection magnitude changes with vector magnitude**

```python
from robo_manim_add_ons.vector_utils import VectorUtils

# Fixed target
vector_a = Arrow(ORIGIN, RIGHT * 3.5, buff=0, color=BLUE)

# Scaling vector
vector_b = Arrow(ORIGIN, RIGHT * 1 + UP * 0.8, buff=0, color=RED)

# Dynamic projection
proj = always_redraw(
    lambda: VectorUtils.project_onto(vector_b, vector_a, color=GREEN)
)

proj_line = always_redraw(
    lambda: DashedLine(proj.get_end(), vector_b.get_end(), color=GRAY)
)

# Scale up vector b - projection grows
self.play(vector_b.animate.put_start_and_end_on(ORIGIN, RIGHT * 2.5 + UP * 2), run_time=2)

# Scale down vector b - projection shrinks
self.play(vector_b.animate.put_start_and_end_on(ORIGIN, RIGHT * 0.5 + UP * 0.4), run_time=2)
```

![ProjectionScaling](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/ProjectionScaling.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/ProjectionScaling.mp4)**

---

## DotProductVisualization
**Visualize dot product as projection times magnitude**

```python
from robo_manim_add_ons.vector_utils import VectorUtils

# Formula
formula = MathTex(r"\vec{a} \cdot \vec{b} = |\vec{a}| \, |\text{proj}_{\vec{a}} \vec{b}|")

vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE)
vector_b = Arrow(ORIGIN, RIGHT * 2.2 + UP * 1.3, buff=0, color=RED)

# Show projection
proj = VectorUtils.project_onto(vector_b, vector_a, color=GREEN)
proj_line = DashedLine(proj.get_end(), vector_b.get_end(), color=GRAY)

# Highlight |a| with brace
brace_a = Brace(vector_a, direction=DOWN, color=BLUE)
label_a = brace_a.get_text(r"$|\vec{a}|$")

# Highlight projection with brace
brace_proj = Brace(proj, direction=DOWN, color=GREEN)
label_proj = brace_proj.get_text(r"$|\text{proj}|$")
```

![DotProductVisualization](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/DotProductVisualization.png)

**[▶️ Watch Video](https://github.com/provility/robo-manim-add-ons/raw/main/demos/vectors/DotProductVisualization.mp4)**
