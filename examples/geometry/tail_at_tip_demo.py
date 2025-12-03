"""
Tail at Tip Demo - Position vector B's tail at vector A's tip
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils


class TailAtTipDemo(Scene):
    """Basic example: Position vector B's tail at vector A's tip"""

    def construct(self):
        vector_a = Arrow(ORIGIN, RIGHT * 2, color=BLUE, buff=0)
        self.play(GrowArrow(vector_a))
        self.wait()

        vector_b = Arrow(ORIGIN, UP * 1.5, color=RED, buff=0)
        self.play(GrowArrow(vector_b))
        self.wait()

        vector_b_shifted = VectorUtils.tail_at_tip(vector_a, vector_b).set_color(ORANGE)
        self.play(TransformFromCopy(vector_b, vector_b_shifted), run_time=2)
        self.wait(2)
