from graphing.geo.model.model_point import ModelPoint
from manim import *

class GeoMapper3D:
    def __init__(self, axes:ThreeDAxes):
        self.axes = axes
        
    def model_to_ui(self, x, y, z):
        return self.axes.c2p(x, y, z)
    
    def model_point_to_ui_point(self, model_point:ModelPoint):
        numpy_array =  self.model_to_ui(model_point.x, model_point.y, model_point.z)
        return ModelPoint(numpy_array[0], numpy_array[1], numpy_array[2])    
