from manim import *
from enum import Enum

# Define an enumeration for z-index values
class ZIndex(Enum):
    DOT = 100025
    LABEL = 26
    LINE = 15
    POLYGON = 14
    PLOT = 16
    ANGLE = -1
    ARC = 13
    CIRCLE = 10 # 10 is the default value for circle    
    BRACE = 24
    COVERING_RECTANGLE = 200000
    

       
class StrokeStyle(Enum):
    DOTTED = "dotted"
    SOLID = "solid"
    DASHED = "dashed"
    BOLD = "bold"
    NORMAL = "normal"       
    

    
   
    