"""
Vector Addition Demo - Vector addition using tip-to-tail with resultant
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils

# Use unfilled arrow tips for textbook-style vectors
Arrow.set_default(tip_shape=ArrowTriangleTip)


class VectorAdditionDemo(Scene):
    """Example: Vector addition using tip-to-tail with resultant"""

    def construct(self):
        vector_a = Arrow(ORIGIN, RIGHT * 2.5, color=BLUE, buff=0)
        self.play(GrowArrow(vector_a))
        self.wait(0.5)

        vector_b = Arrow(ORIGIN, UP * 2, color=RED, buff=0)
        self.play(GrowArrow(vector_b))
        self.wait(0.5)

        vector_b_at_tip = VectorUtils.tail_at_tip(vector_a, vector_b).set_color(RED)
        self.play(
            FadeOut(vector_b),
            GrowArrow(vector_b_at_tip),
            run_time=1.5
        )
        self.wait()

        resultant = Arrow(ORIGIN, vector_b_at_tip.get_end(), color=GREEN, buff=0)
        resultant.set_stroke(width=6)
        self.play(GrowArrow(resultant), run_time=1.5)
        self.wait(2)
