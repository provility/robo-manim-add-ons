"""
Demo of geometry utilities: perp and parallel functions.
"""

from manim import *
from robo_manim_add_ons import perp, parallel


class PerpDemo(Scene):
    """Demonstrate the perp function."""

    def construct(self):
        ref_line = Line(LEFT * 3, RIGHT * 3, color=BLUE)
        dot = Dot(ORIGIN, color=RED)
        perp_line = perp(ref_line, dot, length=4.0, placement="mid").set_color(GREEN)

        self.play(Create(ref_line))
        self.play(Create(dot))
        self.play(Create(perp_line))
        self.wait(2)


class ParallelDemo(Scene):
    """Demonstrate the parallel function."""

    def construct(self):
        ref_line = Line(LEFT + DOWN, RIGHT + UP, color=BLUE)
        dot = Dot(UP * 2, color=RED)
        parallel_line = parallel(ref_line, dot, length=3.0, placement="mid").set_color(YELLOW)

        self.play(Create(ref_line))
        self.play(Create(dot))
        self.play(Create(parallel_line))
        self.wait(2)


class PlacementDemo(Scene):
    """Demonstrate different placement options."""

    def construct(self):
        ref_line = Line(LEFT * 4, RIGHT * 4, color=BLUE)

        dot_mid = Dot(ORIGIN, color=RED)
        dot_start = Dot(UP * 2, color=GREEN)
        dot_end = Dot(DOWN * 2, color=YELLOW)

        perp_mid = perp(ref_line, dot_mid, 2.0, placement="mid").set_color(RED)
        perp_start = perp(ref_line, dot_start, 2.0, placement="start").set_color(GREEN)
        perp_end = perp(ref_line, dot_end, 2.0, placement="end").set_color(YELLOW)

        self.play(Create(ref_line))
        self.wait(0.5)

        self.play(Create(dot_mid))
        self.play(Create(perp_mid))
        self.wait(1)

        self.play(Create(dot_start))
        self.play(Create(perp_start))
        self.wait(1)

        self.play(Create(dot_end))
        self.play(Create(perp_end))
        self.wait(2)


class GeometryComboDemo(Scene):
    """Demonstrate both perp and parallel together."""

    def construct(self):
        ref_line = Line(LEFT * 2 + DOWN, RIGHT * 2 + UP, color=BLUE)
        dot = Dot(ORIGIN, color=RED)
        perp_line = perp(ref_line, dot, 3.0, placement="mid").set_color(GREEN)

        dot2 = Dot(UP * 2 + LEFT, color=ORANGE)
        parallel_line = parallel(ref_line, dot2, 2.5, placement="mid").set_color(YELLOW)

        self.play(Create(ref_line))
        self.wait(0.5)

        self.play(Create(dot))
        self.play(Create(perp_line))
        self.wait(1)

        self.play(Create(dot2))
        self.play(Create(parallel_line))
        self.wait(2)
