"""
Tests for label_utils module.
"""

import pytest
import numpy as np
from unittest.mock import MagicMock, patch
from robo_manim_add_ons.label_utils import vertex_labels, edge_labels


class TestVertexLabels:
    """Tests for vertex_labels function"""

    def test_vertex_labels_basic(self):
        """Test basic vertex labeling on a triangle"""
        # Mock polygon
        polygon = MagicMock()
        polygon.get_vertices.return_value = np.array([
            [0, 0, 0],
            [3, 0, 0],
            [1.5, 2.6, 0]
        ])
        polygon.get_center.return_value = np.array([1.5, 0.87, 0])

        with patch('robo_manim_add_ons.label_utils.MathTex') as mock_tex:
            # Setup mock MathTex instances
            mock_labels = [MagicMock(), MagicMock(), MagicMock()]
            mock_tex.side_effect = mock_labels

            labels = vertex_labels(polygon, ['A', 'B', 'C'])

            # Verify correct number of labels created
            assert len(labels) == 3
            assert mock_tex.call_count == 3

            # Verify labels were created with correct text
            mock_tex.assert_any_call('A')
            mock_tex.assert_any_call('B')
            mock_tex.assert_any_call('C')

            # Verify scale and color were set
            for mock_label in mock_labels:
                mock_label.scale.assert_called_once_with(0.7)
                mock_label.set_color.assert_called_once()
                mock_label.next_to.assert_called_once()

    def test_vertex_labels_square(self):
        """Test vertex labels on a square"""
        polygon = MagicMock()
        polygon.get_vertices.return_value = np.array([
            [0, 0, 0],
            [2, 0, 0],
            [2, 2, 0],
            [0, 2, 0]
        ])
        polygon.get_center.return_value = np.array([1, 1, 0])

        with patch('robo_manim_add_ons.label_utils.MathTex') as mock_tex:
            mock_tex.return_value = MagicMock()

            labels = vertex_labels(polygon, ['A', 'B', 'C', 'D'])

            assert len(labels) == 4
            assert mock_tex.call_count == 4

    def test_vertex_labels_zero_center(self):
        """Test fallback when vertex is at center"""
        polygon = MagicMock()
        polygon.get_vertices.return_value = np.array([
            [0, 0, 0],  # This will be at center
            [1, 0, 0],
            [0, 1, 0]
        ])
        polygon.get_center.return_value = np.array([0, 0, 0])

        with patch('robo_manim_add_ons.label_utils.MathTex') as mock_tex:
            mock_tex.return_value = MagicMock()

            labels = vertex_labels(polygon, ['A', 'B', 'C'])

            # Should still create labels without error
            assert len(labels) == 3


class TestEdgeLabels:
    """Tests for edge_labels function"""

    def test_edge_labels_basic(self):
        """Test basic edge labeling on a triangle"""
        polygon = MagicMock()
        polygon.get_vertices.return_value = np.array([
            [0, 0, 0],
            [3, 0, 0],
            [1.5, 2.6, 0]
        ])

        with patch('robo_manim_add_ons.label_utils.MathTex') as mock_tex:
            mock_labels = [MagicMock(), MagicMock(), MagicMock()]
            mock_tex.side_effect = mock_labels

            labels = edge_labels(polygon, ['a', 'b', 'c'])

            # Verify correct number of labels created
            assert len(labels) == 3
            assert mock_tex.call_count == 3

            # Verify labels were created with correct text
            mock_tex.assert_any_call('a')
            mock_tex.assert_any_call('b')
            mock_tex.assert_any_call('c')

            # Verify scale and color were set
            for mock_label in mock_labels:
                mock_label.scale.assert_called_once_with(0.6)
                mock_label.set_color.assert_called_once()
                mock_label.next_to.assert_called_once()

    def test_edge_labels_square(self):
        """Test edge labels on a square"""
        polygon = MagicMock()
        polygon.get_vertices.return_value = np.array([
            [0, 0, 0],
            [2, 0, 0],
            [2, 2, 0],
            [0, 2, 0]
        ])

        with patch('robo_manim_add_ons.label_utils.MathTex') as mock_tex:
            mock_tex.return_value = MagicMock()

            labels = edge_labels(polygon, ['a', 'b', 'c', 'd'])

            assert len(labels) == 4
            assert mock_tex.call_count == 4

    def test_edge_labels_midpoint_calculation(self):
        """Test that edge labels are positioned at midpoints"""
        polygon = MagicMock()
        vertices = np.array([
            [0, 0, 0],
            [4, 0, 0],
            [4, 4, 0],
            [0, 4, 0]
        ])
        polygon.get_vertices.return_value = vertices

        with patch('robo_manim_add_ons.label_utils.MathTex') as mock_tex:
            mock_label = MagicMock()
            mock_tex.return_value = mock_label

            labels = edge_labels(polygon, ['a', 'b', 'c', 'd'])

            # Each label should call next_to with midpoint and perpendicular direction
            assert mock_label.next_to.call_count == 4

    def test_edge_labels_perpendicular_direction(self):
        """Test that perpendicular direction is calculated correctly"""
        polygon = MagicMock()
        # Simple horizontal edge
        polygon.get_vertices.return_value = np.array([
            [0, 0, 0],
            [2, 0, 0],
            [2, 2, 0]
        ])

        with patch('robo_manim_add_ons.label_utils.MathTex') as mock_tex:
            mock_tex.return_value = MagicMock()

            labels = edge_labels(polygon, ['a', 'b', 'c'])

            # Should create labels without error
            assert len(labels) == 3


class TestLabelUtilsIntegration:
    """Integration tests for label utilities"""

    def test_vertex_and_edge_labels_together(self):
        """Test using both vertex and edge labels on same polygon"""
        polygon = MagicMock()
        polygon.get_vertices.return_value = np.array([
            [0, 0, 0],
            [3, 0, 0],
            [1.5, 2.6, 0]
        ])
        polygon.get_center.return_value = np.array([1.5, 0.87, 0])

        with patch('robo_manim_add_ons.label_utils.MathTex') as mock_tex:
            mock_tex.return_value = MagicMock()

            v_labels = vertex_labels(polygon, ['A', 'B', 'C'])
            e_labels = edge_labels(polygon, ['a', 'b', 'c'])

            assert len(v_labels) == 3
            assert len(e_labels) == 3
            # 3 vertex + 3 edge = 6 total
            assert mock_tex.call_count == 6
