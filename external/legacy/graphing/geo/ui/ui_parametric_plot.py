from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.geo_shape_props import ZIndex
from graphing.geo.model.model_plot import ModelExplicitPlot, ModelParametricPlot
from graphing.geo.ui.ui_style_props import UIStyleProps
from .base_ui import BaseUI
from manim import *

class UIParametricPlot(BaseUI):
      def __init__(self, geo_mapper:GeoMapper, model_plot:ModelParametricPlot, plot_range = None, style_props:UIStyleProps=UIStyleProps.plot_theme()):
          super().__init__(style_props)
          self.geo_mapper = geo_mapper
          self.model_plot = model_plot
          self.plot_shape = None
          self.plot_range = plot_range
          self.create()
          self.plot_shape.set_z_index(ZIndex.PLOT.value)


      def create(self):
          eq_lambda = self.model_plot.eq_lambda
          def ui_lambda(t):
              return self.geo_mapper.model_to_ui(*eq_lambda(t))
          
          self.plot_shape = ParametricFunction(
                lambda t: ui_lambda(t),
                t_range=self.plot_range,
                color=self.color
            )
             
      def view(self):
          return self.plot_shape
      
      def update(self):
          eq_lambda = self.model_plot.eq_lambda
          new_plot = ParametricFunction(
                lambda t: self.geo_mapper.model_to_ui(*eq_lambda(t)),
                t_range=self.plot_range,
                color=self.color
            )
             
          self.plot_shape.become(new_plot)
      
    
              
          