from manim import *
from robo_manim_add_ons import (
    x, y, st, ed, mid, mag, uv, vec, ang, slope, val,
    pt, m2v, v2m, x2v, vl, hl, lra, vra, r2p
)


class XDemo(Scene):
    """Extract x-coordinate from objects"""
    def construct(self):
        dot = Dot(pt(2, 1))
        x_val = x(dot)

        dot_label = Text(f"x = {x_val}", font_size=24).next_to(dot, UP)

        self.add(dot, dot_label)
        self.wait()


class YDemo(Scene):
    """Extract y-coordinate from objects"""
    def construct(self):
        dot = Dot(pt(1, 2))
        y_val = y(dot)

        dot_label = Text(f"y = {y_val}", font_size=24).next_to(dot, UP)

        self.add(dot, dot_label)
        self.wait()


class StDemo(Scene):
    """Get start point of a line"""
    def construct(self):
        line = Line(pt(-2, -1), pt(2, 1))
        start_point = st(line)
        start_dot = Dot(start_point, color=GREEN)

        label = Text("Start", font_size=24, color=GREEN).next_to(start_dot, DOWN)

        self.add(line, start_dot, label)
        self.wait()


class EdDemo(Scene):
    """Get end point of a line"""
    def construct(self):
        line = Line(pt(-2, -1), pt(2, 1))
        end_point = ed(line)
        end_dot = Dot(end_point, color=RED)

        label = Text("End", font_size=24, color=RED).next_to(end_dot, UP)

        self.add(line, end_dot, label)
        self.wait()


class MidDemo(Scene):
    """Get center point of an object"""
    def construct(self):
        line = Line(pt(-2, -1), pt(2, 1))
        center_dot = mid(line)
        center_dot.set_color(YELLOW)

        label = Text("Mid", font_size=24, color=YELLOW).next_to(center_dot, DOWN)

        self.add(line, center_dot, label)
        self.wait()


class MagDemo(Scene):
    """Get magnitude/length"""
    def construct(self):
        line = Line(pt(-2, 0), pt(2, 0))
        length = mag(line)

        label = Text(f"Length = {length:.1f}", font_size=24).next_to(line, DOWN)

        self.add(line, label)
        self.wait()


class UvDemo(Scene):
    """Get unit vector"""
    def construct(self):
        line = Line(ORIGIN, pt(3, 3))
        unit = uv(line)
        unit_arrow = Arrow(ORIGIN, unit * 1.5, buff=0, color=YELLOW)

        label = Text("Unit Vector", font_size=24, color=YELLOW).next_to(unit_arrow, UR)

        self.add(line, unit_arrow, label)
        self.wait()


class VecDemo(Scene):
    """Get vector from line"""
    def construct(self):
        line = Line(pt(-1, -1), pt(2, 1))
        vector = vec(line)
        arrow = Arrow(ORIGIN, vector, buff=0, color=BLUE)

        label = Text("Vector", font_size=24, color=BLUE).next_to(arrow, UP)

        self.add(line, arrow, label)
        self.wait()


class AngDemo(Scene):
    """Get angle of line"""
    def construct(self):
        line = Line(ORIGIN, pt(2, 2))
        angle_rad = ang(line)
        angle_deg = np.degrees(angle_rad)

        arc = Arc(radius=0.5, start_angle=0, angle=angle_rad, color=YELLOW)
        label = Text(f"{angle_deg:.0f}°", font_size=24).move_to(pt(1, -0.5))

        self.add(line, arc, label)
        self.wait()


class SlopeDemo(Scene):
    """Get slope of line"""
    def construct(self):
        line = Line(pt(-2, -1), pt(2, 1))
        slp = slope(line)

        label = Text(f"slope = {slp:.2f}", font_size=24).next_to(line, DOWN)

        self.add(line, label)
        self.wait()


class ValDemo(Scene):
    """Get value from ValueTracker"""
    def construct(self):
        tracker = ValueTracker(3.14)
        value = val(tracker)

        label = Text(f"value = {value:.2f}", font_size=36)

        self.add(label)
        self.wait()


