from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.model.model_aligned_text import ModelAlignedText
from graphing.geo.model.model_point import ModelPoint
from graphing.geo.ui.ui_style_props import UIStyleProps
from graphing.geo.ui.ui_text import UIMathTex
from manim import *

class UIAlignedText(UIMathTex):
    def __init__(self, geo_mapper:GeoMapper, model_aligned_text:ModelAlignedText, style_props:UIStyleProps,  direction = UP, shift = ORIGIN, reverse_direction=False) -> None:
        super().__init__(model_aligned_text, style_props)
        self.geo_mapper = geo_mapper
        self.model_aligned_text = model_aligned_text
        self.direction = direction
        self.amount_to_shift = shift
        self.reverse_direction = reverse_direction
        self.orient_to()
       
    def update(self):   
       super().update()
       self.orient_to()
       
       
    def orient_to(self):
        start_point = self.geo_mapper.model_point_to_ui_point(self.model_aligned_text.start_point)
        end_point = self.geo_mapper.model_point_to_ui_point(self.model_aligned_text.end_point)
        if self.reverse_direction:
          start_point, end_point = end_point, start_point 
        manim_line = Line(start_point, end_point)
        angle = manim_line.get_angle()
        line_center = manim_line.get_center()
        self.view().next_to(line_center, self.direction)
        self.view().rotate(angle, about_point=line_center)
        self.view().shift(self.amount_to_shift)   
        
      
    
        
  