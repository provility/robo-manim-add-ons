from graphing.geo.model.model_image import ModelImage
from graphing.geo.ui.base_ui import BaseUI
from manim import ImageMobject

from graphing.geo.ui.ui_style_props import UIStyleProps

class UIImage(BaseUI):
    def __init__(self,geo_mapper, model_image:ModelImage, 
                 scale_factor = 1):
        super().__init__(UIStyleProps.line_theme())
        self.geo_mapper = geo_mapper    
        self.model_image = model_image
        self.scale_factor = scale_factor
        self.image_shape = self.create_mobject()
        self._move_image()
         
    def create_mobject(self):
        return ImageMobject(self.model_image.get_image()).scale(self.scale_factor)
         
    def view(self):
        return self.image_shape
    
    def _move_image(self):
        model_position = self.model_image.model_position
        ui_position = self.geo_mapper.model_to_ui(model_position)
        self.image_shape.move_to(ui_position)
        
    def update(self):    
        self._move_image()
        
    
    
    
    