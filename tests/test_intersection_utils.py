"""
Tests for intersection_utils module.
"""

import pytest
import numpy as np
from manim import Line, Dot, VGroup, Circle, ORIGIN, LEFT, RIGHT, UP, DOWN


def test_import():
    """Test that intersect_lines can be imported from the package."""
    from robo_manim_add_ons import intersect_lines
    assert callable(intersect_lines)


def test_intersect_lines_perpendicular():
    """Test intersection of perpendicular lines."""
    from robo_manim_add_ons import intersect_lines

    # Horizontal and vertical lines intersecting at origin
    line1 = Line(LEFT, RIGHT)
    line2 = Line(DOWN, UP)

    result = intersect_lines(line1, line2)

    assert isinstance(result, Dot), "Should return a Dot for intersecting lines"
    intersection_point = result.get_center()
    assert np.allclose(intersection_point, ORIGIN, atol=1e-6), "Should intersect at ORIGIN"


def test_intersect_lines_diagonal():
    """Test intersection of diagonal lines."""
    from robo_manim_add_ons import intersect_lines

    # Two diagonal lines crossing at origin
    line1 = Line(LEFT + DOWN, RIGHT + UP)
    line2 = Line(LEFT + UP, RIGHT + DOWN)

    result = intersect_lines(line1, line2)

    assert isinstance(result, Dot), "Should return a Dot for intersecting lines"
    intersection_point = result.get_center()
    assert np.allclose(intersection_point, ORIGIN, atol=1e-6), "Should intersect at ORIGIN"


def test_intersect_lines_offset_intersection():
    """Test intersection at a non-origin point."""
    from robo_manim_add_ons import intersect_lines

    # Lines intersecting at [1, 1, 0]
    line1 = Line(LEFT * 2 + UP, RIGHT * 2 + UP)  # Horizontal line at y=1
    line2 = Line(RIGHT + DOWN, RIGHT + UP * 3)   # Vertical line at x=1

    result = intersect_lines(line1, line2)

    assert isinstance(result, Dot), "Should return a Dot for intersecting lines"
    intersection_point = result.get_center()
    expected = np.array([1, 1, 0])
    assert np.allclose(intersection_point, expected, atol=1e-6), f"Should intersect at {expected}"


def test_intersect_lines_parallel_horizontal():
    """Test parallel horizontal lines (no intersection)."""
    from robo_manim_add_ons import intersect_lines

    # Two parallel horizontal lines
    line1 = Line(LEFT, RIGHT)
    line2 = Line(LEFT + UP, RIGHT + UP)

    result = intersect_lines(line1, line2)

    assert isinstance(result, VGroup), "Should return empty VGroup for parallel lines"
    assert len(result) == 0, "VGroup should be empty"


def test_intersect_lines_parallel_vertical():
    """Test parallel vertical lines (no intersection)."""
    from robo_manim_add_ons import intersect_lines

    # Two parallel vertical lines
    line1 = Line(DOWN, UP)
    line2 = Line(DOWN + RIGHT, UP + RIGHT)

    result = intersect_lines(line1, line2)

    assert isinstance(result, VGroup), "Should return empty VGroup for parallel lines"
    assert len(result) == 0, "VGroup should be empty"


def test_intersect_lines_parallel_diagonal():
    """Test parallel diagonal lines (no intersection)."""
    from robo_manim_add_ons import intersect_lines

    # Two parallel diagonal lines
    line1 = Line(LEFT + DOWN, RIGHT + UP)
    line2 = Line(LEFT + DOWN * 2, RIGHT + ORIGIN)

    result = intersect_lines(line1, line2)

    assert isinstance(result, VGroup), "Should return empty VGroup for parallel lines"
    assert len(result) == 0, "VGroup should be empty"


def test_intersect_lines_extended():
    """Test intersection when lines need to be extended."""
    from robo_manim_add_ons import intersect_lines

    # Line segments that don't physically overlap but their extensions intersect
    line1 = Line(LEFT * 3 + DOWN, LEFT * 2 + DOWN)     # Short horizontal line on left
    line2 = Line(RIGHT * 2 + DOWN * 2, RIGHT * 3 + UP) # Diagonal line on right

    result = intersect_lines(line1, line2)

    # Since lines are extended infinitely, they should intersect
    assert isinstance(result, Dot), "Should return a Dot even when lines need extension"


def test_intersect_lines_coincident():
    """Test coincident lines (same line)."""
    from robo_manim_add_ons import intersect_lines

    # Same line (coincident)
    line1 = Line(LEFT, RIGHT)
    line2 = Line(LEFT * 2, RIGHT * 2)  # Same direction, overlapping

    result = intersect_lines(line1, line2)

    # Coincident lines are treated as parallel (no single intersection point)
    assert isinstance(result, VGroup), "Should return empty VGroup for coincident lines"


