from graphing.geo.ui.ui_style_props import UIStyleProps
from .base_ui import BaseUI
from ..geo_mapper import GeoMapper
from ..model.model_intersection import ModelIntersection
from .ui_point_list import UIPointList
from manim import *

class UIIntersection(UIPointList):
     def __init__(self, geo_mapper:GeoMapper, model_intersection:ModelIntersection, 
                   style_props:UIStyleProps=UIStyleProps.point_theme()) -> None:
          super().__init__(geo_mapper=geo_mapper, model_point_list=model_intersection, 
                            style_props=style_props)
          
          