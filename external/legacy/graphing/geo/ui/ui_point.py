from graphing.geo.ui.ui_style_props import UIStyleProps
from .base_ui import BaseUI
from ..model.model_point import ModelPoint
from ..geo_mapper import GeoMapper
from ..geo_shape_props import ZIndex

from manim import *

class UIPoint(BaseUI):
      def __init__(self, geo_mapper: GeoMapper, 
                   model_point:ModelPoint,  
                   style_props=UIStyleProps.point_theme()) -> None:
            super().__init__(style_props)
            self.model_point = model_point
            self.geo_mapper = geo_mapper
            ui_point = self.geo_mapper.model_to_ui(self.model_point.x, self.model_point.y)
            dot = Dot(ui_point, radius=0.1, color=self.color, fill_opacity=self.fill_opacity)
            self.dot = dot
            self.dot.set_z_index(ZIndex.DOT.value)          
             
      def clear_dynamic(self):
          self.dot.clear_updaters()
                 
  
    
      def view(self):
          return self.dot
       
      def update(self):
        self.update_position()
        
      
      def update_position(self):
           self.dot.move_to(self.geo_mapper.model_to_ui(self.model_point.x, self.model_point.y))
           
     