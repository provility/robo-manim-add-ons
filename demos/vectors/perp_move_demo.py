"""
Demo: Perpendicular Move

Shows how to shift a vector perpendicular to its direction.
Demonstrates the perp_move method from VectorUtils.
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils


class PerpMoveDemo(Scene):
    """Basic perpendicular move: shift vector 90° to its direction"""

    def construct(self):
        # Define vector
        vector_a = VectorUtils.create_vector(ORIGIN, RIGHT * 3, color=BLUE)

        origin = Dot(ORIGIN, color=YELLOW)

        # Show initial vector
        self.add(origin)
        self.play(Create(vector_a))
        self.wait(1)

        # Create perpendicular shifted vector using VectorUtils
        shifted_vector = VectorUtils.perp_move(vector_a, 1)
        shifted_vector.set_color("#b91c1c")

        # KEY ANIMATION: Transform from original to shifted
        self.play(TransformFromCopy(vector_a, shifted_vector), run_time=1.5)
        self.wait(1)