def test_intersect_lines_acute_angle():
    """Test intersection at an acute angle."""
    from robo_manim_add_ons import intersect_lines

    # Two lines meeting at an acute angle
    line1 = Line(LEFT * 2, RIGHT * 2)
    line2 = Line(LEFT + DOWN, RIGHT + UP * 0.5)

    result = intersect_lines(line1, line2)

    assert isinstance(result, Dot), "Should return a Dot for intersecting lines"
    # The intersection should be on line1 (y=0 line)
    intersection_point = result.get_center()
    # Since line2 goes from (LEFT + DOWN) to (RIGHT + UP*0.5)
    # and line1 is at y=0, we need to find where they meet
    assert np.abs(intersection_point[1]) < 1e-6, "Y-coordinate should be approximately 0"


def test_intersect_lines_3d_coordinates():
    """Test that intersection works correctly with 3D coordinates (in xy-plane)."""
    from robo_manim_add_ons import intersect_lines

    # Lines with z-coordinates (should still work in xy-plane)
    line1 = Line(np.array([-1, 0, 0.5]), np.array([1, 0, 0.5]))
    line2 = Line(np.array([0, -1, 0.5]), np.array([0, 1, 0.5]))

    result = intersect_lines(line1, line2)

    assert isinstance(result, Dot), "Should return a Dot for intersecting lines"
    intersection_point = result.get_center()
    # Should intersect at origin in xy-plane (z-coordinate might vary)
    assert np.allclose(intersection_point[:2], [0, 0], atol=1e-6), "Should intersect at xy origin"


# Tests for intersect_line_circle
def test_import_intersect_line_circle():
    """Test that intersect_line_circle can be imported from the package."""
    from robo_manim_add_ons import intersect_line_circle
    assert callable(intersect_line_circle)


def test_intersect_line_circle_horizontal_through_center():
    """Test horizontal line through circle center (two intersections)."""
    from robo_manim_add_ons import intersect_line_circle

    circle = Circle(radius=2)
    line = Line(LEFT * 3, RIGHT * 3)  # Horizontal line through origin

    result = intersect_line_circle(line, circle)

    assert isinstance(result, VGroup), "Should return a VGroup"
    assert len(result) == 2, "Should have 2 intersection points"

    # Check that both are Dots
    assert all(isinstance(dot, Dot) for dot in result), "All elements should be Dots"

    # Get intersection points
    points = [dot.get_center() for dot in result]

    # Should be at (-2, 0, 0) and (2, 0, 0)
    x_coords = sorted([p[0] for p in points])
    assert np.allclose(x_coords, [-2, 2], atol=1e-6), "X-coordinates should be -2 and 2"
    assert all(np.abs(p[1]) < 1e-6 for p in points), "Y-coordinates should be 0"


def test_intersect_line_circle_vertical_through_center():
    """Test vertical line through circle center (two intersections)."""
    from robo_manim_add_ons import intersect_line_circle

    circle = Circle(radius=1.5)
    line = Line(DOWN * 3, UP * 3)  # Vertical line through origin

    result = intersect_line_circle(line, circle)

    assert len(result) == 2, "Should have 2 intersection points"

    # Get intersection points
    points = [dot.get_center() for dot in result]

    # Should be at (0, -1.5, 0) and (0, 1.5, 0)
    y_coords = sorted([p[1] for p in points])
    assert np.allclose(y_coords, [-1.5, 1.5], atol=1e-6), "Y-coordinates should be -1.5 and 1.5"
    assert all(np.abs(p[0]) < 1e-6 for p in points), "X-coordinates should be 0"


def test_intersect_line_circle_diagonal():
    """Test diagonal line intersecting circle."""
    from robo_manim_add_ons import intersect_line_circle

    circle = Circle(radius=2).shift(ORIGIN)
    line = Line(LEFT * 3 + DOWN * 3, RIGHT * 3 + UP * 3)  # Diagonal through origin

    result = intersect_line_circle(line, circle)

    assert len(result) == 2, "Should have 2 intersection points"

    # Check that points are on both the line and circle
    points = [dot.get_center() for dot in result]
    for p in points:
        # Check distance from center
        distance = np.linalg.norm(p - ORIGIN)
        assert np.abs(distance - 2) < 1e-6, f"Point should be on circle (distance={distance})"


