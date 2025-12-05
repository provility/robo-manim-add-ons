from graphing.ex_manim.label_with_arrows import LabelBetweenArrows
from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.model.model_label_with_arrows import ModelLabelWithArrows
from graphing.geo.ui.base_ui import BaseUI
from graphing.geo.ui.ui_style_props import UIStyleProps
from manim import *

class UILabelWithArrows(BaseUI):
    def __init__(self, geo_mapper:GeoMapper, model_label_with_arrows:ModelLabelWithArrows,
                 style_props:UIStyleProps, direction=UP, reverse_direction=False,
                 buff=0.2):
        super().__init__(style_props)
        self.geo_mapper = geo_mapper
        self.model_label_with_arrows = model_label_with_arrows
        self.direction = direction
        self.reverse_direction = reverse_direction
        self.buff = buff
        self.label_with_arrows = None
        self.create()
        
    def create(self):
        start_point = self.geo_mapper.model_point_to_ui_point(self.model_label_with_arrows.start_point)
        end_point = self.geo_mapper.model_point_to_ui_point(self.model_label_with_arrows.end_point)
        if self.reverse_direction:
          start_point, end_point = end_point, start_point 
        self.label_with_arrows = LabelBetweenArrows(start_point, end_point, self.model_label_with_arrows.text, color=self.style_props.color)
        self.label_with_arrows.set_z_index(500)
        self.orient_to()
    
    def update(self):   
        start_point = self.geo_mapper.model_point_to_ui_point(self.model_label_with_arrows.start_point)
        end_point = self.geo_mapper.model_point_to_ui_point(self.model_label_with_arrows.end_point)
        if self.reverse_direction:
          start_point, end_point = end_point, start_point  
        self.label_with_arrows[0].move_to(start_point)
        self.label_with_arrows[1].move_to(end_point)
        self.label_with_arrows.text.set_text(self.model_label_with_arrows.text)
        self.orient_to()
       
    def orient_to(self):
        start_point = self.geo_mapper.model_point_to_ui_point(self.model_label_with_arrows.start_point)
        end_point = self.geo_mapper.model_point_to_ui_point(self.model_label_with_arrows.end_point)
        if self.reverse_direction:
          start_point, end_point = end_point, start_point 

        
        # Get the normal vector by rotating the line direction by 90 degrees
        line_direction = normalize(end_point - start_point)
        normal_direction = rotate_vector(line_direction, PI/2)
        
        direction_to_use  = None
        # Convert the input direction (like UP) to a normal-relative direction
        if np.array_equal(self.direction, UP):
            direction_to_use = normal_direction
        elif np.array_equal(self.direction, DOWN): 
            direction_to_use = -normal_direction
        elif np.array_equal(self.direction, LEFT):
            direction_to_use = -line_direction  
        elif np.array_equal(self.direction, RIGHT):
            direction_to_use = line_direction
      
        self.view().shift(direction_to_use * self.buff)   
      
    def view(self):
        return self.label_with_arrows
        
        