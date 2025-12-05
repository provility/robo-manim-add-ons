from graphing.geo.effect_command import EffectCommandManager
from graphing.geo.geo_mapper_3d import GeoMapper3D
from graphing.geo.model.model_point import ModelPoint
from graphing.geo.threed.camera_confis import CameraConfig
from graphing.geo.threed.model.model_arc_3d import ModelArc3D
from graphing.geo.threed.model.model_line_3d import ModelLine3D
from graphing.geo.threed.model.model_plane_3d import ModelPlane3D
from graphing.geo.threed.model.model_vector_3d import ModelVector3D
from graphing.geo.threed.ui.ui_3d_coordinate import UI3DCoordinate
from graphing.geo.threed.ui.ui_3d_vector import UI3DVector
from graphing.geo.threed.ui.ui_arc_3d import UI3DArc
from graphing.geo.threed.ui.ui_line_3d import UI3DLine
from graphing.geo.threed.ui.ui_plane_3d import UIPlane3D
from graphing.geo.threed.ui.ui_point_3d import UIPoint3D
from graphing.geo.ui.ui_point import UIPoint
from graphing.sheets.axes_builder_3d import AxesBuilder3D
from graphing.sheets.base_graphsheet2d import BaseGraphSheet2D
from graphing.geo.ui.ui_style_props import UIStyleProps
from manim import *

from graphing.sheets.color_themes import CURRENT_COLOR_THEME
from graphing.sheets.common_graphsheet import CommonGraphSheet

