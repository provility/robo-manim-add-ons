"""
Tests for vector_utils module.
"""

import pytest
import numpy as np
from manim import Arrow, ORIGIN, LEFT, RIGHT, UP, DOWN

from robo_manim_add_ons.vector_utils import VectorUtils


class TestForward:
    """Tests for the forward function."""

    def test_forward_basic(self):
        """Test basic forward shift."""
        source = Arrow(ORIGIN, RIGHT * 2, buff=0)
        shifted = VectorUtils.forward(source, 1.0)

        # Should be shifted 1 unit to the right
        assert shifted is not None
        assert isinstance(shifted, Arrow)

        # Check that it's shifted forward
        assert np.allclose(shifted.get_start(), RIGHT, atol=1e-6)
        assert np.allclose(shifted.get_end(), RIGHT * 3, atol=1e-6)

    def test_forward_direction_preserved(self):
        """Test that direction is preserved."""
        source = Arrow(ORIGIN, RIGHT * 2, buff=0)
        shifted = VectorUtils.forward(source, 1.5)

        # Get direction vectors
        source_dir = source.get_end() - source.get_start()
        shifted_dir = shifted.get_end() - shifted.get_start()

        # Should have same direction
        assert np.allclose(source_dir, shifted_dir, atol=1e-6)

    def test_forward_diagonal_vector(self):
        """Test forward shift on diagonal vector."""
        source = Arrow(ORIGIN, RIGHT + UP, buff=0)
        distance = 2.0
        shifted = VectorUtils.forward(source, distance)

        # Calculate expected shift
        direction = RIGHT + UP
        unit_dir = direction / np.linalg.norm(direction)
        expected_shift = unit_dir * distance

        # Check shift amount
        actual_shift = shifted.get_start() - source.get_start()
        assert np.allclose(actual_shift, expected_shift, atol=1e-6)


class TestBackward:
    """Tests for the backward function."""

    def test_backward_basic(self):
        """Test basic backward shift."""
        source = Arrow(ORIGIN, RIGHT * 2, buff=0)
        shifted = VectorUtils.backward(source, 1.0)

        # Should be shifted 1 unit to the left
        assert shifted is not None
        assert isinstance(shifted, Arrow)
        assert np.allclose(shifted.get_start(), LEFT, atol=1e-6)
        assert np.allclose(shifted.get_end(), RIGHT, atol=1e-6)

    def test_backward_direction_preserved(self):
        """Test that direction is preserved."""
        source = Arrow(ORIGIN, RIGHT * 2, buff=0)
        shifted = VectorUtils.backward(source, 1.5)

        # Get direction vectors
        source_dir = source.get_end() - source.get_start()
        shifted_dir = shifted.get_end() - shifted.get_start()

        # Should have same direction
        assert np.allclose(source_dir, shifted_dir, atol=1e-6)

    def test_backward_opposite_of_forward(self):
        """Test that backward is opposite of forward."""
        source = Arrow(ORIGIN, RIGHT * 2, buff=0)
        forward_shifted = VectorUtils.forward(source, 1.0)
        backward_shifted = VectorUtils.backward(source, 1.0)

        # Forward and backward should be opposite
        forward_start = forward_shifted.get_start()
        backward_start = backward_shifted.get_start()

        # Distance from origin should be equal
        assert np.isclose(
            np.linalg.norm(forward_start),
            np.linalg.norm(backward_start),
            atol=1e-6
        )


