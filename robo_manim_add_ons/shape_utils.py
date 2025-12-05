"""
Shape utilities for creating Manim shapes with flexible inputs.

Provides helper functions for creating shapes like rectangles with various input formats.
"""

import numpy as np
from manim import Rectangle
from typing import Union


def rect(*args, **kwargs) -> Rectangle:
    """
    Create a Rectangle with flexible arguments.

    Args can be:
        - 2 args (numbers): (width, height)
        - 2 args (points): (left_bottom, top_right) where each is Dot/np.array/list
        - 4 args (points): (left_bottom, left_top, right_top, right_bottom)

    Additional args:
        **kwargs: Additional styling arguments (color, fill_opacity, etc.)

    Returns:
        A Rectangle object

    Raises:
        TypeError: If arguments don't match expected patterns
        ValueError: If wrong number of arguments provided

    Example:
        >>> from manim import Dot, ORIGIN
        >>> from robo_manim_add_ons import rect
        >>>
        >>> # From width and height
        >>> rectangle = rect(4, 3)  # Rectangle with width=4, height=3 centered at origin
        >>>
        >>> # From two corners (left-bottom and top-right)
        >>> lb = Dot([-2, -1, 0])
        >>> tr = Dot([2, 2, 0])
        >>> rectangle = rect(lb, tr)
        >>>
        >>> # From two arrays
        >>> rectangle = rect([-2, -1, 0], [2, 2, 0])
        >>>
        >>> # From four corners (left-bottom, left-top, right-top, right-bottom)
        >>> lb = [-2, -1.5, 0]
        >>> lt = [-2, 1.5, 0]
        >>> rt = [2, 1.5, 0]
        >>> rb = [2, -1.5, 0]
        >>> rectangle = rect(lb, lt, rt, rb)
    """
    def _is_number(arg):
        """Check if arg is a number"""
        return isinstance(arg, (int, float))

    def _is_point(arg):
        """Check if arg is a Dot/object or np.array"""
        return hasattr(arg, 'get_center') or isinstance(arg, (np.ndarray, list, tuple))

    def _extract_position(obj):
        """Extract position from Dot/object or np.array/list"""
        if hasattr(obj, 'get_center'):
            return obj.get_center()
        elif isinstance(obj, np.ndarray):
            return obj
        elif isinstance(obj, (list, tuple)):
            return np.array(obj)
        else:
            raise TypeError(f"Expected Dot, np.array, or list, got {type(obj).__name__}")

    if len(args) == 2:
        # Could be: (width, height) OR (left_bottom, top_right)
        if _is_number(args[0]) and _is_number(args[1]):
            # Pattern: (width, height)
            width = args[0]
            height = args[1]

            rectangle = Rectangle(width=width, height=height, **kwargs)
            return rectangle

        elif _is_point(args[0]) and _is_point(args[1]):
            # Pattern: (left_bottom, top_right)
            lb_pos = _extract_position(args[0])
            tr_pos = _extract_position(args[1])

            # Calculate width, height, and center
            width = abs(tr_pos[0] - lb_pos[0])
            height = abs(tr_pos[1] - lb_pos[1])
            center_x = (lb_pos[0] + tr_pos[0]) / 2
            center_y = (lb_pos[1] + tr_pos[1]) / 2
            center = np.array([center_x, center_y, 0])

            rectangle = Rectangle(width=width, height=height, **kwargs)
            rectangle.move_to(center)
            return rectangle

        else:
            raise TypeError("For 2 arguments, expected (width, height) or (left_bottom, top_right)")

    elif len(args) == 4:
        # Pattern: (left_bottom, left_top, right_top, right_bottom)
        if not all(_is_point(arg) for arg in args):
            raise TypeError("For 4 arguments, all must be Dot objects, np.arrays, or lists")

        lb_pos = _extract_position(args[0])  # left-bottom
        lt_pos = _extract_position(args[1])  # left-top
        rt_pos = _extract_position(args[2])  # right-top
        rb_pos = _extract_position(args[3])  # right-bottom

        # Calculate width and height
        # Width: distance between left and right sides
        # Height: distance between top and bottom sides
        width = abs(rt_pos[0] - lt_pos[0])
        height = abs(lt_pos[1] - lb_pos[1])

        # Calculate center
        center_x = (lb_pos[0] + rt_pos[0]) / 2
        center_y = (lb_pos[1] + rt_pos[1]) / 2
        center = np.array([center_x, center_y, 0])

        rectangle = Rectangle(width=width, height=height, **kwargs)
        rectangle.move_to(center)
        return rectangle

    else:
        raise ValueError(f"rect() takes 2 or 4 arguments, got {len(args)}")
