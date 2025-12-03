"""
Transform utilities demo: Minimal examples using updater and become methods.

Demonstrates translated(), rotated(), and scaled() functions with dynamic updates.
"""

from manim import *
from robo_manim_add_ons import translated, rotated, scaled


class TranslatedUpdaterExample(Scene):
    """Demonstrates translated() with updater."""
    def construct(self):
        # Create a reference square that will move
        ref_square = Square(color=BLUE).shift(LEFT * 3)

        # Create a follower square that uses updater to stay translated
        follower = Square(color=RED)
        follower.add_updater(
            lambda m: m.become(translated(ref_square, 2, 1))
        )

        self.add(ref_square, follower)
        self.play(ref_square.animate.shift(RIGHT * 2 + UP))
        self.play(ref_square.animate.shift(DOWN * 2))
        self.wait()


class RotatedUpdaterExample(Scene):
    """Demonstrates rotated() with updater."""
    def construct(self):
        # Create a reference line that will rotate
        ref_line = Line(ORIGIN, RIGHT * 2, color=BLUE)
        center_dot = Dot(ORIGIN, color=YELLOW)

        # Create a follower line that stays rotated by 45 degrees
        follower = Line(ORIGIN, RIGHT * 2, color=RED)
        follower.add_updater(
            lambda m: m.become(rotated(ref_line, 45, center_dot))
        )

        self.add(ref_line, follower, center_dot)
        self.play(Rotate(ref_line, PI, about_point=ORIGIN))
        self.wait()


class ScaledUpdaterExample(Scene):
    """Demonstrates scaled() with updater."""
    def construct(self):
        # Create a reference circle that will scale
        ref_circle = Circle(radius=0.5, color=BLUE).shift(LEFT * 2)

        # Create a follower circle that is always 2x the size
        follower = Circle(radius=0.5, color=RED)
        follower.add_updater(
            lambda m: m.become(scaled(ref_circle, 2))
        )

        self.add(ref_circle, follower)
        self.play(ref_circle.animate.scale(2))
        self.play(ref_circle.animate.shift(RIGHT * 2))
        self.wait()


class TranslatedBecomeExample(Scene):
    """Demonstrates translated() with become method."""
    def construct(self):
        original = Square(color=BLUE)
        copy = Square(color=RED)

        self.add(original)
        self.wait(0.5)

        # Use become to transform into translated version
        self.play(copy.animate.become(translated(original, 3, 1)))
        self.add(copy)
        self.wait()


class RotatedBecomeExample(Scene):
    """Demonstrates rotated() with become method."""
    def construct(self):
        original = Line(ORIGIN, RIGHT * 2, color=BLUE)
        copy = Line(ORIGIN, RIGHT * 2, color=RED).shift(DOWN)

        self.add(original, copy)
        self.wait(0.5)

        # Use become to transform into rotated version
        self.play(copy.animate.become(rotated(original, 90)))
        self.wait()


class ScaledBecomeExample(Scene):
    """Demonstrates scaled() with become method."""
    def construct(self):
        original = Circle(radius=1, color=BLUE)
        copy = Circle(radius=1, color=RED).shift(RIGHT * 3)

        self.add(original, copy)
        self.wait(0.5)

        # Use become to transform into scaled version
        self.play(copy.animate.become(scaled(original, 2)))
        self.wait()