class TestPerpMove:
    """Tests for the perp_move function."""

    def test_perp_move_basic(self):
        """Test basic perpendicular shift."""
        source = Arrow(ORIGIN, RIGHT * 2, buff=0)
        shifted = VectorUtils.perp_move(source, 1.0)

        # Should be shifted 1 unit upward
        assert shifted is not None
        assert isinstance(shifted, Arrow)
        assert np.allclose(shifted.get_start(), UP, atol=1e-6)
        assert np.allclose(shifted.get_end(), RIGHT * 2 + UP, atol=1e-6)

    def test_perp_move_direction_preserved(self):
        """Test that direction is preserved."""
        source = Arrow(ORIGIN, RIGHT * 2, buff=0)
        shifted = VectorUtils.perp_move(source, 1.5)

        # Get direction vectors
        source_dir = source.get_end() - source.get_start()
        shifted_dir = shifted.get_end() - shifted.get_start()

        # Should have same direction
        assert np.allclose(source_dir, shifted_dir, atol=1e-6)

    def test_perp_move_perpendicularity(self):
        """Test that perp_move is actually perpendicular."""
        source = Arrow(ORIGIN, RIGHT * 2, buff=0)
        shifted = VectorUtils.perp_move(source, 1.0)

        # Get vectors
        source_dir = source.get_end() - source.get_start()
        shift_dir = shifted.get_start() - source.get_start()

        # Dot product should be zero (perpendicular)
        dot_product = np.dot(source_dir, shift_dir)
        assert np.isclose(dot_product, 0.0, atol=1e-6)

    def test_perp_move_negative_distance(self):
        """Test perp_move with negative distance."""
        source = Arrow(ORIGIN, RIGHT * 2, buff=0)
        shifted_pos = VectorUtils.perp_move(source, 1.0)
        shifted_neg = VectorUtils.perp_move(source, -1.0)

        # Should be opposite directions
        pos_start = shifted_pos.get_start()
        neg_start = shifted_neg.get_start()

        # Sum should be zero (opposite)
        assert np.allclose(pos_start + neg_start, ORIGIN, atol=1e-6)


class TestTailAtTip:
    """Tests for the tail_at_tip function."""

    def test_tail_at_tip_basic(self):
        """Test basic tail-at-tip positioning."""
        vector_a = Arrow(ORIGIN, RIGHT * 2, buff=0)
        vector_b = Arrow(ORIGIN, UP * 1.5, buff=0)
        shifted = VectorUtils.tail_at_tip(vector_a, vector_b)

        # vector_b's tail should be at vector_a's tip
        assert shifted is not None
        assert np.allclose(shifted.get_start(), vector_a.get_end(), atol=1e-6)

    def test_tail_at_tip_direction_preserved(self):
        """Test that vector_b's direction is preserved."""
        vector_a = Arrow(ORIGIN, RIGHT * 2, buff=0)
        vector_b = Arrow(ORIGIN, UP * 1.5, buff=0)
        shifted = VectorUtils.tail_at_tip(vector_a, vector_b)

        # Get direction vectors
        original_dir = vector_b.get_end() - vector_b.get_start()
        shifted_dir = shifted.get_end() - shifted.get_start()

        # Should have same direction
        assert np.allclose(original_dir, shifted_dir, atol=1e-6)

    def test_tail_at_tip_magnitude_preserved(self):
        """Test that vector_b's magnitude is preserved."""
        vector_a = Arrow(ORIGIN, RIGHT * 2, buff=0)
        vector_b = Arrow(LEFT, RIGHT, buff=0)
        shifted = VectorUtils.tail_at_tip(vector_a, vector_b)

        # Get magnitudes
        original_mag = np.linalg.norm(vector_b.get_end() - vector_b.get_start())
        shifted_mag = np.linalg.norm(shifted.get_end() - shifted.get_start())

        # Should have same magnitude
        assert np.isclose(original_mag, shifted_mag, atol=1e-6)

    def test_tail_at_tip_vector_addition(self):
        """Test that tail-at-tip gives correct vector addition."""
        vector_a = Arrow(ORIGIN, RIGHT * 2, buff=0)
        vector_b = Arrow(ORIGIN, UP * 1.5, buff=0)
        shifted_b = VectorUtils.tail_at_tip(vector_a, vector_b)

        # End of shifted_b should be sum of original vectors
        expected_end = (vector_a.get_end() - vector_a.get_start()) + \
                       (vector_b.get_end() - vector_b.get_start())

        assert np.allclose(shifted_b.get_end(), expected_end, atol=1e-6)


