"""
Demo script showing how to use robo-manim-add-ons.

Run this script with:
    manim -pql demo.py DemoScene

Or render in high quality:
    manim -pqh demo.py DemoScene
"""

from manim import *
from robo_manim_add_ons import CustomCircle, CustomSquare
from robo_manim_add_ons.custom_mobjects import create_custom_layout


class DemoScene(Scene):
    """
    A demo scene showcasing the custom mobjects from robo-manim-add-ons.
    """

    def construct(self):
        # Create title
        title = Text("Robo Manim Add-ons Demo", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Create custom circle and square
        circle = CustomCircle(radius=1.5)
        square = CustomSquare(side_length=2.0)

        # Position them using the helper function
        create_custom_layout(circle, square)

        # Animate the objects
        self.play(Create(circle), Create(square))
        self.wait(0.5)

        # Add some transformations
        self.play(
            Rotate(circle, angle=PI),
            square.animate.scale(0.5),
            run_time=2
        )
        self.wait(0.5)

        # Transform circle to square
        self.play(Transform(circle, Square(color=RED, side_length=3).shift(UP * 2)))
        self.wait(0.5)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(circle), FadeOut(square))
        self.wait(0.5)


class SimpleScene(Scene):
    """
    A simpler example for quick testing.
    """

    def construct(self):
        # Just create and show a custom circle
        circle = CustomCircle()
        self.play(Create(circle))
        self.wait(1)


if __name__ == "__main__":
    # This allows you to run the script directly with Python
    # though using the manim CLI is recommended
    print("To render this scene, use:")
    print("  manim -pql demo.py DemoScene")
    print("  manim -pql demo.py SimpleScene")
