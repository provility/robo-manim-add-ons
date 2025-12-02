"""Demo of label() function."""

from manim import *
from robo_manim_add_ons import label


class BasicLabelDemo(Scene):
    """Simple label between two points."""

    def construct(self):
        # Two dots
        dot_a = Dot([-2, 0, 0], color=BLUE)
        dot_b = Dot([2, 0, 0], color=RED)

        # Line connecting them
        line = Line(dot_a, dot_b, color=WHITE)

        # Label positioned above the line
        ab_label = label("AB", dot_a, dot_b, buff=0.5)

        self.play(FadeIn(dot_a), FadeIn(dot_b))
        self.play(Create(line))
        self.play(FadeIn(ab_label))
        self.wait(2)
