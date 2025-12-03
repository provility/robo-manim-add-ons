"""
Demo: extended_line() - Extending lines from specific proportions

Shows how to create lines that extend from points along an existing line.
"""

from manim import *
from robo_manim_add_ons import extended_line


class ExtendedLineBasicDemo(Scene):
    """Basic demonstration of extended_line at different proportions."""

    def construct(self):
        base_line = Line(LEFT * 3, RIGHT * 3, color=BLUE)
        self.play(Create(base_line))
        self.wait(0.5)

        # Extend from start (proportion=0.0)
        ext_start = extended_line(base_line, proportion=0.0, length=1.5).set_color(RED)
        self.play(Create(ext_start))
        self.wait(0.5)

        # Extend from midpoint (proportion=0.5)
        ext_mid = extended_line(base_line, proportion=0.5, length=1.5).set_color(GREEN)
        self.play(Create(ext_mid))
        self.wait(0.5)

        # Extend from end (proportion=1.0)
        ext_end = extended_line(base_line, proportion=1.0, length=1.5).set_color(YELLOW)
        self.play(Create(ext_end))
        self.wait(2)


class ExtendedLineMultipleDemo(Scene):
    """Show multiple extensions at various proportions."""

    def construct(self):
        base_line = Line(LEFT * 3, RIGHT * 3, color=BLUE)
        self.play(Create(base_line))
        self.wait(0.5)

        proportions = [0.0, 0.25, 0.5, 0.75, 1.0]
        colors = [RED, ORANGE, GREEN, YELLOW, PURPLE]

        ext_lines = VGroup()
        for prop, color in zip(proportions, colors):
            ext = extended_line(base_line, proportion=prop, length=1.0).set_color(color)
            ext_lines.add(ext)

        self.play(LaggedStart(*[Create(line) for line in ext_lines], lag_ratio=0.3))
        self.wait(2)


class ExtendedLineDynamicDemo(Scene):
    """Dynamic demonstration with always_redraw."""

    def construct(self):
        base_line = Line(LEFT * 2, RIGHT * 2, color=BLUE)
        t_tracker = ValueTracker(0.0)

        ext_line = always_redraw(
            lambda: extended_line(
                base_line,
                proportion=t_tracker.get_value(),
                length=1.5
            ).set_color(RED)
        )

        self.play(Create(base_line))
        self.add(ext_line)
        self.wait(0.5)

        self.play(t_tracker.animate.set_value(0.5), run_time=2)
        self.wait(0.5)

        self.play(t_tracker.animate.set_value(1.0), run_time=2)
        self.wait(0.5)

        self.play(t_tracker.animate.set_value(0.0), run_time=3)
        self.wait(2)


class ExtendedLineRotatingDemo(Scene):
    """Show extended line with a rotating base."""

    def construct(self):
        base_line = Line(LEFT * 2, RIGHT * 2, color=BLUE)

        ext_line = always_redraw(
            lambda: extended_line(base_line, proportion=1.0, length=1.5).set_color(GREEN)
        )

        self.play(Create(base_line))
        self.add(ext_line)
        self.wait(0.5)

        self.play(Rotate(base_line, angle=PI, about_point=ORIGIN), run_time=4)
        self.wait(0.5)

        self.play(Rotate(base_line, angle=-PI, about_point=ORIGIN), run_time=4)
        self.wait(2)


class ExtendedLineDiagonalDemo(Scene):
    """Demonstrate extending diagonal lines."""

    def construct(self):
        base_line = Line(LEFT * 2 + DOWN, RIGHT * 2 + UP, color=BLUE)
        self.play(Create(base_line))
        self.wait(0.5)

        proportions = [0.0, 0.33, 0.67, 1.0]
        colors = [RED, ORANGE, YELLOW, GREEN]

        ext_lines = VGroup()
        for prop, color in zip(proportions, colors):
            ext = extended_line(base_line, proportion=prop, length=1.2).set_color(color)
            ext_lines.add(ext)

        self.play(LaggedStart(*[Create(line) for line in ext_lines], lag_ratio=0.4))
        self.wait(2)
