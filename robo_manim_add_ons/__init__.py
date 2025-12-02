"""
Robo Manim Add-ons: A collection of utilities and extensions for Manim Community Edition.
"""

__version__ = "0.1.0"

from .geometry_utils import perp, parallel, project, reflect
from .label_utils import vertex_labels, edge_labels
from .annotation_utils import distance_marker
from .intersection_utils import intersect_lines, intersect_line_circle

__all__ = ["perp", "parallel", "project", "reflect", "vertex_labels", "edge_labels", "distance_marker", "intersect_lines", "intersect_line_circle", "show_usage"]


def show_usage():
    """
    Display the API usage documentation.

    Example:
        >>> import robo_manim_add_ons
        >>> robo_manim_add_ons.show_usage()
    """
    import os
    usage_file = os.path.join(os.path.dirname(__file__), "USAGE.md")

    if os.path.exists(usage_file):
        with open(usage_file, 'r') as f:
            print(f.read())
    else:
        print("Usage documentation not found.")
        print("Visit: https://github.com/provility/robo-manim-add-ons")
