"""
Dynamic Geometry Examples using add_updater and always_redraw

This demonstrates how to use perp() and parallel() with Manim's
dynamic update features for interactive geometry.
"""

from manim import *
from robo_manim_add_ons import perp, parallel


class DynamicPerpExample(Scene):
    """Example: Perpendicular line that updates as base line rotates"""

    def construct(self):
        base_line = Line(LEFT * 2, RIGHT * 2, color=BLUE)
        center_dot = Dot(ORIGIN, color=YELLOW)

        perp_line = always_redraw(
            lambda: perp(base_line, center_dot, length=3, placement="mid").set_color(RED)
        )

        self.play(Create(base_line))
        self.play(FadeIn(center_dot))
        self.play(Create(perp_line))
        self.wait()

        self.play(Rotate(base_line, angle=PI/3, about_point=ORIGIN), run_time=3)
        self.wait()

        self.play(Rotate(base_line, angle=-PI/3, about_point=ORIGIN), run_time=3)
        self.wait()


class DynamicParallelExample(Scene):
    """Example: Parallel line that follows a moving reference line"""

    def construct(self):
        ref_line = Line(LEFT * 2 + UP, RIGHT * 2 + UP, color=BLUE)
        parallel_dot = Dot(DOWN * 0.5, color=YELLOW)

        parallel_line = always_redraw(
            lambda: parallel(ref_line, parallel_dot, length=4, placement="mid").set_color(GREEN)
        )

        self.play(Create(ref_line))
        self.play(FadeIn(parallel_dot))
        self.play(Create(parallel_line))
        self.wait()

        self.play(ref_line.animate.shift(DOWN * 2), run_time=2)
        self.wait()

        self.play(Rotate(ref_line, angle=PI/4), run_time=2)
        self.wait()

        self.play(
            ref_line.animate.shift(UP * 2),
            Rotate(ref_line, angle=-PI/4),
            run_time=2
        )
        self.wait()


class InteractivePerpUpdater(Scene):
    """Example: Using add_updater with a moving point"""

    def construct(self):
        base_line = Line(LEFT * 3, RIGHT * 3, color=BLUE)
        moving_dot = Dot(color=YELLOW).move_to(LEFT * 2)

        perp_line = Line(ORIGIN, UP)

        def update_perp(mob):
            new_perp = perp(base_line, moving_dot, length=2, placement="mid").set_color(RED)
            mob.become(new_perp)

        perp_line.add_updater(update_perp)

        self.play(Create(base_line))
        self.play(FadeIn(moving_dot))
        self.add(perp_line)
        self.wait()

        self.play(moving_dot.animate.move_to(RIGHT * 2), run_time=4, rate_func=smooth)
        self.wait()

        self.play(moving_dot.animate.move_to(LEFT * 2), run_time=4, rate_func=smooth)
        self.wait()

        perp_line.clear_updaters()


class ParallelogramUpdater(Scene):
    """Example: Dynamic parallelogram using parallel lines"""

    def construct(self):
        base = Line(LEFT * 2 + DOWN, RIGHT * 2 + DOWN, color=BLUE)
        top_left_dot = Dot(LEFT * 1.5 + UP, color=YELLOW)

        side = always_redraw(
            lambda: Line(base.get_start(), top_left_dot.get_center(), color=BLUE)
        )

        top = always_redraw(
            lambda: parallel(
                base, top_left_dot,
                length=base.get_length(),
                placement="start"
            ).set_color(GREEN)
        )

        top_right_dot = always_redraw(lambda: Dot(top.get_end(), color=YELLOW))

        right_side = always_redraw(
            lambda: parallel(
                side, top_right_dot,
                length=side.get_length(),
                placement="end"
            ).set_color(GREEN)
        )

        self.play(Create(base))
        self.play(FadeIn(top_left_dot))
        self.add(side, top, right_side)
        self.wait()

        self.play(top_left_dot.animate.move_to(LEFT * 2.5 + UP * 2), run_time=3)
        self.wait()

        self.play(top_left_dot.animate.move_to(LEFT * 0.5 + UP * 0.5), run_time=3)
        self.wait()

        self.play(top_left_dot.animate.move_to(LEFT * 1.5 + UP), run_time=2)
        self.wait()


class MultiplePerpendicularUpdaters(Scene):
    """Example: Multiple perpendicular lines with different placements"""

    def construct(self):
        base = Line(LEFT * 3, RIGHT * 3, color=BLUE)

        dot_start = always_redraw(lambda: Dot(base.get_start(), color=RED))
        dot_mid = always_redraw(lambda: Dot(base.get_center(), color=YELLOW))
        dot_end = always_redraw(lambda: Dot(base.get_end(), color=GREEN))

        perp_start = always_redraw(
            lambda: perp(base, dot_start, length=2, placement="mid").set_color(RED)
        )

        perp_mid = always_redraw(
            lambda: perp(base, dot_mid, length=2, placement="mid").set_color(YELLOW)
        )

        perp_end = always_redraw(
            lambda: perp(base, dot_end, length=2, placement="mid").set_color(GREEN)
        )

        self.play(Create(base))
        self.add(dot_start, dot_mid, dot_end)
        self.play(Create(perp_start), Create(perp_mid), Create(perp_end))
        self.wait()

        self.play(Rotate(base, angle=2*PI, about_point=ORIGIN), run_time=8, rate_func=linear)
        self.wait()


class ParallelLinesGrid(Scene):
    """Example: Grid of parallel lines using always_redraw"""

    def construct(self):
        ref_line = Line(LEFT * 3, RIGHT * 3, color=BLUE).shift(UP * 2)

        num_lines = 6
        spacing = 0.6

        dots = [Dot(ORIGIN + DOWN * i * spacing, radius=0.05) for i in range(1, num_lines + 1)]

        parallel_lines = VGroup()
        for i, dot in enumerate(dots):
            color_t = i / (num_lines - 1) if num_lines > 1 else 0
            line_color = interpolate_color(RED, YELLOW, color_t)

            line = always_redraw(
                lambda d=dot, c=line_color: parallel(
                    ref_line, d,
                    length=6,
                    placement="mid"
                ).set_color(c)
            )
            parallel_lines.add(line)

        self.play(Create(ref_line))
        self.play(LaggedStart(*[Create(line) for line in parallel_lines], lag_ratio=0.2))
        self.wait()

        self.play(Rotate(ref_line, angle=PI/6, about_point=ORIGIN), run_time=3)
        self.wait()

        self.play(ref_line.animate.shift(DOWN * 1.5), run_time=2)
        self.wait()

        self.play(
            Rotate(ref_line, angle=-PI/6, about_point=ORIGIN),
            ref_line.animate.shift(UP * 1.5),
            run_time=3
        )
        self.wait()
