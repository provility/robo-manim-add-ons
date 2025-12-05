from graphing.geo.ui.ui_coordinate import UICoordinate
from manim import *
class UI3DCoordinate(UICoordinate):
    def __init__(self, geo_mapper, model_point, direction=UP, style_props=None, **kwargs):
        super().__init__(geo_mapper, model_point, direction, style_props, **kwargs)
        
    def formatted_coords(self):
        model_x = self.model_point.x
        model_y = self.model_point.y
        model_z = self.model_point.z
        point_name = self.model_point.identifier
        # Format x and y coordinates
        x_formatted = f"{model_x:.0f}" if model_x == int(model_x) else f"{model_x:.1f}"
        y_formatted = f"{model_y:.0f}" if model_y == int(model_y) else f"{model_y:.1f}"
        z_formatted = f"{model_z:.0f}" if model_z == int(model_z) else f"{model_z:.1f}"
        # Construct the coordinate string
        coord_str = f"({x_formatted}, {y_formatted}, {z_formatted})"
        # Add point name if it exists
        if point_name is not None:
            return f"{point_name} {coord_str}"
        else:
            return coord_str    