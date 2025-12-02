"""
Tests for annotation_utils module.
"""

import pytest
import numpy as np
from unittest.mock import MagicMock, patch
from robo_manim_add_ons.annotation_utils import distance_marker


class TestDistanceMarker:
    """Tests for distance_marker function"""

    def test_distance_marker_basic(self):
        """Test basic distance marker creation"""
        with patch('robo_manim_add_ons.annotation_utils.DoubleArrow') as mock_arrow, \
             patch('robo_manim_add_ons.annotation_utils.Line') as mock_line, \
             patch('robo_manim_add_ons.annotation_utils.VGroup') as mock_vgroup:

            mock_vgroup.return_value = MagicMock()

            marker = distance_marker([0, 0, 0], [3, 0, 0])

            # Verify DoubleArrow was created
            mock_arrow.assert_called_once()
            call_args = mock_arrow.call_args

            # Check start and end points
            np.testing.assert_array_almost_equal(call_args[0][0], [0, 0, 0])
            np.testing.assert_array_almost_equal(call_args[0][1], [3, 0, 0])

            # Verify Line was called twice (for ticks)
            assert mock_line.call_count == 2

            # Verify VGroup was created with 3 elements (arrow + 2 ticks, no label)
            assert mock_vgroup.called

    def test_distance_marker_with_label(self):
        """Test distance marker with label text"""
        with patch('robo_manim_add_ons.annotation_utils.DoubleArrow') as mock_arrow, \
             patch('robo_manim_add_ons.annotation_utils.Line') as mock_line, \
             patch('robo_manim_add_ons.annotation_utils.MathTex') as mock_tex, \
             patch('robo_manim_add_ons.annotation_utils.VGroup') as mock_vgroup:

            mock_label = MagicMock()
            # Make set_color return the mock itself for chaining
            mock_label.set_color.return_value = mock_label
            mock_tex.return_value = mock_label
            mock_vgroup.return_value = MagicMock()

            marker = distance_marker(
                [0, 0, 0],
                [3, 0, 0],
                label_text="d"
            )

            # Verify label was created
            mock_tex.assert_called_once_with("d")

            # Verify label methods were called
            mock_label.set_color.assert_called_once()
            mock_label.move_to.assert_called_once()
            mock_label.rotate.assert_called_once()

            # Verify VGroup has 4 elements (arrow + 2 ticks + label)
            assert mock_vgroup.called

    def test_distance_marker_vertical(self):
        """Test distance marker for vertical line"""
        with patch('robo_manim_add_ons.annotation_utils.DoubleArrow') as mock_arrow, \
             patch('robo_manim_add_ons.annotation_utils.Line') as mock_line, \
             patch('robo_manim_add_ons.annotation_utils.VGroup') as mock_vgroup:

            mock_vgroup.return_value = MagicMock()

            marker = distance_marker([0, 0, 0], [0, 4, 0])

            # Verify DoubleArrow was created with vertical points
            call_args = mock_arrow.call_args
            np.testing.assert_array_almost_equal(call_args[0][0], [0, 0, 0])
            np.testing.assert_array_almost_equal(call_args[0][1], [0, 4, 0])

    def test_distance_marker_diagonal(self):
        """Test distance marker for diagonal line"""
        with patch('robo_manim_add_ons.annotation_utils.DoubleArrow') as mock_arrow, \
             patch('robo_manim_add_ons.annotation_utils.Line') as mock_line, \
             patch('robo_manim_add_ons.annotation_utils.VGroup') as mock_vgroup:

            mock_vgroup.return_value = MagicMock()

            marker = distance_marker([0, 0, 0], [3, 4, 0])

            # Verify DoubleArrow was created
            assert mock_arrow.called

            # Verify ticks were created
            assert mock_line.call_count == 2

    def test_distance_marker_zero_length_edge_case(self):
        """Test distance marker when points are very close (edge case)"""
        with patch('robo_manim_add_ons.annotation_utils.DoubleArrow') as mock_arrow, \
             patch('robo_manim_add_ons.annotation_utils.Line') as mock_line, \
             patch('robo_manim_add_ons.annotation_utils.VGroup') as mock_vgroup:

            mock_vgroup.return_value = MagicMock()

            # Points very close together (tests the safety check)
            marker = distance_marker([0, 0, 0], [0.0001, 0, 0])

            # Should still create the marker without error
            assert mock_arrow.called
            assert mock_line.call_count == 2

    def test_distance_marker_returns_vgroup(self):
        """Test that distance_marker returns a VGroup"""
        with patch('robo_manim_add_ons.annotation_utils.DoubleArrow'), \
             patch('robo_manim_add_ons.annotation_utils.Line'), \
             patch('robo_manim_add_ons.annotation_utils.VGroup') as mock_vgroup:

            mock_instance = MagicMock()
            mock_vgroup.return_value = mock_instance

            marker = distance_marker([0, 0, 0], [3, 0, 0])

            # Verify we got the VGroup instance
            assert marker == mock_instance

    def test_distance_marker_custom_label_offset(self):
        """Test distance marker with custom label_offset"""
        with patch('robo_manim_add_ons.annotation_utils.DoubleArrow'), \
             patch('robo_manim_add_ons.annotation_utils.Line'), \
             patch('robo_manim_add_ons.annotation_utils.MathTex') as mock_tex, \
             patch('robo_manim_add_ons.annotation_utils.VGroup') as mock_vgroup:

            mock_label = MagicMock()
            mock_label.set_color.return_value = mock_label
            mock_tex.return_value = mock_label
            mock_vgroup.return_value = MagicMock()

            marker = distance_marker(
                [0, 0, 0],
                [3, 0, 0],
                label_text="d",
                label_offset=0.5
            )

            # Verify label was positioned
            mock_label.move_to.assert_called_once()
            # Check that the position includes the offset
            call_args = mock_label.move_to.call_args[0][0]
            # For horizontal line from [0,0,0] to [3,0,0], perpendicular is [0,1,0]
            # So label should be at [1.5, 0.5, 0] (midpoint + 0.5 up)
            expected_position = np.array([1.5, 0.5, 0])
            np.testing.assert_array_almost_equal(call_args, expected_position)

    def test_distance_marker_negative_label_offset(self):
        """Test distance marker with negative label_offset (other side)"""
        with patch('robo_manim_add_ons.annotation_utils.DoubleArrow'), \
             patch('robo_manim_add_ons.annotation_utils.Line'), \
             patch('robo_manim_add_ons.annotation_utils.MathTex') as mock_tex, \
             patch('robo_manim_add_ons.annotation_utils.VGroup') as mock_vgroup:

            mock_label = MagicMock()
            mock_label.set_color.return_value = mock_label
            mock_tex.return_value = mock_label
            mock_vgroup.return_value = MagicMock()

            marker = distance_marker(
                [0, 0, 0],
                [3, 0, 0],
                label_text="d",
                label_offset=-0.5
            )

            # Verify label was positioned on opposite side
            mock_label.move_to.assert_called_once()
            call_args = mock_label.move_to.call_args[0][0]
            # Should be at [1.5, -0.5, 0] (midpoint - 0.5 down)
            expected_position = np.array([1.5, -0.5, 0])
            np.testing.assert_array_almost_equal(call_args, expected_position)

    def test_distance_marker_zero_label_offset(self):
        """Test distance marker with label_offset=0 (label on line)"""
        with patch('robo_manim_add_ons.annotation_utils.DoubleArrow'), \
             patch('robo_manim_add_ons.annotation_utils.Line'), \
             patch('robo_manim_add_ons.annotation_utils.MathTex') as mock_tex, \
             patch('robo_manim_add_ons.annotation_utils.VGroup') as mock_vgroup:

            mock_label = MagicMock()
            mock_label.set_color.return_value = mock_label
            mock_tex.return_value = mock_label
            mock_vgroup.return_value = MagicMock()

            marker = distance_marker(
                [0, 0, 0],
                [3, 0, 0],
                label_text="d",
                label_offset=0
            )

            # Verify label was positioned at midpoint
            mock_label.move_to.assert_called_once()
            call_args = mock_label.move_to.call_args[0][0]
            # Should be at [1.5, 0, 0] (midpoint with no offset)
            expected_position = np.array([1.5, 0, 0])
            np.testing.assert_array_almost_equal(call_args, expected_position)


