from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.geo_shape_props import ZIndex
from graphing.geo.model.model_point import ModelPoint
from graphing.geo.ui.base_ui import BaseUI
from graphing.geo.ui.ui_style_props import UIStyleProps
from manim import *

class UICoordinate(BaseUI):
    def __init__(self, geo_mapper: GeoMapper, 
                   model_point:ModelPoint,  
                   direction=UP,    
                   style_props=UIStyleProps.point_theme()) -> None:
            super().__init__(style_props)
            self.model_point = model_point
            self.direction = direction
            self.geo_mapper = geo_mapper
            self.coord_text = None
            self.create()
            
    def create(self):
        self.coord_text = Text(self.formatted_coords(), color=self.color)
        self.coord_text.set_z_index(ZIndex.DOT.value)
        model_x = self.model_point.x
        model_y = self.model_point.y
        model_z = self.model_point.z
        ui_x = self.geo_mapper.model_to_ui(model_x, model_y, model_z)[0]
        ui_y = self.geo_mapper.model_to_ui(model_x, model_y, model_z)[1] 
        self.coord_text.move_to(np.array([ui_x, ui_y,0])).shift(self.direction)
        self.coord_text.scale(0.5)
        return self.coord_text
               
    def view(self):
          return self.coord_text
       
    def update(self):
        self.update_position()
        
        
    def update_position(self):
        model_x = self.model_point.x
        model_y = self.model_point.y
        model_z = self.model_point.z
        ui_xyz =  self.geo_mapper.model_to_ui(model_x, model_y, model_z)
        ui_x = ui_xyz[0]
        ui_y = ui_xyz[1] 
        ui_z = ui_xyz[2] 
        self.coord_text.become(Text(self.formatted_coords(), color=self.color)) 
        self.coord_text.move_to(np.array([ui_x, ui_y, ui_z])).shift(self.direction)
        self.coord_text.scale(0.5)
              
    def formatted_coords(self):
        model_x = self.model_point.x
        model_y = self.model_point.y
        point_name = self.model_point.identifier
        # Format x and y coordinates
        x_formatted = f"{model_x:.0f}" if model_x == int(model_x) else f"{model_x:.1f}"
        y_formatted = f"{model_y:.0f}" if model_y == int(model_y) else f"{model_y:.1f}"
        
        # Construct the coordinate string
        coord_str = f"({x_formatted}, {y_formatted})"
        
        # Add point name if it exists
        if point_name is not None:
            return f"{point_name} {coord_str}"
        else:
            return coord_str
                     

    
    
    