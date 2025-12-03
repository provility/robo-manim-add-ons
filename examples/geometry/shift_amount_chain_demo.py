"""
Shift Amount Chain Demo - Chain multiple vectors using shift_amount animations
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils


class ShiftAmountChain(Scene):
    """Example: Chain multiple vectors using shift_amount animations"""

    def construct(self):
        vectors = [
            Arrow(ORIGIN, RIGHT * 1.5, color=BLUE, buff=0),
            Arrow(DOWN * 2, DOWN * 2 + UP * 1.2, color=RED, buff=0),
            Arrow(LEFT * 3, LEFT * 3 + RIGHT * 0.8 + UP * 0.5, color=YELLOW, buff=0),
            Arrow(UP * 2, UP * 2 + RIGHT * 1.0, color=PURPLE, buff=0),
        ]

        current = vectors[0]
        self.play(GrowArrow(current))
        self.wait(0.5)

        for i in range(1, len(vectors)):
            self.play(GrowArrow(vectors[i]), run_time=0.8)

        self.wait()

        for i in range(1, len(vectors)):
            shift_vector = VectorUtils.shift_amount(current, vectors[i])
            self.play(vectors[i].animate.shift(shift_vector), run_time=1.5)
            self.wait(0.3)
            current = vectors[i]

        self.wait()

        resultant = Arrow(vectors[0].get_start(), current.get_end(), color=GREEN, buff=0)
        resultant.set_stroke(width=6)
        self.play(GrowArrow(resultant), run_time=1.5)
        self.wait(2)
