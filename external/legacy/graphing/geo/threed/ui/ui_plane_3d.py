from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.threed.model.model_plane_3d import ModelPlane3D
from graphing.geo.ui.base_ui import BaseUI
from manim import *
import numpy as np

class UIPlane3D(BaseUI):
    def __init__(self, model_plane_3d:ModelPlane3D, 
                 geo_mapper:GeoMapper, 
                 side_length:float=3, 
                 show_normal_vector:bool = False):
        self.model_plane_3d = model_plane_3d
        self.plane_shape_group = VGroup() 
        self.normal_vector_arrow = None
        self.geo_mapper = geo_mapper
        self.side_length = side_length
        self.show_normal_vector = show_normal_vector
             
        
    def create(self):
        square, normal_vector_arrow = self.create_plane()
        self.plane_shape_group.add(square)
        if normal_vector_arrow is not None:
            self.plane_shape_group.add(normal_vector_arrow)
    
    def update(self):
        new_square, new_normal_vector_arrow = self.create_plane()
        self.plane_shape_group[0].become(new_square)
        if new_normal_vector_arrow is not None:
            self.plane_shape_group[1].become(new_normal_vector_arrow)
        
        
    def view(self):
        return self.plane_shape_group 
    
    
    def create_plane(self):
        normal_vector = self.model_plane_3d.normal_vector.get_as_numpy_array()
        ui_point_on_plane = self.geo_mapper.model_point_to_ui_point(self.model_plane_3d.point_on_plane)
        point_on_plane = ui_point_on_plane.get_as_numpy_array()
    
        # Create a square polygon initially in the XY-plane centered at the origin
        half_side = self.side_length / 2
        square = Polygon(
            [-half_side, -half_side, 0],
            [half_side, -half_side, 0],
            [half_side, half_side, 0],
            [-half_side, half_side, 0],
            fill_opacity=0.5,
            color=BLUE
        )

        # Step 1: Rotate the square so that it aligns with the normal vector
        # Find the axis of rotation (cross product between Z-axis and normal vector)
        z_axis = np.array([0, 0, 1])
        normal_vector_normalized = normal_vector / np.linalg.norm(normal_vector)
        rotation_axis = np.cross(z_axis, normal_vector_normalized)
        rotation_angle = np.arccos(np.dot(z_axis, normal_vector_normalized))  # Angle between Z and normal vector

        if np.linalg.norm(rotation_axis) != 0:  # Avoid dividing by zero when vectors are aligned
            square.rotate(
                    angle=rotation_angle, 
                    axis=rotation_axis, 
                    about_point=ORIGIN  # Rotate around the origin first
                )

        # Step 2: Move the square to the point on the plane
        square.shift(point_on_plane)

        if self.show_normal_vector:
            # Step 3: Add the normal vector starting at the center of the square
            normal_vector_arrow = Arrow(
                start=point_on_plane,
            end=point_on_plane + normal_vector_normalized,  # Extend in the direction of the normal
                color=RED
            )
        else:
            normal_vector_arrow = None  
        return square, normal_vector_arrow  

        
        
        