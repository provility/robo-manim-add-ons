from sympy import symbols
from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.model.model_parabola import  ModelParabolaParametric
from graphing.geo.ui.ui_style_props import UIStyleProps
from .base_ui import BaseUI
from manim import *

      
class UIParabolaByParametricFunction(BaseUI):
       def __init__(self, geo_mapper:GeoMapper, model_parabola_parametric:ModelParabolaParametric, range, style_props:UIStyleProps = UIStyleProps.ellipse_theme()):
          super().__init__(style_props)
          self.geo_mapper = geo_mapper
          self.model_parabola_parametric = model_parabola_parametric
          self.range = range
          self.parabola_shape = None
          self.create()
          
       def create(self):
          def to_ui(x, y):
              return self.geo_mapper.model_to_ui(x,y)
          
          parametric_x = self.model_parabola_parametric.x_parametric
          parametric_y = self.model_parabola_parametric.y_parametric
          self.parabola_shape = ParametricFunction(
            lambda t: to_ui(parametric_x(t), parametric_y(t)),
            t_range=np.array([-self.range,self.range]),
            color=self.color
        )       
          
       def view(self):
          return self.parabola_shape           
    
    
