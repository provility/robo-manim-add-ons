
from graphing.geo.geo_shape_props import ZIndex
from graphing.geo.model.model_polygon import ModelPolygon
from graphing.geo.ui.base_ui import BaseUI
from manim import *

class UIPolygon(BaseUI):
      
    def __init__(self, geo_mapper, model: ModelPolygon, style_props=None):
        super().__init__(style_props)
        self.geo_mapper = geo_mapper
        self.model = model
        self.polygon_shape = None
        self.create()
        
    def update(self):
        new_points = [self.geo_mapper.model_to_ui(p) for p in self.model.points]
        self.polygon_shape.set_points_as_corners(new_points)

    def create(self):
        points = [self.geo_mapper.model_to_ui(p) for p in self.model.points]
        self.polygon_shape = Polygon(
            *points,
            color=self.style_props.color,
            stroke_width=self.style_props.stroke_width,
            fill_opacity=self.fill_opacity, 
        )
        self.polygon_shape.set_z_index(ZIndex.POLYGON.value)
        
    def view(self):
        return self.polygon_shape
    
   

 
     

      
        
        