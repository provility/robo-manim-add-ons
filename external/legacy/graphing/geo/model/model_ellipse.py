from graphing.math.function_expression_utils import FunctionUtils

from .base_model import BaseModel
import math
import re
import numpy as np
import sympy as sp
from sympy import Point, Segment, Ellipse, symbols, Eq, parse_expr, expand, solve, N, Matrix
from .model_point import ModelPoint
from .model_line import ModelLine
from sympy.parsing.latex import parse_latex

class AbstractEllipse(BaseModel):
      def __init__(self, sympy_ellipse):
          super().__init__()
          self.sympy_ellipse = sympy_ellipse
     
      @property     
      def center(self):
          center_pt =  self.sympy_ellipse.center
          return ModelPoint(center_pt[0].evalf(), center_pt[1].evalf())
          
      @property
      def eccentricity(self):
        return self.sympy_ellipse.eccentricity
    
      @property
      def foci_A(self):
        foc1  = self.sympy_ellipse.foci
        return ModelPoint(foc1[0][0].evalf(), foc1[0][1].evalf())
    
      @property
      def foci_B(self):
        foc1  = self.sympy_ellipse.foci
        return ModelPoint(foc1[1][0].evalf(), foc1[1][1].evalf())
    
      @property
      def vertex_major_1(self):
          vertices = self.get_vertices()
          return ModelPoint(vertices[0][0].evalf(), vertices[0][1].evalf())
      
      @property
      def vertex_major_2(self):
          vertices = self.get_vertices()
          return ModelPoint(vertices[1][0].evalf(), vertices[1][1].evalf())
      
      @property
      def vertex_minor_1(self):
          vertices = self.get_vertices()
          return ModelPoint(vertices[2][0].evalf(), vertices[2][1].evalf())
      
      @property
      def vertex_minor_2(self):
          vertices = self.get_vertices()
          return ModelPoint(vertices[3][0].evalf(), vertices[3][1].evalf())
      
      @property
      def directrix_line_1(self):
          directrix_lines = self.get_directrices_as_lines()
          line_1 = directrix_lines[0]
          points = line_1.points
          return  ModelLine(points[0][0].evalf(),points[0][1].evalf(), points[1][0].evalf(), points[1][1].evalf())
      
      @property
      def directrix_line_2(self):
          directrix_lines = self.get_directrices_as_lines()
          line_2 = directrix_lines[1]
          points = line_2.points
          return  ModelLine(points[0][0].evalf(),points[0][1].evalf(), points[1][0].evalf(), points[1][1].evalf())

    
      def get_vertices(self):
        """
        Given a SymPy Ellipse, return its 4 vertices as a list of Point2D objects.
        
        Parameters:
            ellipse (sympy.geometry.ellipse.Ellipse): The SymPy Ellipse object.
            
        Returns:
            list of sympy.geometry.Point2D: The 4 vertices of the ellipse (2 on the major axis and 2 on the minor axis).
        """
        ellipse = self.sympy_ellipse
        # Get the center of the ellipse
        h, k = ellipse.center.x, ellipse.center.y
        
        # Get the semi-major axis (hradius) and semi-minor axis (vradius)
        a = ellipse.hradius  # Semi-major axis
        b = ellipse.vradius  # Semi-minor axis
        
        # Determine if the major axis is horizontal or vertical
        if a >= b:
            # Major axis is horizontal
            # Vertices on the major axis: (h ± a, k)
            major_vertices = [sp.Point(h + a, k), sp.Point(h - a, k)]
            # Vertices on the minor axis: (h, k ± b)
            minor_vertices = [sp.Point(h, k + b), sp.Point(h, k - b)]
        else:
            # Major axis is vertical
            # Vertices on the major axis: (h, k ± a)
            major_vertices = [sp.Point(h, k + a), sp.Point(h, k - a)]
            # Vertices on the minor axis: (h ± b, k)
            minor_vertices = [sp.Point(h + b, k), sp.Point(h - b, k)]
        
        # Return all four vertices
        return major_vertices + minor_vertices
    
      def get_directrices_as_lines(self):
        """
        Given a SymPy Ellipse, return the directrices as an array of two Line2D objects.
        
        Parameters:
            ellipse (sympy.geometry.ellipse.Ellipse): The SymPy Ellipse object.
            
        Returns:
            list of sympy.geometry.Line2D: The directrix lines as a list of two Line2D objects.
        """
        
        ellipse = self.sympy_ellipse
        # Get the semi-major axis (a) and the eccentricity (e)
        a = ellipse.hradius
        eccentricity = ellipse.eccentricity
        
        # Calculate the distance to the directrices from the center
        d = a / eccentricity**2
        
        # Get the center of the ellipse
        h, k = ellipse.center.x, ellipse.center.y
        
        # Initialize the list to store the directrix lines
        directrices = []

        # Determine if the major axis is horizontal or vertical
        if ellipse.hradius >= ellipse.vradius:
            # Major axis is horizontal, directrices are vertical lines at x = h ± d
            directrix_1 = sp.Line2D(sp.Point(h + d, k), sp.Point(h + d, k + 1))  # Right directrix
            directrix_2 = sp.Line2D(sp.Point(h - d, k), sp.Point(h - d, k + 1))  # Left directrix
        else:
            # Major axis is vertical, directrices are horizontal lines at y = k ± d
            directrix_1 = sp.Line2D(sp.Point(h, k + d), sp.Point(h + 1, k + d))  # Upper directrix
            directrix_2 = sp.Line2D(sp.Point(h, k - d), sp.Point(h + 1, k - d))  # Lower directrix


        # Scale the directrices to a large length
        scale_factor = 10  # Adjust this value as needed
        
        # For directrix_1
        direction_1 = directrix_1.direction
        new_point_1 = directrix_1.p1 + direction_1 * scale_factor
        directrix_1 = sp.Line2D(directrix_1.p1 - direction_1 * scale_factor, new_point_1)
        
        # For directrix_2
        direction_2 = directrix_2.direction
        new_point_2 = directrix_2.p1 + direction_2 * scale_factor
        directrix_2 = sp.Line2D(directrix_2.p1 - direction_2 * scale_factor, new_point_2)
        # Return the directrices as Line2D objects
        return [directrix_1, directrix_2]
              
        
