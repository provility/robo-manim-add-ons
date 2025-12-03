"""
Unit tests for transform utilities.
"""

import numpy as np
import pytest
from manim import Square, Circle, Line, Dot, ORIGIN, RIGHT, UP
from robo_manim_add_ons import translated, rotated, scaled


def test_translated():
    """Test the translated function."""
    square = Square()
    shifted = translated(square, 2, 1)

    # Check that it returns a new object
    assert shifted is not square

    # Check the translation is correct
    original_center = square.get_center()
    new_center = shifted.get_center()
    expected = original_center + np.array([2, 1, 0])

    assert np.allclose(new_center, expected, atol=1e-10)


def test_translated_negative():
    """Test translated with negative values."""
    circle = Circle()
    shifted = translated(circle, -1, -2)

    original_center = circle.get_center()
    new_center = shifted.get_center()
    expected = original_center + np.array([-1, -2, 0])

    assert np.allclose(new_center, expected, atol=1e-10)


def test_rotated_no_about():
    """Test rotated function without about point (rotates around center)."""
    line = Line(ORIGIN, RIGHT)
    rotated_line = rotated(line, 90)

    # Check that it returns a new object
    assert rotated_line is not line

    # After 90 degree rotation around center, horizontal line becomes vertical
    # The line's direction should be perpendicular
    original_vec = line.get_end() - line.get_start()
    new_vec = rotated_line.get_end() - rotated_line.get_start()

    # Dot product of perpendicular vectors is 0
    dot_product = np.dot(original_vec[:2], new_vec[:2])
    assert np.isclose(dot_product, 0, atol=1e-10)


def test_rotated_with_dot():
    """Test rotated function with a Dot as rotation point."""
    line = Line(ORIGIN, RIGHT)
    pivot = Dot(ORIGIN)
    rotated_line = rotated(line, 90, pivot)

    # The start point should remain at origin (rotation point)
    assert np.allclose(rotated_line.get_start(), ORIGIN, atol=1e-10)

    # The end point should be rotated 90 degrees
    # RIGHT rotated 90 degrees around ORIGIN becomes UP
    assert np.allclose(rotated_line.get_end()[:2], UP[:2], atol=1e-10)


def test_rotated_with_array():
    """Test rotated function with numpy array as rotation point."""
    line = Line(ORIGIN, RIGHT)
    rotated_line = rotated(line, 180, np.array([0, 0, 0]))

    # After 180 degree rotation, line should point in opposite direction
    original_vec = line.get_end() - line.get_start()
    new_vec = rotated_line.get_end() - rotated_line.get_start()

    # Vectors should be opposite (dot product should be negative of squared magnitude)
    dot_product = np.dot(original_vec, new_vec)
    magnitude_sq = np.dot(original_vec, original_vec)

    assert np.isclose(dot_product, -magnitude_sq, atol=1e-10)


def test_scaled_no_about():
    """Test scaled function without about point (scales around center)."""
    circle = Circle(radius=1)
    big_circle = scaled(circle, 2)

    # Check that it returns a new object
    assert big_circle is not circle

    # Check that the radius is doubled
    # For a circle, width/height should be doubled
    original_width = circle.width
    new_width = big_circle.width

    assert np.isclose(new_width, original_width * 2, atol=1e-10)


def test_scaled_with_dot():
    """Test scaled function with a Dot as scaling point."""
    square = Square(side_length=1).shift(RIGHT)
    pivot = Dot(ORIGIN)
    big_square = scaled(square, 2, pivot)

    # The distance from pivot to square center should double
    original_distance = np.linalg.norm(square.get_center() - pivot.get_center())
    new_distance = np.linalg.norm(big_square.get_center() - pivot.get_center())

    assert np.isclose(new_distance, original_distance * 2, atol=1e-10)


def test_scaled_with_array():
    """Test scaled function with numpy array as scaling point."""
    square = Square(side_length=1).shift(UP)
    big_square = scaled(square, 0.5, np.array([0, 0, 0]))

    # The distance from origin to square center should be halved
    original_distance = np.linalg.norm(square.get_center())
    new_distance = np.linalg.norm(big_square.get_center())

    assert np.isclose(new_distance, original_distance * 0.5, atol=1e-10)


def test_scaled_fractional():
    """Test scaled with fractional scale factor."""
    circle = Circle(radius=2)
    small_circle = scaled(circle, 0.25)

    original_width = circle.width
    new_width = small_circle.width

    assert np.isclose(new_width, original_width * 0.25, atol=1e-10)
