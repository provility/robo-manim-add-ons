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
        vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE)
        vector_b = Arrow(ORIGIN, UP * 2, buff=0, color=RED)

        origin = Dot(ORIGIN, color=YELLOW)

        # Show initial vectors
        self.add(origin)
        self.play(GrowArrow(vector_a), GrowArrow(vector_b))
        self.wait(1)

        # STEP 1: Create -b at origin using VectorUtils
        reversed_b_at_origin = VectorUtils.reverse_at(
            vector_b, ORIGIN,
            color=PURPLE, tip_length=0.25
        )
        self.play(Create(reversed_b_at_origin), run_time=1.0)
        self.wait(0.5)

        # STEP 2: Move -b to tip of a using VectorUtils
        shift_vector = VectorUtils.shift_amount(vector_a, reversed_b_at_origin)
        self.play(reversed_b_at_origin.animate.shift(shift_vector), run_time=1.0)
        self.wait(0.5)

        # STEP 3: Show result vector using VectorUtils
        result_vector = VectorUtils.subtract(
            vector_a, vector_b,
            color="#047857", tip_length=0.3, stroke_width=6
        )
        self.play(GrowArrow(result_vector), run_time=1.0)
        self.wait(1)


class VectorSubtractionWithLabels(Scene):
    """Vector subtraction with text labels explaining each step"""

    def construct(self):
        # Define vectors
        vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE)
        vector_b = Arrow(ORIGIN, UP * 2, buff=0, color=RED)

        # Labels
        label_a = MathTex(r"\vec{a}", color=BLUE).next_to(vector_a, DOWN)
        label_b = MathTex(r"\vec{b}", color=RED).next_to(vector_b, LEFT)

        # Title
        title = Text("Vector Subtraction: a - b = a + (-b)", font_size=36).to_edge(UP)

        # Show initial setup
        self.play(Write(title))
        self.play(GrowArrow(vector_a), GrowArrow(vector_b))
        self.play(Write(label_a), Write(label_b))
        self.wait(1)

        # Step 1: Show -b
        step1_text = Text("Step 1: Create -b", font_size=24, color=PURPLE).to_edge(DOWN)
        self.play(Write(step1_text))

        neg_b_at_origin = VectorUtils.reverse_at(vector_b, ORIGIN, color=PURPLE)
        label_neg_b = MathTex(r"-\vec{b}", color=PURPLE).next_to(neg_b_at_origin, RIGHT)

        self.play(Create(neg_b_at_origin))
        self.play(Write(label_neg_b))
        self.wait(1)

        # Step 2: Move -b to tip of a
        step2_text = Text("Step 2: Move -b to tip of a", font_size=24, color=PURPLE).to_edge(DOWN)
        self.play(Transform(step1_text, step2_text))

        shift = VectorUtils.shift_amount(vector_a, neg_b_at_origin)
        self.play(
            neg_b_at_origin.animate.shift(shift),
            label_neg_b.animate.shift(shift)
        )
        self.wait(1)

        # Step 3: Show result
        step3_text = Text("Step 3: Result is a - b", font_size=24, color=GREEN).to_edge(DOWN)
        self.play(Transform(step1_text, step3_text))

        result = VectorUtils.subtract(vector_a, vector_b, color=GREEN, stroke_width=6)
        label_result = MathTex(r"\vec{a} - \vec{b}", color=GREEN).next_to(result, DOWN)

        self.play(GrowArrow(result))
        self.play(Write(label_result))
        self.wait(2)


class VectorAdditionDemo(Scene):
    """Comparison: Vector addition a + b"""

    def construct(self):
        # Define vectors
        vector_a = Arrow(ORIGIN, RIGHT * 2.5, buff=0, color=BLUE)
        vector_b = Arrow(ORIGIN, UP * 1.5, buff=0, color=RED)

        # Title
        title = Text("Vector Addition: a + b", font_size=36).to_edge(UP)

        # Show vectors
        self.play(Write(title))
        self.play(GrowArrow(vector_a), GrowArrow(vector_b))
        self.wait(1)

        # Move b to tip of a
        b_shifted = VectorUtils.tail_at_tip(vector_a, vector_b)
        self.play(TransformFromCopy(vector_b, b_shifted))
        self.wait(1)

        # Show result
        result = VectorUtils.add(vector_a, vector_b, color=GREEN, stroke_width=6)
        self.play(GrowArrow(result))
        self.wait(2)


class DynamicVectorSubtraction(Scene):
    """Interactive: Subtraction updates as vectors change"""

    def construct(self):
        # Moving vectors
        vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE)
        vector_b = Arrow(ORIGIN, UP * 2, buff=0, color=RED)

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
        self.play(GrowArrow(vector_a), GrowArrow(vector_b))
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


class ScalarMultiplicationDemo(Scene):
    """Bonus: Scalar multiplication using VectorUtils"""

    def construct(self):
        # Original vector
        vector_a = Arrow(ORIGIN, RIGHT * 2, buff=0, color=BLUE)

        # Show original
        self.play(GrowArrow(vector_a))
        self.wait(1)

        # Create scaled versions
        scaled_2x = VectorUtils.scalar_multiply(vector_a, 2, color=GREEN, stroke_width=5)
        scaled_half = VectorUtils.scalar_multiply(vector_a, 0.5, color=YELLOW, stroke_width=5)
        scaled_neg = VectorUtils.scalar_multiply(vector_a, -1, color=RED, stroke_width=5)

        # Show 2x
        label_2x = MathTex(r"2\vec{a}", color=GREEN).next_to(scaled_2x, DOWN)
        self.play(GrowArrow(scaled_2x), Write(label_2x))
        self.wait(1)

        # Show 0.5x
        label_half = MathTex(r"0.5\vec{a}", color=YELLOW).next_to(scaled_half, DOWN)
        self.play(GrowArrow(scaled_half), Write(label_half))
        self.wait(1)

        # Show -1x (reversal)
        label_neg = MathTex(r"-\vec{a}", color=RED).next_to(scaled_neg, DOWN)
        self.play(GrowArrow(scaled_neg), Write(label_neg))
        self.wait(2)


class ComprehensiveVectorOperations(Scene):
    """All operations in one scene"""

    def construct(self):
        # Base vectors
        a = Arrow(ORIGIN, RIGHT * 2.5, buff=0, color=BLUE)
        b = Arrow(ORIGIN, UP * 1.5, buff=0, color=RED)

        # Show base vectors
        self.play(GrowArrow(a), GrowArrow(b))
        self.wait(1)

        # Addition: a + b
        add_result = VectorUtils.add(a, b, color=GREEN, stroke_width=5)
        add_label = Text("a + b", color=GREEN, font_size=20).next_to(add_result, RIGHT)
        self.play(GrowArrow(add_result), Write(add_label))
        self.wait(1)

        # Subtraction: a - b
        sub_result = VectorUtils.subtract(a, b, color=PURPLE, stroke_width=5)
        sub_label = Text("a - b", color=PURPLE, font_size=20).next_to(sub_result, DOWN)
        self.play(GrowArrow(sub_result), Write(sub_label))
        self.wait(1)

        # Scalar: 2a
        scalar_2a = VectorUtils.scalar_multiply(a, 2, color=YELLOW, stroke_width=5)
        scalar_label = Text("2a", color=YELLOW, font_size=20).next_to(scalar_2a, DOWN)
        self.play(GrowArrow(scalar_2a), Write(scalar_label))
        self.wait(2)
