"""
Shift Amount Vector Addition Demo - Vector addition using shift_amount for animation
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils


class ShiftAmountVectorAddition(Scene):
    """Example: Vector addition using shift_amount for animation"""

    def construct(self):
        vector_a = Arrow(ORIGIN, RIGHT * 2, color=BLUE, buff=0)
        self.play(GrowArrow(vector_a))
        self.wait(0.5)

        vector_b = Arrow(DOWN * 2, DOWN * 2 + UP * 1.5, color=RED, buff=0)
        self.play(GrowArrow(vector_b))
        self.wait()

        shift_vector = VectorUtils.shift_amount(vector_a, vector_b)
        self.play(vector_b.animate.shift(shift_vector), run_time=2)
        self.wait()

        resultant = Arrow(ORIGIN, vector_b.get_end(), color=GREEN, buff=0)
        resultant.set_stroke(width=6)
        self.play(GrowArrow(resultant), run_time=1.5)
        self.wait(2)
