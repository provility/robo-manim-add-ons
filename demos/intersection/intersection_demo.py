"""
Demo of intersection_utils: intersect_lines and intersect_line_circle functions.
"""

from manim import *
from robo_manim_add_ons import intersect_lines, intersect_line_circle


class BasicIntersectionDemo(Scene):
    """Demonstrate basic line intersection."""

    def construct(self):
        # Create two intersecting lines
        line1 = Line(LEFT * 3, RIGHT * 3, color=BLUE)
        line2 = Line(DOWN * 2, UP * 2, color=GREEN)

        # Find intersection
        intersection_dot = intersect_lines(line1, line2)
        intersection_dot.set_color(RED).scale(1.5)

        # Labels
        line1_label = Text("Line 1", font_size=24, color=BLUE).next_to(line1, DOWN)
        line2_label = Text("Line 2", font_size=24, color=GREEN).next_to(line2, RIGHT)
        intersection_label = Text("Intersection", font_size=20, color=RED).next_to(intersection_dot, UP * 1.5)

        # Animate
        self.play(Create(line1), Write(line1_label))
        self.wait(0.5)
        self.play(Create(line2), Write(line2_label))
        self.wait(0.5)
        self.play(FadeIn(intersection_dot, scale=0.5), Write(intersection_label))
        self.wait(2)


class DiagonalIntersectionDemo(Scene):
    """Demonstrate diagonal line intersection."""

    def construct(self):
        # Create two diagonal lines forming an X
        line1 = Line(LEFT * 2 + DOWN * 2, RIGHT * 2 + UP * 2, color=BLUE)
        line2 = Line(LEFT * 2 + UP * 2, RIGHT * 2 + DOWN * 2, color=YELLOW)

        # Find intersection
        intersection_dot = intersect_lines(line1, line2)
        intersection_dot.set_color(RED).scale(1.5)

        title = Text("Diagonal Lines Intersection", font_size=28).to_edge(UP)

        # Animate
        self.add(title)
        self.play(Create(line1))
        self.play(Create(line2))
        self.wait(0.5)
        self.play(FadeIn(intersection_dot, scale=0.3))
        self.wait(2)


class ParallelLinesDemo(Scene):
    """Demonstrate parallel lines (no intersection)."""

    def construct(self):
        # Create parallel horizontal lines
        line1 = Line(LEFT * 3, RIGHT * 3, color=BLUE).shift(UP)
        line2 = Line(LEFT * 3, RIGHT * 3, color=GREEN).shift(DOWN)

        # Try to find intersection
        result = intersect_lines(line1, line2)

        # Labels
        line1_label = Text("Line 1", font_size=24, color=BLUE).next_to(line1, UP)
        line2_label = Text("Line 2", font_size=24, color=GREEN).next_to(line2, DOWN)

        # Check if result is empty
        if len(result) == 0:
            no_intersection_text = Text("No Intersection!", font_size=30, color=RED)
            parallel_text = Text("(Parallel lines)", font_size=20, color=ORANGE)
            message = VGroup(no_intersection_text, parallel_text).arrange(DOWN)

        # Animate
        self.play(Create(line1), Write(line1_label))
        self.play(Create(line2), Write(line2_label))
        self.wait(1)
        self.play(Write(message))
        self.wait(2)


class ExtendedIntersectionDemo(Scene):
    """Demonstrate intersection of extended lines."""

    def construct(self):
        # Two line segments that don't physically touch
        # but their infinite extensions intersect
        line1 = Line(LEFT * 3 + DOWN, LEFT + DOWN, color=BLUE)
        line2 = Line(RIGHT + UP, RIGHT * 3 + UP * 2, color=GREEN)

        # Find intersection (lines extended infinitely)
        intersection_dot = intersect_lines(line1, line2)
        intersection_dot.set_color(RED).scale(1.5)

        # Create dashed extension lines to show the concept
        extension1 = DashedLine(
            line1.get_end(),
            intersection_dot.get_center(),
            color=BLUE,
            dash_length=0.1
        )
        extension2 = DashedLine(
            line2.get_start(),
            intersection_dot.get_center(),
            color=GREEN,
            dash_length=0.1
        )

        title = Text("Extended Line Intersection", font_size=28).to_edge(UP)
        subtitle = Text("(Lines treated as infinite)", font_size=18, color=YELLOW).next_to(title, DOWN)

        # Animate
        self.add(title, subtitle)
        self.play(Create(line1))
        self.play(Create(line2))
        self.wait(1)
        self.play(Create(extension1), Create(extension2))
        self.wait(0.5)
        self.play(FadeIn(intersection_dot, scale=0.3))
        self.wait(2)


