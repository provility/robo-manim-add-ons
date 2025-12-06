"""
Robo Manim Add-ons: A collection of utilities and extensions for Manim Community Edition.
"""

__version__ = "0.1.0"

from .geometry_utils import perp, parallel, project, reflect, extended_line, pll, xl
from .label_utils import vertex_labels, edge_labels
from .annotation_utils import distance_marker, label, hatched_region, dm, hatch
from .intersection_utils import intersect_lines, intersect_line_circle, ill, ilc
from .vector_utils import VectorUtils, addv, subv, sclv
from .point_utils import PointUtils, addp
from .text_utils import TextUtils, text, text2
from .transform_utils import translated, rotated, scaled
from .arrow_utils import ArrowUtil
from .custom_objects import ArcDashedVMobject, ArcArrow
from .exp_utils import Exp, x, y, st, ed, mid, mag, uv, vec, ang, slope, val, pt, m2v, v2m, x2v, vl, hl, lra, vra, r2p, ln, vt, tri, aa, aa2, rect, cr, sss, sas, ssa
from .graph_utils import GraphUtils, graph
from .style_utils import stroke, fill, sopacity, fopacity, sw, Style, style
from .rogebra_scene import RogebraScene

__all__ = ["perp", "parallel", "project", "reflect", "extended_line", "pll", "xl", "vertex_labels", "edge_labels", "distance_marker", "label", "hatched_region", "dm", "hatch", "intersect_lines", "intersect_line_circle", "ill", "ilc", "VectorUtils", "addv", "subv", "sclv", "PointUtils", "addp", "TextUtils", "text", "text2", "translated", "rotated", "scaled", "ArrowUtil", "ArcDashedVMobject", "ArcArrow", "Exp", "x", "y", "st", "ed", "mid", "mag", "uv", "vec", "ang", "slope", "val", "pt", "m2v", "v2m", "x2v", "vl", "hl", "lra", "vra", "r2p", "ln", "vt", "tri", "aa", "aa2", "rect", "cr", "sss", "sas", "ssa", "GraphUtils", "graph", "stroke", "fill", "sopacity", "fopacity", "sw", "Style", "style", "RogebraScene", "show_usage"]


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
