from graphing.geo.model.model_parameter import ModelParameter
from .base_model import BaseModel
import math
import numpy as np
import sympy as sp
from sympy import Point, Segment
from manim import *
from .model_point import ModelPoint
from .model_line import ModelLine

class ModelCircle(BaseModel):
    def __init__(self, start_x, start_y, radius):
        super().__init__()
        self.start_x = start_x
        self.start_y = start_y
        self.radius = radius
        self.sympy_circle = sp.Circle(sp.Point(self.start_x,self.start_y), self.radius) 
        self.origin = ModelPoint(self.start_x, self.start_y, 0)      
        
    def update(self, start_x, start_y, radius):
         self.start_x = start_x
         self.start_y = start_y
         self._radius = radius
         self.sympy_circle = sp.Circle(sp.Point(self.start_x,self.start_y), self.radius)
         self.origin.set(self.start_x, self.start_y, 0) 
         self.notify()
         
    
    @property  
    def center(self):
        return ModelPoint(self.start_x, self.start_y, 0)
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._radius = value
        self.sympy_circle = sp.Circle(sp.Point(self.start_x,self.start_y), self.radius)
        self.notify()
    
    def sympy_circle(self):
        return self.sympy_circle


    def manim_circle(self):
        return Circle(radius=self.radius).shift(np.array([self.start_x, self.start_y, 0]))
    
    def point_at(self, ratio):
        angle = 2 * math.pi * ratio
        return [self.start_x + self.radius * np.cos(angle), self.start_y + self.radius * np.sin(angle), 0]
    
    def point_at_angle(self, degrees):
        radians = math.radians(degrees)
        return ModelPoint(self.start_x + self.radius * np.cos(radians), self.start_y + self.radius * np.sin(radians))
    
    def get_all_points(self):
        return [self.origin]
    
    def point_index(self, index):
        if index == 0:
            return self.origin
        else:
            raise ValueError("Invalid index for circle points")
        
    def intersect_with_line(self, line:ModelLine, index=0):
        sympy_line = sp.Line2D(sp.Point(line.start[0], line.start[1]), sp.Point(line.end[0], line.end[1]))
        intersections =  self.sympy_circle.intersection(sympy_line)
        return ModelPoint(intersections[index][0].evalf(), intersections[index][1].evalf())
    
    @property
    def circumferance(self):
        return 2 * math.pi * self.radius
    
    @property
    def area(self):
        return self.sympy_circle.area
    
    def tangent_line(self, model_parameter:ModelParameter):
        model_line = None
        
        def computation():
            # This is sympy circle
            circle = sp.Circle(sp.Point(self.start_x,self.start_y), self.radius)
            model_point = self.point_at_angle(model_parameter.get_value())
            tangent = circle.tangent_lines(model_point.to_sympy())
            p1, p2 = tangent[0].points
            return p1, p2
        
        def create():
            nonlocal model_line  
            p1, p2 = computation()
            model_line = ModelLine(p1.x, p1.y, p2.x, p2.y)
            
        def update():   
            nonlocal model_line  
            p1, p2 = computation()
            model_line.update(p1.x, p1.y, p2.x, p2.y)
            
        create()
        model_parameter.on_param_change(lambda d: update())
        self.on_change(lambda: update())
        return model_line         
    
    @staticmethod
    def from_center_and_point(origin:ModelPoint, radius_or_parameter):
        model_circle = None
    
        def create():
            nonlocal model_circle  
            radius = radius_or_parameter.get_value()
            model_circle = ModelCircle(origin.x, origin.y, radius)
            
        def update():   
            nonlocal model_circle  
            radius = radius_or_parameter.get_value()
            model_circle.update(origin.x, origin.y, radius)
            
        create()
        
        # hook dependencies, when the origin point changes the circle should get updated    
        origin.on_change(lambda: update())
        radius_or_parameter.on_param_change(lambda d: update())
        return model_circle
    
    @staticmethod
    def circle_from_two_points(start:ModelPoint, end:ModelPoint):
        model_circle = None
        
        def create():
            nonlocal model_circle  
            radius = np.linalg.norm(start.to_numpy() - end.to_numpy())
            model_circle = ModelCircle(start.x, start.y, radius )
            
        def update():   
            nonlocal model_circle  
            radius = np.linalg.norm(start.to_numpy() - end.to_numpy())
            model_circle.update(start.x, start.y, radius)
            
        create()
        
        # hook dependencies, when the start and end points change the circle should get updated 
        start.on_change(lambda: update())
        end.on_change(lambda: update())
        return model_circle
    
    """ of the for (x - h)^2 + (y - k)^2 = r^2
"""
    @staticmethod   
    def from_equation(equation:str):
        model_circle = None
        
        # Parse the equation string
        x, y = sp.symbols('x y')
        # Remove spaces and replace '^' with '**' for proper parsing
        equation = equation.replace(' ', '').replace('^', '**')
        # Ensure the equation is set to zero
        if '=' in equation:
            left, right = equation.split('=')
            equation = f"{left}-({right})"
        eq = sp.Eq(sp.parse_expr(equation), 0)
        # Convert the equation to standard form
        eq = sp.expand(eq.lhs)
        
        # Function to extract coefficient
        def get_coeff(expr, term):
            return expr.coeff(term) if hasattr(expr, 'coeff') else expr.as_coefficients_dict().get(term, 0)
        # Extract coefficients
        x_coeff = get_coeff(eq, x**2)
        y_coeff = get_coeff(eq, y**2)
        x_linear = get_coeff(eq, x)
        y_linear = get_coeff(eq, y)
        constant = eq.as_coeff_add(x, y)[0]
        
        # Ensure the equation is in the form (x-h)^2 + (y-k)^2 = r^2
        if x_coeff != 1 or y_coeff != 1:
            raise ValueError("The equation must be in the form (x-h)^2 + (y-k)^2 = r^2")
        
        # Calculate center coordinates and radius
        h = -x_linear / (2 * x_coeff)
        k = -y_linear / (2 * y_coeff)
        r_squared = (x_linear**2 + y_linear**2) / (4 * x_coeff) - constant
        r = sp.sqrt(r_squared)
        
        # Create ModelCircle
        model_circle = ModelCircle(float(h), float(k), float(r))

        return model_circle
    
    @staticmethod        
    def point_on_circle(model_circle, angle_in_degrees_parameter):
        model_point = None  
        
        def create():
            nonlocal model_point
            model_point = model_circle.point_at_angle(angle_in_degrees_parameter.get_value())
            
        def update():
            nonlocal model_point
            new_point = model_circle.point_at_angle(angle_in_degrees_parameter.get_value())
            model_point.set(new_point.x, new_point.y, new_point.z)
            
        create()
        angle_in_degrees_parameter.on_param_change(lambda d: update())  
        model_circle.on_change(lambda: update())

        return model_point        
    