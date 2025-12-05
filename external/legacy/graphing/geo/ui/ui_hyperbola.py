from graphing.geo.ui.ui_style_props import UIStyleProps
from .base_ui import BaseUI
from manim import *
import numpy as np
class UIHyperbola(BaseUI):
    def __init__(self, geo_mapper, model_hyperbola,  style_props:UIStyleProps = UIStyleProps.ellipse_theme()):
        super().__init__(style_props)   
        self.geo_mapper = geo_mapper
        self.model_hyperbola = model_hyperbola
        self.plot_shape = None
        self.create()
        
   
    def create(self):
          eq_lambda = self.model_hyperbola.hyperbola_implicit_function
          self.plot_shape = ImplicitFunction(
                lambda x, y: eq_lambda(x, y),
                color=self.color
            )               
          
    def update(self):
           eq_lambda = self.model_hyperbola.hyperbola_implicit_function
           new_plot = ImplicitFunction(
                lambda x, y: eq_lambda(x, y),
                color=self.color
            ) 
           self.plot_shape.become(new_plot)
             
    def view(self):
        return self.plot_shape
        
        
        