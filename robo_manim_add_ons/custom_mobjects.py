"""
Custom Mobject examples for robo-manim-add-ons.
These are simple examples to demonstrate how to create custom Manim objects.
"""

from manim import Circle, Square, RED, BLUE, UP, DOWN


class CustomCircle(Circle):
    """
    A custom circle with preset styling.

    Example:
        >>> circle = CustomCircle()
        >>> self.play(Create(circle))
    """

    def __init__(self, radius=1.0, **kwargs):
        super().__init__(radius=radius, color=RED, **kwargs)


class CustomSquare(Square):
    """
    A custom square with preset styling.

    Example:
        >>> square = CustomSquare()
        >>> self.play(Create(square))
    """

    def __init__(self, side_length=2.0, **kwargs):
        super().__init__(side_length=side_length, color=BLUE, **kwargs)


def create_custom_layout(circle, square):
    """
    Helper function to arrange custom objects in a specific layout.

    Args:
        circle: A Circle mobject
        square: A Square mobject

    Returns:
        tuple: (circle, square) positioned in a vertical layout
    """
    circle.shift(UP * 2)
    square.shift(DOWN * 2)
    return circle, square
