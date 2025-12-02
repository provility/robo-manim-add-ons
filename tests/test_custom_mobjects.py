"""
Tests for custom_mobjects module.
"""

import pytest
from manim import RED, BLUE, UP, DOWN
from robo_manim_add_ons import CustomCircle, CustomSquare
from robo_manim_add_ons.custom_mobjects import create_custom_layout


class TestCustomCircle:
    """Test cases for CustomCircle."""

    def test_circle_creation(self):
        """Test that CustomCircle can be created."""
        circle = CustomCircle()
        assert circle is not None

    def test_circle_default_radius(self):
        """Test that CustomCircle has correct default radius."""
        circle = CustomCircle()
        assert circle.radius == 1.0

    def test_circle_custom_radius(self):
        """Test that CustomCircle accepts custom radius."""
        circle = CustomCircle(radius=2.5)
        assert circle.radius == 2.5

    def test_circle_color(self):
        """Test that CustomCircle has the correct default color."""
        circle = CustomCircle()
        assert circle.color.to_hex() == RED.to_hex()


class TestCustomSquare:
    """Test cases for CustomSquare."""

    def test_square_creation(self):
        """Test that CustomSquare can be created."""
        square = CustomSquare()
        assert square is not None

    def test_square_default_side_length(self):
        """Test that CustomSquare has correct default side length."""
        square = CustomSquare()
        assert square.side_length == 2.0

    def test_square_custom_side_length(self):
        """Test that CustomSquare accepts custom side length."""
        square = CustomSquare(side_length=3.0)
        assert square.side_length == 3.0

    def test_square_color(self):
        """Test that CustomSquare has the correct default color."""
        square = CustomSquare()
        assert square.color.to_hex() == BLUE.to_hex()


class TestLayoutHelpers:
    """Test cases for layout helper functions."""

    def test_create_custom_layout(self):
        """Test that create_custom_layout positions objects correctly."""
        circle = CustomCircle()
        square = CustomSquare()

        positioned_circle, positioned_square = create_custom_layout(circle, square)

        # Check that objects are positioned correctly
        assert positioned_circle.get_center()[1] > 0  # Circle should be above center
        assert positioned_square.get_center()[1] < 0  # Square should be below center
