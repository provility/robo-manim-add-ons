"""
Demo: VectorUtils.reverse_at() - Vector Reversal at Specific Points

Shows how to create reversed copies of vectors at specific locations,
particularly useful for vector subtraction visualization (a - b = a + (-b)).
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils


class ReverseAtDemo(Scene):
    def construct(self):
        # Original vectors
        vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE, stroke_width=5)
        vector_b = Arrow(ORIGIN, UP * 2, buff=0, color=RED, stroke_width=5)

        # Labels
        label_a = MathTex("\\vec{a}", color=BLUE).next_to(vector_a, DOWN)
        label_b = MathTex("\\vec{b}", color=RED).next_to(vector_b, LEFT)

        # Show original vectors
        self.play(GrowArrow(vector_a), Write(label_a))
        self.play(GrowArrow(vector_b), Write(label_b))
        self.wait(1)

        # Vector subtraction: a - b = a + (-b)
        title = Text("Vector Subtraction: a - b", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Step 1: Create -b at origin using reverse_at()
        neg_b_at_origin = VectorUtils.reverse_at(vector_b, ORIGIN, color=PURPLE, stroke_width=5)
        label_neg_b = MathTex("-\\vec{b}", color=PURPLE).next_to(neg_b_at_origin, RIGHT)

        self.play(
            Create(neg_b_at_origin),
            Write(label_neg_b)
        )
        self.wait(1)

        # Step 2: Move -b to tip of a using reverse_at()
        neg_b_at_tip = VectorUtils.reverse_at(vector_b, vector_a.get_end(), color=PURPLE, stroke_width=5)
        label_neg_b_moved = MathTex("-\\vec{b}", color=PURPLE).next_to(neg_b_at_tip, RIGHT)

        self.play(
            Transform(neg_b_at_origin, neg_b_at_tip),
            Transform(label_neg_b, label_neg_b_moved)
        )
        self.wait(1)

        # Step 3: Show result vector (a - b)
        result_vector = Arrow(
            ORIGIN,
            vector_a.get_end() - (vector_b.get_end() - vector_b.get_start()),
            buff=0,
            color=GREEN,
            stroke_width=6,
            tip_length=0.3
        )
        label_result = MathTex("\\vec{a} - \\vec{b}", color=GREEN).next_to(result_vector, DOWN, buff=0.3)

        self.play(
            GrowArrow(result_vector),
            Write(label_result)
        )
        self.wait(2)

        # Highlight the result
        self.play(
            result_vector.animate.set_stroke(width=8),
            label_result.animate.scale(1.2)
        )
        self.wait(1)
