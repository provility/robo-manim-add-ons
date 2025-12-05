from manim import *
import numpy as np

class PolyLine(VMobject):
    def __init__(self, points, color=WHITE, stroke_width=1, **kwargs):
        super().__init__(**kwargs)
        # Set the points as corners of the polyline
        self.set_points_as_corners([np.array([x, y, z]) for x, y, z in points])
        # Set color and stroke width
        self.set_color(color)
        self.set_stroke(width=stroke_width)