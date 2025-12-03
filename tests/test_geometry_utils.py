"""
Tests for geometry_utils module.
"""

import pytest
import numpy as np
from manim import Line, Dot, ORIGIN, LEFT, RIGHT, UP, DOWN


from robo_manim_add_ons.geometry_utils import perp, parallel, project, reflect, extended_line


class TestPerp:
    """Tests for the perp function."""

    def test_perp_basic(self):
        """Test basic perpendicular line creation."""
        line = Line(LEFT, RIGHT)
        dot = Dot(ORIGIN)
        perp_line = perp(line, dot, 2.0)

        # Should create a vertical line of length 2
        assert perp_line is not None
        assert isinstance(perp_line, Line)

        # Check length
        length = np.linalg.norm(perp_line.get_end() - perp_line.get_start())
        assert np.isclose(length, 2.0, atol=1e-6)

    def test_perp_placement_mid(self):
        """Test perpendicular line with mid placement."""
        line = Line(LEFT, RIGHT)
        dot = Dot(ORIGIN)
        perp_line = perp(line, dot, 2.0, placement="mid")

        # Dot should be at midpoint of new line
        midpoint = (perp_line.get_start() + perp_line.get_end()) / 2
        dot_pos = dot.get_center()
        assert np.allclose(midpoint, dot_pos, atol=1e-6)

    def test_perp_placement_start(self):
        """Test perpendicular line with start placement."""
        line = Line(LEFT, RIGHT)
        dot = Dot(ORIGIN)
        perp_line = perp(line, dot, 2.0, placement="start")

        # Dot should be at start of new line
        start_pos = perp_line.get_start()
        dot_pos = dot.get_center()
        assert np.allclose(start_pos, dot_pos, atol=1e-6)

    def test_perp_placement_end(self):
        """Test perpendicular line with end placement."""
        line = Line(LEFT, RIGHT)
        dot = Dot(ORIGIN)
        perp_line = perp(line, dot, 2.0, placement="end")

        # Dot should be at end of new line
        end_pos = perp_line.get_end()
        dot_pos = dot.get_center()
        assert np.allclose(end_pos, dot_pos, atol=1e-6)

    def test_perp_orthogonality(self):
        """Test that the perpendicular line is actually perpendicular."""
        line = Line(LEFT, RIGHT)
        dot = Dot(ORIGIN)
        perp_line = perp(line, dot, 2.0)

        # Get direction vectors
        line_dir = line.get_end() - line.get_start()
        perp_dir = perp_line.get_end() - perp_line.get_start()

        # Dot product should be zero for perpendicular vectors
        dot_product = np.dot(line_dir, perp_dir)
        assert np.isclose(dot_product, 0.0, atol=1e-6)

    def test_perp_with_different_dot_position(self):
        """Test perpendicular line when dot is not at origin."""
        line = Line(LEFT, RIGHT)
        dot = Dot(UP * 2 + RIGHT)
        perp_line = perp(line, dot, 3.0, placement="mid")

        # Dot should still be at midpoint
        midpoint = (perp_line.get_start() + perp_line.get_end()) / 2
        dot_pos = dot.get_center()
        assert np.allclose(midpoint, dot_pos, atol=1e-6)

        # Check length
        length = np.linalg.norm(perp_line.get_end() - perp_line.get_start())
        assert np.isclose(length, 3.0, atol=1e-6)

    def test_perp_invalid_placement(self):
        """Test that invalid placement raises ValueError."""
        line = Line(LEFT, RIGHT)
        dot = Dot(ORIGIN)

        with pytest.raises(ValueError, match="placement must be"):
            perp(line, dot, 2.0, placement="invalid")


