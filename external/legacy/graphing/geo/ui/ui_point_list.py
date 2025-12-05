from manim import *

from graphing.geo.model.model_point_list import ModelPointList
from graphing.geo.ui.ui_style_props import UIStyleProps
from ..geo_mapper import GeoMapper
from .base_ui import BaseUI
from .ui_point import UIPoint

class UIPointList(BaseUI):
      def __init__(self, geo_mapper:GeoMapper, model_point_list:ModelPointList,  style_props:UIStyleProps=UIStyleProps.point_theme()):
          super().__init__(style_props)
          self.geo_mapper = geo_mapper
          self.model_point_list = model_point_list
     
          self.ui_point_list:List[UIPoint] = None
          self.ui_group = None
          self.create()
      
      def create(self):
          self.ui_point_list = self._create_ui_points()
          self.ui_group = VGroup(*[ui_point.dot for ui_point in self.ui_point_list])  
         
          
      def view(self):
          return self.ui_group
      
      def _create_ui_points(self):
          return [UIPoint(geo_mapper=self.geo_mapper, model_point=model_point,  style_props=self.style_props) 
                  for model_point 
                  in self.model_point_list.points]
          
      
      def update(self):
          for ui_point in self.ui_point_list:
              ui_point.update() 
              

          
          
      
        