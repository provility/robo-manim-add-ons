"""
Demo: Vector Addition using Parallelogram Law

Shows the parallelogram method for vector addition.
Alternative to tip-to-tail method.
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils



class ParallelogramLawDemo(Scene):
    """Basic parallelogram law: a + b using parallelogram construction"""

    def construct(self):
        # Two vectors from origin
        vector_a = VectorUtils.create_vector(ORIGIN, RIGHT * 2.5, color=BLUE)
        vector_b = VectorUtils.create_vector(ORIGIN, UP * 2, color=RED)

        # Show vectors
        self.play(Create(vector_a), Create(vector_b))
        self.wait(1)

        # Complete the parallelogram
        copy_b_at_a = VectorUtils.copy_at(vector_b, vector_a.get_end(), color=RED, stroke_opacity=0.5)
        copy_a_at_b = VectorUtils.copy_at(vector_a, vector_b.get_end(), color=BLUE, stroke_opacity=0.5)

        self.play(Create(copy_b_at_a), Create(copy_a_at_b))
        self.wait(1)

        # Show resultant (diagonal)
        resultant = VectorUtils.create_vector(ORIGIN, copy_b_at_a.get_end(), color=GREEN)
        resultant.set_stroke(width=6)

        self.play(Create(resultant))
        self.wait(2)


class DynamicParallelogram(Scene):
    """Interactive parallelogram that updates as vectors change"""

    def construct(self):
        # Base vectors
        vector_a = VectorUtils.create_vector(ORIGIN, RIGHT * 2.5, color=BLUE)
        vector_b = VectorUtils.create_vector(ORIGIN, UP * 2, color=RED)

        # Dynamic parallelogram sides
        copy_b = always_redraw(
            lambda: VectorUtils.copy_at(vector_b, vector_a.get_end(), color=RED, stroke_opacity=0.5)
        )

        copy_a = always_redraw(
            lambda: VectorUtils.copy_at(vector_a, vector_b.get_end(), color=BLUE, stroke_opacity=0.5)
        )

        # Dynamic resultant
        resultant = always_redraw(
            lambda: VectorUtils.create_vector(
                ORIGIN,
                vector_a.get_end() + (vector_b.get_end() - vector_b.get_start()),
                color=GREEN, stroke_width=6
            )
        )

        # Show initial state
        self.play(Create(vector_a), Create(vector_b))
        self.add(copy_b, copy_a, resultant)
        self.wait(1)

        # Rotate vector b - parallelogram updates
        self.play(
            Rotate(vector_b, angle=PI/2, about_point=ORIGIN),
            run_time=3
        )
        self.wait(1)

        # Scale vector a
        self.play(
            vector_a.animate.put_start_and_end_on(ORIGIN, RIGHT * 1.5),
            run_time=2
        )
        self.wait(1)
