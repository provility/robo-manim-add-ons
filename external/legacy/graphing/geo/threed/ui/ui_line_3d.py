from manim import Line, DashedVMobject

from graphing.geo.geo_mapper_3d import GeoMapper3D
from graphing.geo.ui.base_ui import BaseUI
from graphing.geo.threed.model.model_line_3d import ModelLine3D
from graphing.geo.ui.ui_style_props import UIStyleProps

class UI3DLine(BaseUI):
    def __init__(self, model_line: ModelLine3D, geo_mapper: GeoMapper3D, style_props:UIStyleProps = UIStyleProps.line_theme()):
        super().__init__(style_props)
        self._model = model_line
        self.geo_mapper = geo_mapper
        self.ui_shape = self.create_view()
        
    def create_view(self):
        model_start, model_end = self._model.model_points
        start = self.geo_mapper.model_point_to_ui_point(model_start)
        end = self.geo_mapper.model_point_to_ui_point(model_end)
        return self.build_shape(start, end)

    def build_shape(self, ui_start, ui_end):
        line = Line(start=ui_start, end=ui_end, color=self.style_props.color)
        if self.style_props.dashed:
            return DashedVMobject(line, num_dashes=20, dashed_ratio=0.5)
        else:
            return line

    def update(self):
        model_start, model_end = self._model.model_points
        start = self.geo_mapper.model_point_to_ui_point(model_start)
        end = self.geo_mapper.model_point_to_ui_point(model_end)
        if isinstance(self.ui_shape, DashedVMobject):
            new_line = Line(start=start, end=end)
            self.ui_shape.become(DashedVMobject(new_line, num_dashes=20, positive_space_ratio=0.5))
        else:
            self.ui_shape.put_start_and_end_on(start, end)

    def view(self):
        return self.ui_shape



