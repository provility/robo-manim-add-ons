"""
copy_at Basic Demo - Copy a vector to a new starting position
"""

from manim import *
from robo_manim_add_ons.vector_utils import VectorUtils


class CopyAtBasicDemo(Scene):
    """Basic example: Copy a vector to a new location"""

    def construct(self):
        # Original vector
        source = Arrow(ORIGIN, RIGHT * 2, color=BLUE, buff=0)
        source_label = Text("Source", font_size=20).next_to(source, DOWN, buff=0.2)

        self.play(GrowArrow(source), Write(source_label))
        self.wait()

        # Copy to new location
        new_start = UP * 2 + LEFT
        copied = VectorUtils.copy_at(source, new_start, color=GREEN)
        copied_label = Text("Copy", font_size=20).next_to(copied, UP, buff=0.2)

        self.play(
            TransformFromCopy(source, copied),
            Write(copied_label),
            run_time=1.5
        )
        self.wait(2)
