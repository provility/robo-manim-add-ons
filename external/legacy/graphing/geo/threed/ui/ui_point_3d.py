from manim import Dot3D
from graphing.geo.model.model_point import ModelPoint
from graphing.geo.ui.ui_style_props import UIStyleProps
from graphing.geo.ui.base_ui import BaseUI
from graphing.geo.geo_mapper_3d import GeoMapper3D
from graphing.geo.geo_shape_props import ZIndex

class UIPoint3D(BaseUI):
    def __init__(self, geo_mapper: GeoMapper3D, 
                 model_point: ModelPoint,  
                 radius = 0.1,
                 style_props=UIStyleProps.point_theme()) -> None:
        super().__init__(style_props)
        self.model_point = model_point
        self.geo_mapper = geo_mapper
        ui_point = self.geo_mapper.model_to_ui(self.model_point.x, self.model_point.y, self.model_point.z)
        dot = Dot3D(point=ui_point, radius=radius, color=self.color)
        dot.set_opacity(self.fill_opacity)
        self.dot = dot
        self.dot.set_z_index(ZIndex.DOT.value)

    def clear_dynamic(self):
        self.dot.clear_updaters()

    def get_center(self):
        return self.dot.get_center()

    def view(self):
        return self.dot

    def update(self):
        self.update_position()

    def update_position(self):
        new_position = self.geo_mapper.model_point_to_ui_point(self.model_point)
        self.dot.move_to(new_position)

    @classmethod
    def create(cls, x, y, z, geo_mapper: GeoMapper3D, style_props=None):
        model_point = ModelPoint(x, y, z)
        return cls(geo_mapper, model_point, style_props or UIStyleProps.point_theme())