class TestShiftAmount:
    """Tests for the shift_amount function."""

    def test_shift_amount_basic(self):
        """Test basic shift amount calculation."""
        vector_a = Arrow(ORIGIN, RIGHT * 2, buff=0)
        vector_b = Arrow(LEFT, LEFT + UP, buff=0)
        shift = VectorUtils.shift_amount(vector_a, vector_b)

        # Should be vector from vector_b's start to vector_a's end
        expected_shift = vector_a.get_end() - vector_b.get_start()
        assert np.allclose(shift, expected_shift, atol=1e-6)

    def test_shift_amount_result_type(self):
        """Test that shift amount returns numpy array."""
        vector_a = Arrow(ORIGIN, RIGHT * 2, buff=0)
        vector_b = Arrow(LEFT, LEFT + UP, buff=0)
        shift = VectorUtils.shift_amount(vector_a, vector_b)

        assert isinstance(shift, np.ndarray)

    def test_shift_amount_correct_positioning(self):
        """Test that applying shift amount positions correctly."""
        vector_a = Arrow(ORIGIN, RIGHT * 2, buff=0)
        vector_b = Arrow(LEFT * 2, LEFT * 2 + UP, buff=0)
        shift = VectorUtils.shift_amount(vector_a, vector_b)

        # Apply shift
        new_start = vector_b.get_start() + shift

        # Should align with vector_a's tip
        assert np.allclose(new_start, vector_a.get_end(), atol=1e-6)


class TestCopyAt:
    """Tests for the copy_at function."""

    def test_copy_at_basic(self):
        """Test basic copy_at functionality."""
        source = Arrow(ORIGIN, RIGHT * 2, buff=0)
        new_start = UP * 2
        copied = VectorUtils.copy_at(source, new_start)

        # Should start at new position
        assert copied is not None
        assert isinstance(copied, Arrow)
        assert np.allclose(copied.get_start(), new_start, atol=1e-6)

    def test_copy_at_direction_preserved(self):
        """Test that direction is preserved."""
        source = Arrow(ORIGIN, RIGHT * 2 + UP, buff=0)
        new_start = LEFT * 3
        copied = VectorUtils.copy_at(source, new_start)

        # Get direction vectors
        source_dir = source.get_end() - source.get_start()
        copied_dir = copied.get_end() - copied.get_start()

        # Should have same direction
        assert np.allclose(source_dir, copied_dir, atol=1e-6)

    def test_copy_at_magnitude_preserved(self):
        """Test that magnitude is preserved."""
        source = Arrow(ORIGIN, RIGHT * 3 + UP * 2, buff=0)
        new_start = DOWN * 2 + LEFT
        copied = VectorUtils.copy_at(source, new_start)

        # Get magnitudes
        source_mag = np.linalg.norm(source.get_end() - source.get_start())
        copied_mag = np.linalg.norm(copied.get_end() - copied.get_start())

        # Should have same magnitude
        assert np.isclose(source_mag, copied_mag, atol=1e-6)

    def test_copy_at_with_color(self):
        """Test copy_at with custom color."""
        from manim import RED
        source = Arrow(ORIGIN, RIGHT * 2, buff=0)
        copied = VectorUtils.copy_at(source, UP, color=RED)

        # Color should be RED
        assert copied.get_color() == RED

    def test_copy_at_parallelogram(self):
        """Test copy_at for parallelogram construction."""
        vector_a = Arrow(ORIGIN, RIGHT * 2, buff=0)
        vector_b = Arrow(ORIGIN, UP * 1.5, buff=0)

        # Create parallelogram sides
        side_a = VectorUtils.copy_at(vector_a, vector_b.get_end())
        side_b = VectorUtils.copy_at(vector_b, vector_a.get_end())

        # side_a should start at vector_b's tip
        assert np.allclose(side_a.get_start(), vector_b.get_end(), atol=1e-6)

        # side_b should start at vector_a's tip
        assert np.allclose(side_b.get_start(), vector_a.get_end(), atol=1e-6)

        # side_a and side_b should meet at the same point (parallelogram closure)
        assert np.allclose(side_a.get_end(), side_b.get_end(), atol=1e-6)

    def test_copy_at_with_multiple_kwargs(self):
        """Test copy_at with multiple styling kwargs."""
        from manim import GREEN
        source = Arrow(ORIGIN, RIGHT * 2, buff=0)
        copied = VectorUtils.copy_at(
            source, UP * 2,
            color=GREEN,
            tip_length=0.3,
            stroke_width=5
        )

        # Check properties
        assert copied.get_color() == GREEN
        assert copied.get_stroke_width() == 5


