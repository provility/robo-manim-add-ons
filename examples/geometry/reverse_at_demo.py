"""
Demo: VectorUtils.reverse_at() - Vector Reversal at Specific Points

Shows how to create reversed copies of vectors at specific locations,
particularly useful for vector subtraction visualization (a - b = a + (-b)).
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils


class ReverseAtDemo(Scene):
    def construct(self):
        origin = Dot(ORIGIN, color=YELLOW)
        vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0, color=BLUE)
        vector_b = Arrow(ORIGIN, UP * 2, buff=0, color=RED)

        self.add(origin)
        self.play(GrowArrow(vector_a))
        self.play(GrowArrow(vector_b))
        self.wait(1)

        # Create -b at origin
        neg_b_at_origin = VectorUtils.reverse_at(vector_b, ORIGIN, color=PURPLE)
        self.play(Create(neg_b_at_origin))
        self.wait(1)

        # Move -b to tip of a
        neg_b_at_tip = VectorUtils.reverse_at(vector_b, vector_a.get_end(), color=PURPLE)
        self.play(Transform(neg_b_at_origin, neg_b_at_tip))
        self.wait(1)

        # Show result vector (a - b)
        vec_a_dir = vector_a.get_end() - vector_a.get_start()
        vec_b_dir = vector_b.get_end() - vector_b.get_start()
        result_vector = Arrow(
            ORIGIN,
            ORIGIN + vec_a_dir - vec_b_dir,
            buff=0,
            color=GREEN,
            stroke_width=6,
            tip_length=0.3
        )
        self.play(GrowArrow(result_vector))
        self.wait(2)
