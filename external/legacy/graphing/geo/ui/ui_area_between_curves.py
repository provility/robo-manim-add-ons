from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.ui.base_ui import BaseUI
from graphing.geo.model.model_area_between_curves import ModelAreaBetweenCurves
from graphing.geo.ui.ui_style_props import UIStyleProps   
from manim import *

class UIAreaBetweenCurves(BaseUI):
    def __init__(self, geo_mapper:GeoMapper, 
                 model_area_between_curves:ModelAreaBetweenCurves, 
                 style_props:UIStyleProps):
        super().__init__(style_props)
        self.geo_mapper = geo_mapper
        self.model_area_between_curves = model_area_between_curves  
        self.create()
        
    def create(self):
        self.area_between_curves_shape = self._create_area_between_curves_shape()
       
    def _create_area_between_curves_shape(self):
        axes = self.geo_mapper.axes
        curve_shape_a = self.model_area_between_curves.curve_a.plot_shape()    
        curve_shape_b = self.model_area_between_curves.curve_b.plot_shape()
        from_x = self.model_area_between_curves.from_x
        to_x = self.model_area_between_curves.to_x
        area_between_curves_shape = axes.get_area(curve_shape_b, 
                        [from_x, to_x],
                        bounded_graph = curve_shape_a, 
                        color=self.style_props.color,
                        opacity=0.3)
        
        
        
        return area_between_curves_shape
        
    def update(self):
        new_area_between_curves_shape = self._create_area_between_curves_shape()
        self.area_between_curves_shape.become(new_area_between_curves_shape)
        
    def view(self):
        return self.area_between_curves_shape

       
        
        
        
        
            