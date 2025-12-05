from manim import *

from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.model.model_tangent import ModelTanget
from graphing.geo.ui.ui_line import UILine
from graphing.geo.ui.ui_style_props import UIStyleProps
from graphing.math.geometry_utils import GeometryUtils
from .base_ui import BaseUI


class UITangent(UILine):
    def __init__(self, geo_mapper:GeoMapper, model_tangent:ModelTanget,
                 style_props:UIStyleProps=UIStyleProps.line_theme()):
        super().__init__(geo_mapper, model_tangent, style_props)   

       
        
    
     
     
     