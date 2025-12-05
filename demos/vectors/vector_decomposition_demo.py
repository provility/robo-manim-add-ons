"""
Demo: Vector Decomposition using VectorUtils

Shows decompose_parallel() and decompose_perp() methods.
Demonstrates splitting a vector into components parallel and perpendicular to a reference.
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils



class BasicDecompositionDemo(Scene):
    """Basic decomposition: split vector into parallel and perpendicular components"""

    def construct(self):
        # Reference vector (horizontal)
        vector_b = VectorUtils.create_vector(ORIGIN, RIGHT * 3, color=BLUE)

        # Vector to decompose
        vector_a = VectorUtils.create_vector(ORIGIN, RIGHT * 2 + UP * 1.5, color=RED)

        # Show vectors
        self.play(Create(vector_b), Create(vector_a))
        self.wait(1)

        # Create and show parallel component
        parallel = VectorUtils.decompose_parallel(vector_a, vector_b, color=GREEN)
        self.play(Create(parallel))
        self.wait(0.5)

        # Create and show perpendicular component
        perp = VectorUtils.decompose_perp(vector_a, vector_b, color=ORANGE)
        self.play(Create(perp))
        self.wait(0.5)

        # Add dashed line to complete triangle
        dashed = DashedLine(vector_a.get_end(), parallel.get_end(), color=GRAY)
        self.play(Create(dashed))
        self.wait(2)


class RotatingVectorDecomposition(Scene):
    """Dynamic decomposition that updates as vector rotates"""

    def construct(self):
        # Fixed reference vector
        vector_b = VectorUtils.create_vector(ORIGIN, RIGHT * 3, color=BLUE)

        # Rotating vector
        vector_a = VectorUtils.create_vector(ORIGIN, RIGHT * 2 + UP * 1, color=RED)

        # Dynamic decomposition with always_redraw
        parallel = always_redraw(
            lambda: VectorUtils.decompose_parallel(vector_a, vector_b, color=GREEN)
        )

        perp = always_redraw(
            lambda: VectorUtils.decompose_perp(vector_a, vector_b, color=ORANGE)
        )

        dashed = always_redraw(
            lambda: DashedLine(vector_a.get_end(), parallel.get_end(), color=GRAY, dash_length=0.1)
        )

        # Show initial state
        self.play(Create(vector_b), Create(vector_a))
        self.add(parallel, perp, dashed)
        self.wait(1)

        # Rotate vector - decomposition updates
        self.play(
            Rotate(vector_a, angle=PI, about_point=ORIGIN),
            run_time=4,
            rate_func=linear
        )
        self.wait(1)
