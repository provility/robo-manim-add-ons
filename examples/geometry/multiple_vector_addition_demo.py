"""
Multiple Vector Addition Demo - Adding multiple vectors using tail_at_tip
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils


class MultipleVectorAddition(Scene):
    """Example: Adding multiple vectors using tail_at_tip"""

    def construct(self):
        vectors = [
            Arrow(ORIGIN, RIGHT * 1.5, color=BLUE, buff=0),
            Arrow(ORIGIN, UP * 1.2, color=RED, buff=0),
            Arrow(ORIGIN, LEFT * 0.8, color=YELLOW, buff=0),
            Arrow(ORIGIN, UP * 0.8, color=PURPLE, buff=0),
        ]

        current = vectors[0]
        self.play(GrowArrow(current))
        self.wait(0.5)

        for i in range(1, len(vectors)):
            next_vector = VectorUtils.tail_at_tip(current, vectors[i])
            self.play(GrowArrow(next_vector), run_time=1)
            self.wait(0.3)
            current = next_vector

        self.wait()

        resultant = Arrow(ORIGIN, current.get_end(), color=GREEN, buff=0)
        resultant.set_stroke(width=6)
        self.play(GrowArrow(resultant), run_time=1.5)
        self.wait(2)
