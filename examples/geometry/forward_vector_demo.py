"""
Forward Vector Demo - Copy and shift a vector forward
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils



class ForwardVectorDemo(Scene):
    """Basic example: Copy and shift a vector forward"""

    def construct(self):
        source = Arrow(LEFT * 2, RIGHT * 2, color=BLUE, buff=0, fill_opacity=0)
        self.play(GrowArrow(source))
        self.wait()

        distance = 1.5
        shifted = VectorUtils.forward(source, distance).set_color(GREEN)

        self.play(TransformFromCopy(source, shifted), run_time=2)
        self.wait(2)
