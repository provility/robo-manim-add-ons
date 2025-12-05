from manim import *

from graphing.geo.model.model_area import ModelArea
from .base_ui import BaseUI
from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.ui.ui_style_props import UIStyleProps
from graphing.geo.geo_shape_props import ZIndex

class UIArea(BaseUI):
     def __init__(self, geo_mapper:GeoMapper, 
                   model_area:ModelArea,
                   style_props:UIStyleProps = UIStyleProps.plot_theme()):
          super().__init__(style_props)
          self.geo_mapper = geo_mapper
          self.model_area = model_area
          self.plot_shape = None
          self.area_shape = None	
          self.create()
          self.area_shape.set_z_index(ZIndex.PLOT.value)
                  
     def create(self):
          axes = self.geo_mapper.axes
          model_plot = self.model_area.model_plot
          plot_range = model_plot.plot_range
          eq_lambda = model_plot.eq_lambda
          if plot_range is not None:
             self.plot_shape = axes.plot(eq_lambda, x_range=plot_range)
          else:
             self.plot_shape = axes.plot(eq_lambda)  
         
             
          self.area_shape = axes.get_area(
				self.plot_shape,
				x_range=self._x_range_from_parameters(),
                color=self.color
			)  
          
     def update(self):
          new_area_shape = self.geo_mapper.axes.get_area(
				self.plot_shape,
				x_range=self._x_range_from_parameters(),
                color=self.color
			)
          self.area_shape.become(new_area_shape)
          
     def view(self):
          return self.area_shape
     
     
     def _x_range_from_parameters(self):
          return [parameter.get_value() for parameter in self.model_area.area_range_parameters]
          