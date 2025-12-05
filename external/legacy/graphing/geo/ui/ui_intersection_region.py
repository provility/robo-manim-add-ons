from graphing.geo.model.model_intersection import ModelIntersectionRegion
from graphing.geo.ui.base_ui import BaseUI
from graphing.geo.ui.ui_style_props import UIStyleProps


class UIIntersectionRegion(BaseUI):
    def __init__(self, model:ModelIntersectionRegion, style_props:UIStyleProps):
        super().__init__(style_props)
        self.model = model
        self.ui_shape = None
        self.create()    
       
    def create(self):
        self.ui_shape = self.model.intersection 
        self.ui_shape.set_color(self.style_props.color)
        self.ui_shape.set_fill_color(self.style_props.fill_color)
        self.ui_shape.set_fill_opacity(self.style_props.fill_opacity)
        self.ui_shape.set_z_index(1000)
        
    def view(self):
        return self.ui_shape
    
    def update(self):
        new_ui_shape = self.model.intersection
        self.ui_shape.become(new_ui_shape)  
        
        
        
        
        