class TestParallel:
    """Tests for the parallel function."""

    def test_parallel_basic(self):
        """Test basic parallel line creation."""
        line = Line(LEFT, RIGHT)
        dot = Dot(ORIGIN)
        parallel_line = parallel(line, dot, 2.0)

        # Should create a horizontal line of length 2
        assert parallel_line is not None
        assert isinstance(parallel_line, Line)

        # Check length
        length = np.linalg.norm(parallel_line.get_end() - parallel_line.get_start())
        assert np.isclose(length, 2.0, atol=1e-6)

    def test_parallel_placement_mid(self):
        """Test parallel line with mid placement."""
        line = Line(LEFT, RIGHT)
        dot = Dot(ORIGIN)
        parallel_line = parallel(line, dot, 2.0, placement="mid")

        # Dot should be at midpoint of new line
        midpoint = (parallel_line.get_start() + parallel_line.get_end()) / 2
        dot_pos = dot.get_center()
        assert np.allclose(midpoint, dot_pos, atol=1e-6)

    def test_parallel_placement_start(self):
        """Test parallel line with start placement."""
        line = Line(LEFT, RIGHT)
        dot = Dot(ORIGIN)
        parallel_line = parallel(line, dot, 2.0, placement="start")

        # Dot should be at start of new line
        start_pos = parallel_line.get_start()
        dot_pos = dot.get_center()
        assert np.allclose(start_pos, dot_pos, atol=1e-6)

    def test_parallel_placement_end(self):
        """Test parallel line with end placement."""
        line = Line(LEFT, RIGHT)
        dot = Dot(ORIGIN)
        parallel_line = parallel(line, dot, 2.0, placement="end")

        # Dot should be at end of new line
        end_pos = parallel_line.get_end()
        dot_pos = dot.get_center()
        assert np.allclose(end_pos, dot_pos, atol=1e-6)

    def test_parallel_same_direction(self):
        """Test that the parallel line has the same direction."""
        line = Line(LEFT, RIGHT)
        dot = Dot(UP)
        parallel_line = parallel(line, dot, 3.0)

        # Get direction vectors
        line_dir = line.get_end() - line.get_start()
        parallel_dir = parallel_line.get_end() - parallel_line.get_start()

        # Normalize both vectors
        line_dir_norm = line_dir / np.linalg.norm(line_dir)
        parallel_dir_norm = parallel_dir / np.linalg.norm(parallel_dir)

        # They should be parallel (same or opposite direction)
        # For same direction, the cross product should be zero
        cross_product = np.cross(line_dir_norm, parallel_dir_norm)
        assert np.allclose(cross_product, 0.0, atol=1e-6)

    def test_parallel_with_different_dot_position(self):
        """Test parallel line when dot is not at origin."""
        line = Line(LEFT, RIGHT)
        dot = Dot(DOWN * 2 + LEFT)
        parallel_line = parallel(line, dot, 4.0, placement="mid")

        # Dot should still be at midpoint
        midpoint = (parallel_line.get_start() + parallel_line.get_end()) / 2
        dot_pos = dot.get_center()
        assert np.allclose(midpoint, dot_pos, atol=1e-6)

        # Check length
        length = np.linalg.norm(parallel_line.get_end() - parallel_line.get_start())
        assert np.isclose(length, 4.0, atol=1e-6)

    def test_parallel_invalid_placement(self):
        """Test that invalid placement raises ValueError."""
        line = Line(LEFT, RIGHT)
        dot = Dot(ORIGIN)

        with pytest.raises(ValueError, match="placement must be"):
            parallel(line, dot, 2.0, placement="invalid")


