from graphing.geo.model.model_parameter import ModelParameter
from graphing.geo.model.model_point import ModelPoint
from .base_model import BaseModel
import numpy as np

class ModelArc(BaseModel):
    # start_angle and end_angle are in radians, varies from -
    def __init__(self, arc_center, radius, start_angle, end_angle):
        super().__init__()
        self.arc_center = arc_center
        self.radius = radius
        self.start_angle = start_angle
        self.end_angle = end_angle 
    
    @property
    def arc_length(self):
        return self.radius * abs(self.end_angle - self.start_angle)
    
    # Manim expects the angle from start_angle, not the absolute end angle
    @property
    def angle(self):
        # Calculate the angle difference, handling the case where it crosses 0/2π
        angle_diff = self.end_angle - self.start_angle
        if angle_diff < 0:
            angle_diff += 2 * np.pi
        return angle_diff
    
    def update_parameters(self, arc_center, radius, start_angle, end_angle):
        self.arc_center = arc_center
        self.radius = radius
        self.start_angle = start_angle
        self.end_angle = end_angle
        self.notify()
    
   
   
    @staticmethod
    def from_center_and_angles(center:ModelPoint, radius_param:ModelParameter,
                               start_angle_param:ModelParameter, end_angle_param:ModelParameter):
        model_arc = None
       
        def computation():
            radius = radius_param.get_value()
            start_angle = start_angle_param.get_value() * np.pi / 180
            end_angle = end_angle_param.get_value() * np.pi / 180   
            return radius, start_angle, end_angle
           
        
        def create():
            nonlocal model_arc 
            radius, start_angle, end_angle = computation()
            model_arc = ModelArc(center, radius, start_angle, end_angle)
            
        def update():
            nonlocal model_arc 
            radius, start_angle, end_angle = computation()
            model_arc.update_parameters(center, radius, start_angle, end_angle)
            
        # hook dependencies
        center.on_change(update)
        radius_param.on_change(update)
        start_angle_param.on_change(update)
        end_angle_param.on_change(update)
        
        create()
        return model_arc
    
    