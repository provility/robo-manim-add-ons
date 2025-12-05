"""
Demo showing how to use the graph() function and style the results.

The graph() function returns (axes, plot) as a tuple, which you can
style before adding to the scene using chainable style methods.
"""

from manim import *
from robo_manim_add_ons import graph, style

# Set white background for all scenes
config.background_color = WHITE


class ExplicitPlotDemo(Scene):
    """Demo of explicit plot y = f(x) with custom styling."""

    def construct(self):
        # Create a graph of sin(x)
        # Coordinates are added automatically (coords=True by default)
        axes, plot = graph("sin(x)", x_range=[-4, 4], y_range=[-2, 2])

        # Add axis labels
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")

        # Add to scene
        self.add(axes, plot, x_label, y_label)


class ImplicitPlotDemo(Scene):
    """Demo of implicit plot (equation) with custom styling."""

    def construct(self):
        # Create a circle using implicit equation
        # Coordinates added automatically
        axes, plot = graph("x**2 + y**2 = 4", x_range=[-3, 3], y_range=[-3, 3])

        # Add title
        title = Text("Circle: x² + y² = 4", font_size=24, color=BLACK).to_edge(UP)

        # Add to scene
        self.add(axes, plot, title)


class ParametricPlotDemo(Scene):
    """Demo of parametric plot with custom styling."""

    def construct(self):
        # Create a parametric circle
        # Coordinates added automatically
        axes, plot = graph("cos(t)", "sin(t)", x_range=[-2, 2], y_range=[-2, 2])

        # Customize plot color
        style(plot).stroke(GREEN).sw(3)

        # Add labels
        labels = VGroup(
            axes.get_x_axis_label("x"),
            axes.get_y_axis_label("y")
        )

        # Add to scene
        self.add(axes, plot, labels)


class MultipleGraphsDemo(Scene):
    """Demo showing multiple graphs on the same axes using the axes parameter."""

    def construct(self):
        # Create first graph (sin)
        axes, plot1 = graph("sin(x)", x_range=[-4, 4], y_range=[-2, 2])

        # Create second graph (cos) using the SAME axes
        _, plot2 = graph("cos(x)", axes=axes)

        # Style plots with different colors
        style(plot1).stroke(RED).sw(3)
        style(plot2).stroke(BLUE).sw(3)

        # Create labels
        label_sin = Text("sin(x)", color=RED, font_size=24).to_corner(UR)
        label_cos = Text("cos(x)", color=BLUE, font_size=24).next_to(label_sin, DOWN)

        # Add to scene - use shared axes and both plots
        self.add(axes, plot1, plot2, label_sin, label_cos)


class StyledAxesDemo(Scene):
    """Demo showing various axes styling options."""

    def construct(self):
        # Create a parabola
        axes, plot = graph("x**2", x_range=[-3, 3], y_range=[0, 10])

        # Axes default to BLACK
        # Add coordinates with custom decimal places
        axes.add_coordinates(
            dict(
                [(x, MathTex(f"{x}", color=BLACK)) for x in range(-3, 4)]
            ),
            dict(
                [(y, MathTex(f"{y}", color=BLACK)) for y in range(0, 11, 2)]
            )
        )

        # Style the plot with custom color
        style(plot).stroke(ORANGE).sw(4)

        # Add axis labels with LaTeX
        x_label = axes.get_x_axis_label(MathTex("x", color=BLACK))
        y_label = axes.get_y_axis_label(MathTex("f(x) = x^2", color=BLACK))

        # Add title
        title = Text("Parabola with Styled Axes", font_size=28, color=BLACK).to_edge(UP)

        self.add(axes, plot, x_label, y_label, title)


class AnimatedGraphDemo(Scene):
    """Demo showing how to animate the graph creation."""

    def construct(self):
        # Create graph
        axes, plot = graph("sin(x)", x_range=[-4, 4], y_range=[-2, 2])

        # Axes default to BLACK, customize plot
        style(plot).stroke(ORANGE).sw(3)

        # Add labels
        x_label = axes.get_x_axis_label(MathTex("x", color=BLACK))
        y_label = axes.get_y_axis_label(MathTex("y", color=BLACK))
        title = Text("y = sin(x)", font_size=32, color=BLACK).to_edge(UP)

        # Animate
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Write(title))
        self.play(Create(plot), run_time=2)
        self.wait()


class ComplexExpressionDemo(Scene):
    """Demo with more complex mathematical expressions."""

    def construct(self):
        # Create a more complex function
        # Coordinates added automatically
        axes, plot = graph("sin(x) * exp(-x/5)", x_range=[0, 10], y_range=[-1, 1])

        # Customize plot
        style(plot).stroke(PURPLE).sw(3)

        # Add labels
        title = MathTex(r"f(x) = \sin(x) \cdot e^{-x/5}", font_size=36, color=BLACK).to_edge(UP)
        x_label = axes.get_x_axis_label(MathTex("x", color=BLACK))
        y_label = axes.get_y_axis_label(MathTex("f(x)", color=BLACK))

        self.add(axes, plot, title, x_label, y_label)


class CustomRangeDemo(Scene):
    """Demo showing different axis ranges."""

    def construct(self):
        # Create graph with custom ranges
        # Coordinates added automatically
        axes, plot = graph("x**3", x_range=[-2, 2], y_range=[-10, 10])

        # Customize plot
        style(plot).stroke(RED).sw(3)

        # Add zero line highlighting
        zero_line_x = DashedLine(
            axes.c2p(-2, 0), axes.c2p(2, 0), color=LIGHT_GRAY, stroke_width=1
        )
        zero_line_y = DashedLine(
            axes.c2p(0, -10), axes.c2p(0, 10), color=LIGHT_GRAY, stroke_width=1
        )

        # Labels
        title = MathTex(r"f(x) = x^3", font_size=36, color=BLACK).to_edge(UP)

        self.add(zero_line_x, zero_line_y, axes, plot, title)


class EllipseImplicitDemo(Scene):
    """Demo of an ellipse using implicit function."""

    def construct(self):
        # Create ellipse: x²/4 + y²/1 = 1
        # Coordinates added automatically
        axes, plot = graph("x**2/4 + y**2 = 1", x_range=[-3, 3], y_range=[-2, 2])

        # Customize plot
        style(plot).stroke(TEAL).sw(4)

        # Add labels
        title = MathTex(r"\frac{x^2}{4} + y^2 = 1", font_size=36, color=BLACK).to_edge(UP)

        # Mark foci (for ellipse with a=2, b=1, c=sqrt(3))
        import numpy as np
        c = np.sqrt(3)
        focus1 = Dot(axes.c2p(-c, 0), color=RED)
        focus2 = Dot(axes.c2p(c, 0), color=RED)
        focus_label = Text("Foci", font_size=20, color=RED).next_to(focus2, RIGHT)

        self.add(axes, plot, title, focus1, focus2, focus_label)
