from graphing.geo.ui.ui_style_props import UIStyleProps
from .base_ui import BaseUI
from ..model.model_point import ModelPoint
from ..model.model_line import ModelLine
from ..model.model_circle import ModelCircle
from ..geo_mapper import GeoMapper
from ..geo_shape_props import ZIndex
from manim import *
class UICircle(BaseUI):
    def __init__(self, geo_mapper: GeoMapper, 
                 model_circle:ModelCircle, style_props:UIStyleProps = UIStyleProps.circle_theme()) -> None:
        super().__init__(style_props)
        self.model_circle = model_circle
        self.geo_mapper = geo_mapper
       
        self.circle_shape = None
      
        self.create()
        self.update()
      
        
    def create(self):
        center = self.model_circle.center
        center = self.geo_mapper.model_to_ui(center.x, center.y)
        ui_radius = self.geo_mapper.model_radius_to_ui(self.model_circle.radius)
        circle_shape = Circle(radius=ui_radius, color=self.color, fill_opacity=self.fill_opacity)
        circle_shape.move_to(center)
        circle_shape.set_z_index(ZIndex.CIRCLE.value)
        self.circle_shape = circle_shape
      
            
    def update(self):
        center = self.model_circle.center
        ui_center = self.geo_mapper.model_to_ui(center.x, center.y)
        ui_radius = self.geo_mapper.model_radius_to_ui(self.model_circle.radius)
        new_circle = Circle(radius=ui_radius, color=self.color, fill_opacity=self.fill_opacity)
        self.circle_shape.become(new_circle)    
        self.circle_shape.move_to(ui_center)
      
        
    def view(self):
        return self.circle_shape     
    
  
    
    