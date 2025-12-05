from graphing.sheets.color_themes import CURRENT_COLOR_THEME
from manim import *


class UIStyleProps:
    def __init__(self, color, 
                 stroke_width=DEFAULT_STROKE_WIDTH,
                 fill_color=None, fill_opacity=0.1, 
                 scale_factor=1, dashed=False):
        self.color = color
        self.stroke_width = stroke_width
        self.fill_color = fill_color
        self.fill_opacity = fill_opacity
        self.scale_factor = scale_factor
        self.dashed = dashed
    @staticmethod
    def line_theme(color=CURRENT_COLOR_THEME.line_color(), stroke_width=6):
        return UIStyleProps(color=color, stroke_width=stroke_width)

    @staticmethod
    def point_theme(color=CURRENT_COLOR_THEME.point_color()):
        return UIStyleProps(color=color)

    @staticmethod
    def angle_theme(color=CURRENT_COLOR_THEME.angle_color()):
        return UIStyleProps(color=color)

    @staticmethod
    def ellipse_theme(color=CURRENT_COLOR_THEME.ellipse_color(), stroke_width=6):
        return UIStyleProps(color=color)

    @staticmethod
    def circle_theme(color=CURRENT_COLOR_THEME.circle_color(), stroke_width=6):
        return UIStyleProps(color=color)

    @staticmethod
    def triangle_theme(color=CURRENT_COLOR_THEME.triangle_color(), stroke_width=6):
        return UIStyleProps(color=color, stroke_width=stroke_width)

    @staticmethod
    def plot_theme(color=CURRENT_COLOR_THEME.plot_color(), stroke_width=6):
        return UIStyleProps(color=color)

    @staticmethod
    def number_line_theme(color=CURRENT_COLOR_THEME.number_line_color()):
        return UIStyleProps(color=color)

    @staticmethod
    def brace_theme(color=CURRENT_COLOR_THEME.brace_color()):
        return UIStyleProps(color=color)

    @staticmethod
    def distance_marker_theme(color=CURRENT_COLOR_THEME.distance_marker_color()):
        return UIStyleProps(color=color)

    @staticmethod
    def dynamic_prop_theme(color=CURRENT_COLOR_THEME.dynamic_prop_color()):
        return UIStyleProps(color=color)

    @staticmethod
    def trace_theme(color=CURRENT_COLOR_THEME.trace_color()):
        return UIStyleProps(color=color)

    @staticmethod
    def text_theme(color=CURRENT_COLOR_THEME.text_color()):
        return UIStyleProps(color=color)

    @staticmethod
    def arc_theme(color=CURRENT_COLOR_THEME.arc_color(), stroke_width=6):
        return UIStyleProps(color=color)

    @staticmethod
    def polygon_theme(color=CURRENT_COLOR_THEME.polygon_color(), stroke_width=6):
        return UIStyleProps(color=color)

    @staticmethod
    def vector_theme(color=CURRENT_COLOR_THEME.vector_color(), stroke_width=6):
        return UIStyleProps(color=color)