def test_intersect_line_circle_tangent():
    """Test line tangent to circle (one intersection)."""
    from robo_manim_add_ons import intersect_line_circle

    circle = Circle(radius=2)
    # Horizontal line at y=2 (tangent to top of circle)
    line = Line(LEFT * 3 + UP * 2, RIGHT * 3 + UP * 2)

    result = intersect_line_circle(line, circle)

    assert isinstance(result, VGroup), "Should return a VGroup"
    assert len(result) == 1, "Tangent line should have 1 intersection point"

    # Check the tangent point
    point = result[0].get_center()
    assert np.allclose(point, [0, 2, 0], atol=1e-6), "Tangent point should be at (0, 2, 0)"


def test_intersect_line_circle_no_intersection():
    """Test line that doesn't intersect circle."""
    from robo_manim_add_ons import intersect_line_circle

    circle = Circle(radius=1)
    # Horizontal line far above the circle
    line = Line(LEFT * 3 + UP * 5, RIGHT * 3 + UP * 5)

    result = intersect_line_circle(line, circle)

    assert isinstance(result, VGroup), "Should return a VGroup"
    assert len(result) == 0, "Should have no intersection points"


def test_intersect_line_circle_offset_circle():
    """Test line intersecting an offset circle."""
    from robo_manim_add_ons import intersect_line_circle

    circle = Circle(radius=1).shift(RIGHT * 2 + UP)
    # Vertical line at x=2 (through circle center)
    line = Line(RIGHT * 2 + DOWN * 3, RIGHT * 2 + UP * 3)

    result = intersect_line_circle(line, circle)

    assert len(result) == 2, "Should have 2 intersection points"

    # Get intersection points
    points = [dot.get_center() for dot in result]

    # All points should have x=2
    assert all(np.abs(p[0] - 2) < 1e-6 for p in points), "X-coordinates should be 2"

    # Y-coordinates should be 0 and 2 (center at y=1, radius=1)
    y_coords = sorted([p[1] for p in points])
    assert np.allclose(y_coords, [0, 2], atol=1e-6), "Y-coordinates should be 0 and 2"


def test_intersect_line_circle_extended_line():
    """Test that line is treated as infinite (extended)."""
    from robo_manim_add_ons import intersect_line_circle

    circle = Circle(radius=2)
    # Short line segment near origin (but when extended, intersects circle)
    line = Line(LEFT * 0.5, RIGHT * 0.5)

    result = intersect_line_circle(line, circle)

    # Even though the line segment doesn't reach the circle,
    # its extension should intersect
    assert len(result) == 2, "Extended line should intersect circle at 2 points"


def test_intersect_line_circle_various_radii():
    """Test with different circle radii."""
    from robo_manim_add_ons import intersect_line_circle

    line = Line(LEFT * 5, RIGHT * 5)  # Horizontal line through origin

    for radius in [0.5, 1, 2, 3]:
        circle = Circle(radius=radius)
        result = intersect_line_circle(line, circle)

        assert len(result) == 2, f"Should have 2 intersections for radius {radius}"

        # Check distances
        points = [dot.get_center() for dot in result]
        x_coords = sorted([p[0] for p in points])
        assert np.allclose(x_coords, [-radius, radius], atol=1e-6), \
            f"Intersections should be at ±{radius}"


def test_intersect_line_circle_diagonal_offset():
    """Test diagonal line with offset circle."""
    from robo_manim_add_ons import intersect_line_circle

    circle = Circle(radius=1.5).shift(RIGHT + UP)
    # Diagonal line that passes through the circle
    line = Line(LEFT * 2, RIGHT * 4 + UP * 3)

    result = intersect_line_circle(line, circle)

    # Should have 2 intersections (or possibly 0 or 1 depending on geometry)
    assert isinstance(result, VGroup), "Should return a VGroup"

    # Verify all intersection points are on the circle
    for dot in result:
        point = dot.get_center()
        distance = np.linalg.norm(point - (RIGHT + UP))
        assert np.abs(distance - 1.5) < 1e-5, "Point should be on the circle"


def test_intersect_line_circle_near_tangent():
    """Test line very close to being tangent (should still have 2 intersections)."""
    from robo_manim_add_ons import intersect_line_circle

    circle = Circle(radius=2)
    # Line slightly below tangent point
    line = Line(LEFT * 3 + UP * 1.9, RIGHT * 3 + UP * 1.9)

    result = intersect_line_circle(line, circle)

    # Should have 2 very close intersection points
    assert len(result) == 2, "Should have 2 intersection points"

    # Points should be relatively close together (closer than diameter)
    points = [dot.get_center() for dot in result]
    distance_between = np.linalg.norm(points[0] - points[1])
    assert distance_between < 2, "Intersection points should be closer than diameter"
