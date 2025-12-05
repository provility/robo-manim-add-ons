from graphing.geo.geo_mapper_3d import GeoMapper3D
from graphing.geo.model.model_plot import ModelParametricPlot
from graphing.geo.ui.base_ui import BaseUI
from graphing.geo.ui.ui_style_props import UIStyleProps


class UI3DParametricPlot(BaseUI):
    def __init__(self, geo_mapper:GeoMapper3D, model_parametric_plot:ModelParametricPlot, style_props:UIStyleProps) -> None:
        super().__init__(style_props)
        self.model_parametric_plot = model_parametric_plot
        self.geo_mapper = geo_mapper
        self.axes_3d = geo_mapper.axes
        self.create()
        
    def create(self):
          axes = self.geo_mapper.axes
          eq_lambda = self.model_parametric_plot.eq_lambda
          self.plot_shape = self.axes_3d.plot_parametric_curve(
            lambda t: eq_lambda(t),
            t_range=self.model_parametric_plot.plot_range,
            color=self.color
        )   
    def view(self):
          return self.plot_shape
    
    def update(self):
       axes = self.geo_mapper.axes
       eq_lambda = self.model_parametric_plot.eq_lambda
       new_plot = self.axes_3d.plot_parametric_curve(
            lambda t: eq_lambda(t),
            t_range=self.model_parametric_plot.plot_range,
            color=self.color
        )   
       self.plot_shape.become(new_plot)
        