class ModelEllipseParametric(AbstractEllipse):
      def __init__(self, symp_ellipse, parametric_x, parametric_y):
          super().__init__(symp_ellipse)        
          self.parametric_x = parametric_x
          self.parametric_y = parametric_y
          
      def update(self, symp_ellipse, parametric_x, parametric_y):
          self.sympy_ellipse = symp_ellipse
          self.parametric_x = parametric_x
          self.parametric_y = parametric_y    
          
      def point_at_angle(self, degrees):
        radians = math.radians(degrees)
        return ModelPoint(self.parametric_x(radians), self.parametric_y(radians))
    
      def intersect_with_line(self, line:ModelLine, index=0):
        sympy_line = sp.Line2D(sp.Point(line.start[0], line.start[1]), sp.Point(line.end[0], line.end[1]))
        intersections =  self.sympy_ellipse.intersection(sympy_line)
        return ModelPoint(intersections[index][0].evalf(), intersections[index][1].evalf())
  
               
          
      @staticmethod
      def sympy_ellipse_to_parametric_function(ellipse):
        """
        Convert a SymPy Ellipse object into parametric functions.
        """
        
        # Extract ellipse parameters from the SymPy Ellipse object
        center = ellipse.center  # Center (h, k)
        h, k = float(center.x), float(center.y)
        a = float(ellipse.hradius)  # Semi-major axis (horizontal radius)
        b = float(ellipse.vradius)  # Semi-minor axis (vertical radius)
        theta = float(ellipse.rotation) if hasattr(ellipse, 'rotation') else 0  # Rotation angle in radians, if available
        
        # Parametric equations for the rotated ellipse
        def parametric_x(t):
            return h + a * np.cos(t) * np.cos(theta) - b * np.sin(t) * np.sin(theta)

        def parametric_y(t):
            return k + a * np.cos(t) * np.sin(theta) + b * np.sin(t) * np.cos(theta)
        
        return parametric_x, parametric_y
    
      @staticmethod
      def from_sympy(sympy_ellipse):
        parametric_x, parametric_y =  ModelEllipseParametric.sympy_ellipse_to_parametric_function(ellipse)
        return ModelEllipseParametric(sympy_ellipse, parametric_x, parametric_y)
      
    
      @staticmethod
      def from_origin_major_minor(origin_point, major, minor):
          model_ellipse_parametric = None
          def compute():
              nonlocal model_ellipse_parametric
              sp_point = sp.Point(origin_point.x, origin_point.y)   
              major_radius = major.get_value()  
              minor_radius = minor.get_value()
              sympy_ellipse = sp.Ellipse(sp_point, major_radius, minor_radius)
              return sympy_ellipse
          
          def create():
              nonlocal model_ellipse_parametric
              sympy_ellipse = compute()
              parametric_x, parametric_y =  ModelEllipseParametric.sympy_ellipse_to_parametric_function(sympy_ellipse)
              model_ellipse_parametric = ModelEllipseParametric(sympy_ellipse, parametric_x, parametric_y)
              return model_ellipse_parametric
          
          def update():
              nonlocal model_ellipse_parametric
              sympy_ellipse = compute()
              model_ellipse_parametric.sympy_ellipse = sympy_ellipse
              parametric_x, parametric_y =  ModelEllipseParametric.sympy_ellipse_to_parametric_function(sympy_ellipse)
              model_ellipse_parametric.update(sympy_ellipse, parametric_x, parametric_y)    
              return model_ellipse_parametric
          
          create()
          
          origin_point.on_change(update)
          major.on_param_change(lambda d: update())
          minor.on_param_change(lambda d: update()) 

          return model_ellipse_parametric
      
    
      @staticmethod        
      def point_on_ellipse(model_ellipse, angle_in_degrees_parameter):
          model_point = None  
        
          def create():
              nonlocal model_point
              model_point = model_ellipse.point_at_angle(angle_in_degrees_parameter.get_value())
            
          def update():
              nonlocal model_point
              new_point = model_ellipse.point_at_angle(angle_in_degrees_parameter.get_value())
              model_point.set(new_point.x, new_point.y, new_point.z)
            
          create()
          angle_in_degrees_parameter.on_param_change(lambda d: update())  
          model_ellipse.on_change(lambda: update())

          return model_point     
              
         
          
    
    
    