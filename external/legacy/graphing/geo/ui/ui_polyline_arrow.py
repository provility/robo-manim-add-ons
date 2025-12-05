from graphing.ex_manim.poly_line import PolyLine
from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.model.model_poly_line_arrow import ModelPolyLineArrow
from graphing.geo.ui.base_ui import BaseUI
from graphing.geo.ui.ui_style_props import UIStyleProps
from manim import *

class UIPolyLineArrow(BaseUI):
    def __init__(self, geo_mapper: GeoMapper, 
                 model_poly_line_arrow:ModelPolyLineArrow,
                 style_props:UIStyleProps = UIStyleProps.line_theme()):
        self.model_poly_line_arrow = model_poly_line_arrow
        super().__init__(style_props) 
        self.geo_mapper = geo_mapper
        self.ui_shape = self.build_shape()
        
    def build_shape(self):
        polyline, arrow_tip = self._build_line_and_arrow()
        return VGroup(polyline, arrow_tip)
    
    def _get_line_and_arrow(self):
        polyline = self.ui_shape[0]
        arrow_tip = self.ui_shape[1]
        return polyline, arrow_tip
    
    def _build_line_and_arrow(self):
        ui_points = [self.geo_mapper.model_to_ui(point) for point in self.model_poly_line_arrow.points]
        polyline = PolyLine(ui_points, color=self.color)
        arrow_tip_start = self.geo_mapper.model_to_ui(self.model_poly_line_arrow.points[len(self.model_poly_line_arrow.points) - 2])
        arrow_tip_end = self.geo_mapper.model_to_ui(self.model_poly_line_arrow.points[len(self.model_poly_line_arrow.points) - 1]) 
        arrow_tip = Arrow(
            start=arrow_tip_start,
            end=arrow_tip_end,
            color=self.color)
        return polyline, arrow_tip

    def update(self):
        previous_polyline, previous_arrow_tip = self._get_line_and_arrow()
        new_polyline, new_arrow_tip = self._build_line_and_arrow()
        previous_polyline.become(new_polyline)
        previous_arrow_tip.become(new_arrow_tip)
       

    def shape_to_trace(self):
        polyline, arrow_tip = self._get_line_and_arrow()
        return polyline
    
    def view(self):
        return self.ui_shape

  