class TestReverseAt:
    """Tests for the reverse_at function."""

    def test_reverse_at_basic(self):
        """Test basic reverse_at functionality."""
        source = Arrow(ORIGIN, RIGHT * 2, buff=0)
        new_start = UP * 2
        reversed_arrow = VectorUtils.reverse_at(source, new_start)

        # Should start at new position
        assert reversed_arrow is not None
        assert isinstance(reversed_arrow, Arrow)
        assert np.allclose(reversed_arrow.get_start(), new_start, atol=1e-6)

    def test_reverse_at_direction_reversed(self):
        """Test that direction is reversed."""
        source = Arrow(ORIGIN, RIGHT * 2, buff=0)
        new_start = UP
        reversed_arrow = VectorUtils.reverse_at(source, new_start)

        # Get direction vectors
        source_dir = source.get_end() - source.get_start()
        reversed_dir = reversed_arrow.get_end() - reversed_arrow.get_start()

        # Should have opposite direction
        assert np.allclose(source_dir, -reversed_dir, atol=1e-6)

    def test_reverse_at_magnitude_preserved(self):
        """Test that magnitude is preserved."""
        source = Arrow(ORIGIN, RIGHT * 3 + UP * 2, buff=0)
        new_start = DOWN * 2 + LEFT
        reversed_arrow = VectorUtils.reverse_at(source, new_start)

        # Get magnitudes
        source_mag = np.linalg.norm(source.get_end() - source.get_start())
        reversed_mag = np.linalg.norm(reversed_arrow.get_end() - reversed_arrow.get_start())

        # Should have same magnitude
        assert np.isclose(source_mag, reversed_mag, atol=1e-6)

    def test_reverse_at_with_color(self):
        """Test reverse_at with custom color."""
        from manim import PURPLE
        source = Arrow(ORIGIN, RIGHT * 2, buff=0)
        reversed_arrow = VectorUtils.reverse_at(source, UP, color=PURPLE)

        # Color should be PURPLE
        assert reversed_arrow.get_color() == PURPLE

    def test_reverse_at_vector_subtraction(self):
        """Test reverse_at for vector subtraction (a - b = a + (-b))."""
        # Define vectors for subtraction
        vector_a = Arrow(ORIGIN, RIGHT * 2, buff=0)
        vector_b = Arrow(ORIGIN, UP * 1.5, buff=0)

        # Create -b at origin
        neg_b_at_origin = VectorUtils.reverse_at(vector_b, ORIGIN)

        # Verify it's at origin with opposite direction
        assert np.allclose(neg_b_at_origin.get_start(), ORIGIN, atol=1e-6)

        vec_b_dir = vector_b.get_end() - vector_b.get_start()
        neg_b_dir = neg_b_at_origin.get_end() - neg_b_at_origin.get_start()
        assert np.allclose(vec_b_dir, -neg_b_dir, atol=1e-6)

    def test_reverse_at_tip_positioning(self):
        """Test reverse_at positioning at tip of another vector."""
        vector_a = Arrow(ORIGIN, RIGHT * 2, buff=0)
        vector_b = Arrow(ORIGIN, UP * 1.5, buff=0)

        # Create -b at tip of a
        neg_b_at_tip = VectorUtils.reverse_at(vector_b, vector_a.get_end())

        # Should start at tip of vector_a
        assert np.allclose(neg_b_at_tip.get_start(), vector_a.get_end(), atol=1e-6)

        # Should point downward (opposite of UP)
        vec_b_dir = vector_b.get_end() - vector_b.get_start()
        neg_b_dir = neg_b_at_tip.get_end() - neg_b_at_tip.get_start()
        assert np.allclose(vec_b_dir, -neg_b_dir, atol=1e-6)

    def test_reverse_at_with_multiple_kwargs(self):
        """Test reverse_at with multiple styling kwargs."""
        from manim import PURPLE
        source = Arrow(ORIGIN, RIGHT * 2, buff=0)
        reversed_arrow = VectorUtils.reverse_at(
            source, UP * 2,
            color=PURPLE,
            tip_length=0.25,
            stroke_width=4
        )

        # Check properties
        assert reversed_arrow.get_color() == PURPLE
        assert reversed_arrow.get_stroke_width() == 4