class DynamicIntersectionDemo(Scene):
    """Demonstrate dynamic intersection with rotating line."""

    def construct(self):
        # Fixed horizontal line
        fixed_line = Line(LEFT * 3, RIGHT * 3, color=BLUE)

        # Rotating line
        rotating_line = Line(DOWN * 2, UP * 2, color=GREEN)

        # Dynamic intersection point using always_redraw
        intersection_dot = always_redraw(
            lambda: intersect_lines(fixed_line, rotating_line).set_color(RED).scale(1.5)
        )

        # Labels
        title = Text("Dynamic Intersection", font_size=28).to_edge(UP)
        fixed_label = Text("Fixed", font_size=20, color=BLUE).next_to(fixed_line, DOWN)
        rotating_label = Text("Rotating", font_size=20, color=GREEN).next_to(rotating_line, RIGHT, buff=0.3)

        # Animate
        self.add(title)
        self.play(Create(fixed_line), Write(fixed_label))
        self.play(Create(rotating_line), Write(rotating_label))
        self.add(intersection_dot)
        self.wait(1)

        # Rotate the line - intersection point follows!
        self.play(
            Rotate(rotating_line, angle=PI/3, about_point=ORIGIN),
            run_time=3
        )
        self.wait(1)

        # Rotate more
        self.play(
            Rotate(rotating_line, angle=PI/3, about_point=ORIGIN),
            run_time=3
        )
        self.wait(2)


class MultipleIntersectionsDemo(Scene):
    """Demonstrate multiple line intersections."""

    def construct(self):
        # Create a central line
        center_line = Line(LEFT * 3, RIGHT * 3, color=BLUE)

        # Create multiple lines intersecting the center line
        angles = [PI/6, PI/4, PI/3, 2*PI/3, 3*PI/4, 5*PI/6]
        colors = [RED, YELLOW, GREEN, ORANGE, PURPLE, PINK]

        intersecting_lines = []
        intersection_dots = []

        for angle, color in zip(angles, colors):
            # Create a line rotated by the angle
            line = Line(DOWN * 2, UP * 2, color=color)
            line.rotate(angle, about_point=ORIGIN)
            intersecting_lines.append(line)

            # Find intersection with center line
            dot = intersect_lines(center_line, line)
            dot.set_color(color).scale(0.8)
            intersection_dots.append(dot)

        title = Text("Multiple Intersections", font_size=28).to_edge(UP)

        # Animate
        self.add(title)
        self.play(Create(center_line))
        self.wait(0.5)

        # Add lines and dots one by one
        for line, dot in zip(intersecting_lines, intersection_dots):
            self.play(Create(line), FadeIn(dot, scale=0.3), run_time=0.5)

        self.wait(2)


class TriangleIntersectionDemo(Scene):
    """Demonstrate finding the orthocenter of a triangle using intersect_lines."""

    def construct(self):
        from robo_manim_add_ons import perp

        # Create a triangle
        triangle = Polygon(
            [-2, -1.5, 0],
            [2, -1.5, 0],
            [0, 2, 0],
            color=BLUE
        )

        vertices = triangle.get_vertices()

        # Create perpendicular lines from each vertex to opposite side
        # Perpendicular from vertex A to side BC
        side_bc = Line(vertices[1], vertices[2])
        perp1 = perp(side_bc, Dot(vertices[0]), length=5, placement="start").set_color(RED)

        # Perpendicular from vertex B to side AC
        side_ac = Line(vertices[0], vertices[2])
        perp2 = perp(side_ac, Dot(vertices[1]), length=5, placement="start").set_color(GREEN)

        # Find orthocenter (intersection of perpendiculars)
        orthocenter = intersect_lines(perp1, perp2)
        orthocenter.set_color(YELLOW).scale(2)

        title = Text("Triangle Orthocenter", font_size=28).to_edge(UP)
        subtitle = Text("(Intersection of altitudes)", font_size=18, color=YELLOW).next_to(title, DOWN)

        # Animate
        self.add(title, subtitle)
        self.play(Create(triangle))
        self.wait(1)
        self.play(Create(perp1))
        self.play(Create(perp2))
        self.wait(1)
        self.play(FadeIn(orthocenter, scale=0.3))
        self.wait(2)


