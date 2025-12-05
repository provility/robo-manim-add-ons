from graphing.commands.ex_brace_between_points import ExBraceBetweenPoints
from graphing.geo.model.model_distance import ModelDistance
from graphing.geo.ui.ui_style_props import UIStyleProps
from .base_ui import BaseUI
from ..model.model_point import ModelPoint
from ..model.model_angle import ModelAngle
from ..geo_mapper import GeoMapper
from ..geo_shape_props import ZIndex
from manim import *
class UIDistance(BaseUI):
      def __init__(self, geo_mapper: GeoMapper, 
                   model_distance:ModelDistance, 
                   direction=RIGHT,
                   style_props:UIStyleProps = UIStyleProps.distance_marker_theme() ) -> None:
         super().__init__(style_props)
         self.geo_mapper = geo_mapper
         self.model_distance = model_distance
         self.brace_between_points = None
         self.direction = direction
         self.create()
       
    
      def create(self):
         ui_start, ui_end = self._get_ui_start_and_end()
         self.brace_between_points = BraceBetweenPoints(ui_start, ui_end, direction=self.direction)
         self.brace_between_points.set_color(self.style_props.color)
         self.brace_between_points.set_z_index(ZIndex.BRACE.value)
        
    
      def _get_ui_start_and_end(self):
          start_x, start_y = self.model_distance.start
          end_x, end_y = self.model_distance.end
          ui_start = self.geo_mapper.model_to_ui(start_x, start_y)  
          ui_end = self.geo_mapper.model_to_ui(end_x, end_y)
          return ui_start, ui_end 
      
     
      def update(self):
         ui_start, ui_end = self._get_ui_start_and_end()
         perp = self.unit_perpendicular_direction(ui_start, ui_end)
         new_brace = BraceBetweenPoints(ui_start, ui_end, direction=perp)
         new_brace.set_color(self.style_props.color)
         new_brace.set_z_index(ZIndex.BRACE.value)
         self.brace_between_points.become(new_brace)
         self.brace_between_points.set_z_index(ZIndex.BRACE.value)    
      
      def unit_perpendicular_direction(self, ui_start_numpy, ui_end_numpy):
         direction = ui_end_numpy - ui_start_numpy
         perp = np.array([-direction[1], direction[0], 0])
         return perp / np.linalg.norm(perp)
              
      def view(self):
         return self.brace_between_points
     
     
    
      