class TestProject:
    """Tests for the project function."""

    def test_project_basic(self):
        """Test basic projection."""
        line = Line(LEFT, RIGHT)
        point = Dot(UP)
        projection = project(line, point)

        # Projection of UP onto horizontal line should be at ORIGIN
        assert projection is not None
        assert isinstance(projection, Dot)
        assert np.allclose(projection.get_center(), ORIGIN, atol=1e-6)

    def test_project_with_numpy_array(self):
        """Test projection with numpy array input."""
        line = Line(LEFT, RIGHT)
        point_array = np.array([0, 1, 0])  # Same as UP
        projection = project(line, point_array)

        # Should give same result as with Dot
        assert projection is not None
        assert np.allclose(projection.get_center(), ORIGIN, atol=1e-6)

    def test_project_on_diagonal_line(self):
        """Test projection on a diagonal line."""
        line = Line(ORIGIN, RIGHT + UP)
        point = Dot(RIGHT)
        projection = project(line, point)

        # Projection should be on the line
        proj_pos = projection.get_center()
        line_start = line.get_start()
        line_end = line.get_end()
        line_dir = line_end - line_start

        # Check if projection is on the line
        vec_to_proj = proj_pos - line_start
        cross = np.cross(vec_to_proj, line_dir)
        assert np.allclose(cross, 0.0, atol=1e-6)

    def test_project_outside_segment(self):
        """Test projection that falls outside the original line segment."""
        line = Line(LEFT, RIGHT)
        point = Dot(LEFT * 3 + UP)  # Far to the left
        projection = project(line, point)

        # Should still return a projection (extended infinitely)
        assert projection is not None
        proj_pos = projection.get_center()
        # Projection should be at LEFT * 3 (on the extended horizontal line)
        assert np.allclose(proj_pos, LEFT * 3, atol=1e-6)

    def test_project_point_on_line(self):
        """Test projection of a point already on the line."""
        line = Line(LEFT, RIGHT)
        point = Dot(ORIGIN)
        projection = project(line, point)

        # Projection should be at the same position
        assert np.allclose(projection.get_center(), ORIGIN, atol=1e-6)


class TestReflect:
    """Tests for the reflect function."""

    def test_reflect_basic(self):
        """Test basic reflection."""
        line = Line(LEFT, RIGHT)  # Horizontal line
        point = Dot(UP)
        reflected = reflect(line, point)

        # Reflection of UP across horizontal line should be DOWN
        assert reflected is not None
        assert isinstance(reflected, Dot)
        assert np.allclose(reflected.get_center(), DOWN, atol=1e-6)

    def test_reflect_with_numpy_array(self):
        """Test reflection with numpy array input."""
        line = Line(LEFT, RIGHT)
        point_array = np.array([0, 1, 0])  # Same as UP
        reflected = reflect(line, point_array)

        # Should give same result as with Dot
        assert reflected is not None
        assert np.allclose(reflected.get_center(), DOWN, atol=1e-6)

    def test_reflect_on_diagonal_line(self):
        """Test reflection across a diagonal line."""
        # 45-degree line through origin
        line = Line(LEFT + DOWN, RIGHT + UP)
        point = Dot(RIGHT)
        reflected = reflect(line, point)

        # Reflection of RIGHT across 45-degree line should be UP
        assert reflected is not None
        assert np.allclose(reflected.get_center(), UP, atol=1e-6)

    def test_reflect_point_on_line(self):
        """Test reflection of a point on the line."""
        line = Line(LEFT, RIGHT)
        point = Dot(ORIGIN)
        reflected = reflect(line, point)

        # Reflection should be at the same position
        assert np.allclose(reflected.get_center(), ORIGIN, atol=1e-6)

    def test_reflect_symmetry(self):
        """Test that reflecting twice returns to original position."""
        line = Line(LEFT + DOWN, RIGHT + UP)
        point = Dot(UP * 2 + RIGHT)

        # Reflect once
        reflected1 = reflect(line, point)
        # Reflect again
        reflected2 = reflect(line, reflected1)

        # Should return to original position
        assert np.allclose(reflected2.get_center(), point.get_center(), atol=1e-6)

    def test_reflect_distance_preservation(self):
        """Test that distance to line is preserved."""
        line = Line(LEFT, RIGHT)
        point = Dot(UP * 3)
        reflected = reflect(line, point)

        # Distance from point to line
        projection = project(line, point)
        dist_original = np.linalg.norm(point.get_center() - projection.get_center())

        # Distance from reflected point to line
        dist_reflected = np.linalg.norm(reflected.get_center() - projection.get_center())

        # Should be equal
        assert np.isclose(dist_original, dist_reflected, atol=1e-6)