class ConditionalIntersectionDemo(Scene):
    """Demonstrate checking if intersection exists."""

    def construct(self):
        # Start with intersecting lines
        line1 = Line(LEFT * 2, RIGHT * 2, color=BLUE)
        line2 = Line(DOWN * 2 + LEFT, UP * 2 + RIGHT, color=GREEN)

        # Function to check and display intersection
        def show_intersection_status():
            result = intersect_lines(line1, line2)

            if isinstance(result, Dot):
                # Lines intersect
                result.set_color(RED).scale(1.5)
                status = Text("Lines Intersect!", font_size=24, color=GREEN)
                return VGroup(result, status.to_edge(DOWN))
            else:
                # Lines are parallel
                status = Text("Lines are Parallel!", font_size=24, color=RED)
                return status.to_edge(DOWN)

        intersection_group = always_redraw(show_intersection_status)

        title = Text("Conditional Intersection Check", font_size=28).to_edge(UP)

        # Animate
        self.add(title)
        self.play(Create(line1), Create(line2))
        self.add(intersection_group)
        self.wait(2)

        # Rotate line2 to make it parallel to line1
        self.play(
            Rotate(line2, angle=-PI/4, about_point=line2.get_center()),
            run_time=3
        )
        self.wait(2)

        # Rotate back to intersecting
        self.play(
            Rotate(line2, angle=PI/4, about_point=line2.get_center()),
            run_time=3
        )
        self.wait(2)


# Line-Circle Intersection Demos
class BasicLineCircleIntersection(Scene):
    """Demonstrate basic line-circle intersection."""

    def construct(self):
        # Create circle
        circle = Circle(radius=2, color=BLUE)

        # Create line through center
        line = Line(LEFT * 3, RIGHT * 3, color=GREEN)

        # Find intersections
        intersections = intersect_line_circle(line, circle)
        for dot in intersections:
            dot.set_color(RED).scale(1.5)

        # Labels
        title = Text("Line-Circle Intersection", font_size=28).to_edge(UP)
        circle_label = Text("Circle", font_size=20, color=BLUE).next_to(circle, DOWN, buff=0.5)
        line_label = Text("Line", font_size=20, color=GREEN).next_to(line, UP, buff=0.3)

        # Animate
        self.add(title)
        self.play(Create(circle), Write(circle_label))
        self.play(Create(line), Write(line_label))
        self.wait(1)
        self.play(FadeIn(intersections, scale=0.3))
        self.wait(2)


class TangentLineDemo(Scene):
    """Demonstrate tangent line to circle (one intersection)."""

    def construct(self):
        # Create circle
        circle = Circle(radius=2, color=BLUE)

        # Create tangent line at top
        line = Line(LEFT * 3 + UP * 2, RIGHT * 3 + UP * 2, color=GREEN)

        # Find intersection (should be one point)
        intersections = intersect_line_circle(line, circle)
        for dot in intersections:
            dot.set_color(YELLOW).scale(2)

        # Labels
        title = Text("Tangent Line", font_size=28).to_edge(UP)
        subtitle = Text(f"({len(intersections)} intersection point)", font_size=18, color=YELLOW)
        subtitle.next_to(title, DOWN)

        # Animate
        self.add(title, subtitle)
        self.play(Create(circle))
        self.play(Create(line))
        self.wait(1)
        self.play(FadeIn(intersections, scale=0.5))
        self.wait(2)


class NoIntersectionDemo(Scene):
    """Demonstrate line missing circle (no intersection)."""

    def construct(self):
        # Create circle
        circle = Circle(radius=1.5, color=BLUE)

        # Create line that misses the circle
        line = Line(LEFT * 3 + UP * 3, RIGHT * 3 + UP * 3, color=GREEN)

        # Find intersections (should be empty)
        intersections = intersect_line_circle(line, circle)

        # Labels
        title = Text("No Intersection", font_size=28).to_edge(UP)
        message = Text("Line misses the circle", font_size=20, color=RED).to_edge(DOWN)

        # Animate
        self.add(title)
        self.play(Create(circle))
        self.play(Create(line))
        self.wait(1)

        if len(intersections) == 0:
            self.play(Write(message))

        self.wait(2)


class DynamicLineCircleIntersection(Scene):
    """Demonstrate dynamic line-circle intersection with rotating line."""

    def construct(self):
        # Create circle
        circle = Circle(radius=2, color=BLUE)

        # Create rotating line
        line = Line(LEFT * 3, RIGHT * 3, color=GREEN)

        # Dynamic intersections using always_redraw
        intersections = always_redraw(
            lambda: VGroup(*[
                dot.set_color(RED).scale(1.5)
                for dot in intersect_line_circle(line, circle)
            ])
        )

        title = Text("Dynamic Line-Circle Intersection", font_size=24).to_edge(UP)

        # Animate
        self.add(title)
        self.play(Create(circle))
        self.play(Create(line))
        self.add(intersections)
        self.wait(1)

        # Rotate line - intersections follow!
        self.play(
            Rotate(line, angle=PI/4, about_point=ORIGIN),
            run_time=3
        )
        self.wait(1)

        # Continue rotating
        self.play(
            Rotate(line, angle=PI/4, about_point=ORIGIN),
            run_time=3
        )
        self.wait(2)


