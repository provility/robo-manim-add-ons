from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.ui.ui_style_props import UIStyleProps
from .base_ui import BaseUI
from ..model.model_triangle import ModelTriangle
from manim import *
class UITriangle(BaseUI):
      def __init__(self, geo_mapper:GeoMapper, model_triangle:ModelTriangle,  style_props:UIStyleProps = UIStyleProps.triangle_theme()) -> None:
            super().__init__(style_props=style_props   )
            self.model_triangle = model_triangle
            self.geo_mapper = geo_mapper
            self.triangle = None
            self.create()
                  
      def create(self):
           self.triangle = self._create_polygon()
         
      
      def _create_polygon(self):
            ui_point_a = self.geo_mapper.model_point_to_ui_point(self.model_triangle.model_point_a)         
            ui_point_b = self.geo_mapper.model_point_to_ui_point(self.model_triangle.model_point_b)
            ui_point_c = self.geo_mapper.model_point_to_ui_point(self.model_triangle.model_point_c)
            return Polygon(ui_point_a, ui_point_b, ui_point_c, fill_opacity=self.fill_opacity, color=self.color)
      
      def view(self):
            return self.triangle
      
      def update(self):
            new_triangle = self._create_polygon()
            self.triangle.become(new_triangle)
      