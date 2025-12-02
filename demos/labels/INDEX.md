# Label Utilities

Demonstrations of `vertex_labels()` and `edge_labels()` functions.

---

## DynamicVertexLabelsExample
**Vertex labels following transforming triangle**

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/labels/DynamicVertexLabelsExample.mp4" controls width="100%"></video>

```python
from robo_manim_add_ons import vertex_labels

triangle = Polygon([-2, -1, 0], [2, -1, 0], [0, 2, 0], color=BLUE)

# Labels update automatically as polygon transforms
labels = always_redraw(
    lambda: VGroup(*vertex_labels(
        triangle,
        labels=["A", "B", "C"],
        scale=0.8,
        color=WHITE,
        buff=0.3  # Distance from vertex to label
    ))
)

self.play(triangle.animate.scale(1.5))  # Labels follow!
self.play(Rotate(triangle, angle=PI/3))  # Labels follow!
```

---

## DynamicEdgeLabelsExample
**Edge labels on transforming square**

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/labels/DynamicEdgeLabelsExample.mp4" controls width="100%"></video>

```python
from robo_manim_add_ons import edge_labels

square = Square(side_length=3, color=GREEN)

# Labels update automatically and stay perpendicular to edges
labels = always_redraw(
    lambda: VGroup(*edge_labels(
        square,
        labels=["a", "b", "c", "d"],
        scale=0.7,
        color=YELLOW,
        buff=0.25
    ))
)

self.play(Rotate(square, angle=PI/4))      # Labels rotate!
self.play(square.animate.stretch(1.5, dim=0))  # Labels adapt!
```

---

## DynamicVertexAndEdgeLabels
**Both vertex and edge labels together**

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/labels/DynamicVertexAndEdgeLabels.mp4" controls width="100%"></video>

```python
pentagon = RegularPolygon(n=5, color=PURPLE).scale(2)

# Vertex labels
vertex_label_objects = always_redraw(
    lambda: VGroup(*vertex_labels(
        pentagon,
        labels=["V_1", "V_2", "V_3", "V_4", "V_5"],
        scale=0.6,
        buff=0.35
    ))
)

# Edge labels
edge_label_objects = always_redraw(
    lambda: VGroup(*edge_labels(
        pentagon,
        labels=["e_1", "e_2", "e_3", "e_4", "e_5"],
        scale=0.5,
        color=YELLOW,
        buff=0.2
    ))
)
```

---

## MorphingPolygonLabels
**Labels adapt to morphing polygons**

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/labels/MorphingPolygonLabels.mp4" controls width="100%"></video>

```python
triangle = Polygon([-2, -1.5, 0], [2, -1.5, 0], [0, 2, 0], color=BLUE)
square = Square(side_length=3, color=GREEN)

# Labels adapt as number of vertices changes
vertex_labels_obj = always_redraw(
    lambda: VGroup(*vertex_labels(
        triangle,
        # Slice labels to match current vertex count
        labels=["A", "B", "C", "D"][:len(triangle.get_vertices())],
        scale=0.7
    ))
)

# Triangle morphs to square - labels adjust automatically!
self.play(Transform(triangle, square))
```

---

## InteractivePolygonWithUpdater
**Real-time edge length calculation**

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/labels/InteractivePolygonWithUpdater.mp4" controls width="100%"></video>

```python
hexagon = RegularPolygon(n=6, color=RED).scale(2)
edge_label_group = VGroup()

def update_edge_labels(mob):
    vertices = hexagon.get_vertices()
    n = len(vertices)

    # Calculate actual edge lengths
    edge_lengths = []
    for i in range(n):
        p1 = vertices[i]
        p2 = vertices[(i + 1) % n]
        length = np.linalg.norm(p2 - p1)
        edge_lengths.append(f"{length:.1f}")

    # Update labels with calculated lengths
    mob.become(VGroup(*edge_labels(hexagon, labels=edge_lengths, scale=0.5)))

edge_label_group.add_updater(update_edge_labels)

# Edge lengths update as hexagon transforms!
self.play(hexagon.animate.scale(0.5))
self.play(hexagon.animate.stretch(1.8, dim=1))
```

---

## AnimatedLabelColors
**Color animation with ValueTracker**

<video src="https://github.com/provility/robo-manim-add-ons/raw/main/demos/labels/AnimatedLabelColors.mp4" controls width="100%"></video>

```python
triangle = Polygon([-2, -1.5, 0], [2, -1.5, 0], [0, 2, 0], color=BLUE)
vertex_label_objects = VGroup()
color_tracker = ValueTracker(0)

def update_labels_with_color(mob):
    t = color_tracker.get_value()
    label_color = interpolate_color(WHITE, RED, t)

    mob.become(VGroup(*vertex_labels(
        triangle,
        labels=["A", "B", "C"],
        color=label_color,
        scale=0.8
    )))

vertex_label_objects.add_updater(update_labels_with_color)

# Animate color while rotating
self.play(
    Rotate(triangle, angle=PI),
    color_tracker.animate.set_value(1),
    run_time=4
)
```
