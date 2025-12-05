from fractions import Fraction
from .base_model import BaseModel
import math
import numpy as np
import sympy as sp
from sympy import Point, Segment
from manim import *
from .model_point import ModelPoint

class ModelAngle(BaseModel):
    def __init__(self, point_from:ModelPoint, vertex:ModelPoint,
                       to_point:ModelPoint, clock_wise=False):
        super().__init__()
        self.point_from = point_from
        self.vertex = vertex
        self.to_point = to_point
        self.clock_wise = clock_wise
    
     
    def update(self):
        self.notify()
        
    def update_points(self, point_from:ModelPoint, vertex:ModelPoint,
                       to_point:ModelPoint):
        self.point_from.set(point_from.x, point_from.y)
        self.vertex.set(vertex.x, vertex.y)
        self.to_point.set(to_point.x, to_point.y)
        self.notify()
        
    def point_index(self, index):       
        if index == 0:
            return self.point_from
        elif index == 1:
            return self.vertex
        elif index == 2:
            return self.to_point
        else:
            raise ValueError("Invalid index for angle points")
            
    @staticmethod    
    def from_three_points(point_from:ModelPoint, vertex:ModelPoint,
                       to_point:ModelPoint, clock_wise=False):
       model_angle = None
        
       def create():
            nonlocal model_angle  
            model_angle = ModelAngle(point_from, vertex, to_point, clock_wise)
            
       def update():   
            nonlocal model_angle  
            model_angle.update()
            
       create()
        
        # hook dependencies, when the input points change, the angle should update
       point_from.on_change(lambda: update())
       vertex.on_change(lambda: update())
       to_point.on_change(lambda: update())
       return model_angle
   
    @property
    def angle_in_degrees(self):
       return self.angle_value()
   
    @property
    def angle_in_radians(self):
       return self.angle_value() * np.pi / 180
   
    @property
    def degress_in_latex(self):
        return rf"${self.angle_in_degrees}^\circ$"
   
    @property
    def radians_in_latex(self):
        angle = self.angle_in_radians
        pi = np.pi
        ratio = angle / pi
        
        if abs(ratio - round(ratio)) < 0.01:  # Close to whole number
            if ratio == 1:
                return r"$\pi$"
            elif ratio == -1:
                return r"$-\pi$" 
            elif ratio == 0:
                return r"$0$"
            else:
                return rf"${int(ratio)}\pi$"
        else:  # Fraction of pi
            frac = Fraction(ratio).limit_denominator(10)
            if frac.numerator == 1:
                return rf"$\frac{{\pi}}{{{frac.denominator}}}$"
            elif frac.numerator == -1:
                return rf"$-\frac{{\pi}}{{{frac.denominator}}}$"
            else:
                return rf"$\frac{{{frac.numerator}}}{{\pi}}{{{frac.denominator}}}$"
            
            
    def angle_value(self):
        A = self.point_from.to_numpy()
        B = self.vertex.to_numpy()
        C = self.to_point.to_numpy()
        
        # Calculate vectors AB and BC
        AB = A - B
        BC = C - B
        
        # Calculate the dot product of AB and BC
        dot_product = np.dot(AB, BC)
        
        # Calculate the magnitudes of AB and BC
        AB_magnitude = np.linalg.norm(AB)
        BC_magnitude = np.linalg.norm(BC)
        
        # Calculate the cosine of the angle
        cos_theta = dot_product / (AB_magnitude * BC_magnitude)
        
        # Calculate the angle in radians and then convert to degrees
        angle_radians = np.arccos(cos_theta)
        angle_degrees = np.degrees(angle_radians)
        
        return angle_degrees    
    
    
    @staticmethod
    def angle_between_lines(model_line_a, model_line_b):
        model_angle = None
        
        def computation():
            from_point = model_line_a.end_model_point()
            vertex = model_line_b.intersection(model_line_a)    
            to_point = model_line_b.end_model_point()
            return ModelAngle(from_point, vertex, to_point, 
                              clock_wise=False)
        
        def create():
            nonlocal model_angle  
            model_angle = computation()
            
        def update():   
            nonlocal model_angle  
            new_model_angle = computation()
            model_angle.update_points(new_model_angle.point_from, 
                                     new_model_angle.vertex, 
                                     new_model_angle.to_point)
            
        create()
        
        # hook dependencies, when the input points change, the angle should update
        model_line_a.on_change(lambda: update())
        model_line_b.on_change(lambda: update())
        return model_angle