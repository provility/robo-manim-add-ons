"""
Annotation utility functions for Manim diagrams.

This module provides utilities to create annotations like distance markers.
"""

import numpy as np
from manim import DoubleArrow, Line, MathTex, VGroup


def distance_marker(point1, point2, color="#1e40af", stroke_width=2, tick_size=0.25, label_text="", label_offset=0.3, marker_offset=0):
    """
    Create a distance marker with double arrow and perpendicular ticks.

    Args:
        point1: Starting point - can be:
                - List/tuple: [x, y, z]
                - numpy array
                - Manim Dot or any Mobject with get_center() method
        point2: Ending point - can be:
                - List/tuple: [x, y, z]
                - numpy array
                - Manim Dot or any Mobject with get_center() method
        color: Color of the marker (default "#1e40af")
        stroke_width: Width of the marker lines (default 2)
        tick_size: Size of perpendicular tick marks (default 0.25)
        label_text: Optional label text to display at midpoint (default "")
        label_offset: Distance to offset label perpendicular to line (default 0.3)
                     Positive values offset in one direction, negative in the other
        marker_offset: Distance to offset entire marker perpendicular to line (default 0)
                      Positive values offset in one direction, negative in the other
                      Useful for showing markers away from overlapping geometry

    Returns:
        VGroup containing the marker (arrow, ticks, and optional label)

    Example:
        >>> from manim import *
        >>> from robo_manim_add_ons import distance_marker
        >>>
        >>> # Basic usage
        >>> marker1 = distance_marker(
        ...     [0, 0, 0],
        ...     [3, 0, 0],
        ...     label_text="3",
        ...     color=BLUE
        ... )
        >>>
        >>> # Offset marker away from line
        >>> marker2 = distance_marker(
        ...     [0, 0, 0],
        ...     [3, 0, 0],
        ...     label_text="d",
        ...     marker_offset=0.5  # Marker offset perpendicular to line
        ... )
    """
    # Extract coordinates from point1
    if hasattr(point1, 'get_center'):
        start_pt = point1.get_center()
    else:
        start_pt = np.array(point1)

    # Extract coordinates from point2
    if hasattr(point2, 'get_center'):
        end_pt = point2.get_center()
    else:
        end_pt = np.array(point2)

    # Calculate direction and perpendicular
    direction = end_pt - start_pt
    perpendicular = np.array([-direction[1], direction[0], 0])

    # Normalize perpendicular (with safety check)
    if np.linalg.norm(perpendicular) > 0.001:
        perpendicular_normalized = perpendicular / np.linalg.norm(perpendicular)
    else:
        perpendicular_normalized = np.array([0, 1, 0])

    # Apply marker offset to shift entire marker perpendicular to line
    if marker_offset != 0:
        offset_vector = perpendicular_normalized * marker_offset
        start_pt = start_pt + offset_vector
        end_pt = end_pt + offset_vector

    # Create double arrow
    arrow = DoubleArrow(start_pt, end_pt, color=color, buff=0, stroke_width=stroke_width)

    tick_offset = perpendicular_normalized * tick_size
    tick_start = Line(start_pt - tick_offset, start_pt + tick_offset, color=color, stroke_width=stroke_width)
    tick_end = Line(end_pt - tick_offset, end_pt + tick_offset, color=color, stroke_width=stroke_width)

    # Create VGroup with or without label
    if label_text:
        marker_label = MathTex(label_text).set_color(color)
        # Position label at midpoint + perpendicular offset
        midpoint = (start_pt + end_pt) / 2
        label_position = midpoint + perpendicular_normalized * label_offset
        marker_label.move_to(label_position)
        angle = np.arctan2(direction[1], direction[0])
        marker_label.rotate(angle)
        marker_obj = VGroup(arrow, tick_start, tick_end, marker_label)
    else:
        marker_obj = VGroup(arrow, tick_start, tick_end)

    return marker_obj
