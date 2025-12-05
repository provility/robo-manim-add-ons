from manim import *

from graphing.geo.model.model_reimann import ModelRiemann
from .base_ui import BaseUI
from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.ui.ui_style_props import UIStyleProps
from graphing.geo.geo_shape_props import ZIndex

class UIReimann(BaseUI):
     def __init__(self, scene:Scene,
                  geo_mapper:GeoMapper, 
                  model_riemann:ModelRiemann,
                   style_props:UIStyleProps = UIStyleProps.plot_theme()):
          super().__init__(style_props)
          self.scene = scene
          self.geo_mapper = geo_mapper
          self.model_riemann = model_riemann
          self.plot_shape = None
          self.area_shape = None	
          self.create()
          self.area_shape.set_z_index(ZIndex.PLOT.value)
                  
     def create(self):
          axes = self.geo_mapper.axes
          model_plot = self.model_riemann.model_plot	
          plot_range = model_plot.plot_range
          eq_lambda = model_plot.eq_lambda
          if plot_range is not None:
             self.plot_shape = axes.plot(eq_lambda, x_range=plot_range)
          else:
             self.plot_shape = axes.plot(eq_lambda)  
             
          dx_value = self.model_riemann.dx_parameter.get_value()   
             
          self.area_shape = axes.get_riemann_rectangles(
				self.plot_shape,
				x_range=self.model_riemann.sum_range,
				dx=dx_value,
				stroke_width=1,
				stroke_color=self.color
			).set_color_by_gradient(RED, BLUE, GREEN)    
          
     def update(self):
         dx_value = self.model_riemann.dx_parameter.get_value()
         new_area_shape = self.geo_mapper.axes.get_riemann_rectangles(
				self.plot_shape,
				x_range=self.model_riemann.sum_range,
				dx=dx_value,
				stroke_width=1,
				stroke_color=self.color
			).set_color_by_gradient(RED, BLUE, GREEN)
         self.area_shape.become(new_area_shape)
         
          
     def view(self):
          return self.area_shape
          



    