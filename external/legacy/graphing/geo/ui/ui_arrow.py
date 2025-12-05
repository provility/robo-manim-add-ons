from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.model.model_vector import ModelVector
from graphing.geo.ui.ui_line import UILine
from graphing.geo.ui.ui_style_props import UIStyleProps
from manim import *

class UIArrow(UILine):
    def __init__(self, geo_mapper: GeoMapper, 
                 model_arrow:ModelVector, 
                 curved:bool = False,
                 angle: float = TAU / 4,
                 radius: float = None,
                 style_props:UIStyleProps = UIStyleProps.line_theme()):
        self.arrow = None   
        self.curved = curved
        self.angle = angle
        self.radius = radius
        super().__init__(geo_mapper, model_arrow, style_props)
        
    def build_shape(self, arrow_start, arrow_end):    
        if self.curved == True:
            arrow = CurvedArrow(arrow_start, arrow_end,
                                color=self.color, stroke_width=self.style_props.stroke_width,
                                angle=self.angle, radius=self.radius)
        else:
            arrow = DashedLine(arrow_start, arrow_end, dash_length=0.15, dashed_ratio=0.5)
            arrow.add_tip(tip_length=0.3, tip_width=0.3)  # Reduced tip size   
              
        self.arrow = arrow
        return VGroup(arrow)
    
  
    def update(self):
        arrow_start, arrow_end = self._get_ui_start_and_end()
        
        if self.curved == True:
            new_arrow = CurvedArrow(arrow_start, arrow_end, color=self.color,
                                    stroke_width=self.style_props.stroke_width,
                                    angle=self.angle, radius=self.radius)
        else:   
            new_arrow = DashedLine(arrow_start, arrow_end, dash_length=0.15, dashed_ratio=0.5)
            new_arrow.add_tip(tip_length=0.3, tip_width=0.3)  # Reduced tip size   
        self.arrow.become(new_arrow)
       