class Graphsheet3D(CommonGraphSheet):
    def __init__(self, scene, add_coordinates=False, show_axes_labels=False):
        super().__init__(scene) 
        self.axes_builder = AxesBuilder3D(scene, show_axes_labels=show_axes_labels  ) # this is 3D scene
        self.axes_group = self.axes_builder.axes_group
        self.axes = self.axes_builder.axes
        self.scene.add(self.axes_group)
        self.geo_mapper = GeoMapper3D(self.axes)
        self.effect_command_manager = EffectCommandManager(scene)

    def x_right_y_up_z_towards_origin(self):
        self._orient_camera(**CameraConfig.x_right_y_up_z_towards_origin())
        self.axes_group.rotate(angle=-PI / 4, axis=UP)
        
        
    def _orient_camera(self, phi=0, theta=0, gamma=0, zoom=0.7, frame_center=None):
        self.scene.set_camera_orientation(phi=phi * DEGREES, theta=theta*DEGREES, gamma=gamma*DEGREES, zoom=zoom)  
        if frame_center:
            self.scene.set_camera_frame_center(frame_center)
    
            
    def point_3d(self, model_point_or_tuple, color=CURRENT_COLOR_THEME.point_color(), no_animate =True, fill_color=None, fill_opacity=0.8):
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        model_point = self._point_from_input(model_point_or_tuple)
        ui_point = UIPoint3D(self.geo_mapper, model_point, style_props=style_props)
        self._register_object(model_point, ui_point, no_animate)
        return model_point
    
    def coordinate_3d(self, model_point_or_tuple, direction=UP,    color=CURRENT_COLOR_THEME.point_color(), fill_color=None, fill_opacity=0.8):
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        model_point = self._point_from_input(model_point_or_tuple)
        ui_coordinate = UI3DCoordinate(self.geo_mapper, model_point, direction=direction, style_props=style_props)
        self._register_object(model_point, ui_coordinate)
        return model_point  

    def point_next_to_model(self, next_to_model_name_or_model, direction, color=CURRENT_COLOR_THEME.point_color(), 
                            no_animate =False, fill_color=None, fill_opacity=0.8):
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        reference_model = self._model_from_input(next_to_model_name_or_model)
        model_point = ModelPoint.next_to_model(reference_model, direction=direction)
        ui_point = UIPoint(self.geo_mapper, model_point, style_props=style_props)
        self._register_object(model_point, ui_point, no_animate)
        return model_point
    

    def new_translated_point(self, model_point_or_tuple, model_vector, color=CURRENT_COLOR_THEME.point_color(), 
                             no_animate =False, fill_color=None, fill_opacity=0.8):
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        model_point = self._point_from_input(model_point_or_tuple)
        model_point = ModelPoint.synch_translate(model_point, model_vector)
        ui_point = UIPoint3D(self.geo_mapper, model_point, style_props=style_props)
        self._register_object(model_point, ui_point, no_animate)
        return model_point
    
    def new_scaled_point(self, model_point_or_tuple, scale_factor_parameter, color=CURRENT_COLOR_THEME.point_color(), 
                         no_animate =False, fill_color=None, fill_opacity=0.8):
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        model_point = self._point_from_input(model_point_or_tuple)
        scaled_point = model_point.scale(scale_factor_parameter)
        ui_point = UIPoint3D(self.geo_mapper, scaled_point, style_props=style_props)
        self._register_object(scaled_point, ui_point, no_animate)
        return scaled_point  
    
    def translate_by_vector(self, model_point, model_vector, run_time=2, rate_func=linear):
        self.alpha_animator.translate_point(model_point, model_vector, run_time, rate_func)
       
    def translate_to(self, model_point, target_point, run_time=2, rate_func=linear):
        model_vector = ModelVector3D.from_points(model_point, target_point)   
        self.alpha_animator.translate_point(model_point, model_vector, run_time, rate_func)      
        
        
    def line_3d(self, start_point, end_point, color=CURRENT_COLOR_THEME.line_color(), dashed=False, no_animate=True):
        style_props = self._create_style_props(color,
                                               fill_color=color,
                                               fill_opacity=1,
                                               default_style= UIStyleProps.line_theme(), 
                                               dashed=dashed)
       
        model_line = ModelLine3D.from_points(start_point, end_point)
        ui_line = UI3DLine(model_line, self.geo_mapper, style_props=style_props)    
        self._register_object(model_line, ui_line, no_animate)
        return model_line
            
    def vector_3d(self, start_point, end_point, identifier, color=CURRENT_COLOR_THEME.line_color(), dashed=False, no_animate=True):
        style_props = self._create_style_props(color,
                                               fill_color=color,
                                               fill_opacity=1,
                                               default_style= UIStyleProps.line_theme(), 
                                               dashed=dashed)
        model_vector = ModelVector3D.from_points(start_point, end_point)
        ui_vector = UI3DVector(model_vector, self.geo_mapper, style_props=style_props)
        self._register_object(model_vector, ui_vector, no_animate)
        return model_vector
    
    def arc_3d(self, left_point, right_point, center_point, color=CURRENT_COLOR_THEME.line_color(), dashed=False, no_animate=True):
        style_props = self._create_style_props(color,
                                               fill_color=color,
                                               fill_opacity=1,
                                               default_style= UIStyleProps.line_theme(), 
                                               dashed=dashed)
        model_arc = ModelArc3D.arc_from_points(left_point, right_point, center_point)
        ui_arc = UI3DArc(model_arc, self.geo_mapper, style_props=style_props)
        self._register_object(model_arc, ui_arc, no_animate)
        return model_arc
    
    def plane_3d(self,  normal_vector, point,  identifier, 
                 side_length = 3, show_normal_vector = False, color=CURRENT_COLOR_THEME.line_color(), dashed=False, no_animate=True):
        style_props = self._create_style_props(color,
                                               fill_color=color,
                                               fill_opacity=1,
                                               default_style= UIStyleProps.line_theme(), 
                                               dashed=dashed)
        model_plane = ModelPlane3D.from_point_and_normal(normal_vector,point)
        ui_plane = UIPlane3D(model_plane, self.geo_mapper, side_length=side_length, show_normal_vector=show_normal_vector, style_props=style_props)
        self._register_object(model_plane, ui_plane, no_animate)
        return model_plane
            
        
   