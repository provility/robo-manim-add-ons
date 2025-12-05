from manim import * 

from graphing.ex_manim.arc_3d import Arc3d
from graphing.geo.geo_mapper_3d import GeoMapper3D
from graphing.geo.threed.model.model_arc_3d import ModelArc3D
from graphing.geo.ui.base_ui import BaseUI
from graphing.geo.ui.ui_style_props import UIStyleProps

class UI3DArc(BaseUI):  
    def __init__(self, model_arc: ModelArc3D, geo_mapper: GeoMapper3D, style_props:UIStyleProps = UIStyleProps.line_theme()):
        super().__init__(style_props)
        self._model = model_arc
        self.geo_mapper = geo_mapper
        self.ui_shape = self.create_view()

    def create_view(self):
        ui_left = self.geo_mapper.model_point_to_ui_point(self._model.left_point)
        ui_right = self.geo_mapper.model_point_to_ui_point(self._model.right_point)
        ui_center = self.geo_mapper.model_point_to_ui_point(self._model.center_point)
        return Arc3d(A=ui_left, B=ui_right, center=ui_center, radius=self._model.radius, segments=self._model.segments)
 
    def view(self):
        return self.ui_shape
    
    def update(self):
        ui_left = self.geo_mapper.model_point_to_ui_point(self._model.left_point)
        ui_right = self.geo_mapper.model_point_to_ui_point(self._model.right_point)
        ui_center = self.geo_mapper.model_point_to_ui_point(self._model.center_point)
        self.ui_shape.become(Arc3d(A=ui_left, B=ui_right, center=ui_center, radius=self._model.radius, segments=self._model.segments))
