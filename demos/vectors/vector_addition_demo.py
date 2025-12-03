"""
Demo: Vector Addition using Tip-to-Tail Method

Shows vector addition a + b using VectorUtils methods.
Demonstrates copy_at, shift_amount, and add methods.
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils


class VectorAdditionDemo(Scene):
    """Basic vector addition: a + b using tip-to-tail method"""

    def construct(self):
        # Define vectors
        vector_a = VectorUtils.create_vector(ORIGIN, RIGHT * 3, color=BLUE)
        vector_b = VectorUtils.create_vector(ORIGIN, UP * 2, color=RED)

        origin = Dot(ORIGIN, color=YELLOW)

        # Show initial vectors
        self.add(origin)
        self.play(Create(vector_a), Create(vector_b))
        self.wait(1)

        # STEP 1: Create vector B at its original position
        vector_b_at_origin = VectorUtils.copy_at(
            vector_b, vector_b.get_start(),
            color="#c2410c", tip_length=0.25
        )
        self.play(Create(vector_b_at_origin), run_time=1.0)
        self.wait(0.3)

        # STEP 2: Move vector B to tip of A
        # Calculate the shift needed (tail of B should be at tip of A)
        shift_vector = VectorUtils.shift_amount(vector_a, vector_b_at_origin)
        self.play(vector_b_at_origin.animate.shift(shift_vector), run_time=1.0)
        self.wait(0.5)

        # STEP 3: Create the result vector
        result_vector = VectorUtils.add(
            vector_a, vector_b,
            color="#047857", tip_length=0.3, stroke_width=6
        )
        self.play(GrowArrow(result_vector), run_time=1.0)
        self.wait(1)


class DynamicVectorAddition(Scene):
    """Interactive: Addition updates as vectors change"""

    def construct(self):
        # Moving vectors
        vector_a = VectorUtils.create_vector(ORIGIN, RIGHT * 3, color=BLUE)
        vector_b = VectorUtils.create_vector(ORIGIN, UP * 2, color=RED)

        # Dynamic b at tip of a
        b_at_tip = always_redraw(
            lambda: VectorUtils.copy_at(
                vector_b, vector_a.get_end(),
                color="#c2410c", stroke_width=4
            )
        )

        # Dynamic result
        result = always_redraw(
            lambda: VectorUtils.add(
                vector_a, vector_b,
                color=GREEN, stroke_width=6
            )
        )

        # Dynamic dashed line from origin to tip of a
        dashed = always_redraw(
            lambda: DashedLine(
                vector_b.get_end(),
                vector_a.get_end() + (vector_b.get_end() - vector_b.get_start()),
                color=GRAY, dash_length=0.1
            )
        )

        # Show initial state
        self.play(Create(vector_a), Create(vector_b))
        self.add(b_at_tip, dashed, result)
        self.wait(1)

        # Rotate vector b - addition updates
        self.play(
            Rotate(vector_b, angle=PI, about_point=ORIGIN),
            run_time=4,
            rate_func=smooth
        )
        self.wait(1)

        # Scale vector a - addition updates
        scaled_vector_a = VectorUtils.scalar_multiply(vector_a, 0.5, color=BLUE)
        self.play(
            Transform(vector_a, scaled_vector_a),
            run_time=2
        )
        self.wait(1)
