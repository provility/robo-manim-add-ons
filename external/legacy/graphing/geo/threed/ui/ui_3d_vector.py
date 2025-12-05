from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.geo_mapper_3d import GeoMapper3D
from graphing.geo.threed.model.model_vector_3d import ModelVector3D
from graphing.geo.threed.ui.ui_line_3d import UI3DLine
from graphing.geo.ui.base_ui import BaseUI
from graphing.geo.ui.ui_line import UILine
from graphing.geo.ui.ui_style_props import UIStyleProps
from manim import *

from graphing.geo.ui.ui_vector import UIVector

class UI3DVector(BaseUI):
    def __init__(self, model_vector:ModelVector3D, geo_mapper: GeoMapper3D, 
                 style_props:UIStyleProps = UIStyleProps.line_theme()):
        super().__init__(style_props) 
        self.model_vector = model_vector
        self.geo_mapper = geo_mapper    
        self.ui_shape = self.create_view()
 
    def create_view(self):
        model_start, model_end = self.model_vector.model_points
        start = self.geo_mapper.model_point_to_ui_point(model_start)
        end = self.geo_mapper.model_point_to_ui_point(model_end)
        return self.build_shape(start, end)

    def build_shape(self, ui_start, ui_end):
        arrow = Arrow3D(start=ui_start, end=ui_end, color=self.style_props.color)
        return arrow

    def update(self):
        model_start, model_end = self.model_vector.model_points
        start = self.geo_mapper.model_point_to_ui_point(model_start)
        end = self.geo_mapper.model_point_to_ui_point(model_end)
        self.ui_shape.put_start_and_end_on(start, end)

    def view(self):
        return self.ui_shape



    
   