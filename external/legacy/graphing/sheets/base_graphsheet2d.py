from graphing.geo.geo_mapper import GeoMapper
from manim import *

from graphing.geo.model.base_model import BaseModel
from graphing.geo.model.model_angle import ModelAngle
from graphing.geo.model.model_vector import ModelVector
from graphing.geo.model.model_circle import ModelCircle
from graphing.geo.model.model_line import ModelLine, ModelLine2Points
from graphing.geo.model.model_parameter import ModelParameter
from graphing.geo.model.model_plot import ModelExplicitPlot, ModelPlot
from graphing.geo.model.model_point import ModelPoint
from graphing.geo.number_line_geo_mapper import NumberLineGeoMapper
from graphing.geo.ui.ui_angle import UIAngle, UIArrowAngle, UISectorAngle
from graphing.geo.ui.ui_circle import UICircle
from graphing.geo.ui.ui_line import UILine
from graphing.geo.ui.ui_point import UIPoint
from graphing.geo.ui.ui_polygon import UIPolygon
from graphing.geo.ui.ui_style_props import UIStyleProps
from graphing.geo.ui.ui_vector import UIComplex, UIVector
from graphing.sheets.alpha_animators import AlphaAnimator
from graphing.sheets.arrow_animator import ArrowAnimator
from graphing.sheets.common_graphsheet import CommonGraphSheet
from graphing.sheets.geo_property_calculator import GeoPropertyCalculator
from graphing.sheets.speech_markup_helper import SpeechMarkupHelper
from graphing.sheets.text_animator import TextAnimator

