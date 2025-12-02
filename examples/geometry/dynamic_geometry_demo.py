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
        # Create a base line that we'll animate
        base_line = Line(LEFT * 2, RIGHT * 2, color=BLUE)

        # Fixed dot at center where perpendicular passes through
        center_dot = Dot(ORIGIN, color=YELLOW)

        # Create a perpendicular line using always_redraw
        # This will automatically recreate whenever base_line changes
        perp_line = always_redraw(
            lambda: perp(
                base_line,
                center_dot,
                length=3,
                placement="mid"
            ).set_color(RED)
        )

        # Add labels
        base_label = Text("Base Line", font_size=24).next_to(base_line, DOWN, buff=0.5)
        perp_label = always_redraw(
            lambda: Text("Perpendicular", font_size=24, color=RED)
            .next_to(perp_line.get_center(), RIGHT, buff=0.3)
        )

        # Show initial setup
        self.play(Create(base_line))
        self.play(FadeIn(center_dot))
        self.play(Write(base_label))
        self.play(Create(perp_line))
        self.play(Write(perp_label))
        self.wait()

        # Rotate the base line - perpendicular updates automatically!
        self.play(
            Rotate(base_line, angle=PI/3, about_point=ORIGIN),
            run_time=3
        )
        self.wait()

        # Rotate back
        self.play(
            Rotate(base_line, angle=-PI/3, about_point=ORIGIN),
            run_time=3
        )
        self.wait()


class DynamicParallelExample(Scene):
    """Example: Parallel line that follows a moving reference line"""

    def construct(self):
        # Reference line (we'll move this)
        ref_line = Line(LEFT * 2 + UP, RIGHT * 2 + UP, color=BLUE)

        # Fixed dot for parallel line to pass through
        parallel_dot = Dot(DOWN * 0.5, color=YELLOW)

        # Parallel line using always_redraw
        parallel_line = always_redraw(
            lambda: parallel(
                ref_line,
                parallel_dot,
                length=4,
                placement="mid"
            ).set_color(GREEN)
        )

        # Labels
        ref_label = Text("Reference", font_size=24).next_to(ref_line, UP)
        parallel_label = always_redraw(
            lambda: Text("Parallel", font_size=24, color=GREEN)
            .next_to(parallel_line, DOWN)
        )

        # Show setup
        self.play(Create(ref_line), Write(ref_label))
        self.play(FadeIn(parallel_dot))
        self.play(Create(parallel_line), Write(parallel_label))
        self.wait()

        # Move reference line - parallel line follows!
        self.play(
            ref_line.animate.shift(DOWN * 2),
            run_time=2
        )
        self.wait()

        # Rotate reference line
        self.play(
            Rotate(ref_line, angle=PI/4),
            run_time=2
        )
        self.wait()

        # Move back
        self.play(
            ref_line.animate.shift(UP * 2),
            Rotate(ref_line, angle=-PI/4),
            run_time=2
        )
        self.wait()


class InteractivePerpUpdater(Scene):
    """Example: Using add_updater with a moving point"""

    def construct(self):
        # Fixed base line
        base_line = Line(LEFT * 3, RIGHT * 3, color=BLUE)

        # Moving point (this dot moves along the base line)
        moving_dot = Dot(color=YELLOW).move_to(LEFT * 2)

        # Perpendicular line from the point - using add_updater
        perp_line = Line(ORIGIN, UP)  # Initial dummy line

        def update_perp(mob):
            # Create new perpendicular line passing through moving_dot
            new_perp = perp(
                base_line,
                moving_dot,
                length=2,
                placement="mid"
            ).set_color(RED)

            # Update the mobject to match the new perpendicular
            mob.become(new_perp)

        perp_line.add_updater(update_perp)

        # Labels
        title = Text("Perpendicular follows the moving dot", font_size=28)
        title.to_edge(UP)

        # Show scene
        self.add(title)
        self.play(Create(base_line))
        self.play(FadeIn(moving_dot))
        self.add(perp_line)
        self.wait()

        # Move point along - perpendicular updates continuously
        self.play(
            moving_dot.animate.move_to(RIGHT * 2),
            run_time=4,
            rate_func=smooth
        )
        self.wait()

        # Move back
        self.play(
            moving_dot.animate.move_to(LEFT * 2),
            run_time=4,
            rate_func=smooth
        )
        self.wait()

        # Remove updater before finishing
        perp_line.clear_updaters()