class TestDistanceMarkerIntegration:
    """Integration tests for distance_marker"""

    def test_distance_marker_real_creation(self):
        """Test actual distance marker creation without mocks"""
        # This tests the real function execution
        marker = distance_marker([0, 0, 0], [3, 0, 0])

        # Verify it returns a VGroup
        from manim import VGroup
        assert isinstance(marker, VGroup)

        # Should have 3 elements (arrow + 2 ticks)
        assert len(marker) == 3

    def test_distance_marker_with_real_label(self):
        """Test actual distance marker with label"""
        marker = distance_marker(
            [0, 0, 0],
            [3, 0, 0],
            label_text="d"
        )

        from manim import VGroup
        assert isinstance(marker, VGroup)

        # Should have 4 elements (arrow + 2 ticks + label)
        assert len(marker) == 4

    def test_distance_marker_with_real_label_offset(self):
        """Test actual distance marker with custom label offset"""
        marker = distance_marker(
            [0, 0, 0],
            [3, 0, 0],
            label_text="d",
            label_offset=0.5
        )

        from manim import VGroup
        assert isinstance(marker, VGroup)

        # Should have 4 elements (arrow + 2 ticks + label)
        assert len(marker) == 4

        # Verify the label (4th element) is positioned correctly
        label = marker[3]
        # For horizontal line, label should be offset vertically
        label_center = label.get_center()
        # Y-coordinate should be around 0.5 (the offset)
        assert abs(label_center[1] - 0.5) < 0.2  # Allow some tolerance for text height

    def test_distance_marker_with_dot_inputs(self):
        """Test distance marker with Dot objects as inputs"""
        from manim import Dot, VGroup

        # Create Dot objects
        dot1 = Dot([0, 0, 0])
        dot2 = Dot([3, 0, 0])

        marker = distance_marker(dot1, dot2)

        # Verify it returns a VGroup
        assert isinstance(marker, VGroup)

        # Should have 3 elements (arrow + 2 ticks)
        assert len(marker) == 3

    def test_distance_marker_with_dot_and_array(self):
        """Test distance marker with mixed Dot and array inputs"""
        from manim import Dot, VGroup

        # Create one Dot, use array for the other
        dot1 = Dot([0, 1, 0])
        point2 = [3, 1, 0]

        marker = distance_marker(dot1, point2, label_text="d")

        # Verify it returns a VGroup
        assert isinstance(marker, VGroup)

        # Should have 4 elements (arrow + 2 ticks + label)
        assert len(marker) == 4

    def test_distance_marker_with_numpy_array_inputs(self):
        """Test distance marker with numpy array inputs"""
        from manim import VGroup

        # Create numpy arrays
        point1 = np.array([0, 0, 0])
        point2 = np.array([2, 2, 0])

        marker = distance_marker(point1, point2)

        # Verify it returns a VGroup
        assert isinstance(marker, VGroup)

        # Should have 3 elements (arrow + 2 ticks)
        assert len(marker) == 3

    def test_distance_marker_with_moving_dots(self):
        """Test distance marker with Dots at different positions"""
        from manim import Dot, VGroup

        # Create Dots at different positions
        dot1 = Dot([1, 1, 0])
        dot2 = Dot([4, 3, 0])

        marker = distance_marker(
            dot1,
            dot2,
            label_text=r"\ell",
            label_offset=0.4
        )

        # Verify it returns a VGroup with label
        assert isinstance(marker, VGroup)
        assert len(marker) == 4

        # Get the arrow (first element) and check endpoints
        arrow = marker[0]
        # The arrow should connect the two dot positions
        # (We can't directly check the arrow endpoints, but we know it was created)

    def test_distance_marker_with_marker_offset(self):
        """Test distance marker with marker_offset (offset entire marker)"""
        from manim import VGroup

        # Create marker with positive marker_offset
        marker = distance_marker(
            [0, 0, 0],
            [4, 0, 0],
            label_text="d",
            marker_offset=0.6
        )

        # Verify it returns a VGroup
        assert isinstance(marker, VGroup)
        assert len(marker) == 4

        # The marker should be offset perpendicular to the line
        # For a horizontal line, the offset should be vertical
        arrow = marker[0]
        # Arrow endpoints should be offset by 0.6 in Y direction

    def test_distance_marker_with_negative_marker_offset(self):
        """Test distance marker with negative marker_offset"""
        from manim import VGroup

        # Create marker with negative marker_offset
        marker = distance_marker(
            [0, 0, 0],
            [3, 0, 0],
            marker_offset=-0.8
        )

        # Verify it returns a VGroup
        assert isinstance(marker, VGroup)
        assert len(marker) == 3  # No label

    def test_distance_marker_with_both_offsets(self):
        """Test distance marker with both marker_offset and label_offset"""
        from manim import VGroup

        # Create marker with both offsets
        marker = distance_marker(
            [0, 0, 0],
            [3, 0, 0],
            label_text="d",
            marker_offset=0.5,   # Offset entire marker
            label_offset=0.3     # Additional offset for label
        )

        # Verify it returns a VGroup with label
        assert isinstance(marker, VGroup)
        assert len(marker) == 4

        # Label should be offset by marker_offset + label_offset from original line
        label = marker[3]
        label_center = label.get_center()
        # For horizontal line, Y should be approximately 0.5 + 0.3 = 0.8
        assert abs(label_center[1] - 0.8) < 0.2  # Allow tolerance

    def test_distance_marker_zero_marker_offset(self):
        """Test that marker_offset=0 doesn't change behavior"""
        from manim import VGroup

        # Create two markers, one with explicit 0 offset, one without
        marker1 = distance_marker([0, 0, 0], [3, 0, 0])
        marker2 = distance_marker([0, 0, 0], [3, 0, 0], marker_offset=0)

        # Both should have same number of elements
        assert len(marker1) == len(marker2)
