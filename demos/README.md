# Demo Outputs

This folder contains rendered videos (MP4) and screenshots (PNG) from all example demonstrations.

## Browse Demos

### 🔷 [Geometry Demos](geometry/INDEX.md)
Perpendicular and parallel line construction utilities.
- 10 demonstrations with videos and screenshots

### 🔢 [Vector Demos](vectors/INDEX.md)
Vector operations including projection, decomposition, and transformations.
- 18 demonstrations with videos and screenshots

### 📏 [Annotation Demos](annotation/INDEX.md)
Distance marker and geometric annotation utilities.
- 7 demonstrations with videos and screenshots

### 🏷️ [Label Demos](labels/INDEX.md)
Vertex and edge labeling for polygons.
- 5 demonstrations with videos and screenshots

### ⚡ [Intersection Demos](intersection/INDEX.md)
Line-line and line-circle intersection utilities.
- 6 demonstrations with videos and screenshots

### 🔄 [Transform Demos](transform/)
Vector transformation utilities (translated, rotated, scaled).
- 6 demonstrations with videos and screenshots

---

## Summary

**Total: 52 demonstrations**
- 52 MP4 videos
- 52 PNG screenshots
- Organized by utility category

## Regenerating Demos

```bash
# Screenshots only
manim -s -ql examples/geometry/geometry_demo.py -a

# Videos + screenshots
manim -ql examples/geometry/geometry_demo.py -a
manim -ql examples/geometry/dynamic_geometry_demo.py -a
manim -ql examples/geometry/vector_decomposition_demo.py -a
manim -ql examples/geometry/vector_projection_demo.py -a
manim -ql examples/annotation/annotation_demo.py -a
manim -ql examples/labels/dynamic_labels_demo.py -a
manim -ql examples/intersection/intersection_demo.py -a
```
