"""
Intersection utility functions for Manim objects.

Provides helper functions for finding intersections between geometric objects.
"""

import numpy as np
from manim import Line, Dot, VGroup, Circle
from typing import Union


def intersect_lines(line1: Line, line2: Line) -> Union[Dot, VGroup]:
    """
    Find the intersection point of two lines (extended infinitely).

    Args:
        line1: The first Line object
        line2: The second Line object

    Returns:
        Dot at the intersection point if lines intersect,
        Empty VGroup if lines are parallel or don't intersect

    Example:
        >>> from manim import *
        >>> from robo_manim_add_ons import intersect_lines
        >>>
        >>> line1 = Line(LEFT, RIGHT)  # Horizontal line
        >>> line2 = Line(DOWN, UP)     # Vertical line
        >>> intersection = intersect_lines(line1, line2)
        >>> # Returns Dot at ORIGIN
        >>>
        >>> # Parallel lines
        >>> line3 = Line(LEFT + UP, RIGHT + UP)
        >>> line4 = Line(LEFT, RIGHT)
        >>> intersection2 = intersect_lines(line3, line4)
        >>> # Returns empty VGroup
    """
    # Get endpoints of both lines
    p1 = line1.get_start()
    p2 = line1.get_end()
    p3 = line2.get_start()
    p4 = line2.get_end()

    # Direction vectors
    d1 = p2 - p1  # Direction of line1
    d2 = p4 - p3  # Direction of line2

    # Vector from line1 start to line2 start
    p1_to_p3 = p3 - p1

    # Calculate the cross product in 2D (ignoring z-component)
    # For 3D vectors [x, y, z], we use the z-component of the cross product
    cross_d1_d2 = d1[0] * d2[1] - d1[1] * d2[0]

    # If cross product is zero, lines are parallel or coincident
    if np.abs(cross_d1_d2) < 1e-10:
        return VGroup()  # Empty VGroup for parallel/coincident lines

    # Calculate parameter t for line1
    # Using the formula from line intersection:
    # t = ((p3 - p1) × d2) / (d1 × d2)
    cross_p1p3_d2 = p1_to_p3[0] * d2[1] - p1_to_p3[1] * d2[0]
    t = cross_p1p3_d2 / cross_d1_d2

    # Calculate intersection point
    # P = p1 + t * d1
    intersection_point = p1 + t * d1

    return Dot(intersection_point)


def intersect_line_circle(line: Line, circle: Circle) -> VGroup:
    """
    Find the intersection points of a line (extended infinitely) and a circle.

    Args:
        line: The Line object (treated as infinite)
        circle: The Circle object

    Returns:
        VGroup containing:
        - 2 Dots if line intersects circle at two points
        - 1 Dot if line is tangent to circle
        - Empty VGroup if line doesn't intersect circle

    Example:
        >>> from manim import *
        >>> from robo_manim_add_ons import intersect_line_circle
        >>>
        >>> line = Line(LEFT * 3, RIGHT * 3)
        >>> circle = Circle(radius=2)
        >>> intersections = intersect_line_circle(line, circle)
        >>> # Returns VGroup with 2 Dots
        >>>
        >>> # Line missing the circle
        >>> line2 = Line(LEFT * 3 + UP * 5, RIGHT * 3 + UP * 5)
        >>> intersections2 = intersect_line_circle(line2, circle)
        >>> # Returns empty VGroup
    """
    # Get line parameters
    p1 = line.get_start()
    p2 = line.get_end()
    direction = p2 - p1

    # Normalize direction vector
    d = direction / np.linalg.norm(direction)

    # Get circle parameters
    center = circle.get_center()
    # Calculate radius from the circle's width
    radius = circle.width / 2

    # Vector from line start to circle center
    f = p1 - center

    # Solve quadratic equation: |p1 + t*d - center|² = radius²
    # Expanding: (f + t*d)·(f + t*d) = r²
    # t²(d·d) + 2t(f·d) + (f·f - r²) = 0
    # Since d is normalized, d·d = 1
    a = np.dot(d, d)  # Should be 1 for normalized vector
    b = 2 * np.dot(f, d)
    c = np.dot(f, f) - radius * radius

    # Calculate discriminant
    discriminant = b * b - 4 * a * c

    # No intersection if discriminant is negative
    if discriminant < -1e-10:
        return VGroup()

    # Tangent case (one intersection point)
    if abs(discriminant) < 1e-10:
        t = -b / (2 * a)
        intersection_point = p1 + t * d
        return VGroup(Dot(intersection_point))

    # Two intersection points
    sqrt_discriminant = np.sqrt(discriminant)
    t1 = (-b - sqrt_discriminant) / (2 * a)
    t2 = (-b + sqrt_discriminant) / (2 * a)

    point1 = p1 + t1 * d
    point2 = p1 + t2 * d

    return VGroup(Dot(point1), Dot(point2))


# ============================================================================
# Aliases
# ============================================================================

def ill(line1: Line, line2: Line) -> Union[Dot, VGroup]:
    """Alias for intersect_lines(). See intersect_lines() for full documentation."""
    return intersect_lines(line1, line2)


def ilc(line: Line, circle: Circle) -> VGroup:
    """Alias for intersect_line_circle(). See intersect_line_circle() for full documentation."""
    return intersect_line_circle(line, circle)
