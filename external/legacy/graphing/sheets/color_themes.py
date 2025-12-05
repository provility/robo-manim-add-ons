from manim import *

DARK_THEME = {
    "line_color": GREEN,
    "label_color": RED,
    "point_color": YELLOW,
    "angle_color": BLUE,
    "plot_color": LIGHT_BROWN,
    "ellipse_color": GOLD,
    "parabola_color": GREEN_B,
    "hyperbola_color": LIGHT_BROWN,
    "circle_color": BLUE_A,
    "triangle_color": YELLOW_B,
    "square_color": RED,
    "pentagon_color": BLUE_C,
    "hexagon_color": RED,   
    "distance_marker_color": RED,
    "background_color": BLUE_A,
    "grid_color": GRAY,
    "axis_color": GREEN,
    "tick_color": GREEN,
    "tick_label_color": GREEN,
    "number_line_color": GREEN,
    "number_line_label_color": GREEN,
    "brace_color": GREEN,
    "brace_label_color": GREEN,
    "brace_label_scale_factor": 24,
    "arrow_color": GREEN,
    "arrow_tip_color": GREEN,
    "dynamic_prop_color": RED,
    "trace_color":GREEN,
    "text_color":RED,
    "arc_color":PURPLE,
    "polygon_color":PURPLE,
    "vector_color":ORANGE,    
}
LIGHT_THEME = {
    "line_color": GREEN,
    "label_color": GREEN,
    "angle_color": BLUE,
    "point_color": GREEN,
    "plot_color": BLUE_A,
    "ellipse_color": BLUE_B,
    "parabola_color": BLUE_C,
    "hyperbola_color": BLUE_D,
    "circle_color": GREEN_A,
    "triangle_color": GREEN_B,
    "distance_marker_color": GREEN_C,
    "square_color": RED,
    "background_color": GREEN,
    "grid_color": GRAY,
    "axis_color": BLUE_A,
    "tick_color": BLUE_A,
    "tick_label_color": BLUE_A,
    "number_line_color": BLUE_A,
    "number_line_label_color": BLUE_A,
    "brace_color": BLUE_A,
    "brace_label_color": BLUE_A,
    "brace_label_scale_factor": 24,
    "arrow_color": RED_A,
    "arrow_tip_color": RED_B,
    "dynamic_prop_color":RED,
    "trace_color":GREEN,
    "text_color":RED,
    "arc_color":PURPLE,
    "polygon_color":PURPLE,
    "vector_color":RED, 
}

class ColorTheme:
    _instance = None

    def __new__(cls, theme_dict = DARK_THEME):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Initialize any attributes here
        return cls._instance
    
    def __init__(self, theme_dict = DARK_THEME):
        self.theme_dict = theme_dict
    def set_color_theme(self, theme):
        self.theme_dict = theme
        
    def point_color(self):
        return self.theme_dict["point_color"]
    def line_color(self):
        return self.theme_dict["line_color"]
    def angle_color(self):
        return self.theme_dict["angle_color"]   
    def label_color(self):
        return self.theme_dict["label_color"]
    def plot_color(self):
        return self.theme_dict["plot_color"]
    def ellipse_color(self):
        return self.theme_dict["ellipse_color"]
    def parabola_color(self):
        return self.theme_dict["parabola_color"]
    def hyperbola_color(self):
        return self.theme_dict["hyperbola_color"]
    def circle_color(self):
        return self.theme_dict["circle_color"]
    def  triangle_color(self):
        return self.theme_dict["triangle_color"]
    def square_color(self):
        return self.theme_dict["square_color"]
   
    def background_color(self):
        return self.theme_dict["background_color"]
    def grid_color(self):
        return self.theme_dict["grid_color"]
    def axis_color(self):
        return self.theme_dict["axis_color"]
    def tick_color(self):
        return self.theme_dict["tick_color"]
    def tick_label_color(self): 
        return self.theme_dict["tick_label_color"]
    def number_line_color(self):
        return self.theme_dict["number_line_color"]
    def number_line_label_color(self):
        return self.theme_dict["number_line_label_color"]
    def brace_color(self):
        return self.theme_dict["brace_color"]
    def brace_label_color(self):
        return self.theme_dict["brace_label_color"]
    def brace_label_scale_factor(self):
        return self.theme_dict["brace_label_scale_factor"] 
    def arrow_color(self):
        return self.theme_dict["arrow_color"]
    def arrow_tip_color(self):  
        return self.theme_dict["arrow_tip_color"]   
    
    def distance_marker_color(self):
        return self.theme_dict["distance_marker_color"] 
    
    def dynamic_prop_color(self):
        return self.theme_dict["dynamic_prop_color"]   
    
    def trace_color(self):
        return self.theme_dict["trace_color"]      
    
    def text_color(self):
        return self.theme_dict["text_color"]    
    
    def arc_color(self):
        return self.theme_dict["arc_color"]
    def polygon_color(self):
        return self.theme_dict["polygon_color"] 
    
    def vector_color(self):
        return self.theme_dict["vector_color"]  
    
    
    @staticmethod   
    def dark_theme():
        return ColorTheme(DARK_THEME)
    @staticmethod
    def light_theme():
        return ColorTheme(LIGHT_THEME)
    
   
        
CURRENT_COLOR_THEME  = ColorTheme.dark_theme()

def set_current_theme(color_theme):
    global CURRENT_COLOR_THEME  
    CURRENT_COLOR_THEME = color_theme
    
    
  