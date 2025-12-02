"""
Vector Utils Examples - Simple demonstrations of vector operations
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils


class ForwardVectorDemo(Scene):
    """Basic example: Copy and shift a vector forward"""

    def construct(self):
        source = Arrow(LEFT * 2, RIGHT * 2, color=BLUE, buff=0)
        self.play(GrowArrow(source))
        self.wait()

        distance = 1.5
        shifted = VectorUtils.forward(source, distance).set_color(GREEN)

        self.play(TransformFromCopy(source, shifted), run_time=2)
        self.wait(2)


class BackwardVectorDemo(Scene):
    """Basic example: Copy and shift a vector backward"""

    def construct(self):
        source = Arrow(LEFT * 2, RIGHT * 2, color=BLUE, buff=0)
        self.play(GrowArrow(source))
        self.wait()

        distance = 1.5
        shifted = VectorUtils.backward(source, distance).set_color(RED)

        self.play(TransformFromCopy(source, shifted), run_time=2)
        self.wait(2)


class PerpMoveDemo(Scene):
    """Basic example: Copy and shift a vector perpendicular"""

    def construct(self):
        source = Arrow(LEFT * 2, RIGHT * 2, color=BLUE, buff=0)
        self.play(GrowArrow(source))
        self.wait()

        distance = 1.5
        shifted = VectorUtils.perpMove(source, distance).set_color(PURPLE)

        self.play(TransformFromCopy(source, shifted), run_time=2)
        self.wait(2)


class FourDirectionsDemo(Scene):
    """Example: Show all four directions - forward, backward, perp+, perp-"""

    def construct(self):
        source = Arrow(LEFT * 0.5, RIGHT * 0.5, color=YELLOW, buff=0)
        self.play(GrowArrow(source))
        self.wait()

        distance = 1.5

        forward = VectorUtils.forward(source, distance).set_color(GREEN)
        backward = VectorUtils.backward(source, distance).set_color(ORANGE)
        perp_up = VectorUtils.perpMove(source, distance).set_color(BLUE)
        perp_down = VectorUtils.perpMove(source, -distance).set_color(RED)

        self.play(TransformFromCopy(source, forward), run_time=1)
        self.wait(0.3)
        self.play(TransformFromCopy(source, backward), run_time=1)
        self.wait(0.3)
        self.play(TransformFromCopy(source, perp_up), run_time=1)
        self.wait(0.3)
        self.play(TransformFromCopy(source, perp_down), run_time=1)
        self.wait(2)


class TailAtTipDemo(Scene):
    """Basic example: Position vector B's tail at vector A's tip"""

    def construct(self):
        vector_a = Arrow(ORIGIN, RIGHT * 2, color=BLUE, buff=0)
        self.play(GrowArrow(vector_a))
        self.wait()

        vector_b = Arrow(ORIGIN, UP * 1.5, color=RED, buff=0)
        self.play(GrowArrow(vector_b))
        self.wait()

        vector_b_shifted = VectorUtils.tailAtTip(vector_a, vector_b).set_color(ORANGE)
        self.play(TransformFromCopy(vector_b, vector_b_shifted), run_time=2)
        self.wait(2)


class VectorAdditionDemo(Scene):
    """Example: Vector addition using tip-to-tail with resultant"""

    def construct(self):
        vector_a = Arrow(ORIGIN, RIGHT * 2.5, color=BLUE, buff=0)
        self.play(GrowArrow(vector_a))
        self.wait(0.5)

        vector_b = Arrow(ORIGIN, UP * 2, color=RED, buff=0)
        self.play(GrowArrow(vector_b))
        self.wait(0.5)

        vector_b_at_tip = VectorUtils.tailAtTip(vector_a, vector_b).set_color(RED)
        self.play(
            FadeOut(vector_b),
            GrowArrow(vector_b_at_tip),
            run_time=1.5
        )
        self.wait()

        resultant = Arrow(ORIGIN, vector_b_at_tip.get_end(), color=GREEN, buff=0)
        resultant.set_stroke(width=6)
        self.play(GrowArrow(resultant), run_time=1.5)
        self.wait(2)


class MultipleVectorAddition(Scene):
    """Example: Adding multiple vectors using tailAtTip"""

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
            next_vector = VectorUtils.tailAtTip(current, vectors[i])
            self.play(GrowArrow(next_vector), run_time=1)
            self.wait(0.3)
            current = next_vector

        self.wait()

        resultant = Arrow(ORIGIN, current.get_end(), color=GREEN, buff=0)
        resultant.set_stroke(width=6)
        self.play(GrowArrow(resultant), run_time=1.5)
        self.wait(2)


class ShiftAmountDemo(Scene):
    """Basic example: Use shiftAmount to animate a vector to position"""

    def construct(self):
        vector_a = Arrow(ORIGIN, RIGHT * 2.5, color=BLUE, buff=0)
        self.play(GrowArrow(vector_a))
        self.wait()

        vector_b = Arrow(LEFT * 2 + DOWN, LEFT * 2 + UP * 1.5, color=RED, buff=0)
        self.play(GrowArrow(vector_b))
        self.wait()

        shift_vector = VectorUtils.shiftAmount(vector_a, vector_b)
        self.play(vector_b.animate.shift(shift_vector), run_time=2)
        self.wait(2)


class ShiftAmountVectorAddition(Scene):
    """Example: Vector addition using shiftAmount for animation"""

    def construct(self):
        vector_a = Arrow(ORIGIN, RIGHT * 2, color=BLUE, buff=0)
        self.play(GrowArrow(vector_a))
        self.wait(0.5)

        vector_b = Arrow(DOWN * 2, DOWN * 2 + UP * 1.5, color=RED, buff=0)
        self.play(GrowArrow(vector_b))
        self.wait()

        shift_vector = VectorUtils.shiftAmount(vector_a, vector_b)
        self.play(vector_b.animate.shift(shift_vector), run_time=2)
        self.wait()

        resultant = Arrow(ORIGIN, vector_b.get_end(), color=GREEN, buff=0)
        resultant.set_stroke(width=6)
        self.play(GrowArrow(resultant), run_time=1.5)
        self.wait(2)


class ShiftAmountChain(Scene):
    """Example: Chain multiple vectors using shiftAmount animations"""

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
            shift_vector = VectorUtils.shiftAmount(current, vectors[i])
            self.play(vectors[i].animate.shift(shift_vector), run_time=1.5)
            self.wait(0.3)
            current = vectors[i]

        self.wait()

        resultant = Arrow(vectors[0].get_start(), current.get_end(), color=GREEN, buff=0)
        resultant.set_stroke(width=6)
        self.play(GrowArrow(resultant), run_time=1.5)
        self.wait(2)


class CombinedVectorOperations(Scene):
    """Example: Combining tailAtTip and shiftAmount"""

    def construct(self):
        # Vector A
        vector_a = Arrow(ORIGIN, RIGHT * 2, color=BLUE, buff=0)
        self.play(GrowArrow(vector_a))
        self.wait(0.5)

        # Vector B at origin
        vector_b = Arrow(ORIGIN, UP * 1.5, color=RED, buff=0)
        self.play(GrowArrow(vector_b))
        self.wait(0.5)

        # Use shiftAmount to animate B to A's tip
        shift_vector = VectorUtils.shiftAmount(vector_a, vector_b)
        self.play(vector_b.animate.shift(shift_vector), run_time=1.5)
        self.wait()

        # Resultant
        resultant = Arrow(ORIGIN, vector_b.get_end(), color=GREEN, buff=0)
        resultant.set_stroke(width=6)
        self.play(GrowArrow(resultant), run_time=1.5)
        self.wait(2)


class DynamicVectorAddition(Scene):
    """Example: Dynamic vector addition with rotating base"""

    def construct(self):
        vector_a = Arrow(ORIGIN, RIGHT * 2, color=BLUE, buff=0)
        vector_b_template = Arrow(ORIGIN, UP * 1.5, color=RED, buff=0)

        vector_b_at_tip = always_redraw(
            lambda: VectorUtils.tailAtTip(vector_a, vector_b_template).set_color(ORANGE)
        )

        resultant = always_redraw(
            lambda: Arrow(ORIGIN, vector_b_at_tip.get_end(), color=GREEN, buff=0).set_stroke(width=5)
        )

        self.play(GrowArrow(vector_a))
        self.play(Create(vector_b_at_tip))
        self.play(Create(resultant))
        self.wait()

        self.play(
            Rotate(vector_a, angle=2*PI, about_point=ORIGIN),
            run_time=8,
            rate_func=linear
        )
        self.wait(2)
