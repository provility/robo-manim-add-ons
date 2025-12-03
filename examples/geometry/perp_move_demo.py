"""
Perpendicular Move Demo - Copy and shift a vector perpendicular
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils


class PerpMoveDemo(Scene):
    """Basic example: Copy and shift a vector perpendicular"""

    def construct(self):
        source = Arrow(LEFT * 2, RIGHT * 2, color=BLUE, buff=0)
        self.play(GrowArrow(source))
        self.wait()

        distance = 1.5
        shifted = VectorUtils.perp_move(source, distance).set_color(PURPLE)

        self.play(TransformFromCopy(source, shifted), run_time=2)
        self.wait(2)
