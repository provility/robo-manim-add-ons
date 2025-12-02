"""Demo of hatched_region() function for textbook-style shading."""

from manim import *
from robo_manim_add_ons import hatched_region


class DiagonalHatchDemo(Scene):
    """Diagonal hatching pattern on a rectangle."""

    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 8, 1],
            x_length=6,
            y_length=5,
            axis_config={"include_tip": False}
        )

        # Define rectangle vertices
        vertices = [(2, 2), (8, 2), (8, 6), (2, 6)]

        # Create hatched region with diagonal lines
        hatched, boundary = hatched_region(
            axes, vertices,
            spacing=0.2,
            direction="/",
            color=BLUE,
            stroke_width=1.5
        )

        title = Text("Diagonal Hatching (/)", font_size=32).to_edge(UP)

        # Animate
        self.add(axes, title)
        self.play(Create(boundary))
        self.wait(0.5)
        self.play(Create(hatched))
        self.wait(2)


class TriangleHatchDemo(Scene):
    """Different hatch patterns on a triangle."""

    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 8, 1],
            x_length=6,
            y_length=5,
            axis_config={"include_tip": False}
        )

        # Define triangle vertices
        vertices = [(2, 2), (8, 2), (5, 6)]

        # Create hatched region with backslash pattern
        hatched, boundary = hatched_region(
            axes, vertices,
            spacing=0.25,
            direction="\\",
            color=RED,
            stroke_width=1.5
        )

        title = Text("Backslash Hatching (\\)", font_size=32).to_edge(UP)

        # Animate
        self.add(axes, title)
        self.play(Create(boundary))
        self.wait(0.5)
        self.play(Create(hatched))
        self.wait(2)