class TestVectorUtilsIntegration:
    """Integration tests for vector_utils functions."""

    def test_forward_backward_cancel(self):
        """Test that forward and backward cancel each other."""
        source = Arrow(ORIGIN, RIGHT * 2, buff=0)
        forward_then_backward = VectorUtils.backward(
            VectorUtils.forward(source, 1.5), 1.5
        )

        # Should return to original position
        assert np.allclose(
            forward_then_backward.get_start(),
            source.get_start(),
            atol=1e-6
        )
        assert np.allclose(
            forward_then_backward.get_end(),
            source.get_end(),
            atol=1e-6
        )

    def test_tail_at_tip_equals_shift_amount(self):
        """Test that tail_at_tip and shift_amount give same result."""
        vector_a = Arrow(ORIGIN, RIGHT * 2, buff=0)
        vector_b = Arrow(DOWN * 2, DOWN * 2 + UP * 1.5, buff=0)

        # Using tail_at_tip
        result_tail_at_tip = VectorUtils.tail_at_tip(vector_a, vector_b)

        # Using shift_amount
        shift = VectorUtils.shift_amount(vector_a, vector_b)
        result_shift = vector_b.copy().shift(shift)

        # Should give same result
        assert np.allclose(
            result_tail_at_tip.get_start(),
            result_shift.get_start(),
            atol=1e-6
        )
        assert np.allclose(
            result_tail_at_tip.get_end(),
            result_shift.get_end(),
            atol=1e-6
        )

    def test_copy_at_creates_parallelogram(self):
        """Test complete parallelogram construction with copy_at."""
        vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0)
        vector_b = Arrow(ORIGIN, UP * 2, buff=0)

        # Create all four sides
        side_a_copy = VectorUtils.copy_at(vector_a, vector_b.get_end())
        side_b_copy = VectorUtils.copy_at(vector_b, vector_a.get_end())

        # Check parallelogram property: opposite sides should meet
        assert np.allclose(side_a_copy.get_end(), side_b_copy.get_end(), atol=1e-6)

        # Check that diagonals work: resultant should go from origin to meeting point
        expected_resultant_end = side_a_copy.get_end()
        actual_resultant_end = (vector_a.get_end() - vector_a.get_start()) + \
                               (vector_b.get_end() - vector_b.get_start())

        assert np.allclose(expected_resultant_end, actual_resultant_end, atol=1e-6)

    def test_perp_move_shift_perpendicular(self):
        """Test that perp_move shifts perpendicular to direction."""
        side1 = Arrow(ORIGIN, RIGHT * 2, buff=0)
        side2 = VectorUtils.perp_move(side1, 2.0)

        # Check that directions are the same (perp_move doesn't rotate, it shifts)
        dir1 = side1.get_end() - side1.get_start()
        dir2 = side2.get_end() - side2.get_start()

        # Directions should be the same
        assert np.allclose(dir1, dir2, atol=1e-6)

        # But the shift should be perpendicular to the direction
        shift = side2.get_start() - side1.get_start()
        dot_product = np.dot(dir1, shift)
        assert np.isclose(dot_product, 0.0, atol=1e-6)


