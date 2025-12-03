"""
Four Directions Demo - Show all four directions: forward, backward, perp+, perp-
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils


class FourDirectionsDemo(Scene):
    """Example: Show all four directions - forward, backward, perp+, perp-"""

    def construct(self):
        source = Arrow(LEFT * 0.5, RIGHT * 0.5, color=YELLOW, buff=0)
        self.play(GrowArrow(source))
        self.wait()

        distance = 1.5

        forward = VectorUtils.forward(source, distance).set_color(GREEN)
        backward = VectorUtils.backward(source, distance).set_color(ORANGE)
        perp_up = VectorUtils.perp_move(source, distance).set_color(BLUE)
        perp_down = VectorUtils.perp_move(source, -distance).set_color(RED)

        self.play(TransformFromCopy(source, forward), run_time=1)
        self.wait(0.3)
        self.play(TransformFromCopy(source, backward), run_time=1)
        self.wait(0.3)
        self.play(TransformFromCopy(source, perp_up), run_time=1)
        self.wait(0.3)
        self.play(TransformFromCopy(source, perp_down), run_time=1)
        self.wait(2)
