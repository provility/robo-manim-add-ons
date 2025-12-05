"""
  lines = axes.get_lines_to_point(dot.get_center())

"""
from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.model.model_axis_lines import ModelAxisLine
from graphing.geo.model.model_line import ModelLine
from graphing.geo.model.model_point import ModelPoint
from graphing.geo.ui.base_ui import BaseUI
from graphing.geo.ui.ui_style_props import UIStyleProps


class UIAxisLines(BaseUI):
      def __init__(self, geo_mapper: GeoMapper, 
                 model_axis_line:ModelAxisLine, 
                
                 style_props:UIStyleProps = UIStyleProps.line_theme()
                   ) -> None:
        super().__init__(style_props)
        self.model_axis_line = model_axis_line
        self.geo_mapper = geo_mapper
        self.axis_lines = None
    
           
        self.create()
        self.update()
        
        
      def create(self):
          axes = self.geo_mapper.axes
          center = self.geo_mapper.model_to_ui(self.model_point.x, self.model_point.y)
          self.axis_lines = axes.get_lines_to_point(center)
          
      def update(self):
          axes = self.geo_mapper.axes
          center = self.geo_mapper.model_to_ui(self.model_point.x, self.model_point.y)
          new_axis_lines = axes.get_lines_to_point(center)
          self.axis_lines.become(new_axis_lines)
      
      @property    
      def model_point(self):
          return self.model_axis_line.model_point    
          
      def view(self):
          return self.axis_lines
      
      
          
            