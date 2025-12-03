"""
Dynamic Vector Addition Demo - Dynamic vector addition with rotating base
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils



class DynamicVectorAddition(Scene):
    """Example: Dynamic vector addition with rotating base"""

    def construct(self):
        vector_a = Arrow(ORIGIN, RIGHT * 2, color=BLUE, buff=0, fill_opacity=0)
        vector_b_template = Arrow(ORIGIN, UP * 1.5, color=RED, buff=0, fill_opacity=0)

        vector_b_at_tip = always_redraw(
            lambda: VectorUtils.tail_at_tip(vector_a, vector_b_template).set_color(ORANGE)
        )

        resultant = always_redraw(
            lambda: Arrow(ORIGIN, vector_b_at_tip.get_end(), color=GREEN, buff=0).set_stroke(width=5)
        )

        self.play(GrowArrow(vector_a))
        self.play(Create(vector_b_at_tip))
        self.play(Create(resultant))
        self.wait()

        self.play(
            Rotate(vector_a, angle=2*PI, about_point=ORIGIN),
            run_time=8,
            rate_func=linear
        )
        self.wait(2)
