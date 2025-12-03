"""
Combined Vector Operations Demo - Combining tail_at_tip and shift_amount
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils


class CombinedVectorOperations(Scene):
    """Example: Combining tail_at_tip and shift_amount"""

    def construct(self):
        # Vector A
        vector_a = Arrow(ORIGIN, RIGHT * 2, color=BLUE, buff=0)
        self.play(GrowArrow(vector_a))
        self.wait(0.5)

        # Vector B at origin
        vector_b = Arrow(ORIGIN, UP * 1.5, color=RED, buff=0)
        self.play(GrowArrow(vector_b))
        self.wait(0.5)

        # Use shift_amount to animate B to A's tip
        shift_vector = VectorUtils.shift_amount(vector_a, vector_b)
        self.play(vector_b.animate.shift(shift_vector), run_time=1.5)
        self.wait()

        # Resultant
        resultant = Arrow(ORIGIN, vector_b.get_end(), color=GREEN, buff=0)
        resultant.set_stroke(width=6)
        self.play(GrowArrow(resultant), run_time=1.5)
        self.wait(2)