class BaseGraphSheet2D(CommonGraphSheet):
    def __init__(self, scene, axes, **kwargs):
        super().__init__(scene=scene, **kwargs) 
        self.scene = scene
        self.axes = axes
        self.covering_rectangles = []
        self.geo_property_calculator = GeoPropertyCalculator()
        self.speech_markup_helper = SpeechMarkupHelper()
        self.text_animator = TextAnimator(scene, self)
        self.arrow_animator = ArrowAnimator(self, scene)
        self.alpha_animator = AlphaAnimator(scene)
        self.add(axes)
        if isinstance(axes, NumberLine):
            self.geo_mapper = NumberLineGeoMapper(axes)
        else:
            self.geo_mapper = GeoMapper(axes)
        self.add_default_models()
        
    def add_covering_rectangle(self, covering_rectangle):
        self.covering_rectangles.append(covering_rectangle)
        
    def _line_from_input(self, line_or_tuple):
        if isinstance(line_or_tuple, (ModelLine, ModelLine2Points)):
            return line_or_tuple
        if isinstance(line_or_tuple, tuple):
            a = ModelPoint.from_x_y(line_or_tuple[0], line_or_tuple[1])
            b = ModelPoint.from_x_y(line_or_tuple[2], line_or_tuple[3])
            return ModelLine(a.x,a.y, b.x, b.y)
        raise ValueError(f"Invalid line input: {line_or_tuple}")
        
    def _translate_vector_from_input(self, vector_model_or_tuple    ):   
        if isinstance(vector_model_or_tuple, ModelVector):
            return vector_model_or_tuple
        if isinstance(vector_model_or_tuple, np.ndarray):
            if len(vector_model_or_tuple) == 2:
                a = ModelPoint.from_x_y(vector_model_or_tuple[0], vector_model_or_tuple[1], 0)
                return ModelVector.position_vector(a)
            elif len(vector_model_or_tuple) == 3:
                a = ModelPoint(vector_model_or_tuple[0], vector_model_or_tuple[1], vector_model_or_tuple[2])
                return ModelVector.position_vector(a)
            else:
                raise ValueError("Vector tuple must have 2 or 3 components")    
        if isinstance(vector_model_or_tuple, tuple):
            if len(vector_model_or_tuple) == 3:
                a = ModelPoint(vector_model_or_tuple[0], vector_model_or_tuple[1], vector_model_or_tuple[2])
                return ModelVector.position_vector(a)
            elif len(vector_model_or_tuple) == 2:
                a = ModelPoint(vector_model_or_tuple[0], vector_model_or_tuple[1], 0) 
                return ModelVector.position_vector(a)
            else:
                raise ValueError("Vector tuple must have 2 or 3 components")
        raise ValueError(f"Invalid vector input: {vector_model_or_tuple}")
 
            
    def _add_line(self, model_line, style_props:UIStyleProps = UIStyleProps.line_theme(), no_animate=True, voiceover_text=None):
        ui_line = UILine(self.geo_mapper, model_line, style_props=style_props) 
        self._register_object(model_line, ui_line, no_animate, voiceover_text)
       
    def _add_circle(self, model_circle:ModelCircle, style_props:UIStyleProps=UIStyleProps.circle_theme(), 
                    no_animate=True, voiceover_text=None):
        ui_circle = UICircle(self.geo_mapper, model_circle, style_props=style_props)
        self._register_object(model_circle, ui_circle, no_animate, voiceover_text) 
        
    def _add_vector(self, model_vector:ModelVector, 
                    style_props:UIStyleProps=UIStyleProps.vector_theme(), 
                    vector_name=None,  
                    label_direction=UP, 
                    label_reverse_orientation=False, 
                    label_shift=ORIGIN,
                    no_animate=True, 
                    voiceover_text=None):
        
        if vector_name is not None: 
            ui_vector = UIVector(self.geo_mapper, model_vector,     
                                 style_props=style_props,
                             vector_name=vector_name, 
                             label_direction=label_direction,
                             label_reverse_orientation=label_reverse_orientation, 
                             label_shift=label_shift)
        else:
            ui_vector = UIComplex(self.geo_mapper, model_vector, style_props=style_props)   
            
        self._register_object(model_vector, ui_vector, no_animate, voiceover_text)
        
    def _angle(self, point_from:ModelPoint, vertex:ModelPoint,
               to_point:ModelPoint, clock_wise=False, 
               style_props:UIStyleProps=UIStyleProps.angle_theme(),   
               radius=0.8,
               directional_arrow=False,
               no_animate=False, voiceover_text=None):
        model_angle = ModelAngle.from_three_points(point_from, vertex, to_point, clock_wise)
        ui_angle = None
        if directional_arrow is False:
            ui_angle = UISectorAngle(self.geo_mapper, model_angle, radius=radius,
                           style_props=style_props)
        else:
            ui_angle = UIArrowAngle(self.geo_mapper, model_angle, radius=radius,
                           style_props=style_props)
       
        if directional_arrow is False:
            self._register_in_background(model_angle, ui_angle, no_animate, voiceover_text)
        else:
            self._register_object(model_angle, ui_angle, no_animate, voiceover_text)
        return model_angle    
    
    
    
    
    def _projection_on_line(self, point:ModelPoint, 
                           line:ModelLine, 
                           style_props:UIStyleProps=UIStyleProps.point_theme(), 
                           no_animate=False, voiceover_text=None) -> ModelPoint:
        projected_model_point = ModelLine.projection_on_line(point_to_project=point, line_to_project_onto=line)
        projected_ui_point = UIPoint(self.geo_mapper, projected_model_point, style_props=style_props)   
        self._register_object(projected_model_point, projected_ui_point, no_animate, voiceover_text)
        return projected_model_point   
    
    def _create_polygon(self, model_polygon, color, fill_color,
                       fill_opacity, no_animate, voiceover_text=None):
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.triangle_theme())
        ui_polygon = UIPolygon(self.geo_mapper, model_polygon, style_props=style_props)
        self._register_object(model_polygon, ui_polygon, no_animate, voiceover_text)
        return model_polygon        
    
    def direct_hide(self, *model_objects):
        for model_object in model_objects:
            ui_obj = self.model_to_ui[model_object]
            ui_obj.view().set_opacity(0) 
        
    
             
    """
    Removes all objects created through graphsheet methods and text animators
    """
    def _clear_all(self, fade_out_time=0.2):
        views_of_models = [model_object.view() for model_object in self.model_to_ui.keys()]
    
        if len(views_of_models) > 0:
            self.scene.play(FadeOut(*views_of_models, run_time=fade_out_time))
            self.scene.remove(*views_of_models)
            
            # remove the views from the ui_to_model and model_to_ui 
        for view in views_of_models:
            if view in self.ui_to_model:
                del self.ui_to_model[view]
            if view in self.model_to_ui:
                del self.model_to_ui[view]
                     
            
        self.text_animator.clear_implicitly_created_objects()       
        for covering_rectangle in self.covering_rectangles:
            self.scene.remove(covering_rectangle)
            
              
        
  
        