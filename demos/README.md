# Demo Outputs

This folder contains rendered screenshots (PNG) from all example demonstrations.

## Structure

- **geometry/** - Geometry utility demos (perp, parallel, project, reflect)
- **annotation/** - Distance marker annotation demos
- **labels/** - Vertex and edge label demos
- **intersection/** - Line and circle intersection demos

## Viewing

All images are last-frame screenshots generated with `manim -s` command.

To regenerate these demos:
```bash
manim -s -ql examples/geometry/geometry_demo.py -a
manim -s -ql examples/geometry/dynamic_geometry_demo.py -a
manim -s -ql examples/annotation/annotation_demo.py -a
manim -s -ql examples/labels/dynamic_labels_demo.py -a
manim -s -ql examples/intersection/intersection_demo.py -a
```
