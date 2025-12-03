"""
Demo of geometry utilities: perp and parallel functions.
"""

from manim import *
from robo_manim_add_ons import perp, parallel


class PerpDemo(Scene):
    """Demonstrate the perp function with different placements."""

    def construct(self):
        ref_line = Line(LEFT * 3, RIGHT * 3, color=BLUE)

        # Mid placement
        dot_mid = Dot(ORIGIN, color=RED)
        perp_mid = perp(ref_line, dot_mid, length=2.0, placement="mid").set_color(RED)

        # Start placement
        dot_start = Dot(UP * 1.5, color=GREEN)
        perp_start = perp(ref_line, dot_start, length=2.0, placement="start").set_color(GREEN)

        # End placement
        dot_end = Dot(DOWN * 1.5, color=YELLOW)
        perp_end = perp(ref_line, dot_end, length=2.0, placement="end").set_color(YELLOW)

        self.play(Create(ref_line))
        self.wait(0.5)

        self.play(Create(dot_mid), Create(perp_mid))
        self.wait(0.5)

        self.play(Create(dot_start), Create(perp_start))
        self.wait(0.5)

        self.play(Create(dot_end), Create(perp_end))
        self.wait(1)


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
