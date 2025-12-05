from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.geo_shape_props import ZIndex
from graphing.geo.model.model_plot import ModelExplicitPlot
from graphing.geo.ui.ui_style_props import UIStyleProps
from .base_ui import BaseUI
from manim import *

class UIExplicitPlot(BaseUI):
      def __init__(self, geo_mapper:GeoMapper, 
                   model_plot:ModelExplicitPlot, 
                   style_props:UIStyleProps = UIStyleProps.plot_theme()):
          super().__init__(style_props)
          self.geo_mapper = geo_mapper
          self.model_plot = model_plot
          self.plot_shape = None
          self.plot_range = model_plot.plot_range
          self.create()
          
      def create(self):
           self.plot_shape = self._build_plot()
           self.plot_shape.set_z_index(ZIndex.PLOT.value)
           
           
      def view(self):
          return self.plot_shape
    
      def update(self):
          new_plot = self._build_plot()
          self.plot_shape.become(new_plot)
          self.plot_shape.set_z_index(ZIndex.PLOT.value)
          
      def _build_plot(self):
          axes = self.geo_mapper.axes
          eq_lambda = self.model_plot.eq_lambda
          if self.plot_range is not None:
             return axes.plot(eq_lambda, x_range=self.plot_range, color=self.color)
          else:
             return axes.plot(eq_lambda, color=self.color) 
      
    
              
          