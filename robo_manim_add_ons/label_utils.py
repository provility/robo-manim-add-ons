"""
Label utility functions for Manim polygons.

This module provides utilities to create vertex and edge labels for polygons.
"""

import numpy as np
from manim import MathTex, BLACK, BLUE, UP, VGroup, Arc


def vertex_labels(polygon, labels, scale=0.7, color=BLACK, buff=0.3):
    """
    Create vertex labels positioned outside polygon

    Args:
        polygon: Manim Polygon object
        labels: List of label strings ['A', 'B', 'C']
        scale: Label text scale (default 0.7)
        color: Label color (default BLACK)
        buff: Distance from vertex to label (default 0.3)

    Returns:
        List of positioned MathTex objects
    """
    vertices = polygon.get_vertices()
    center = polygon.get_center()
    label_objects = []

    for vertex, label_text in zip(vertices, labels):
        # Calculate outward direction from center
        direction = vertex - center
        norm = np.linalg.norm(direction)
        if norm > 0:
            direction = direction / norm
        else:
            direction = UP  # Fallback if vertex is at center

        # Create and position label
        label = MathTex(label_text)
        label.scale(scale)
        label.set_color(color)
        label.next_to(vertex, direction, buff=buff)

        label_objects.append(label)

    return label_objects


def edge_labels(polygon, labels, scale=0.6, color=BLACK, buff=0.2):
    """
    Create edge labels at midpoints with perpendicular offset

    Args:
        polygon: Manim Polygon object
        labels: List of label strings for each edge ['a', 'b', 'c']
        scale: Label text scale (default 0.6)
        color: Label color (default BLACK)
        buff: Distance from edge midpoint (default 0.2)

    Returns:
        List of positioned MathTex objects
    """
    vertices = polygon.get_vertices()
    label_objects = []
    n = len(vertices)

    for i, label_text in enumerate(labels):
        # Get edge endpoints
        p1 = vertices[i]
        p2 = vertices[(i + 1) % n]

        # Calculate midpoint
        midpoint = (p1 + p2) / 2

        # Calculate perpendicular direction (rotate edge vector 90°)
        edge_vector = p2 - p1
        perp = np.array([-edge_vector[1], edge_vector[0], 0])

        # Normalize perpendicular vector
        perp_norm = np.linalg.norm(perp)
        if perp_norm > 0:
            perp = perp / perp_norm
        else:
            perp = UP  # Fallback

        # Create and position label
        label = MathTex(label_text)
        label.scale(scale)
        label.set_color(color)
        label.next_to(midpoint, perp, buff=buff)

        label_objects.append(label)

    return label_objects


def angle_labels(polygon, labels, radius=0.4, scale=0.5, color=BLUE, arc_color=None):
    """
    Create angle arcs with labels at each vertex of a polygon.

    Args:
        polygon: Manim Polygon object
        labels: List of label strings for each angle [r'\\alpha', r'\\beta', r'\\gamma']
        radius: Radius of the angle arc (default 0.4)
        scale: Label text scale (default 0.5)
        color: Label color (default BLUE)
        arc_color: Arc color (default same as color)

    Returns:
        List of VGroups, each containing an Arc and MathTex label

    Example:
        >>> triangle = Polygon([-2, -1, 0], [2, -1, 0], [0, 2, 0])
        >>> angles = angle_labels(triangle, [r'\\alpha', r'\\beta', r'\\gamma'])
    """
    if arc_color is None:
        arc_color = color

    vertices = polygon.get_vertices()
    n = len(vertices)
    result = []

    for i in range(n):
        # Get current vertex and adjacent vertices
        prev_vertex = vertices[(i - 1) % n]
        curr_vertex = vertices[i]
        next_vertex = vertices[(i + 1) % n]

        # Vectors from current vertex to adjacent vertices
        v1 = prev_vertex - curr_vertex
        v2 = next_vertex - curr_vertex

        # Normalize vectors
        v1_norm = np.linalg.norm(v1)
        v2_norm = np.linalg.norm(v2)
        if v1_norm > 0:
            v1 = v1 / v1_norm
        if v2_norm > 0:
            v2 = v2 / v2_norm

        # Calculate angles from positive x-axis
        angle1 = np.arctan2(v1[1], v1[0])
        angle2 = np.arctan2(v2[1], v2[0])

        # Ensure we get the interior angle (smaller arc)
        diff = angle2 - angle1
        # Normalize to [-pi, pi]
        while diff > np.pi:
            diff -= 2 * np.pi
        while diff < -np.pi:
            diff += 2 * np.pi

        # Determine start angle and arc angle for interior
        if diff > 0:
            start_angle = angle1
            arc_angle = diff
        else:
            start_angle = angle2
            arc_angle = -diff

        # Create the arc
        arc = Arc(
            radius=radius,
            start_angle=start_angle,
            angle=arc_angle,
            arc_center=curr_vertex,
            color=arc_color
        )

        # Position label at the middle of the arc
        mid_angle = start_angle + arc_angle / 2
        label_pos = curr_vertex + radius * 1.6 * np.array([np.cos(mid_angle), np.sin(mid_angle), 0])

        # Create label
        label = MathTex(labels[i])
        label.scale(scale)
        label.set_color(color)
        label.move_to(label_pos)

        # Group arc and label
        group = VGroup(arc, label)
        result.append(group)

    return result
