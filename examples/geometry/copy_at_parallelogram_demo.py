"""
copy_at Parallelogram Demo - Simplified parallelogram construction
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils


class CopyAtParallelogramDemo(Scene):
    """Example: Construct parallelogram law of vector addition using copy_at"""

    def construct(self):
        # Two vectors starting from origin
        vector_a = Arrow(ORIGIN, RIGHT * 2.5, color="#3b82f6", buff=0, tip_length=0.2)
        vector_b = Arrow(ORIGIN, UP * 2, color="#ef4444", buff=0, tip_length=0.2)

        # Labels
        label_a = MathTex(r"\vec{a}", font_size=28, color="#3b82f6").next_to(vector_a, DOWN, buff=0.15)
        label_b = MathTex(r"\vec{b}", font_size=28, color="#ef4444").next_to(vector_b, LEFT, buff=0.15)

        origin_dot = Dot(ORIGIN, color=YELLOW)

        # Add static elements
        self.add(origin_dot)

        # STEP 1: Show initial vectors
        self.play(GrowArrow(vector_a), Write(label_a), run_time=1.0)
        self.wait(0.3)
        self.play(GrowArrow(vector_b), Write(label_b), run_time=1.0)
        self.wait(0.5)

        # STEP 2: Create parallelogram sides using copy_at
        # Copy vector_b starting from vector_a's tip
        side_b = VectorUtils.copy_at(vector_b, vector_a.get_end(), color="#c2410c", tip_length=0.2)

        # Copy vector_a starting from vector_b's tip
        side_a = VectorUtils.copy_at(vector_a, vector_b.get_end(), color="#b91c1c", tip_length=0.2)

        self.play(Create(side_b), run_time=1.0)
        self.wait(0.3)
        self.play(Create(side_a), run_time=1.0)
        self.wait(0.5)

        # STEP 3: Create result diagonal
        result_vector = Arrow(
            ORIGIN,
            side_b.get_end(),
            buff=0,
            color="#047857",
            tip_length=0.25,
            stroke_width=6
        )
        result_label = MathTex(r"\vec{a} + \vec{b}", font_size=28, color="#047857")
        result_label.next_to(result_vector.get_center(), UP + LEFT, buff=0.2)

        self.play(GrowArrow(result_vector), run_time=1.0)
        self.wait(0.3)
        self.play(Write(result_label), run_time=0.8)
        self.wait(2)


class CopyAtParallelogramComparisonDemo(Scene):
    """Example: Show how copy_at simplifies code - before and after"""

    def construct(self):
        # Title
        title = Text("Parallelogram Construction", font_size=32)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.5)

        # Vectors
        vector_a = Arrow(ORIGIN, RIGHT * 2, color=BLUE, buff=0, tip_length=0.2)
        vector_b = Arrow(ORIGIN, UP * 1.5, color=RED, buff=0, tip_length=0.2)

        self.play(GrowArrow(vector_a), GrowArrow(vector_b))
        self.wait()

        # OLD WAY: Manual direction extraction
        old_text = Text("Without copy_at:", font_size=20, color=YELLOW)
        old_text.to_corner(UL, buff=0.5).shift(DOWN * 0.8)
        self.play(Write(old_text))

        # Show the manual process
        vec_a_dir = vector_a.get_end() - vector_a.get_start()
        vec_b_dir = vector_b.get_end() - vector_b.get_start()

        # Manual arrow creation
        side_b_manual = Arrow(
            vector_a.get_end(),
            vector_a.get_end() + vec_b_dir,
            buff=0,
            color=ORANGE,
            tip_length=0.2
        )
        side_a_manual = Arrow(
            vector_b.get_end(),
            vector_b.get_end() + vec_a_dir,
            buff=0,
            color=ORANGE,
            tip_length=0.2
        )

        self.play(Create(side_b_manual), Create(side_a_manual), run_time=1.5)
        self.wait()

        # Fade out manual version
        self.play(
            FadeOut(side_b_manual),
            FadeOut(side_a_manual),
            FadeOut(old_text)
        )
        self.wait(0.3)

        # NEW WAY: Using copy_at
        new_text = Text("With copy_at:", font_size=20, color=GREEN)
        new_text.to_corner(UL, buff=0.5).shift(DOWN * 0.8)
        self.play(Write(new_text))

        # Clean one-liners
        side_b_clean = VectorUtils.copy_at(vector_b, vector_a.get_end(), color=GREEN, tip_length=0.2)
        side_a_clean = VectorUtils.copy_at(vector_a, vector_b.get_end(), color=GREEN, tip_length=0.2)

        self.play(Create(side_b_clean), Create(side_a_clean), run_time=1.0)
        self.wait()

        # Show result
        result = Arrow(ORIGIN, side_b_clean.get_end(), buff=0, color=PURPLE, stroke_width=6, tip_length=0.25)
        self.play(GrowArrow(result), run_time=1.0)
        self.wait(2)
