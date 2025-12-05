from graphing.geo.ui.ui_style_props import UIStyleProps
from .base_ui import BaseUI
from ..model.model_point import ModelPoint
from ..model.model_line import ModelLine
from ..geo_mapper import GeoMapper
from ..geo_shape_props import ZIndex
from manim import *

class UILine(BaseUI):
      def __init__(self, geo_mapper: GeoMapper, 
                 model_line:ModelLine, 
                 style_props:UIStyleProps = UIStyleProps.line_theme()
                   ) -> None:
        super().__init__(style_props)
        self.model_line = model_line
        self.geo_mapper = geo_mapper
        self.ui_shape = None
           
        self.create()
        self.update()
       
          
      def _get_ui_start_and_end(self):
          start_x, start_y = self.model_line.start
          end_x, end_y = self.model_line.end
          ui_start = self.geo_mapper.model_to_ui(start_x, start_y)  
          ui_end = self.geo_mapper.model_to_ui(end_x, end_y)
          return ui_start, ui_end 
      
      def create(self):
          ui_start, ui_end = self._get_ui_start_and_end()
          self.ui_shape = self.build_shape(ui_start, ui_end)
          self.ui_shape.set_z_index(ZIndex.LINE.value)
        
          
      def build_shape(self, ui_start, ui_end):
          if self.style_props.dashed:
              line = DashedLine(ui_start, ui_end, 
                                color=self.color, 
                                stroke_width=self.style_props.stroke_width,
                                dashed_ratio=0.5, dash_length=0.1)
              line.set_color(self.color)
              return line    
          else:
              line = Line(ui_start, ui_end, color=self.color, stroke_width=self.style_props.stroke_width)
              line.set_color(self.color)
              return line
        
      def update(self):
          ui_start, ui_end = self._get_ui_start_and_end()
          new_line = self.build_shape(ui_start, ui_end)
          self.ui_shape.become(new_line)
         
          
      def shape_to_trace(self):
          return self.view()    
                   
      def view(self):
          return self.ui_shape    
        
   
      
   
        