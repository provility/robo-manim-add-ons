"""
Demo: Vector Subtraction using VectorUtils

Shows vector subtraction a - b = a + (-b) using VectorUtils methods.
Demonstrates reverse_at, shift_amount, and subtract methods.
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils



class VectorSubtractionDemo(Scene):
    """Basic vector subtraction: a - b = a + (-b)"""

    def construct(self):
        # Define vectors
        vector_a = VectorUtils.create_vector(ORIGIN, RIGHT * 3, color=BLUE)
        vector_b = VectorUtils.create_vector(ORIGIN, UP * 2, color=RED)

        origin = Dot(ORIGIN, color=YELLOW)

        # Show initial vectors
        self.add(origin)
        self.play(Create(vector_a), Create(vector_b))
        self.wait(1)

        # STEP 1: Reverse vector b at its original position
        reversed_b_at_origin = VectorUtils.reverse_at(
            vector_b, vector_b.get_start(),
            color=PURPLE, tip_length=0.25
        )
        self.play(Create(reversed_b_at_origin), run_time=1.0)
        self.wait(0.5)

        # STEP 2: Move reversed vector to tip of a
        # Calculate the shift needed (tail of reversed_b should be at tip of a)
        shift_vector = VectorUtils.shift_amount(vector_a, reversed_b_at_origin)
        self.play(reversed_b_at_origin.animate.shift(shift_vector), run_time=1.0)
        self.wait(0.5)

        # STEP 3: Create the result vector
        result_vector = VectorUtils.subtract(
            vector_a, vector_b,
            color="#047857", tip_length=0.3, stroke_width=6
        )
        self.play(GrowArrow(result_vector), run_time=1.0)
        self.wait(1)


class DynamicVectorSubtraction(Scene):
    """Interactive: Subtraction updates as vectors change"""

    def construct(self):
        # Moving vectors
        vector_a = VectorUtils.create_vector(ORIGIN, RIGHT * 3, color=BLUE)
        vector_b = VectorUtils.create_vector(ORIGIN, UP * 2, color=RED)

        # Dynamic -b at tip of a
        neg_b = always_redraw(
            lambda: VectorUtils.reverse_at(
                vector_b, vector_a.get_end(),
                color=PURPLE, stroke_width=4
            )
        )

        # Dynamic result
        result = always_redraw(
            lambda: VectorUtils.subtract(
                vector_a, vector_b,
                color=GREEN, stroke_width=6
            )
        )

        # Dynamic dashed line
        dashed = always_redraw(
            lambda: DashedLine(
                vector_a.get_end() - (vector_b.get_end() - vector_b.get_start()),
                vector_a.get_end(),
                color=GRAY, dash_length=0.1
            )
        )

        # Show initial state
        self.play(Create(vector_a), Create(vector_b))
        self.add(neg_b, dashed, result)
        self.wait(1)

        # Rotate vector b - subtraction updates
        self.play(
            Rotate(vector_b, angle=PI, about_point=ORIGIN),
            run_time=4,
            rate_func=smooth
        )
        self.wait(1)

        # Scale vector a - subtraction updates
        self.play(
            vector_a.animate.put_start_and_end_on(ORIGIN, RIGHT * 1.5),
            run_time=2
        )
        self.wait(1)
