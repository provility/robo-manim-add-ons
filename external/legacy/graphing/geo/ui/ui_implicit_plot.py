from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.geo_shape_props import ZIndex
from graphing.geo.model.model_plot import  ModelImplicitPlot
from graphing.geo.ui.ui_style_props import UIStyleProps
from .base_ui import BaseUI
from manim import *

class   UIImplicitPlot(BaseUI):
      def __init__(self, geo_mapper:GeoMapper, 
                   model_implicit_plot:ModelImplicitPlot, 
             
                   plot_range = None, 
                   style_props:UIStyleProps=UIStyleProps.plot_theme()):
          super().__init__(style_props)
          self.geo_mapper = geo_mapper
          self.model_implicit_plot = model_implicit_plot
      
          self.plot_shape = None
          self.create()
          self.plot_shape.set_z_index(ZIndex.PLOT.value)


      def create(self):
          eq_lambda = self.model_implicit_plot.eq_lambda
          self.plot_shape = ImplicitFunction(
                lambda x, y: eq_lambda(x, y),
                color=self.color
            )               
          
      def update(self):
           eq_lambda = self.model_implicit_plot.eq_lambda
           new_plot = ImplicitFunction(
                lambda x, y: eq_lambda(x, y),
                color=self.color
            ) 
           self.plot_shape.become(new_plot)
             
      def view(self):
          return self.plot_shape
      
   
              
          