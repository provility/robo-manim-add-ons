from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.geo_shape_props import ZIndex
from graphing.geo.ui.base_ui import BaseUI
from graphing.geo.model.model_arc import ModelArc
from graphing.geo.ui.ui_style_props import UIStyleProps
from manim import *

class UIArc(BaseUI):
    def __init__(self, geo_mapper: GeoMapper, 
                 model_arc: ModelArc, 
                 style_props:UIStyleProps = UIStyleProps.arc_theme()
                 ) -> None:
        super().__init__(style_props)
        self.model_arc = model_arc
        self.geo_mapper = geo_mapper
        self.arc_shape = VGroup()   
        self.create()
       
    def create(self):
        ui_center = self.geo_mapper.model_to_ui(self.model_arc.arc_center)  
        ui_radius = self.geo_mapper.model_radius_to_ui(self.model_arc.radius)
        arc = Arc(
            radius=ui_radius,
            start_angle=self.model_arc.start_angle,
            angle=self.model_arc.angle,
            arc_center=ui_center,
            color=self.style_props.color,
            stroke_width=self.style_props.stroke_width)
        arc.set_z_index(ZIndex.ARC.value)
        self.arc_shape.add(arc)
        
    def update(self):
        ui_center = self.geo_mapper.model_to_ui(self.model_arc.arc_center)  
        ui_radius = self.geo_mapper.model_radius_to_ui(self.model_arc.radius)
        new_arc = Arc(
            radius=ui_radius,
            start_angle=self.model_arc.start_angle,
            angle=self.model_arc.angle,
            arc_center=ui_center,
            color=self.style_props.color,
            stroke_width=self.style_props.stroke_width
            )
        self.arc_shape.become(new_arc)
        
    def view(self):
        return self.arc_shape
    
    
    def add_arrow_tip(self, arc):
        end_point = arc.get_end()
        tangent_direction = arc.get_end() - arc.point_from_proportion(0.99)
        tangent_direction /= np.linalg.norm(tangent_direction)  # Normalize

        # Add an arrow tip at the end of the arc
        arrow_tip = ArrowTip(color=self.color, tip_length=0.3)
        arrow_tip.rotate(angle_of_vector(tangent_direction))  # Align with tangent
        arrow_tip.move_to(end_point + tangent_direction * 0.1)  # Adjust position slightly
        return arrow_tip

      
        
        