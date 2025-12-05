"""
Demo showing trigonometric graphs with automatic π tick detection.

The graph() function automatically detects trig functions and adds π-based ticks.
"""

from manim import *
from robo_manim_add_ons import graph, style

# Set white background for all scenes
config.background_color = WHITE


class AutoPiTicksDemo(Scene):
    """Demo showing automatic π tick detection for trig functions."""

    def construct(self):
        # Auto-detects sin(x) → π ticks on x-axis
        axes, plot = graph("sin(x)", x_range=[0, 2*PI], y_range=[-1.5, 1.5])

        # Use defaults (BLACK axes, BLUE_D plot)

        # Add title
        title = Text("Automatic π ticks: y = sin(x)", font_size=28, color=BLACK).to_edge(UP)

        self.add(axes, plot, title)


class InverseTrigDemo(Scene):
    """Demo showing automatic π tick detection for inverse trig functions."""

    def construct(self):
        # Auto-detects asin(x) → π ticks on y-axis
        axes, plot = graph("asin(x)", x_range=[-1, 1], y_range=[-PI, PI])

        # Use defaults (BLACK axes, BLUE_D plot)

        # Add title
        title = MathTex(r"y = \arcsin(x)", font_size=36, color=BLACK).to_edge(UP)

        self.add(axes, plot, title)


class ManualPiTicksDemo(Scene):
    """Demo showing manual control over π tick spacing."""

    def construct(self):
        # Use finer π/2 ticks
        axes, plot = graph("cos(x)", x_range=[0, 4*PI], y_range=[-1.5, 1.5], x_ticks="pi/2")

        # Customize plot color
        style(plot).stroke(GREEN).sw(3)

        # Add title
        title = Text("Manual π/2 ticks: y = cos(x)", font_size=28, color=BLACK).to_edge(UP)

        self.add(axes, plot, title)


class DisablePiTicksDemo(Scene):
    """Demo showing how to disable automatic π ticks."""

    def construct(self):
        # Disable π ticks even for trig function
        # When π ticks are disabled, regular coordinates are added automatically
        axes, plot = graph("tan(x)", x_range=[-PI, PI], y_range=[-3, 3], x_ticks=False)

        # Customize plot
        style(plot).stroke(RED).sw(3)

        # Add title
        title = Text("Disabled π ticks: y = tan(x)", font_size=28, color=BLACK).to_edge(UP)

        self.add(axes, plot, title)


class BothAxesPiDemo(Scene):
    """Demo showing π ticks on both axes."""

    def construct(self):
        # sin(asin(x)) has both forward and inverse trig
        # Auto-detects π ticks on both axes
        axes, plot = graph("sin(asin(x))", x_range=[-1, 1], y_range=[-1, 1])

        # Manually force π ticks on both for demo clarity
        axes, plot = graph("x", x_range=[-PI, PI], y_range=[-PI, PI],
                          x_ticks="pi", y_ticks="pi")

        # Customize plot color
        style(plot).stroke(PURPLE).sw(3)

        # Add title
        title = Text("π ticks on both axes: y = x", font_size=28, color=BLACK).to_edge(UP)

        self.add(axes, plot, title)


class MultipleTrigGraphsDemo(Scene):
    """Demo showing multiple trig graphs on same axes."""

    def construct(self):
        # Create first graph
        axes, plot1 = graph("sin(x)", x_range=[0, 2*PI], y_range=[-1.5, 1.5])

        # Plot second and third on same axes
        _, plot2 = graph("cos(x)", axes=axes)
        _, plot3 = graph("sin(2*x)", axes=axes)

        # Customize plot colors
        style(plot1).stroke(RED).sw(3)
        style(plot2).stroke(BLUE).sw(3)
        style(plot3).stroke(GREEN_D).sw(3)

        # Labels
        labels = VGroup(
            Text("sin(x)", color=RED, font_size=20),
            Text("cos(x)", color=BLUE, font_size=20),
            Text("sin(2x)", color=GREEN_D, font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UR)

        self.add(axes, plot1, plot2, plot3, labels)


class CoarsePiTicksDemo(Scene):
    """Demo showing coarse 2π ticks."""

    def construct(self):
        # Use only 2π multiples
        axes, plot = graph("sin(x)", x_range=[0, 6*PI], y_range=[-1.5, 1.5], x_ticks="2pi")

        # Customize plot color
        style(plot).stroke(ORANGE).sw(3)

        # Add title
        title = Text("Coarse 2π ticks: y = sin(x)", font_size=28, color=BLACK).to_edge(UP)

        self.add(axes, plot, title)


class AtanDemo(Scene):
    """Demo showing arctan with automatic π ticks on y-axis."""

    def construct(self):
        # Auto-detects atan → π ticks on y-axis
        axes, plot = graph("atan(x)", x_range=[-5, 5], y_range=[-PI, PI])

        # Customize plot color
        style(plot).stroke(TEAL).sw(3)

        # Add title
        title = MathTex(r"y = \arctan(x)", font_size=36, color=BLACK).to_edge(UP)

        # Add asymptote lines
        asymptote_top = DashedLine(
            axes.c2p(-5, PI/2), axes.c2p(5, PI/2),
            color=LIGHT_GRAY, stroke_width=2
        )
        asymptote_bottom = DashedLine(
            axes.c2p(-5, -PI/2), axes.c2p(5, -PI/2),
            color=LIGHT_GRAY, stroke_width=2
        )

        self.add(asymptote_top, asymptote_bottom, axes, plot, title)
