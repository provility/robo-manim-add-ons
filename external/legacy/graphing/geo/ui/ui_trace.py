
from graphing.geo.ui.ui_style_props import UIStyleProps
from .base_ui import BaseUI
from ..model.model_trace import ModelTrace
from ..geo_mapper import GeoMapper
from ..geo_shape_props import ZIndex

from manim import *

class UITrace(BaseUI):
        def __init__(self, geo_mapper: GeoMapper, 
                     model_trace:ModelTrace, 
                     style_props:UIStyleProps = UIStyleProps.trace_theme()) -> None:
                super().__init__(style_props)
                self.model_trace = model_trace
                self.geo_mapper = geo_mapper
                self.trace = None
                self.create()        
     
        def create(self):
            self.trace = self.build_trace()
                        
        def get_ui_point(self):
            point =  self.geo_mapper.model_to_ui(self.model_trace.x, self.model_trace.y)
            return point
        
        def view(self):
            return self.trace
        
        def clear_trace(self):
            self.trace.become(self.build_trace())
            
       
        def build_trace(self):
            def trace_point_func():
                point = self.get_ui_point()
                return np.array([point[0], point[1], 0])
            
            trace = TracedPath(trace_point_func, stroke_width=self.stroke_width, stroke_color=self.color)
            trace.set_z_index(ZIndex.DOT.value)
            return trace
            
   
            