class TestProjectionMethods:
    """Tests for projection-related methods: project_onto, projection_line, projection_region."""

    def test_project_onto_basic(self):
        """Test basic projection onto a vector."""
        vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0)
        vector_b = Arrow(ORIGIN, RIGHT * 2 + UP * 1.5, buff=0)

        projection = VectorUtils.project_onto(vector_b, vector_a)

        # Should start at origin
        assert np.allclose(projection.get_start(), ORIGIN, atol=1e-6)

        # Projection should be along vector_a direction (horizontal)
        proj_dir = projection.get_end() - projection.get_start()
        assert np.isclose(proj_dir[1], 0.0, atol=1e-6)  # No vertical component
        assert proj_dir[0] > 0  # Positive horizontal component

    def test_project_onto_perpendicular_vectors(self):
        """Test projection of perpendicular vectors gives zero."""
        vector_a = Arrow(ORIGIN, RIGHT * 2, buff=0)
        vector_b = Arrow(ORIGIN, UP * 1.5, buff=0)

        projection = VectorUtils.project_onto(vector_b, vector_a)

        # Projection of perpendicular vector should be zero length
        proj_length = np.linalg.norm(projection.get_end() - projection.get_start())
        assert np.isclose(proj_length, 0.0, atol=1e-6)

    def test_project_onto_parallel_vectors(self):
        """Test projection of parallel vectors."""
        vector_a = Arrow(ORIGIN, RIGHT * 2, buff=0)
        vector_b = Arrow(ORIGIN, RIGHT * 1.5, buff=0)

        projection = VectorUtils.project_onto(vector_b, vector_a)

        # Projection should equal vector_b itself
        vec_b_dir = vector_b.get_end() - vector_b.get_start()
        proj_dir = projection.get_end() - projection.get_start()
        assert np.allclose(vec_b_dir, proj_dir, atol=1e-6)

    def test_project_onto_negative_projection(self):
        """Test projection with negative component."""
        vector_a = Arrow(ORIGIN, RIGHT * 2, buff=0)
        vector_b = Arrow(ORIGIN, LEFT * 1.5 + UP, buff=0)

        projection = VectorUtils.project_onto(vector_b, vector_a)

        # Projection should point left (negative x direction)
        proj_dir = projection.get_end() - projection.get_start()
        assert proj_dir[0] < 0

    def test_projection_line_basic(self):
        """Test basic projection line creation."""
        vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0)
        vector_b = Arrow(ORIGIN, RIGHT * 2 + UP * 1.5, buff=0)

        proj_line = VectorUtils.projection_line(vector_b, vector_a)

        # Line should end at tip of vector_b
        assert np.allclose(proj_line.get_end(), vector_b.get_end(), atol=1e-6)

        # Line should be perpendicular to vector_a
        vec_a_dir = vector_a.get_end() - vector_a.get_start()
        line_dir = proj_line.get_end() - proj_line.get_start()
        dot_product = np.dot(vec_a_dir, line_dir)
        assert np.isclose(dot_product, 0.0, atol=1e-6)

    def test_projection_line_perpendicular_vectors(self):
        """Test projection line for perpendicular vectors."""
        vector_a = Arrow(ORIGIN, RIGHT * 2, buff=0)
        vector_b = Arrow(ORIGIN, UP * 1.5, buff=0)

        proj_line = VectorUtils.projection_line(vector_b, vector_a)

        # Line should equal vector_b (from origin to its tip)
        line_length = np.linalg.norm(proj_line.get_end() - proj_line.get_start())
        vec_b_length = np.linalg.norm(vector_b.get_end() - vector_b.get_start())
        assert np.isclose(line_length, vec_b_length, atol=1e-6)

    def test_projection_line_parallel_vectors(self):
        """Test projection line for parallel vectors is zero."""
        vector_a = Arrow(ORIGIN, RIGHT * 2, buff=0)
        vector_b = Arrow(ORIGIN, RIGHT * 1.5, buff=0)

        proj_line = VectorUtils.projection_line(vector_b, vector_a)

        # Line should have zero length for parallel vectors
        line_length = np.linalg.norm(proj_line.get_end() - proj_line.get_start())
        assert np.isclose(line_length, 0.0, atol=1e-6)

    def test_projection_region_basic(self):
        """Test basic projection region creation."""
        vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0)
        vector_b = Arrow(ORIGIN, RIGHT * 2 + UP * 1.5, buff=0)

        region = VectorUtils.projection_region(vector_b, vector_a)

        # Should be a polygon
        from manim import Polygon
        assert isinstance(region, Polygon)

        # Should have 3 vertices (triangle)
        assert len(region.get_vertices()) == 3

    def test_projection_region_perpendicular_collapses(self):
        """Test that projection region collapses for perpendicular vectors."""
        vector_a = Arrow(ORIGIN, RIGHT * 2, buff=0)
        vector_b = Arrow(ORIGIN, UP * 1.5, buff=0)

        region = VectorUtils.projection_region(vector_b, vector_a)

        # All vertices except the last should be collinear (degenerate triangle)
        vertices = region.get_vertices()[:-1]  # Exclude closing vertex
        # First two vertices should be at origin (collapsed)
        assert np.allclose(vertices[0], vertices[1], atol=1e-6)

    def test_projection_region_contains_origin(self):
        """Test that projection region includes origin."""
        vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0)
        vector_b = Arrow(ORIGIN, RIGHT * 2 + UP * 1.5, buff=0)

        region = VectorUtils.projection_region(vector_b, vector_a)

        # First vertex should be at origin
        vertices = region.get_vertices()
        assert np.allclose(vertices[0], ORIGIN, atol=1e-6)

    def test_projection_consistency(self):
        """Test that projection methods are consistent with each other."""
        vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0)
        vector_b = Arrow(ORIGIN, RIGHT * 2 + UP * 1.5, buff=0)

        projection = VectorUtils.project_onto(vector_b, vector_a)
        proj_line = VectorUtils.projection_line(vector_b, vector_a)

        # Projection line should start where projection ends
        assert np.allclose(proj_line.get_start(), projection.get_end(), atol=1e-6)

        # Projection line should end at vector_b tip
        assert np.allclose(proj_line.get_end(), vector_b.get_end(), atol=1e-6)

        # Projection + projection_line should form a right angle
        proj_dir = projection.get_end() - projection.get_start()
        line_dir = proj_line.get_end() - proj_line.get_start()
        dot_product = np.dot(proj_dir, line_dir)

        # Should be perpendicular (dot product near zero)
        # Allow larger tolerance for numerical precision
        assert np.isclose(dot_product, 0.0, atol=1e-5)

    def test_projection_with_custom_styling(self):
        """Test that custom styling is applied."""
        from manim import RED
        vector_a = Arrow(ORIGIN, RIGHT * 3, buff=0)
        vector_b = Arrow(ORIGIN, RIGHT * 2 + UP * 1.5, buff=0)

        projection = VectorUtils.project_onto(vector_b, vector_a, color=RED, stroke_width=5)

        # Check styling was applied
        assert projection.get_color() == RED
        assert projection.get_stroke_width() == 5
