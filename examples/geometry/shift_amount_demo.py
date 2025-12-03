"""
Shift Amount Demo - Use shift_amount to animate a vector to position
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils


class ShiftAmountDemo(Scene):
    """Basic example: Use shift_amount to animate a vector to position"""

    def construct(self):
        vector_a = Arrow(ORIGIN, RIGHT * 2.5, color=BLUE, buff=0)
        self.play(GrowArrow(vector_a))
        self.wait()

        vector_b = Arrow(LEFT * 2 + DOWN, LEFT * 2 + UP * 1.5, color=RED, buff=0)
        self.play(GrowArrow(vector_b))
        self.wait()

        shift_vector = VectorUtils.shift_amount(vector_a, vector_b)
        self.play(vector_b.animate.shift(shift_vector), run_time=2)
        self.wait(2)
