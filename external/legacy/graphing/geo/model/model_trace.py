from graphing.geo.model.model_plot import ModelExplicitPlot
from .base_model import BaseModel
import math
import numpy as np
import sympy as sp
from sympy import Point, Segment
from manim import *
from .model_point import ModelPoint
from .model_parameter import ModelParameter

class ModelTrace(ModelPoint):
    def __init__(self, x, y, ratio):
        super().__init__(x, y)
        self.ratio = ratio
        self.update(ratio)
        
    def update(self, ratio):
         self.ratio = ratio
         numpy_pt = self.point_at(ratio)
         self.set(numpy_pt[0], numpy_pt[1])
         self.notify()      
         
         
    def clear_trace(self):
         self.ui_part.clear_trace() 
        
    def point_at(self, ratio):
        raise NotImplementedError("ModelTrace Subclass must implement point_at method")     
         
class ModelPointTrace(ModelTrace):
     def __init__(self, x, y, z):
        super().__init__(x, y, 0)
        
     def update_trace(self, x, y, z):
        self.set(x, y, z)
        self.notify()   
        
     def update(self, ratio):   
        self.update_trace(self.x, self.y, self.z)
        
     def point_at(self, ratio):   
        return self
    
     @staticmethod
     def from_point(model_point:ModelPoint):
        model_trace = ModelPointTrace(model_point.x, model_point.y, model_point.z)
        model_point.on_change(lambda: model_trace.update_trace(model_point.x, model_point.y, model_point.z))    
        return model_trace
        
        
         
class ModelShapeTrace(ModelTrace):
     def __init__(self, model_shape:BaseModel, ratio):
        self.ratio = ratio
        self.model_shape = model_shape
        numpy_pt = self.point_at(ratio)
        super().__init__(numpy_pt[0], numpy_pt[1], ratio=ratio)
        
     def point_at(self, ratio):
         self.ratio = ratio
         return self.model_shape.point_at(ratio)
     
     
     @staticmethod
     def from_shape(model_shape:BaseModel, ratio_parameter:ModelParameter|str):
        model_trace = None
        def create():
            nonlocal model_trace  
            model_trace = ModelShapeTrace(model_shape, ratio_parameter.get_value())
            
        def update():   
            nonlocal model_trace  
            model_trace.update(ratio_parameter.get_value())   
       
        create()
      #  model_shape.on_change(lambda: update())
        ratio_parameter.on_param_change(lambda d: update())
        return model_trace
    
    
class ModelPlotTrace(ModelTrace):
     def __init__(self, model_plot:ModelExplicitPlot, ratio):
        self.ratio = ratio
        self.model_plot = model_plot
        numpy_pt = self.point_at(ratio)
        super().__init__(numpy_pt[0], numpy_pt[1], ratio=ratio)
        
     def point_at(self, ratio):
         self.ratio = ratio
         return self.model_plot.point_at(ratio)
          
     
     @staticmethod
     def from_plot(model_plot:ModelExplicitPlot, model_parameter:ModelParameter):
        model_trace = None
        def create():
            nonlocal model_trace  
            param_value = model_parameter.get_value()
            model_trace = ModelPlotTrace(model_plot, param_value)
            
        def update():   
            nonlocal model_trace  
            param_value = model_parameter.get_value()
            model_trace.update(param_value)
            
        create()
        
        # hook dependencies, when the input line and the point change, 
        # the output line should get changed as well
        model_plot.on_change(lambda: update())
        model_parameter.on_param_change(lambda d: update())
        
        return model_trace
           
             
             
             
             