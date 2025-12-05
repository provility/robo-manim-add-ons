"""
Backward Vector Demo - Copy and shift a vector backward
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils



class BackwardVectorDemo(Scene):
    """Basic example: Copy and shift a vector backward"""

    def construct(self):
        source = VectorUtils.create_vector(LEFT * 2, RIGHT * 2, color=BLUE)
        self.play(Create(source))
        self.wait()

        distance = 1.5
        shifted = VectorUtils.backward(source, distance).set_color(RED)

        self.play(TransformFromCopy(source, shifted), run_time=2)
        self.wait(2)
