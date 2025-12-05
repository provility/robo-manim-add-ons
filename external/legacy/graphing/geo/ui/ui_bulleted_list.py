from graphing.geo.model.model_bulleted_list import ModelBulletedList
from graphing.geo.ui.base_ui import BaseUI
from manim import *

from graphing.geo.ui.ui_part import UIPart
from graphing.geo.ui.ui_style_props import UIStyleProps

class UIBulletedList(BaseUI):
    def __init__(self, model:ModelBulletedList,
                 buff=MED_LARGE_BUFF,
                 line_spacing=0.6,
                 style_props:UIStyleProps = UIStyleProps.text_theme()):
        super().__init__(style_props)
        self.model = model  
        self.buff = buff
        self.line_spacing = line_spacing
        self.ui_shape = None
        self.create_ui()
        
    def create_ui(self):
        self.ui_shape = BulletedList(*self.model.items, 
                                     color=self.style_props.color,
                                     dot_scale_factor=self.style_props.scale_factor,
                                     buff=self.buff)
        self.ui_shape.scale(self.style_props.scale_factor) 
        self.ui_shape.arrange(DOWN, aligned_edge=LEFT, buff=self.line_spacing)
        
    def view(self):
        return self.ui_shape
    
    def item(self, row_index, column_index=None):
        element = self.ui_shape[row_index]
        ui_part = UIPart(element, self.graphsheet, self.geo_mapper, self.scene, style_props=self.style_props)
        return ui_part
        
        