class ParallelogramUpdater(Scene):
    """Example: Dynamic parallelogram using parallel lines"""

    def construct(self):
        # Base of parallelogram (movable)
        base = Line(LEFT * 2 + DOWN, RIGHT * 2 + DOWN, color=BLUE)

        # Moving dot for the top-left corner
        top_left_dot = Dot(LEFT * 1.5 + UP, color=YELLOW)

        # Side connects base start to the moving dot
        side = always_redraw(
            lambda: Line(base.get_start(), top_left_dot.get_center(), color=BLUE)
        )

        # Top edge - parallel to base, passing through top_left_dot
        top = always_redraw(
            lambda: parallel(
                base,
                top_left_dot,
                length=base.get_length(),
                placement="start"
            ).set_color(GREEN)
        )

        # Right side - parallel to left side
        # Need a dot at the top-right corner
        top_right_dot = always_redraw(
            lambda: Dot(top.get_end(), color=YELLOW)
        )

        right_side = always_redraw(
            lambda: parallel(
                side,
                top_right_dot,
                length=side.get_length(),
                placement="end"
            ).set_color(GREEN)
        )

        title = Text("Dynamic Parallelogram", font_size=28).to_edge(UP)
        instruction = Text("Top-left corner follows dot", font_size=20).to_edge(DOWN)

        # Show construction
        self.add(title, instruction)
        self.play(Create(base))
        self.play(FadeIn(top_left_dot))
        self.add(side, top, right_side)
        self.wait()

        # Move the top-left dot
        self.play(
            top_left_dot.animate.move_to(LEFT * 2.5 + UP * 2),
            run_time=3
        )
        self.wait()

        # Move it again
        self.play(
            top_left_dot.animate.move_to(LEFT * 0.5 + UP * 0.5),
            run_time=3
        )
        self.wait()

        # Reset
        self.play(
            top_left_dot.animate.move_to(LEFT * 1.5 + UP),
            run_time=2
        )
        self.wait()


class MultiplePerpendicularUpdaters(Scene):
    """Example: Multiple perpendicular lines with different placements"""

    def construct(self):
        # Rotating base line
        base = Line(LEFT * 3, RIGHT * 3, color=BLUE)

        # Three dots at different positions
        dot_start = always_redraw(lambda: Dot(base.get_start(), color=RED))
        dot_mid = always_redraw(lambda: Dot(base.get_center(), color=YELLOW))
        dot_end = always_redraw(lambda: Dot(base.get_end(), color=GREEN))

        # Three perpendiculars at different positions
        perp_start = always_redraw(
            lambda: perp(base, dot_start, length=2, placement="mid").set_color(RED)
        )

        perp_mid = always_redraw(
            lambda: perp(base, dot_mid, length=2, placement="mid").set_color(YELLOW)
        )

        perp_end = always_redraw(
            lambda: perp(base, dot_end, length=2, placement="mid").set_color(GREEN)
        )

        # Labels
        title = Text("Perpendiculars at start, mid, and end", font_size=24)
        title.to_edge(UP)

        label_start = Text("start", font_size=20, color=RED)
        label_mid = Text("mid", font_size=20, color=YELLOW)
        label_end = Text("end", font_size=20, color=GREEN)

        labels = VGroup(label_start, label_mid, label_end)
        labels.arrange(RIGHT, buff=0.5).to_edge(DOWN)

        # Show scene
        self.add(title, labels)
        self.play(Create(base))
        self.add(dot_start, dot_mid, dot_end)
        self.play(
            Create(perp_start),
            Create(perp_mid),
            Create(perp_end)
        )
        self.wait()

        # Rotate base line around center
        self.play(
            Rotate(base, angle=2*PI, about_point=ORIGIN),
            run_time=8,
            rate_func=linear
        )
        self.wait()


class ParallelLinesGrid(Scene):
    """Example: Grid of parallel lines using always_redraw"""

    def construct(self):
        # Reference line
        ref_line = Line(LEFT * 3, RIGHT * 3, color=BLUE).shift(UP * 2)

        # Create dots for parallel lines at different vertical positions
        num_lines = 6
        spacing = 0.6

        # Create fixed dots at different vertical positions
        dots = [Dot(ORIGIN + DOWN * i * spacing, radius=0.05) for i in range(1, num_lines + 1)]

        parallel_lines = VGroup()
        for i, dot in enumerate(dots):
            # Calculate color gradient
            color_t = i / (num_lines - 1) if num_lines > 1 else 0
            line_color = interpolate_color(RED, YELLOW, color_t)

            line = always_redraw(
                lambda d=dot, c=line_color: parallel(
                    ref_line,
                    d,
                    length=6,
                    placement="mid"
                ).set_color(c)
            )
            parallel_lines.add(line)

        title = Text("Parallel Lines Grid", font_size=28).to_edge(UP)

        # Show construction
        self.add(title)
        self.play(Create(ref_line))
        self.play(LaggedStart(*[Create(line) for line in parallel_lines], lag_ratio=0.2))
        self.wait()

        # Rotate reference - all parallels follow
        self.play(
            Rotate(ref_line, angle=PI/6, about_point=ORIGIN),
            run_time=3
        )
        self.wait()

        # Move reference
        self.play(
            ref_line.animate.shift(DOWN * 1.5),
            run_time=2
        )
        self.wait()

        # Rotate back and reset
        self.play(
            Rotate(ref_line, angle=-PI/6, about_point=ORIGIN),
            ref_line.animate.shift(UP * 1.5),
            run_time=3
        )
        self.wait()
