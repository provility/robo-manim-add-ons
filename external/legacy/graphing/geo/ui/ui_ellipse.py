from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.model.base_model import BaseModel
from graphing.geo.ui.ui_style_props import UIStyleProps
from .base_ui import BaseUI
from ..model.model_ellipse import  ModelEllipseParametric
from manim import *

      
class UIEllipseByParametricFunction(BaseUI):
       def __init__(self, geo_mapper:GeoMapper, model_ellipse_parameteric:ModelEllipseParametric,  style_props:UIStyleProps = UIStyleProps.ellipse_theme()):
          super().__init__(style_props)
          self.geo_mapper = geo_mapper
          self.model_ellipse_parameteric = model_ellipse_parameteric
          self.ellipse_shape = None
          self.create()
          
       def create(self):
          def to_ui(x, y):
              return self.geo_mapper.model_to_ui(x,y)
          
          parametric_x = self.model_ellipse_parameteric.parametric_x
          parametric_y = self.model_ellipse_parameteric.parametric_y
          self.ellipse_shape = ParametricFunction(
            lambda t: to_ui(parametric_x(t), parametric_y(t)),
            t_range=np.array([0, TAU]),
            color=self.color
        )    
          
       def view(self):
          return self.ellipse_shape           
