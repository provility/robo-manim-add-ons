from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.model.model_vector import ModelVector
from graphing.geo.ui.base_ui import BaseUI
from graphing.geo.ui.ui_style_props import UIStyleProps
from manim import *

class UIComplex(BaseUI):
    def __init__(self, geo_mapper: GeoMapper, 
                 model_vector:ModelVector, 
                 style_props:UIStyleProps = UIStyleProps.vector_theme()):
        super().__init__(style_props) 
        self.model_vector = model_vector
        self.geo_mapper = geo_mapper    
        self.ui_shape = None
        self.create()
        
    def create(self):
        self.ui_shape = self.build_shape()    
        
    def build_shape(self):
        return self._build_arrow()
        
    def view(self):
        return self.ui_shape    
    
    def _build_arrow(self):
        model_points = self.model_vector.model_points       
        if self.style_props.dashed:
            arrow = DashedLine(self.geo_mapper.model_point_to_ui_point(model_points[0]), 
                               self.geo_mapper.model_point_to_ui_point(model_points[1]), 
                               dash_length=0.15, dashed_ratio=0.5)
            arrow.add_tip(tip_length=0.3, tip_width=0.3)  # Reduced tip size   
            arrow.set_color(self.color) 
        else:
            arrow = Arrow(self.geo_mapper.model_point_to_ui_point(model_points[0]), 
                         self.geo_mapper.model_point_to_ui_point(model_points[1]), 
                         color=self.color,
                         stroke_width=self.style_props.stroke_width,
                         buff=0)
            
        return arrow    
    
    def update(self):
        previous_arrow =  self.ui_shape
        new_arrow = self._build_arrow()
        previous_arrow.become(new_arrow)
        
        
        
class UIVector(UIComplex):
    def __init__(self, geo_mapper: GeoMapper, 
                 model_vector:ModelVector, 
                 vector_name = None,
                 style_props:UIStyleProps = UIStyleProps.vector_theme(),
                 label_direction=UP,
                 label_reverse_orientation=False,
                 label_shift=ORIGIN):
      
        self.vector_name = vector_name
        if '\\' in vector_name or '{' in vector_name:
            self.vector_name = vector_name
        else:    
            self.vector_name = r'\vec{' + vector_name + '}'
            
        self.label_shape = MathTex(self.vector_name)
        self.label_direction = label_direction
        self.label_reverse_orientation = label_reverse_orientation
        self.label_shift = label_shift
        super().__init__(
            geo_mapper = geo_mapper,
            model_vector = model_vector,
            style_props = style_props) 
   
    def build_shape(self):
        arrow = self._build_arrow()
        label_shape = self.oriented_label()
        vector_group = VGroup(arrow, label_shape)
        return vector_group
    
    def update(self):
        previous_arrow = self.view().submobjects[0]
        new_arrow = self._build_arrow()
        previous_arrow.become(new_arrow)
        previous_label_shape = self.view().submobjects[1]
        new_label_shape = self.oriented_label()
        previous_label_shape.become(new_label_shape)

    def shape_to_trace(self):
        return self.view().submobjects[0]
    
    def oriented_label(self):
        model_points = self.model_vector.model_points       
        start_point = self.geo_mapper.model_point_to_ui_point(model_points[0])
        end_point = self.geo_mapper.model_point_to_ui_point(model_points[1])        
        if self.label_reverse_orientation:
          start_point, end_point = end_point, start_point 
        manim_line = Line(start_point, end_point)
        angle = manim_line.get_angle()
        line_center = manim_line.get_center()
        new_label_shape = MathTex(self.vector_name) 
        new_label_shape.set_color(self.color)
        new_label_shape.next_to(line_center, self.label_direction)
        new_label_shape.rotate(angle, about_point=line_center)
        new_label_shape.shift(self.label_shift)
        return new_label_shape
        
    
    