class MultipleCirclesIntersection(Scene):
    """Demonstrate line intersecting multiple circles."""

    def construct(self):
        # Create vertical line
        line = Line(DOWN * 3, UP * 3, color=GREEN)

        # Create multiple circles of different sizes
        circles = [
            Circle(radius=0.8, color=BLUE).shift(LEFT * 2),
            Circle(radius=1.2, color=PURPLE),
            Circle(radius=1.0, color=RED).shift(RIGHT * 2),
        ]

        # Find all intersections
        all_intersections = VGroup()
        for circle in circles:
            intersections = intersect_line_circle(line, circle)
            for dot in intersections:
                dot.set_color(YELLOW).scale(0.8)
            all_intersections.add(intersections)

        title = Text("Line Intersecting Multiple Circles", font_size=24).to_edge(UP)

        # Animate
        self.add(title)
        self.play(Create(line))
        self.play(*[Create(circle) for circle in circles])
        self.wait(1)
        self.play(FadeIn(all_intersections, scale=0.3))
        self.wait(2)


class ChordLengthDemo(Scene):
    """Demonstrate measuring chord length from intersections."""

    def construct(self):
        # Create circle
        circle = Circle(radius=2, color=BLUE)

        # Create line creating a chord
        line = Line(LEFT * 3 + UP * 1, RIGHT * 3 + UP * 1, color=GREEN)

        # Find intersections
        intersections = intersect_line_circle(line, circle)

        if len(intersections) == 2:
            # Create chord line segment
            p1 = intersections[0].get_center()
            p2 = intersections[1].get_center()
            chord = Line(p1, p2, color=YELLOW, stroke_width=8)

            # Calculate chord length
            chord_length = np.linalg.norm(p2 - p1)

            # Style dots
            for dot in intersections:
                dot.set_color(RED).scale(1.5)

            # Label
            title = Text("Chord Length Measurement", font_size=28).to_edge(UP)
            length_label = Text(f"Chord length: {chord_length:.2f}", font_size=20, color=YELLOW)
            length_label.to_edge(DOWN)

            # Animate
            self.add(title)
            self.play(Create(circle))
            self.play(Create(line))
            self.wait(1)
            self.play(FadeIn(intersections, scale=0.3))
            self.wait(1)
            self.play(Create(chord))
            self.play(Write(length_label))
            self.wait(2)


class DiameterDemo(Scene):
    """Demonstrate that diameter is the longest chord."""

    def construct(self):
        # Create circle
        circle = Circle(radius=2, color=BLUE)

        # Create horizontal line through center (creates diameter)
        diameter_line = Line(LEFT * 3, RIGHT * 3, color=GREEN)

        # Create another line creating a shorter chord
        chord_line = Line(LEFT * 3 + UP * 1.5, RIGHT * 3 + UP * 1.5, color=ORANGE)

        # Find intersections
        diameter_intersections = intersect_line_circle(diameter_line, circle)
        chord_intersections = intersect_line_circle(chord_line, circle)

        # Calculate lengths
        if len(diameter_intersections) == 2:
            p1, p2 = [d.get_center() for d in diameter_intersections]
            diameter_length = np.linalg.norm(p2 - p1)
            diameter = Line(p1, p2, color=YELLOW, stroke_width=8)
            diameter_label = Text(f"Diameter: {diameter_length:.2f}", font_size=18, color=YELLOW)
            diameter_label.next_to(diameter, DOWN, buff=0.3)

        if len(chord_intersections) == 2:
            p3, p4 = [d.get_center() for d in chord_intersections]
            chord_length = np.linalg.norm(p4 - p3)
            chord = Line(p3, p4, color=ORANGE, stroke_width=8)
            chord_label = Text(f"Chord: {chord_length:.2f}", font_size=18, color=ORANGE)
            chord_label.next_to(chord, UP, buff=0.3)

        for dot in diameter_intersections:
            dot.set_color(YELLOW).scale(1.2)
        for dot in chord_intersections:
            dot.set_color(ORANGE).scale(1.2)

        title = Text("Diameter vs Chord", font_size=28).to_edge(UP)

        # Animate
        self.add(title)
        self.play(Create(circle))
        self.wait(1)

        # Show diameter
        self.play(Create(diameter_line))
        self.play(FadeIn(diameter_intersections, scale=0.3))
        self.play(Create(diameter), Write(diameter_label))
        self.wait(1)

        # Show chord
        self.play(Create(chord_line))
        self.play(FadeIn(chord_intersections, scale=0.3))
        self.play(Create(chord), Write(chord_label))
        self.wait(2)
