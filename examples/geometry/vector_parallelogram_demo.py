"""
Demo: Parallelogram Law for Vector Addition using VectorUtils

Shows tail-to-tail parallelogram method for vector addition.
Uses copy_at() for parallelogram sides and add() for the diagonal result.
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils



class ParallelogramLawDemo(Scene):
    """Basic parallelogram law: tail-to-tail vectors form a parallelogram"""

    def construct(self):
        # Define vectors starting from same point (tail-to-tail)
        vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0, fill_opacity=0, color=BLUE)
        vector_b = Arrow(ORIGIN, UP * 2, buff=0, fill_opacity=0, color=RED)

        origin = Dot(ORIGIN, color=YELLOW)

        # Show initial vectors
        self.add(origin)
        self.play(GrowArrow(vector_a), GrowArrow(vector_b))
        self.wait(1)

        # STEP 1: Create parallelogram sides using VectorUtils.copy_at()
        vector_b_from_a = VectorUtils.copy_at(
            vector_b, vector_a.get_end(),
            color="#c2410c", tip_length=0.2
        )
        vector_a_from_b = VectorUtils.copy_at(
            vector_a, vector_b.get_end(),
            color="#b91c1c", tip_length=0.2
        )

        self.play(Create(vector_b_from_a), run_time=1.0)
        self.wait(0.3)
        self.play(Create(vector_a_from_b), run_time=1.0)
        self.wait(0.5)

        # STEP 2: Create result diagonal using VectorUtils.add()
        result_vector = VectorUtils.add(
            vector_a, vector_b,
            color="#047857", tip_length=0.25, stroke_width=6
        )

        self.play(GrowArrow(result_vector), run_time=1.0)
        self.wait(1)


class ParallelogramWithLabels(Scene):
    """Parallelogram law with labels and annotations"""

    def construct(self):
        # Vectors
        vector_a = Arrow(ORIGIN, RIGHT * 2.5, buff=0, fill_opacity=0, color=BLUE)
        vector_b = Arrow(ORIGIN, UP * 1.5, buff=0, fill_opacity=0, color=RED)

        # Labels
        label_a = MathTex(r"\vec{a}", color=BLUE).next_to(vector_a, DOWN)
        label_b = MathTex(r"\vec{b}", color=RED).next_to(vector_b, LEFT)

        # Title
        title = Text("Parallelogram Law: Tail-to-Tail", font_size=36).to_edge(UP)

        # Show setup
        self.play(Write(title))
        self.play(GrowArrow(vector_a), GrowArrow(vector_b))
        self.play(Write(label_a), Write(label_b))
        self.wait(1)

        # Step 1: Complete parallelogram
        step1_text = Text("Step 1: Complete the parallelogram", font_size=24).to_edge(DOWN)
        self.play(Write(step1_text))

        # Copy vectors to form parallelogram
        b_copy = VectorUtils.copy_at(vector_b, vector_a.get_end(), color=RED, stroke_opacity=0.5)
        a_copy = VectorUtils.copy_at(vector_a, vector_b.get_end(), color=BLUE, stroke_opacity=0.5)

        self.play(Create(b_copy), Create(a_copy))
        self.wait(1)

        # Step 2: Draw diagonal
        step2_text = Text("Step 2: Diagonal is a + b", font_size=24, color=GREEN).to_edge(DOWN)
        self.play(Transform(step1_text, step2_text))

        result = VectorUtils.add(vector_a, vector_b, color=GREEN, stroke_width=6)
        label_result = MathTex(r"\vec{a} + \vec{b}", color=GREEN).move_to(result.get_center() + RIGHT * 0.5)

        self.play(GrowArrow(result))
        self.play(Write(label_result))
        self.wait(2)


class DynamicParallelogram(Scene):
    """Interactive: Parallelogram updates as vectors change"""

    def construct(self):
        # Base vectors
        vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0, fill_opacity=0, color=BLUE)
        vector_b = Arrow(ORIGIN, UP * 2, buff=0, fill_opacity=0, color=RED)

        # Dynamic parallelogram sides
        b_copy = always_redraw(
            lambda: VectorUtils.copy_at(
                vector_b, vector_a.get_end(),
                color=RED, stroke_opacity=0.5
            )
        )

        a_copy = always_redraw(
            lambda: VectorUtils.copy_at(
                vector_a, vector_b.get_end(),
                color=BLUE, stroke_opacity=0.5
            )
        )

        # Dynamic result diagonal
        result = always_redraw(
            lambda: VectorUtils.add(
                vector_a, vector_b,
                color=GREEN, stroke_width=6
            )
        )

        # Show initial state
        self.play(GrowArrow(vector_a), GrowArrow(vector_b))
        self.add(b_copy, a_copy, result)
        self.wait(1)

        # Rotate vector b - parallelogram updates
        self.play(
            Rotate(vector_b, angle=PI/2, about_point=ORIGIN),
            run_time=3
        )
        self.wait(1)

        # Scale vector a - parallelogram updates
        self.play(
            vector_a.animate.put_start_and_end_on(ORIGIN, RIGHT * 1.5),
            run_time=2
        )
        self.wait(1)

        # Rotate vector a
        self.play(
            Rotate(vector_a, angle=-PI/4, about_point=ORIGIN),
            run_time=2
        )
        self.wait(1)


class ComparisonTipToTailVsParallelogram(Scene):
    """Side-by-side: Tip-to-tail vs Parallelogram methods"""

    def construct(self):
        # Left side: Tip-to-tail method
        left_title = Text("Tip-to-Tail", font_size=28).move_to(LEFT * 3 + UP * 3)
        left_a = Arrow(LEFT * 4.5, LEFT * 4.5 + RIGHT * 1.5, buff=0, fill_opacity=0, color=BLUE)
        left_b_original = Arrow(LEFT * 4.5, LEFT * 4.5 + UP * 1.2, buff=0, fill_opacity=0, color=RED)

        # Right side: Parallelogram method
        right_title = Text("Parallelogram", font_size=28).move_to(RIGHT * 3 + UP * 3)
        right_a = Arrow(RIGHT * 1.5, RIGHT * 1.5 + RIGHT * 1.5, buff=0, fill_opacity=0, color=BLUE)
        right_b = Arrow(RIGHT * 1.5, RIGHT * 1.5 + UP * 1.2, buff=0, fill_opacity=0, color=RED)

        # Show titles and base vectors
        self.play(Write(left_title), Write(right_title))
        self.play(
            GrowArrow(left_a), GrowArrow(left_b_original),
            GrowArrow(right_a), GrowArrow(right_b)
        )
        self.wait(1)

        # Left: Move b to tip of a (tip-to-tail)
        left_b_shifted = VectorUtils.tail_at_tip(left_a, left_b_original)
        self.play(TransformFromCopy(left_b_original, left_b_shifted))
        self.wait(0.5)

        # Right: Complete parallelogram
        right_b_copy = VectorUtils.copy_at(right_b, right_a.get_end(), color=RED, stroke_opacity=0.5)
        right_a_copy = VectorUtils.copy_at(right_a, right_b.get_end(), color=BLUE, stroke_opacity=0.5)

        self.play(Create(right_b_copy), Create(right_a_copy))
        self.wait(0.5)

        # Both: Show result
        left_result = VectorUtils.add(left_a, left_b_original, color=GREEN, stroke_width=5)
        right_result = VectorUtils.add(right_a, right_b, color=GREEN, stroke_width=5)

        self.play(GrowArrow(left_result), GrowArrow(right_result))
        self.wait(2)


class MultipleVectorAdditions(Scene):
    """Adding three vectors using parallelogram method"""

    def construct(self):
        # Three vectors from origin
        vec_a = Arrow(ORIGIN, RIGHT * 2, buff=0, fill_opacity=0, color=BLUE)
        vec_b = Arrow(ORIGIN, UP * 1.5, buff=0, fill_opacity=0, color=RED)
        vec_c = Arrow(ORIGIN, LEFT * 0.5 + UP * 0.8, buff=0, fill_opacity=0, color=YELLOW)

        # Labels
        label_a = MathTex(r"\vec{a}", color=BLUE).next_to(vec_a, DOWN)
        label_b = MathTex(r"\vec{b}", color=RED).next_to(vec_b, LEFT)
        label_c = MathTex(r"\vec{c}", color=YELLOW).next_to(vec_c, LEFT)

        # Show vectors
        self.play(GrowArrow(vec_a), GrowArrow(vec_b), GrowArrow(vec_c))
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(1)

        # First: Add a + b using parallelogram
        b_copy1 = VectorUtils.copy_at(vec_b, vec_a.get_end(), color=RED, stroke_opacity=0.4)
        a_copy1 = VectorUtils.copy_at(vec_a, vec_b.get_end(), color=BLUE, stroke_opacity=0.4)
        result_ab = VectorUtils.add(vec_a, vec_b, color=PURPLE, stroke_width=4)

        self.play(Create(b_copy1), Create(a_copy1))
        self.play(GrowArrow(result_ab))
        self.wait(1)

        # Second: Add (a+b) + c using parallelogram
        c_copy = VectorUtils.copy_at(vec_c, result_ab.get_end(), color=YELLOW, stroke_opacity=0.4)
        ab_copy = VectorUtils.copy_at(result_ab, vec_c.get_end(), color=PURPLE, stroke_opacity=0.4)

        self.play(Create(c_copy), Create(ab_copy))
        self.wait(0.5)

        # Final result: a + b + c
        # Need to calculate manually since we don't have a 3-vector add method
        vec_a_dir = vec_a.get_end() - vec_a.get_start()
        vec_b_dir = vec_b.get_end() - vec_b.get_start()
        vec_c_dir = vec_c.get_end() - vec_c.get_start()
        final_end = ORIGIN + vec_a_dir + vec_b_dir + vec_c_dir
        final_result = Arrow(ORIGIN, final_end, buff=0, fill_opacity=0, color=GREEN, stroke_width=6)

        label_final = MathTex(r"\vec{a} + \vec{b} + \vec{c}", color=GREEN).next_to(final_result, DOWN)

        self.play(GrowArrow(final_result))
        self.play(Write(label_final))
        self.wait(2)


class ParallelogramGrid(Scene):
    """Grid of parallelograms showing vector addition patterns"""

    def construct(self):
        # Base vectors
        vec_a = Arrow(ORIGIN, RIGHT * 1.5, buff=0, fill_opacity=0, color=BLUE)
        vec_b = Arrow(ORIGIN, UP * 1, buff=0, fill_opacity=0, color=RED)

        # Create grid of parallelograms
        positions = [
            LEFT * 3 + UP * 1.5,
            ORIGIN + UP * 1.5,
            RIGHT * 3 + UP * 1.5,
            LEFT * 3 + DOWN * 1.5,
            ORIGIN + DOWN * 1.5,
            RIGHT * 3 + DOWN * 1.5,
        ]

        for pos in positions:
            # Shift vectors to position
            a_local = Arrow(pos, pos + (vec_a.get_end() - vec_a.get_start()), buff=0, color=BLUE, stroke_width=2)
            b_local = Arrow(pos, pos + (vec_b.get_end() - vec_b.get_start()), buff=0, color=RED, stroke_width=2)

            # Create parallelogram
            b_copy = VectorUtils.copy_at(b_local, a_local.get_end(), color=RED, stroke_width=2, stroke_opacity=0.3)
            a_copy = VectorUtils.copy_at(a_local, b_local.get_end(), color=BLUE, stroke_width=2, stroke_opacity=0.3)

            # Result diagonal
            result = VectorUtils.add(a_local, b_local, color=GREEN, stroke_width=3)

            self.add(a_local, b_local, b_copy, a_copy, result)

        self.wait(3)


class ParallelogramProof(Scene):
    """Visual proof that both diagonals give the same result"""

    def construct(self):
        # Base vectors
        vector_a = Arrow(ORIGIN, RIGHT * 2.5, buff=0, fill_opacity=0, color=BLUE)
        vector_b = Arrow(ORIGIN, UP * 2, buff=0, fill_opacity=0, color=RED)

        # Show vectors
        self.play(GrowArrow(vector_a), GrowArrow(vector_b))
        self.wait(1)

        # Complete parallelogram
        b_copy = VectorUtils.copy_at(vector_b, vector_a.get_end(), color=RED, stroke_opacity=0.5)
        a_copy = VectorUtils.copy_at(vector_a, vector_b.get_end(), color=BLUE, stroke_opacity=0.5)

        self.play(Create(b_copy), Create(a_copy))
        self.wait(1)

        # Show MAIN diagonal (a + b)
        diagonal1 = VectorUtils.add(vector_a, vector_b, color=GREEN, stroke_width=6)
        label1 = MathTex(r"\vec{a} + \vec{b}", color=GREEN).next_to(diagonal1, RIGHT)

        self.play(GrowArrow(diagonal1), Write(label1))
        self.wait(1)

        # Show OTHER diagonal (b + a) - should be the same!
        diagonal2 = Arrow(
            vector_b.get_start(),
            vector_a.get_end() + (vector_b.get_end() - vector_b.get_start()),
            buff=0, color=YELLOW, stroke_width=6, stroke_opacity=0.6
        )
        label2 = MathTex(r"\vec{b} + \vec{a}", color=YELLOW).next_to(diagonal2, LEFT)

        self.play(GrowArrow(diagonal2), Write(label2))
        self.wait(1)

        # Highlight they're the same
        equals_text = MathTex(r"\vec{a} + \vec{b} = \vec{b} + \vec{a}", font_size=48).to_edge(DOWN)
        equals_text.set_color(GREEN)

        self.play(Write(equals_text))
        self.wait(2)
