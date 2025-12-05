from graphing.math.function_expression_utils import FunctionUtils
from .base_model import BaseModel
import math
import numpy as np
import sympy as sp
from sympy import Point, Segment
from manim import *
from .model_point import ModelPoint
from .model_line import ModelLine

class ModelPlot(BaseModel):
    def __init__(self, eq_lambda, plot_range=None):
        super().__init__()
        self.eq_lambda = eq_lambda  
        self.plot_range = plot_range
        
    def update_lambda(self, new_eq_lambda):
        self.eq_lambda = new_eq_lambda
        self.notify()
        

    @staticmethod
    def from_expression(expression:str, subs_dict_of_model_parameters = {}, plot_range=None):
        model_plot = None
        
        def computation():
            sub_dict = {k:v.get_value() for k,v in subs_dict_of_model_parameters.items()}
            sympy_expression = FunctionUtils.evaulatable_sympy_expression(expression, sub_dict)          
            # Determine the variables in the equation
            variables = sympy_expression.free_symbols
            # If there are two variables, use ImplicitFunction
            if len(variables) == 2:
                x, y = variables
                eq_lambda = sp.lambdify((x, y), sympy_expression, "numpy")
                return ModelImplicitPlot(eq_lambda=eq_lambda)
            else:
                var = list(variables)[0]
                # Standard function plot y = f(x)
                eq_lambda = sp.lambdify(var, sympy_expression, "numpy")
                return ModelExplicitPlot(eq_lambda=eq_lambda, plot_range=plot_range)
            
        def create():
            nonlocal model_plot
            model_plot = computation()
            return model_plot
        
        def update(value):   
            nonlocal model_plot
            new_model_plot = computation()
            model_plot.update_lambda(new_model_plot.eq_lambda)  
   
        create()
        
        # hook each paramter in the subs_dict_of_model_parameters to the update function
        for k,model_parameter in subs_dict_of_model_parameters.items():
            model_parameter.on_param_change(update) 
            
        return model_plot
        
    @staticmethod
    def plot_parametric(expression1, expression2, para_range, subs_dict_of_model_parameters = {}, color=YELLOW):
        model_plot = None
        sympy_expression1 = FunctionUtils.ensure_expression(expression1)
        sympy_expression2 = FunctionUtils.ensure_expression(expression2)
        
        def computation():
            nonlocal sympy_expression1, sympy_expression2   
            subs_dict = {k:v.get_value() for k,v in subs_dict_of_model_parameters.items()}
            substitued_expression1 = sympy_expression1.subs(subs_dict)
            substitued_expression2 = sympy_expression2.subs(subs_dict)
            var = substitued_expression1.free_symbols.pop()    
            eq_lambda1 = sp.lambdify(var, substitued_expression1, "numpy")
            eq_lambda2 = sp.lambdify(var, substitued_expression2, "numpy")
            def eq_lambda(t):
                return np.array([eq_lambda1(t), eq_lambda2(t), 0])
            return eq_lambda    
        
        def create():
            nonlocal model_plot
            eq_lambda = computation()
            model_plot = ModelParametricPlot(eq_lambda=eq_lambda, plot_range=para_range)
           
        
        def update(value):   
            nonlocal model_plot
            new_lamabda = computation()
            model_plot.update_lambda(new_lamabda)  

        create()
        # hook each paramter in the subs_dict_of_model_parameters to the update function
        for k,model_parameter in subs_dict_of_model_parameters.items():
            model_parameter.on_param_change(update) 
        return model_plot       

    @staticmethod
    def from_lambda_function(lambda_function, plot_range=None):
        model_plot = None
        def computation():
            eq_lambda = lambda_function
            return ModelExplicitPlot(eq_lambda=eq_lambda, plot_range=plot_range)
        
        def create():
            nonlocal model_plot
            model_plot = computation()
        
        create()
        return model_plot   
    
    @staticmethod
    def plot_parametric_lambda(lambda_function_1, lambda_function_2, plot_range):
            eq_lambda1 = lambda_function_1
            eq_lambda2 = lambda_function_2
           
            def eq_lambda(t):
                return np.array([eq_lambda1(t), eq_lambda2(t), 0])
            
            return ModelParametricPlot(eq_lambda=eq_lambda, plot_range=plot_range)
        
        
               
        
        
class ModelExplicitPlot(ModelPlot):
      def __init__(self, eq_lambda, plot_range=None):
          super().__init__(eq_lambda, plot_range)
          
      def point_at(self, at): # the eq_lambda returns a number, unlike parametric plot which returns an array
          return np.array([at, self.eq_lambda(at), 0])  
      
      def point_at_x(self, x):
          return ModelPoint(x, self.eq_lambda(x))   
      
      def plot_shape(self):
          return self.view()
      
      @staticmethod
      def point_on_plot(model_plot, model_parameter):
          model_point = None    
          
          def create():
              nonlocal model_point  
              model_point = model_plot.point_at_x(model_parameter.get_value())
              
          def update():
              nonlocal model_point
              new_point = model_plot.point_at_x(model_parameter.get_value())
              model_point.set(new_point.x, new_point.y, 0)
              
          create()  
          model_parameter.on_param_change(lambda d: update())
          model_plot.on_change(lambda: update())    
          return model_point
          
class ModelParametricPlot(ModelPlot):
      def __init__(self, eq_lambda, plot_range=None):
          super().__init__(eq_lambda, plot_range)
          
      def point_at(self, at):
          return self.eq_lambda(at)       
      
      def point_at_t(self, t):
          return ModelPoint(self.eq_lambda(t)[0], self.eq_lambda(t)[1])
      
      @staticmethod
      def point_on_plot(model_plot, model_parameter):
          model_point = None    
          
          def create():
              nonlocal model_point  
              model_point = model_plot.point_at_t(model_parameter.get_value())
              
          def update():
              nonlocal model_point
              new_point = model_plot.point_at_t(model_parameter.get_value())
              model_point.set(new_point.x, new_point.y, 0)
              
          create()  
          model_parameter.on_param_change(lambda d: update())
          model_plot.on_change(lambda: update())    
          return model_point
                    
class ModelImplicitPlot(ModelPlot):
      def __init__(self, eq_lambda, plot_range=None):
          super().__init__(eq_lambda, plot_range)
          