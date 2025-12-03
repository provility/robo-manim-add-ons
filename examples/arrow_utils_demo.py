"""
Demo showcasing ArrowUtil capabilities:
- Basic arrows
- Dashed arrows
- Perpendicular buffer
- Bidirectional arrows
- Curved arrows
- Label positioning
- Markers
"""

from manim import *
from robo_manim_add_ons.arrow_utils import ArrowUtil


class BasicArrowDemo(Scene):
    """Demonstrate basic arrow creation."""
    def construct(self):
        # Title
        title = Text("Basic Arrow", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Basic arrow
        arrow = ArrowUtil.arrow(LEFT * 2, RIGHT * 2, color=BLUE)
        self.play(Create(arrow))
        self.wait()


class DashedArrowDemo(Scene):
    """Demonstrate dashed arrow."""
    def construct(self):
        # Title
        title = Text("Dashed Arrow", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Dashed arrow
        arrow = ArrowUtil.arrow(LEFT * 2, RIGHT * 2, dashed=True, color=RED)
        self.play(Create(arrow))
        self.wait()


class PerpendicularBufferDemo(Scene):
    """Demonstrate perpendicular buffer offset."""
    def construct(self):
        # Title
        title = Text("Perpendicular Buffer", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Reference line
        ref_line = Line(LEFT * 3, RIGHT * 3, color=GRAY, stroke_opacity=0.5)
        self.add(ref_line)

        # Arrow with positive buffer (upward)
        arrow1 = ArrowUtil.arrow(LEFT * 2.5, RIGHT * 2.5, buff=0.5, color=BLUE)
        label1 = Text("buff=0.5", font_size=24, color=BLUE).next_to(arrow1, UP)

        # Arrow with negative buffer (downward)
        arrow2 = ArrowUtil.arrow(LEFT * 2.5, RIGHT * 2.5, buff=-0.5, color=RED)
        label2 = Text("buff=-0.5", font_size=24, color=RED).next_to(arrow2, DOWN)

        self.play(Create(arrow1), Write(label1))
        self.wait()
        self.play(Create(arrow2), Write(label2))
        self.wait()


class BidirectionalArrowDemo(Scene):
    """Demonstrate bidirectional arrows."""
    def construct(self):
        # Title
        title = Text("Bidirectional Arrow", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Bidirectional arrow
        arrow = ArrowUtil.arrow(
            LEFT * 2, RIGHT * 2,
            bidirectional=True,
            color=GREEN
        )
        self.play(Create(arrow))
        self.wait()


class CurvedArrowDemo(Scene):
    """Demonstrate curved arrows with different angles."""
    def construct(self):
        # Title
        title = Text("Curved Arrows", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Start and end points
        start = LEFT * 2 + DOWN
        end = RIGHT * 2 + DOWN

        # Dots at start and end
        dot_start = Dot(start, color=YELLOW)
        dot_end = Dot(end, color=YELLOW)
        self.add(dot_start, dot_end)

        # Curved arrow with 30 degrees
        arrow1 = ArrowUtil.curved_arrow(
            start, end,
            angle=30 * DEGREES,
            color=BLUE
        )
        label1 = Text("30°", font_size=24, color=BLUE).move_to(UP * 0.5)

        # Curved arrow with 60 degrees
        arrow2 = ArrowUtil.curved_arrow(
            start, end,
            angle=60 * DEGREES,
            color=RED
        )
        label2 = Text("60°", font_size=24, color=RED).move_to(UP * 1.5)

        # Curved arrow with 90 degrees
        arrow3 = ArrowUtil.curved_arrow(
            start, end,
            angle=90 * DEGREES,
            color=GREEN
        )
        label3 = Text("90°", font_size=24, color=GREEN).move_to(UP * 2.5)

        self.play(Create(arrow1), Write(label1))
        self.wait()
        self.play(Create(arrow2), Write(label2))
        self.wait()
        self.play(Create(arrow3), Write(label3))
        self.wait()


class LabelPositioningDemo(Scene):
    """Demonstrate automatic label positioning."""
    def construct(self):
        # Title
        title = Text("Label Positioning", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Horizontal arrow with label
        arrow1 = ArrowUtil.arrow(LEFT * 2 + UP, RIGHT * 2 + UP, buff=0.2, color=BLUE)
        label1 = ArrowUtil.label(arrow1, MathTex("L_1"), buff=0.3)

        # Diagonal arrow with label
        arrow2 = ArrowUtil.arrow(LEFT * 2 + DOWN, RIGHT * 1 + DOWN * 2, buff=0.2, color=RED)
        label2 = ArrowUtil.label(arrow2, MathTex("L_2"), buff=0.3)

        self.play(Create(arrow1), Write(label1))
        self.wait()
        self.play(Create(arrow2), Write(label2))
        self.wait()


class MarkerDemo(Scene):
    """Demonstrate directional markers."""
    def construct(self):
        # Title
        title = Text("Directional Markers", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Create a circle
        circle = Circle(radius=2, color=GRAY, stroke_opacity=0.5)
        self.add(circle)

        # Add markers at different positions around the circle
        markers = VGroup()
        for i in range(8):
            proportion = i / 8
            point = circle.point_from_proportion(proportion)
            # Tangent direction
            next_point = circle.point_from_proportion((proportion + 0.01) % 1)
            direction = next_point - point

            marker = ArrowUtil.marker(
                point, direction,
                tip_length=0.4,
                color=BLUE
            )
            markers.add(marker)

        self.play(Create(markers))
        self.wait()


class CombinedFeaturesDemo(Scene):
    """Demonstrate combining multiple features."""
    def construct(self):
        # Title
        title = Text("Combined Features", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Square with labeled sides
        square = Square(side_length=3, color=GRAY, stroke_opacity=0.3)
        v1, v2, v3, v4 = square.get_vertices()

        # Top side - dashed with label
        arrow_top = ArrowUtil.arrow(
            v1, v2,
            dashed=True,
            buff=-0.3,
            color=BLUE
        )
        label_top = ArrowUtil.label(arrow_top, MathTex("a"), buff=-0.3)

        # Right side - solid bidirectional
        arrow_right = ArrowUtil.arrow(
            v2, v3,
            bidirectional=True,
            buff=-0.3,
            color=RED
        )
        label_right = ArrowUtil.label(arrow_right, MathTex("b"), buff=-0.3)

        # Bottom side - dashed with label
        arrow_bottom = ArrowUtil.arrow(
            v3, v4,
            dashed=True,
            buff=-0.3,
            color=BLUE
        )
        label_bottom = ArrowUtil.label(arrow_bottom, MathTex("a"), buff=-0.3)

        # Left side - solid bidirectional
        arrow_left = ArrowUtil.arrow(
            v4, v1,
            bidirectional=True,
            buff=-0.3,
            color=RED
        )
        label_left = ArrowUtil.label(arrow_left, MathTex("b"), buff=-0.3)

        self.add(square)
        self.play(
            Create(arrow_top), Write(label_top),
            Create(arrow_right), Write(label_right),
            Create(arrow_bottom), Write(label_bottom),
            Create(arrow_left), Write(label_left)
        )
        self.wait()


class AllFeaturesShowcase(Scene):
    """Comprehensive showcase of all ArrowUtil features."""
    def construct(self):
        # Title
        title = Text("ArrowUtil Features", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait()

        # Section 1: Basic and Dashed
        subtitle1 = Text("Basic & Dashed", font_size=28).to_edge(UP).shift(DOWN * 0.7)
        arrow1 = ArrowUtil.arrow(LEFT * 3 + UP * 2, LEFT + UP * 2, color=BLUE)
        arrow2 = ArrowUtil.arrow(RIGHT + UP * 2, RIGHT * 3 + UP * 2, dashed=True, color=RED)

        self.play(Transform(title, subtitle1))
        self.play(Create(arrow1), Create(arrow2))
        self.wait()

        # Section 2: Perpendicular Buffer
        subtitle2 = Text("Perpendicular Offset", font_size=28).to_edge(UP).shift(DOWN * 0.7)
        self.play(
            Transform(title, subtitle2),
            FadeOut(arrow1), FadeOut(arrow2)
        )

        ref_line = Line(LEFT * 3, RIGHT * 3, color=GRAY, stroke_opacity=0.3)
        arrow3 = ArrowUtil.arrow(LEFT * 2.5, RIGHT * 2.5, buff=0.5, color=GREEN)
        arrow4 = ArrowUtil.arrow(LEFT * 2.5, RIGHT * 2.5, buff=-0.5, color=ORANGE)

        self.play(Create(ref_line))
        self.play(Create(arrow3), Create(arrow4))
        self.wait()

        # Section 3: Curved Arrows
        subtitle3 = Text("Curved Arrows", font_size=28).to_edge(UP).shift(DOWN * 0.7)
        self.play(
            Transform(title, subtitle3),
            FadeOut(ref_line), FadeOut(arrow3), FadeOut(arrow4)
        )

        start_pt = LEFT * 2
        end_pt = RIGHT * 2
        Dot(start_pt, color=YELLOW).add(Dot(end_pt, color=YELLOW))

        curved1 = ArrowUtil.curved_arrow(start_pt, end_pt, angle=45 * DEGREES, color=PURPLE)
        curved2 = ArrowUtil.curved_arrow(start_pt, end_pt, angle=90 * DEGREES, color=PINK)

        self.play(Create(curved1))
        self.play(Create(curved2))
        self.wait(2)


if __name__ == "__main__":
    # Run with: manim -pql arrow_utils_demo.py AllFeaturesShowcase
    pass