class TestExtendedLine:
    """Tests for the extended_line function."""

    def test_extended_line_from_end(self):
        """Test extending from the end of a line (proportion=1.0)."""
        line = Line(LEFT, RIGHT)
        ext_line = extended_line(line, proportion=1.0, length=2.0)

        # New line should start at the end of original line
        assert ext_line is not None
        assert isinstance(ext_line, Line)
        assert np.allclose(ext_line.get_start(), RIGHT, atol=1e-6)

        # Check length
        length = np.linalg.norm(ext_line.get_end() - ext_line.get_start())
        assert np.isclose(length, 2.0, atol=1e-6)

    def test_extended_line_from_start(self):
        """Test extending from the start of a line (proportion=0.0)."""
        line = Line(LEFT, RIGHT)
        ext_line = extended_line(line, proportion=0.0, length=1.5)

        # New line should start at the beginning of original line
        assert np.allclose(ext_line.get_start(), LEFT, atol=1e-6)

        # Check length
        length = np.linalg.norm(ext_line.get_end() - ext_line.get_start())
        assert np.isclose(length, 1.5, atol=1e-6)

    def test_extended_line_from_midpoint(self):
        """Test extending from the midpoint of a line (proportion=0.5)."""
        line = Line(LEFT, RIGHT)
        ext_line = extended_line(line, proportion=0.5, length=1.0)

        # New line should start at the midpoint
        midpoint = (line.get_start() + line.get_end()) / 2
        assert np.allclose(ext_line.get_start(), midpoint, atol=1e-6)

        # Check length
        length = np.linalg.norm(ext_line.get_end() - ext_line.get_start())
        assert np.isclose(length, 1.0, atol=1e-6)

    def test_extended_line_same_direction(self):
        """Test that extended line has the same direction as original."""
        line = Line(LEFT, RIGHT)
        ext_line = extended_line(line, proportion=1.0, length=2.0)

        # Get direction vectors
        line_dir = line.get_end() - line.get_start()
        ext_dir = ext_line.get_end() - ext_line.get_start()

        # Normalize both
        line_dir_norm = line_dir / np.linalg.norm(line_dir)
        ext_dir_norm = ext_dir / np.linalg.norm(ext_dir)

        # Should be in the same direction
        assert np.allclose(line_dir_norm, ext_dir_norm, atol=1e-6)

    def test_extended_line_diagonal(self):
        """Test extending a diagonal line."""
        line = Line(ORIGIN, RIGHT + UP)
        ext_line = extended_line(line, proportion=1.0, length=np.sqrt(2))

        # Should extend diagonally
        assert ext_line is not None

        # Check that it starts at the end of original line
        assert np.allclose(ext_line.get_start(), RIGHT + UP, atol=1e-6)

        # Check direction is preserved
        line_dir = line.get_end() - line.get_start()
        ext_dir = ext_line.get_end() - ext_line.get_start()
        line_dir_norm = line_dir / np.linalg.norm(line_dir)
        ext_dir_norm = ext_dir / np.linalg.norm(ext_dir)
        assert np.allclose(line_dir_norm, ext_dir_norm, atol=1e-6)

    def test_extended_line_quarter_point(self):
        """Test extending from a quarter point (proportion=0.25)."""
        line = Line(LEFT * 4, RIGHT * 4)
        ext_line = extended_line(line, proportion=0.25, length=2.0)

        # Calculate expected start point
        expected_start = LEFT * 4 + 0.25 * (RIGHT * 4 - LEFT * 4)
        assert np.allclose(ext_line.get_start(), expected_start, atol=1e-6)

        # Check length
        length = np.linalg.norm(ext_line.get_end() - ext_line.get_start())
        assert np.isclose(length, 2.0, atol=1e-6)

    def test_extended_line_invalid_proportion_too_low(self):
        """Test that proportion < 0 raises ValueError."""
        line = Line(LEFT, RIGHT)

        with pytest.raises(ValueError, match="proportion must be between 0 and 1"):
            extended_line(line, proportion=-0.1, length=2.0)

    def test_extended_line_invalid_proportion_too_high(self):
        """Test that proportion > 1 raises ValueError."""
        line = Line(LEFT, RIGHT)

        with pytest.raises(ValueError, match="proportion must be between 0 and 1"):
            extended_line(line, proportion=1.5, length=2.0)

    def test_extended_line_various_proportions(self):
        """Test extended lines at various proportions maintain correct properties."""
        line = Line(LEFT * 2, RIGHT * 2)
        proportions = [0.0, 0.1, 0.3, 0.5, 0.7, 0.9, 1.0]
        length = 1.5

        for prop in proportions:
            ext_line = extended_line(line, proportion=prop, length=length)

            # Check length is correct
            actual_length = np.linalg.norm(ext_line.get_end() - ext_line.get_start())
            assert np.isclose(actual_length, length, atol=1e-6)

            # Check direction is preserved
            line_dir = line.get_end() - line.get_start()
            ext_dir = ext_line.get_end() - ext_line.get_start()
            line_dir_norm = line_dir / np.linalg.norm(line_dir)
            ext_dir_norm = ext_dir / np.linalg.norm(ext_dir)
            assert np.allclose(line_dir_norm, ext_dir_norm, atol=1e-6)

    def test_extended_line_vertical(self):
        """Test extending a vertical line."""
        line = Line(DOWN, UP)
        ext_line = extended_line(line, proportion=1.0, length=1.0)

        # Should start at UP and extend upward
        assert np.allclose(ext_line.get_start(), UP, atol=1e-6)

        # End should be further up
        expected_end = UP + np.array([0, 1, 0])
        assert np.allclose(ext_line.get_end(), expected_end, atol=1e-6)