class PtDemo(Scene):
    """Create point from coordinates"""
    def construct(self):
        point = pt(2, 1.5)
        dot = Dot(point, color=BLUE)

        label = Text("pt(2, 1.5)", font_size=24).next_to(dot, UR)

        self.add(dot, label)
        self.wait()


class M2vDemo(Scene):
    """Convert model to view coordinates"""
    def construct(self):
        axes = Axes(x_range=[-3, 3], y_range=[-2, 2], x_length=6, y_length=4)
        dot = m2v(axes, 2, 1)  # Returns a Dot at screen coordinates for (2, 1)
        dot.set_color(GREEN)

        label = Text("(2, 1)", font_size=24, color=GREEN).next_to(dot, UR)

        self.add(axes, dot, label)
        self.wait()


class V2mDemo(Scene):
    """Convert view to model coordinates"""
    def construct(self):
        axes = Axes(x_range=[-3, 3], y_range=[-2, 2], x_length=6, y_length=4)
        dot = v2m(axes, 2, 1)  # Returns a Dot at model coordinates for screen point (2, 1)
        dot.set_color(RED)

        # Get the model coordinates for the label
        model_coords = axes.p2c(pt(2, 1))
        label = Text(f"({model_coords[0]:.1f}, {model_coords[1]:.1f})",
                     font_size=24, color=RED).next_to(dot, UR)

        self.add(axes, dot, label)
        self.wait()


class X2vDemo(Scene):
    """Get dot on graph at x-value"""
    def construct(self):
        axes = Axes(x_range=[-3, 3], y_range=[0, 9], x_length=6, y_length=4)
        parabola = axes.plot(lambda x: x**2, color=BLUE)

        dot = x2v(axes, parabola, 2)  # Returns a Dot on parabola at x=2
        dot.set_color(YELLOW)

        label = Text("x=2", font_size=24, color=YELLOW).next_to(dot, UR)

        self.add(axes, parabola, dot, label)
        self.wait()


class VlDemo(Scene):
    """Create vertical line"""
    def construct(self):
        line = vl(1, -2, 2)
        label = Text("vl(1, -2, 2)", font_size=24).next_to(line, RIGHT)

        self.add(line, label)
        self.wait()


class HlDemo(Scene):
    """Create horizontal line"""
    def construct(self):
        line = hl(1, -2, 2)
        label = Text("hl(1, -2, 2)", font_size=24).next_to(line, UP)

        self.add(line, label)
        self.wait()


class LraDemo(Scene):
    """Create line with radius and angle (polar)"""
    def construct(self):
        line = lra(2.5, 30)
        label = Text("lra(2.5, 30°)", font_size=24).next_to(line, UR)

        self.add(line, label)
        self.wait()


class VraDemo(Scene):
    """Create arrow with radius and angle (polar)"""
    def construct(self):
        arrow = vra(2.5, 120)
        label = Text("vra(2.5, 120°)", font_size=24, color=YELLOW).next_to(arrow, UP)

        self.add(arrow, label)
        self.wait()


class R2pDemo(Scene):
    """Get dot at proportion along line"""
    def construct(self):
        line = Line(pt(-3, -1), pt(3, 2))
        dot_25 = r2p(line, 0.25)
        dot_50 = r2p(line, 0.5)
        dot_75 = r2p(line, 0.75)

        dot_25.set_color(GREEN)
        dot_50.set_color(YELLOW)
        dot_75.set_color(RED)

        label_25 = Text("25%", font_size=20, color=GREEN).next_to(dot_25, DOWN)
        label_50 = Text("50%", font_size=20, color=YELLOW).next_to(dot_50, DOWN)
        label_75 = Text("75%", font_size=20, color=RED).next_to(dot_75, UP)

        self.add(line, dot_25, dot_50, dot_75, label_25, label_50, label_75)
        self.wait()
