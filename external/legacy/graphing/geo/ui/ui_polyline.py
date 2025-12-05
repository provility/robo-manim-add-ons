from graphing.ex_manim.poly_line import PolyLine
from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.model.model_poly_line_arrow import ModelPolyLineArrow
from graphing.geo.model.model_polyline import ModelPolyLine
from graphing.geo.ui.base_ui import BaseUI
from graphing.geo.ui.ui_style_props import UIStyleProps
from manim import *

class UIPolyLine(BaseUI):
    def __init__(self, geo_mapper: GeoMapper, 
                 model_poly_line:ModelPolyLine,
                 style_props:UIStyleProps = UIStyleProps.line_theme()):
        self.model_poly_line = model_poly_line
        super().__init__(style_props) 
        self.geo_mapper = geo_mapper
        self.ui_shape = self.build_shape()
        
    def build_shape(self):
        ui_points = [self.geo_mapper.model_to_ui(point) for point in self.model_poly_line.points]
        polyline = PolyLine(ui_points, color=self.color)
        return polyline
    
    def update(self):
        new_polyline = self._build_polyline()
        self.ui_shape.become(new_polyline)
       
    def view(self):
        return self.ui_shape
    
    def show(self):
        self.view().set_stroke(opacity=1)
    
    def hide(self):
        self.view().set_stroke(opacity=0)
    
    @property    
    def fill_opacity(self):
        return 0 
  