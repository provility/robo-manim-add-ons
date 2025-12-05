from graphing.geo.model.model_line import ModelLine
from graphing.geo.model.model_parameter import ModelParameter
from graphing.geo.model.model_point import ModelPoint
from graphing.math.geometry_utils import GeometryUtils
from .base_model import BaseModel
from .model_plot import ModelExplicitPlot
from manim import *
import sympy as sp
class ModelTanget(ModelLine):
      def __init__(self, model_plot:ModelExplicitPlot, 
                   model_parameter:ModelParameter,
                   model_line:ModelLine):
          self.model_plot = model_plot
          self.model_parameter = model_parameter
          super().__init__(*model_line.as_points())
          
          
      def update_slope_line(self, new_slope_line):
           self.update(*new_slope_line.as_points())
     
      def slope_line(self):
          return self
      
      @staticmethod   
      def tangent_on_plot(model_plot:ModelExplicitPlot, model_parameter:ModelParameter, slope_length=2, dx = 0.01):
          model_tangent = None
          
          
          def computation():
              at = model_parameter.get_value()
              numpy_pt1 = model_plot.point_at(at)
              numpy_pt2  = model_plot.point_at(at+dx)
              direction_vector = numpy_pt2 - numpy_pt1
              direction_vector_sympy = sp.Point(direction_vector[0], direction_vector[1])
              point1 = sp.Point(numpy_pt1[0], numpy_pt1[1])
              start_point, end_point = GeometryUtils.get_slope_line(point1, direction_vector_sympy, slope_length)
              model_start_point = ModelPoint.from_sym_point(start_point)
              model_end_point = ModelPoint.from_sym_point(end_point)
              return ModelLine.from_points(model_start_point, model_end_point)    

        
          def create():
              nonlocal model_tangent  
              model_line = computation()
              model_tangent = ModelTanget(model_plot, model_parameter, model_line)
        

          def update():   
              nonlocal model_tangent   
              model_line = computation()   
              model_tangent.update_slope_line(model_line)
               
          
            
          create()
        
        # hook dependencies, when the input line and the point change, 
        # the output line should get changed as well
          model_plot.on_change(lambda: update())
          model_parameter.on_param_change(lambda param: update())
          return model_tangent
          
      
     
      
         
    