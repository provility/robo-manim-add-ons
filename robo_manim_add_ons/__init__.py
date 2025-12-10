"""
Robo Manim Add-ons: A collection of utilities and extensions for Manim Community Edition.
"""

__version__ = "0.2.3"

from .geometry_utils import perp, pll, project, reflect, xl
from .label_utils import vertex_labels, edge_labels, angle_labels
from .annotation_utils import dm, label, hatch
from .intersection_utils import ill, ilc, icc, ilp
from .vector_utils import VectorUtils, addv, subv, scalev, fw, bw, pm, cp, rv
from .point_utils import PointUtils, addp
from .text_utils import TextUtils, part, part2
from .transform_utils import translated, rotated, scaled
from .exp_utils import Exp, x, y, st, ed, mid, mag, uv, vec, ang, slope, val, pt, m2v, v2m, x2v, vl, hl, lra, vra, r2p, a2p, ln, vt, tri, aa, aa2, rangle, rect, cr, sss, sas, ssa
from .graph_utils import GraphUtils, graph
from .style_utils import stroke, fill, sopacity, fopacity, sw, Style, style
from .rogebra_scene import RogebraScene
from .circle_utils import tangentc, chord, normal, sector
from .triangle_utils import centroid, circumcenter, orthocenter, incenter, altitude

__all__ = ["perp", "pll", "project", "reflect", "xl", "vertex_labels", "edge_labels", "angle_labels", "dm", "label", "hatch", "ill", "ilc", "icc", "ilp", "VectorUtils", "addv", "subv", "scalev", "fw", "bw", "pm", "cp", "rv", "PointUtils", "addp", "TextUtils", "part", "part2", "translated", "rotated", "scaled", "Exp", "x", "y", "st", "ed", "mid", "mag", "uv", "vec", "ang", "slope", "val", "pt", "m2v", "v2m", "x2v", "vl", "hl", "lra", "vra", "r2p", "a2p", "ln", "vt", "tri", "aa", "aa2", "rangle", "rect", "cr", "sss", "sas", "ssa", "GraphUtils", "graph", "stroke", "fill", "sopacity", "fopacity", "sw", "Style", "style", "RogebraScene", "show_usage", "tangentc", "chord", "normal", "sector", "centroid", "circumcenter", "orthocenter", "incenter", "altitude"]


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