class TestGeometryUtilsIntegration:
    """Integration tests for geometry_utils functions."""

    def test_perp_and_parallel_together(self):
        """Test using perp and parallel together."""
        # Create a horizontal line
        horizontal = Line(LEFT, RIGHT)
        dot1 = Dot(ORIGIN)

        # Create perpendicular (should be vertical)
        vertical = perp(horizontal, dot1, 2.0)

        # Create parallel to horizontal at a different point
        dot2 = Dot(UP)
        horizontal2 = parallel(horizontal, dot2, 3.0)

        # Verify perpendicularity
        h_dir = horizontal.get_end() - horizontal.get_start()
        v_dir = vertical.get_end() - vertical.get_start()
        assert np.isclose(np.dot(h_dir, v_dir), 0.0, atol=1e-6)

        # Verify parallelism
        h2_dir = horizontal2.get_end() - horizontal2.get_start()
        cross = np.cross(h_dir / np.linalg.norm(h_dir), h2_dir / np.linalg.norm(h2_dir))
        assert np.allclose(cross, 0.0, atol=1e-6)

    def test_project_and_reflect_together(self):
        """Test using project and reflect together."""
        line = Line(LEFT, RIGHT)
        point = Dot(UP * 2)

        # Get projection
        projection = project(line, point)

        # Get reflection
        reflected = reflect(line, point)

        # Projection should be midpoint between point and reflection
        midpoint = (point.get_center() + reflected.get_center()) / 2
        assert np.allclose(projection.get_center(), midpoint, atol=1e-6)

        # Point and reflection should be equidistant from projection
        dist1 = np.linalg.norm(point.get_center() - projection.get_center())
        dist2 = np.linalg.norm(reflected.get_center() - projection.get_center())
        assert np.isclose(dist1, dist2, atol=1e-6)
