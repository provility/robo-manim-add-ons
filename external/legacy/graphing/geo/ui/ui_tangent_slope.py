from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.model.model_slope import ModelTangentSlope
from graphing.geo.ui.base_ui import BaseUI
from graphing.geo.ui.ui_style_props import UIStyleProps
from manim import *

class UITangentSlope(BaseUI):
    def __init__(self, geo_mapper:GeoMapper, model_tangent_slope:ModelTangentSlope,
                 style_props:UIStyleProps,
                 dx_label:str="dx",
                 dy_label:str="dy", 
                 dx_value:float=0.1,
                 tangent_length:float=1.5):
        super().__init__(style_props=style_props)
        self.geo_mapper = geo_mapper
        self.model_tangent_slope = model_tangent_slope
        self.ui_shape = None
        self.dx_label = dx_label
        self.dy_label = dy_label
        self.dx_value = dx_value
        self.tangent_length = tangent_length
        self.create()   
        
    
    def create(self):
        self.ui_shape = self.get_tangent_slope_group()
        

    def update(self):
        new_shape = self.get_tangent_slope_group()
        tangent_line, dx_line, dy_line, dx_label, dy_label = new_shape
        self.ui_shape[0].become(tangent_line)   
        self.ui_shape[1].become(dx_line)
        self.ui_shape[2].become(dy_line)
        self.ui_shape[3].become(dx_label)
        self.ui_shape[4].become(dy_label)
     
    
    def view(self):
        return self.ui_shape
    
    
    def get_tangent_slope_group(self, dx_color=GREEN, dy_color=ORANGE, ):
        axes = self.geo_mapper.axes
        graph = self.model_tangent_slope.plot_shape()
        x_value = self.model_tangent_slope.model_x  
        # Get the point on the graph at x_value
        point = axes.i2gp(x_value, graph)

        # Calculate dx and dy for display purposes
        delta_x = self.dx_value  # Small value to display dx and dy
        dx = delta_x
        # Get the nearby point for dy calculation
        next_point = axes.i2gp(x_value + dx, graph)
        dy = next_point[1] - point[1]
        slope = dy / dx

      # Define the direction vector for the tangent line based on the slope
        direction_vector = np.array([1, slope, 0])
        direction_vector /= np.linalg.norm(direction_vector)  # Normalize to unit vector

        # Create the tangent line with fixed length
        tangent_line = Line(
            start=point - direction_vector * self.tangent_length / 2,
            end=point + direction_vector * self.tangent_length / 2,
            color=YELLOW
        )

        # Calculate the dx and dy lines based on the tangent line's endpoint
        dx_line = Line(
            start=point,
            end=[tangent_line.get_end()[0], point[1], 0],
            color=dx_color
        )
        dy_line = Line(
            start=dx_line.get_end(),
            end=tangent_line.get_end(),
            color=dy_color
        )

        # Labels for dx and dy
        dx_label_tex = MathTex(self.dx_label, color=dx_color).next_to(dx_line, DOWN)
        dy_label_tex = MathTex(self.dy_label, color=dy_color).next_to(dy_line, RIGHT)

        # Group all elements together
        tangent_slope_group = VGroup(tangent_line, dx_line, dy_line, dx_label_tex, dy_label_tex)
        return tangent_slope_group
    
    