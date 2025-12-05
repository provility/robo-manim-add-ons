
import uuid
from manim import *
import numpy as np
import sympy


from graphing.geo.effect_command import ComposeEffectCommand, EffectCommandManager, ZoomEffectCommand
from graphing.geo.effect_command import EffectCommand
from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.model.base_model import BaseModel
from graphing.geo.model.model_aligned_text import ModelAlignedText
from graphing.geo.model.model_angle import ModelAngle
from graphing.geo.model.model_arc import ModelArc
from graphing.geo.model.model_area import ModelArea
from graphing.geo.model.model_area_between_curves import ModelAreaBetweenCurves
from graphing.geo.model.model_axis_lines import ModelAxisLine
from graphing.geo.model.model_bulleted_list import ModelBulletedList
from graphing.geo.model.model_circle import ModelCircle
from graphing.geo.model.model_distance import ModelDistance
from graphing.geo.model.model_dynamic_property import ModelDynamicProperty
from graphing.geo.model.model_ellipse import  ModelEllipseParametric
from graphing.geo.model.model_group import ModelGroup
from graphing.geo.model.model_hyperbola import ModelHyperbola
from graphing.geo.model.model_image import ModelImage
from graphing.geo.model.model_intersection import ModelIntersection, ModelIntersectionRegion, ModelLineToLineIntersection, ModelLineToCircleIntersection, ModelCircleToCircleIntersection, ModelLineToPolygonIntersection, ModelPolygonToPolygonIntersection
from graphing.geo.model.model_label_with_arrows import ModelLabelWithArrows
from graphing.geo.model.model_line import ModelLine, ModelLine2Points
from graphing.geo.model.model_matrix import ModelMatrix
from graphing.geo.model.model_parabola import  ModelParabolaParametric
from graphing.geo.model.model_parameter import  ModelChainedParameter, ModelParameter, ModelLambdaParameter, ModelPointParameter
from graphing.geo.model.model_part import ModelPart
from graphing.geo.model.model_plot import ModelExplicitPlot, ModelParametricPlot, ModelPlot
from graphing.geo.model.model_point import ModelPoint
from graphing.geo.model.model_poly_line_arrow import ModelPolyLineArrow
from graphing.geo.model.model_polygon import ModelPolygon
from graphing.geo.model.model_polyline import ModelPolyLine
from graphing.geo.model.model_reimann import ModelRiemann
from graphing.geo.model.model_slope import ModelTangentSlope
from graphing.geo.model.model_tangent import  ModelTanget
from graphing.geo.model.model_table import ModelTable
from graphing.geo.model.model_text import BaseModelText, MathModelText, ModelMixedText, ModelPartialMathText, ModelPlainText
from graphing.geo.model.model_trace import ModelPlotTrace, ModelPointTrace, ModelShapeTrace
from graphing.geo.model.model_triangle import ModelTriangle
from graphing.geo.model.model_vector import ModelVector
from graphing.geo.parameter_lambda_updater import ParameterLambdaUpdater
from graphing.geo.ui.ui_aligned_text import UIAlignedText
from graphing.geo.ui.ui_angle import UIAngle, UIArrowAngle, UISectorAngle
from graphing.geo.ui.ui_arc import UIArc
from graphing.geo.ui.ui_area import UIArea
from graphing.geo.ui.ui_area_between_curves import UIAreaBetweenCurves
from graphing.geo.ui.ui_arrow import UIArrow
from graphing.geo.ui.ui_axis_line import UIAxisLines
from graphing.geo.ui.ui_bulleted_list import UIBulletedList
from graphing.geo.ui.ui_circle import UICircle
from graphing.geo.ui.ui_coordinate import UICoordinate
from graphing.geo.ui.ui_distance import UIDistance
from graphing.geo.ui.ui_dynamic_property import  UIDynamicSimple, UIDynamicVariableProperty
from graphing.geo.ui.ui_ellipse import  UIEllipseByParametricFunction
from graphing.geo.ui.ui_explicit_plot import UIExplicitPlot
from graphing.geo.ui.ui_group import UIGroup
from graphing.geo.ui.ui_hyperbola import UIHyperbola
from graphing.geo.ui.ui_image import UIImage
from graphing.geo.ui.ui_implicit_plot import UIImplicitPlot
from graphing.geo.ui.ui_intersection import UIIntersection
from graphing.geo.ui.ui_intersection_region import UIIntersectionRegion
from graphing.geo.ui.ui_label_with_arrows import UILabelWithArrows
from graphing.geo.ui.ui_line import UILine
from graphing.geo.ui.ui_matrix import UIMatrix
from graphing.geo.ui.ui_parabola import  UIParabolaByParametricFunction
from graphing.geo.ui.ui_parameter import UIParameter
from graphing.geo.ui.ui_parametric_plot import UIParametricPlot
from graphing.geo.ui.ui_part import UIPart
from graphing.geo.ui.ui_point import UIPoint


from graphing.geo.ui.ui_polygon import UIPolygon

from graphing.geo.ui.ui_polyline import UIPolyLine
from graphing.geo.ui.ui_polyline_arrow import UIPolyLineArrow
from graphing.geo.ui.ui_reimann import UIReimann
from graphing.geo.ui.ui_tangent import  UITangent
from graphing.geo.ui.ui_style_props import *
from graphing.geo.ui.ui_table import UITable
from graphing.geo.ui.ui_tangent_slope import UITangentSlope
from graphing.geo.ui.ui_text import UIMathTex, UIMixedText, UIPartialMathTex, UIPlainText, UIText
from graphing.geo.ui.ui_trace import UITrace
from graphing.geo.ui.ui_triangle import UITriangle
from graphing.geo.ui.ui_vector import UIComplex, UIVector
from graphing.helpers.formula_parts_item_factory import FormulaPartsFactory
from graphing.helpers.latex_generator import LatexGenerator
from graphing.math.function_expression_utils import FunctionUtils
from graphing.sheets.base_graphsheet2d import BaseGraphSheet2D
from graphing.sheets.point_positioner import PointPositioner
from graphing.sheets.model_annotater import ModelAnnotater
from graphing.sheets.text_position_render_helper import TextPositionRenderHelper


class GraphSheet2D(BaseGraphSheet2D):
    def __init__(self, scene, axes, hide_axes=False, **kwargs):
        super().__init__(scene, axes, **kwargs)
        self.effect_command_manager = EffectCommandManager(scene)
        self._point_positioner = PointPositioner(scene, self)
        self._model_annotater = ModelAnnotater(self)
        self._formula_parts_factory = FormulaPartsFactory()
        self._latex_generator = LatexGenerator()
        self.X_POSITIVE_LINE = ModelLine2Points(ModelPoint(0,0), ModelPoint(1,0))
        self.Y_POSITIVE_LINE = ModelLine2Points(ModelPoint(0,0), ModelPoint(0,1))
        self.X_NEGATIVE_LINE = ModelLine2Points(ModelPoint(0,0), ModelPoint(-1,0))
        self.Y_NEGATIVE_LINE = ModelLine2Points(ModelPoint(0,0), ModelPoint(0,-1))
        self.REVERSED_X_POSITIVE_LINE = ModelLine2Points(ModelPoint(1,0), ModelPoint(0,0))
        self.REVERSED_Y_POSITIVE_LINE = ModelLine2Points(ModelPoint(0,1), ModelPoint(0,0))
        self.REVERSED_X_NEGATIVE_LINE = ModelLine2Points(ModelPoint(-1,0), ModelPoint(0,0))
        self.REVERSED_Y_NEGATIVE_LINE = ModelLine2Points(ModelPoint(0,-1), ModelPoint(0,0))
        self.MODEL_ORIGIN = ModelPoint(0,0)
        if hide_axes:
            self.hide_axes()    
            

    def hide_axes(self):
        self.axes.set_opacity(0)    
        
    def show_axes(self):
        self.axes.set_opacity(1)    
        
    def clear_all(self, fade_out_time=0.2):
        self._clear_all(fade_out_time)
        
    def hide(self, *model_objects):
        self.direct_hide(*model_objects)
        
    def show(self, *model_objects):
        for model_object in model_objects:
            ui_obj = self.model_to_ui[model_object]
            ui_obj.view().set_opacity(1)    

    def to_ui(self, model_point_or_tuple):
        model_point = self._point_from_input(model_point_or_tuple)
        return self.geo_mapper.model_to_ui(model_point)
    

    
    @property    
    def point_positioner(self) -> PointPositioner:
        return self._point_positioner
    
    def model_annotater(self) -> ModelAnnotater:
        return self._model_annotater
    
    @property
    def latex_generator(self) -> LatexGenerator :
        return self._latex_generator
    
    
    @property
    def formula_parts_factory(self) -> FormulaPartsFactory:
        return self._formula_parts_factory

    
    def reset_zoom(self, run_time=2):
        self.play(Restore(self.scene.camera.frame), run_time=run_time)
        
        
    def voiceover(self, text):
        with self.scene.voiceover(text=text) as tracker:
             pass

    def point(self, model_point_or_tuple,  color=RED,
              no_animate=False, fill_color=None, fill_opacity=0.8, voiceover_text=None)->ModelPoint:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        model_point = self._point_from_input(model_point_or_tuple)
        ui_point = UIPoint(self.geo_mapper, model_point, style_props=style_props)
        self._register_object(model_point, ui_point, no_animate, voiceover_text)
        return model_point
    
    def point_from_polar(self, radius_value_or_parameter, theta_value_or_parameter, color=RED,
                         no_animate =False, fill_color=None, fill_opacity=0.8, voiceover_text=None)->ModelPoint:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        radius_parameter = self._parameter_from_input(radius_value_or_parameter)
        theta_parameter = self._parameter_from_input(theta_value_or_parameter)  
        model_point = ModelPoint.from_polar(radius_parameter, theta_parameter)
        ui_point = UIPoint(self.geo_mapper, model_point, style_props=style_props)
        self._register_object(model_point, ui_point, no_animate, voiceover_text)
        return model_point
    
    def coordinate(self, model_point_or_tuple,  direction=UP,    color=RED,
                   fill_color=None, fill_opacity=0.8, no_animate=False, voiceover_text=None)->ModelPoint:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        model_point = self._point_from_input(model_point_or_tuple)
        ui_coordinate = UICoordinate(self.geo_mapper, model_point, direction=direction, style_props=style_props)
        self._register_object(model_point, ui_coordinate, no_animate, voiceover_text)
        return model_point  
    
    """
    This can be useful to create a point on a graph from a parameter. 
    The actual coordinates of the point are given by the x_lambda_function and y_lambda_function. 
    """
    def point_by_function(self, parameter_model, 
                          x_lambda_function, y_lambda_function, 
                          color=RED, 
                           no_animate =False, fill_color=None, fill_opacity=0.8, voiceover_text=None)->ModelPoint:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        model_point = ModelPoint.from_function(parameter_model, x_lambda_function, y_lambda_function)
        ui_point = UIPoint(self.geo_mapper, model_point, style_props=style_props)
        self._register_object(model_point, ui_point, no_animate, voiceover_text)
        return model_point
    
    """
    The angle_in_degrees_parameter_or_value ranges from 0 to 360
    """
    def point_on_circle(self, model_circle, angle_in_degrees_parameter_or_value,  color=RED, 
                        no_animate =False, fill_color=None, fill_opacity=0.8, voiceover_text=None)->ModelPoint:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        angle_in_degrees_parameter = self._parameter_from_input(angle_in_degrees_parameter_or_value)
        model_point = ModelCircle.point_on_circle(model_circle, angle_in_degrees_parameter)
        ui_point = UIPoint(self.geo_mapper, model_point, style_props=style_props)
        self._register_object(model_point, ui_point, no_animate, voiceover_text)
        return model_point
    
    """
    The angle_in_degrees_parameter_or_value ranges from 0 to 360
    """
    def point_on_ellipse(self, model_ellipse, angle_in_degrees_parameter_or_value,  color=RED, 
                        no_animate =False, fill_color=None, fill_opacity=0.8, voiceover_text=None)->ModelPoint:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        angle_in_degrees_parameter = self._parameter_from_input(angle_in_degrees_parameter_or_value)
        model_point = ModelEllipseParametric.point_on_ellipse(model_ellipse, angle_in_degrees_parameter)
        ui_point = UIPoint(self.geo_mapper, model_point, style_props=style_props)
        self._register_object( model_point, ui_point, no_animate, voiceover_text)
        return model_point
    
    """
    The parameter ranges from 0 to 1
    """
    def point_on_line(self, model_line, parameter_or_value, color=RED, 
                      no_animate =False, fill_color=None, fill_opacity=0.8, voiceover_text=None)->ModelPoint:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        parameter = self._parameter_from_input(parameter_or_value)
        model_point = ModelLine.point_on_line(model_line, parameter)
        ui_point = UIPoint(self.geo_mapper, model_point, style_props=style_props)
        self._register_object(model_point, ui_point, no_animate, voiceover_text)
        return model_point
    
    def point_projection_on_line(self, point_to_project, line_to_project_onto, color=RED, 
                        no_animate =False, fill_color=None, fill_opacity=0.8, voiceover_text=None)->ModelPoint:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        point_to_project = self._point_from_input(point_to_project)
        line_to_project_onto = self._line_from_input(line_to_project_onto)
        model_point = ModelLine.projection_on_line(point_to_project, line_to_project_onto)    
        ui_point = UIPoint(self.geo_mapper, model_point, style_props=style_props)
        self._register_object(model_point, ui_point, no_animate, voiceover_text)
        return model_point  
    
    def line_projection_on_line(self, point_to_project, line_to_project_onto, color=DARK_BLUE, 
                        no_animate =False, 
                        dashed=True,
                        stroke_width=DEFAULT_STROKE_WIDTH,
                        fill_color=None, fill_opacity=0.8, voiceover_text=None)->ModelLine:
        style_props = self._create_style_props(color, fill_color, fill_opacity,
                                               UIStyleProps.line_theme(),
                                               dashed=dashed, stroke_width=stroke_width)
        point_to_project = self._point_from_input(point_to_project)
        line_to_project_onto = self._line_from_input(line_to_project_onto)
        model_line = ModelLine.projection_line_on_line(point_to_project, line_to_project_onto)  
        ui_line = UILine(self.geo_mapper, model_line, style_props=style_props)
        self._register_object(model_line, ui_line, no_animate, voiceover_text)
        return model_line   
    
    """
    The parameter range is any domain of the function
    """
    def point_on_plot(self, model_plot, parameter_or_value, color=RED, 
                      no_animate =False, fill_color=None, fill_opacity=0.8, voiceover_text=None)->ModelPoint:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        parameter = self._parameter_from_input(parameter_or_value)
        model_point = ModelExplicitPlot.point_on_plot(model_plot, parameter)
        ui_point = UIPoint(self.geo_mapper, model_point, style_props=style_props)
        self._register_object(model_point, ui_point, no_animate, voiceover_text)
        return model_point
    
    """
    The parameter range is any domain of the function
    """
    def point_on_parametric_plot(self, model_plot, parameter_or_value, color=RED, 
                      no_animate =False, fill_color=None, fill_opacity=0.8, voiceover_text=None)->ModelPoint:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        parameter = self._parameter_from_input(parameter_or_value)
        model_point = ModelParametricPlot.point_on_plot(model_plot, parameter)
        ui_point = UIPoint(self.geo_mapper, model_point, style_props=style_props)
        self._register_object(model_point, ui_point, no_animate, voiceover_text)
        return model_point  
    
    """
    The property_name is a property of the reference_model
    Example: focus of a parabola, center of a circle, vertex of a parabola etc.
    """
    def point_by_property(self, reference_model, property_name, 
                              color=RED, 
                          no_animate =False, fill_color=None, fill_opacity=0.8, voiceover_text=None)->ModelPoint:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        model_point = ModelPoint.from_property(reference_model, property_name)
        ui_point = UIPoint(self.geo_mapper, model_point, style_props=style_props)
        self._register_object(model_point, ui_point, no_animate, voiceover_text)
        return model_point
    
    """
    The property_name is a property of the reference_model that returns a line
    Example: directrix of an ellipse, axis of a parabola etc.
    """
    def line_by_property(self, reference_model, property_name, 
                              color=CURRENT_COLOR_THEME.line_color  (), 
                          no_animate =False, fill_color=None, fill_opacity=0.8, 
                          stroke_width=DEFAULT_STROKE_WIDTH, voiceover_text=None)->ModelLine:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.line_theme(), stroke_width=stroke_width)
        model_line = self._from_property(reference_model, property_name)
        ui_line = UILine(self.geo_mapper, model_line, style_props=style_props)
        self._register_object(model_line, ui_line, no_animate, voiceover_text)
        return model_line
    
    """
    angle_name is either angle_a, angle_b or angle_c
    """
    def angle_by_property(self, reference_model, angle_name, 
                          color=CURRENT_COLOR_THEME.angle_color(), 
                          directional_arrow=False,
                          radius=0.8,
                          no_animate =False, fill_color=None, fill_opacity=0.8, 
                          voiceover_text=None)->ModelAngle:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.angle_theme())
        model_angle = self._from_property(reference_model, angle_name)   
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
        
        
    """
    The direction is one of the four compass directions: UP, DOWN, LEFT, RIGHT or the combinations of these values
    """
    def point_next_to_model(self, reference_model, direction,  color=RED, 
                            no_animate =False, fill_color=None, fill_opacity=0.8, voiceover_text=None)->ModelPoint:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        model_point = ModelPoint.next_to_model(reference_model, direction=direction)
        ui_point = UIPoint(self.geo_mapper, model_point, style_props=style_props)
        self._register_object(model_point, ui_point, no_animate, voiceover_text)
        return model_point
    
    def point_from_equation(self, equation, x_value, 
                            color=RED,
                            fill_color=None, fill_opacity=1)->List[ModelPoint]:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        y_values = FunctionUtils.find_y_given_x(equation, x_value=x_value)
        model_points = []
        for index, y_value in enumerate(y_values):
            model_points.append(self.point((x_value, y_value), color=color, fill_color=fill_color, fill_opacity=fill_opacity))
        return model_points

    def new_translated_point(self, model_point_or_tuple, model_vector, color=RED, 
                             no_animate =False, fill_color=None, fill_opacity=0.8, voiceover_text=None)->ModelPoint:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        model_point = self._point_from_input(model_point_or_tuple)
        model_vector = self._translate_vector_from_input(model_vector)
        model_point = ModelPoint.synch_translate(model_point, model_vector)
        ui_point = UIPoint(self.geo_mapper, model_point, style_props=style_props)
        self._register_object(model_point, ui_point, no_animate, voiceover_text)
        return model_point
    
    def new_scaled_point(self, model_point_or_tuple, scale_parameter,  color=RED, 
                         no_animate =False, fill_color=None, fill_opacity=0.8)->ModelPoint:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        model_point = self._point_from_input(model_point_or_tuple)
        scale_factor_parameter = self._parameter_from_input(scale_parameter)
        scaled_point = model_point.scale(scale_factor_parameter)
        ui_point = UIPoint(self.geo_mapper, scaled_point, style_props=style_props)
        self._register_object(scaled_point, ui_point, no_animate)
        return scaled_point  
    
    def translate_by_vector(self, model_point, model_vector_or_tuple, run_time=2,  voiceover_text=None)->ModelPoint:
        model_vector = self._translate_vector_from_input(model_vector_or_tuple)
        self.alpha_animator.translate_point(model_point, model_vector, 
                                            run_time=run_time, 
                                            rate_func=linear,
                                            voiceover_text=voiceover_text)
       
    def translate_to(self, model_point, target_point_or_tuple, run_time=2, voiceover_text=None)->ModelPoint:  
        target_point = self._point_from_input(target_point_or_tuple)    
        model_vector = ModelVector.as_translation_vector(model_point, target_point)   
        self.alpha_animator.translate_point(model_point, model_vector, 
                                            run_time=run_time, 
                                            rate_func=linear,
                                            voiceover_text=voiceover_text)
        
    def rotate_point_by_angle(self, model_point_or_tuple, angle_in_degrees_parameter, about_point_or_tuple=ORIGIN, 
                              run_time=2, voiceover_text=None)->ModelPoint:
        model_point = self._point_from_input(model_point_or_tuple)
        angle_parameter = self._parameter_from_input(angle_in_degrees_parameter)
        about_point = self._point_from_input(about_point_or_tuple)  
        self.alpha_animator.rotate_point(model_point, angle_parameter, 
                                         about_point, 
                                         run_time=run_time, 
                                         rate_func=linear,
                                         voiceover_text=voiceover_text)
        
    def rotate_point_to(self, model_point, target_point_or_tuple,  about_point_or_tuple=ORIGIN, 
                        run_time=2, voiceover_text=None)->ModelPoint:
        target_point = self._point_from_input(target_point_or_tuple)
        about_point = self._point_from_input(about_point_or_tuple)
        self.alpha_animator.rotate_to(model_point, target_point, about_point, 
                                      run_time=run_time, 
                                      rate_func=linear,
                                      voiceover_text=voiceover_text)

    def reflect_point_over_line(self, model_point_or_tuple, line_or_tuple, color=RED, fill_color=None, fill_opacity=0.8)->ModelPoint:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        model_point = self._point_from_input(model_point_or_tuple)
        line = self._line_from_input(line_or_tuple)
        model_point = ModelLine.reflect_over_line(line, model_point)
        ui_point = UIPoint(self.geo_mapper, model_point, style_props=style_props)
        self._register_object(model_point, ui_point)
        return model_point
    
    """
    angle_value_or_parameter is an angle in degrees
    """
    def rotate_model(self, model, angle_value_or_parameter, about_point_or_tuple=ORIGIN, 
                     run_time=2, rate_func=linear, voiceover_text=None)->BaseModel:
        angle_parameter = self._parameter_from_input(angle_value_or_parameter)
        about_point = self._point_from_input(about_point_or_tuple)
        self.alpha_animator.rotate_model(model, angle_parameter, about_point, run_time, rate_func, voiceover_text)
        
    def translate_model(self, model, vector_or_tuple, run_time=2, rate_func=linear, voiceover_text=None)->BaseModel:
        vector = self._translate_vector_from_input(vector_or_tuple)
        self.alpha_animator.translate_model(model, vector, run_time, rate_func, voiceover_text) 
        
    def scale_model(self, model, scale_value_or_parameter, run_time=2, rate_func=linear, voiceover_text=None)->BaseModel:
        scale_factor_parameter = self._parameter_from_input(scale_value_or_parameter)
        self.alpha_animator.scale_model(model, scale_factor_parameter, run_time, rate_func, voiceover_text) 


    def line(self, model_point_or_tuple_a, model_point_or_tuple_b,  color=DARK_BLUE,
             dashed=False, no_animate=False,
             stroke_width=DEFAULT_STROKE_WIDTH, voiceover_text=None)->ModelLine:
        style_props = self._create_style_props(color, fill_color=None, fill_opacity=None, default_style=UIStyleProps.line_theme(), dashed=dashed, stroke_width=stroke_width)
        a = self._point_from_input(model_point_or_tuple_a)
        b = self._point_from_input(model_point_or_tuple_b)
        model_line = ModelLine.from_points(a, b)
        self._add_line(model_line=model_line,  style_props=style_props, no_animate=no_animate, voiceover_text=voiceover_text)
        return model_line
    
    def new_rotated_point_about_point(self, model_point_or_tuple, angle_value_or_parameter, about_point_or_tuple,  color=RED,
                                      no_animate =False, fill_color=None, fill_opacity=0.8)->ModelPoint:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        model_point = self._point_from_input(model_point_or_tuple)
        angle = self._parameter_from_input(angle_value_or_parameter)
        about_point = self._point_from_input(about_point_or_tuple)
        model_point = ModelPoint.rotate_about_point(model_point, angle, about_point)
        ui_point = UIPoint(self.geo_mapper, model_point, style_props=style_props)
        self._register_object(model_point, ui_point, no_animate)
        return model_point

    def project_on_x_axis(self, point_or_tuple,  color=RED, 
                          no_animate =False,  fill_color=None, fill_opacity=0.8, voiceover_text=None)->ModelPoint:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        return self._projection_on_line(point_or_tuple, self.x_axis_model_line, style_props, no_animate, voiceover_text)

    def project_on_y_axis(self, point_or_tuple, color=RED, 
                          no_animate =False, fill_color=None, fill_opacity=0.8, voiceover_text=None):
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        return self._projection_on_line(point_or_tuple, self.y_axis_model_line, style_props, no_animate, voiceover_text)

    """
    vector_name is a string that is the name of the vector
    """
    def vector(self, model_point_or_tuple_a, model_point_or_tuple_b,
               vector_name=None,
               color=CURRENT_COLOR_THEME.vector_color(),
               label_direction=UP, label_reverse_orientation=False,
               label_shift=ORIGIN,
               dashed=False,    
               no_animate=False, fill_color=None, 
               fill_opacity=0.8, voiceover_text=None)->ModelVector:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.vector_theme(), dashed=dashed)
        a = self._point_from_input(model_point_or_tuple_a)
        b = self._point_from_input(model_point_or_tuple_b)
        model_vector = ModelVector.from_end_points(a, b)
        self._add_vector(model_vector, style_props, 
                         vector_name = vector_name, 
                         label_direction = label_direction, 
                         label_reverse_orientation = label_reverse_orientation, 
                         label_shift = label_shift, 
                         no_animate = no_animate, 
                         voiceover_text = voiceover_text)
        return model_vector

    def sum_vectors(self, vector_a, vector_b, vector_name=None,
               color=CURRENT_COLOR_THEME.vector_color(),
               label_direction=UP, label_reverse_orientation=False,
               label_shift=ORIGIN,
               dashed=False,
               no_animate=False, fill_color=None, 
               fill_opacity=0.8, voiceover_text=None)->ModelVector:
        style_props = self._create_style_props(color, fill_color, fill_opacity,
                                               UIStyleProps.vector_theme(), dashed=dashed)
        sum_vector = ModelVector.add_vector(vector_a, vector_b)
        self._add_vector(sum_vector, style_props, 
                         vector_name = vector_name, 
                         label_direction = label_direction, 
                         label_reverse_orientation = label_reverse_orientation, 
                         label_shift = label_shift, 
                         no_animate = no_animate, 
                         voiceover_text = voiceover_text)
        return sum_vector
    
    def difference_vectors(self, vector_a, vector_b, vector_name=None,   
               color=CURRENT_COLOR_THEME.vector_color(),
               label_direction=UP, label_reverse_orientation=False,
               label_shift=ORIGIN,
               dashed=False,
            no_animate=False, fill_color=None, 
               fill_opacity=0.8, voiceover_text=None):
        style_props = self._create_style_props(color, fill_color, 
                                               fill_opacity, 
                                               UIStyleProps.vector_theme(), 
                                               dashed=dashed)
        difference_vector = ModelVector.subtract_vector(vector_a, vector_b)
        self._add_vector(difference_vector, style_props, 
                         vector_name = vector_name, label_direction = label_direction, 
                         label_reverse_orientation = label_reverse_orientation, 
                         label_shift = label_shift,  no_animate = no_animate, 
                         voiceover_text = voiceover_text)
        return difference_vector
    
    def parallel_vector(self, from_vector, parallel_to_vector, 
                        vector_name=None,
                        color=CURRENT_COLOR_THEME.vector_color(),
                        label_direction=UP, label_reverse_orientation=False,
                        label_shift=ORIGIN,
                        dashed=True,
                        no_animate=False, fill_color=None, fill_opacity=0.8, voiceover_text=None)->ModelVector:  
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.vector_theme(), dashed=dashed)
        parallel_vector = ModelVector.parallelled_vector(from_vector, parallel_to_vector)
        self._add_vector(parallel_vector, style_props,
                         vector_name = vector_name,
                         label_direction = label_direction, 
                         label_reverse_orientation = label_reverse_orientation, 
                         label_shift = label_shift,     
                         no_animate = no_animate, voiceover_text = voiceover_text)
        return parallel_vector
    
    def reverse_vector(self, vector, vector_name=None, 
                       color=CURRENT_COLOR_THEME.vector_color(),
                       label_direction=UP, label_reverse_orientation=False,
                       label_shift=ORIGIN,
                       dashed=True, 
                       no_animate=False, 
                       fill_color=None, fill_opacity=0.8, voiceover_text=None)->ModelVector:  
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.vector_theme())
        reversed_vector = ModelVector.reversed_vector(vector)
        self._add_vector(reversed_vector, style_props, vector_name = vector_name, no_animate = no_animate, voiceover_text = voiceover_text)
        return reversed_vector
    
    def scale_vector(self, model_vector, scale_factor_parameter, vector_name=None,
                     color=CURRENT_COLOR_THEME.vector_color(),
                     label_direction=UP, label_reverse_orientation=False,   
                     label_shift=ORIGIN,
                     dashed=True,
                     no_animate=False, 
                     fill_color=None, fill_opacity=0.8, voiceover_text=None):
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.vector_theme(), dashed=dashed)
        scaled_vector = ModelVector.scaled_vector(model_vector, scale_factor_parameter)
        self._add_vector(scaled_vector, style_props, vector_name = vector_name, no_animate = no_animate, voiceover_text = voiceover_text)
        return scaled_vector

    
    def perpendicular_vector(self, start_vector, source_vector, vector_name=None, 
                             color=CURRENT_COLOR_THEME.vector_color(),
                             label_direction=UP, label_reverse_orientation=False,
                             label_shift=ORIGIN,
                             dashed=True,
                             no_animate=False,  
                             fill_color=None, fill_opacity=0.8, voiceover_text=None)->ModelVector:  
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.vector_theme())
        perpendicular_vector = ModelVector.perped_vector(start_vector, source_vector)
        self._add_vector(perpendicular_vector, style_props, vector_name = vector_name, no_animate = no_animate, voiceover_text = voiceover_text)
        return perpendicular_vector
    
    def position_vector(self, model_point_or_tuple, 
                        vector_name=None,
                        color=PINK,
                        dashed=False,
                        fill_color=None, fill_opacity=1, 
                        no_animate=False,   voiceover_text=None)->ModelVector:  
        style_props = self._create_style_props(color, fill_color, fill_opacity, 
                                               UIStyleProps.vector_theme(), 
                                               dashed=dashed)
        a = self._point_from_input(model_point_or_tuple)
        model_vector = ModelVector.position_vector(a)
        ui_object = None
        if vector_name is not None:
            ui_object = UIVector(self.geo_mapper, model_vector,
                             vector_name=vector_name,
                             style_props=style_props)
        else:    
            ui_object = UIComplex(self.geo_mapper, model_vector,
                             style_props=style_props)
        self._register_object(model_vector, ui_object, no_animate, voiceover_text)
        return model_vector
    
    def arrow(self, model_point_or_tuple_a, model_point_or_tuple_b,
              curved=False, angle: float = TAU / 4,
        radius: float = None, color=CURRENT_COLOR_THEME.vector_color(), 
        fill_color=None, fill_opacity=1, no_animate=False, voiceover_text=None)->ModelLine:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.vector_theme())
        a = self._point_from_input(model_point_or_tuple_a)
        b = self._point_from_input(model_point_or_tuple_b)
        model_arrow = ModelVector.from_points(a, b)
        ui_arrow = UIArrow(self.geo_mapper, model_arrow, curved=curved, angle=angle, radius=radius, 
                           style_props=style_props)
        self._register_arrow(model_arrow, ui_arrow, no_animate, voiceover_text)
        return model_arrow
    
    def polyline_arrow(self, points, color=CURRENT_COLOR_THEME.vector_color(), 
                       fill_color=None, fill_opacity=1,
                       stroke_width=DEFAULT_STROKE_WIDTH, no_animate=False, voiceover_text=None)->ModelPolyLineArrow:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.vector_theme(), stroke_width=stroke_width)
        model_polyline_arrow = ModelPolyLineArrow.from_points(points)
        ui_polyline_arrow = UIPolyLineArrow(self.geo_mapper, model_polyline_arrow, style_props=style_props)
        self._register_object(model_polyline_arrow, ui_polyline_arrow, no_animate, voiceover_text)
        return model_polyline_arrow
    
    def polyline(self, points, color=CURRENT_COLOR_THEME.vector_color(), 
                    fill_color=None, fill_opacity=1, no_animate=False, stroke_width=DEFAULT_STROKE_WIDTH,
                    voiceover_text=None)->ModelPolyLine:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.vector_theme(), stroke_width=stroke_width)
        model_polyline = ModelPolyLine.from_points(points)
        ui_polyline = UIPolyLine(self.geo_mapper, model_polyline, style_props=style_props)
        self._register_object(model_polyline, ui_polyline, no_animate, voiceover_text)
        return model_polyline

  

    def circle_by_center_and_radius(self, model_point_or_tuple_center, radius_or_parameter, 
                                    color=DARK_BROWN, fill_color=None, fill_opacity=0.2,
                                    no_animate=False, 
                                    stroke_width=DEFAULT_STROKE_WIDTH, voiceover_text=None)->ModelCircle:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.circle_theme(), stroke_width=stroke_width)
        center = self._point_from_input(model_point_or_tuple_center)
        radius = self._parameter_from_input(radius_or_parameter)
        model_circle = ModelCircle.from_center_and_point(center, radius)
        self._add_circle(model_circle, style_props=style_props, no_animate=no_animate, voiceover_text=voiceover_text)
        return model_circle

    def circle_between_two_points(self, model_point_or_tuple_start, model_point_or_tuple_end, 
                                  color=DARK_BROWN, fill_color=None, 
                                  fill_opacity=0.2, no_animate=False, stroke_width=DEFAULT_STROKE_WIDTH, voiceover_text=None)->ModelCircle:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.circle_theme(), stroke_width=stroke_width)
        start = self._point_from_input(model_point_or_tuple_start)
        end = self._point_from_input(model_point_or_tuple_end)
        model_circle = ModelCircle.circle_from_two_points(start, end)
        self._add_circle(model_circle, style_props=style_props, no_animate=no_animate, voiceover_text=voiceover_text)
        return model_circle

    def triangle_from_three_points(self, model_point_or_tuple_a, model_point_or_tuple_b, model_point_or_tuple_c, color=CURRENT_COLOR_THEME.triangle_color(), 
                                   fill_color=None, fill_opacity=0.2, no_animate=False, stroke_width=DEFAULT_STROKE_WIDTH, voiceover_text=None)->ModelTriangle:    
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.triangle_theme(), stroke_width=stroke_width)
        a = self._point_from_input(model_point_or_tuple_a)
        b = self._point_from_input(model_point_or_tuple_b)
        c = self._point_from_input(model_point_or_tuple_c)
        model_triangle = ModelTriangle(a, b, c)
        ui_triangle = UITriangle(self.geo_mapper, model_triangle, style_props=style_props)
        self._register_object(model_triangle, ui_triangle, no_animate, voiceover_text)  
        return model_triangle
    
    def triangle_from_three_sides(self, side_length_parameter_a, side_length_parameter_b, 
                                  side_length_parameter_c, origin_point_or_tuple, 
                                  color=CURRENT_COLOR_THEME.triangle_color(), 
                                  fill_color=None, fill_opacity=0.2,
                                  no_animate=False, voiceover_text=None)->ModelTriangle:    
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.triangle_theme())
        a = self._parameter_from_input(side_length_parameter_a)
        b = self._parameter_from_input(side_length_parameter_b)
        c = self._parameter_from_input(side_length_parameter_c)
        origin_point = self._point_from_input(origin_point_or_tuple)
        model_triangle = ModelTriangle.from_three_sides(a, b, c, origin_point)
        ui_triangle = UITriangle(self.geo_mapper, model_triangle, style_props=style_props)
        self._register_object(model_triangle, ui_triangle, no_animate, voiceover_text)
        return model_triangle   
    
    def polygon_from_sides(self, side_size_or_parameters, origin_point_or_tuple, color=CURRENT_COLOR_THEME.triangle_color(), 
                           fill_color=None, fill_opacity=0.2, no_animate=False, 
                           voiceover_text=None)->ModelPolygon:
        side_size_parameters = [self._parameter_from_input(param) for param in side_size_or_parameters]
        origin_point = self._point_from_input(origin_point_or_tuple)
        model_polygon = ModelPolygon.from_side_length_and_origin(side_size_parameters, origin_point)
        return self._create_polygon(model_polygon, color, fill_color, fill_opacity, no_animate, voiceover_text)

    def rectangle_from_width_and_height(self, width_value_or_parameter, height_value_or_parameter, 
                                        origin_point_or_tuple, color=CURRENT_COLOR_THEME.triangle_color(), 
                                       fill_color=None, fill_opacity=0.2, 
                                       no_animate=False, voiceover_text=None)->ModelPolygon:
        width_parameter = self._parameter_from_input(width_value_or_parameter)
        height_parameter = self._parameter_from_input(height_value_or_parameter)
        origin_point = self._point_from_input(origin_point_or_tuple)
        model_polygon = ModelPolygon.from_width_and_height(width_parameter, height_parameter, origin_point)
        return self._create_polygon(model_polygon, color, fill_color, fill_opacity, no_animate, voiceover_text)

    def square_from_side_length(self, side_length_value_or_parameter, origin_point_or_tuple, color=CURRENT_COLOR_THEME.triangle_color(), 
                                fill_color=None, fill_opacity=0.2, no_animate=False,
                                voiceover_text=None)->ModelPolygon:
        side_length_parameter = self._parameter_from_input(side_length_value_or_parameter)
        origin_point = self._point_from_input(origin_point_or_tuple)
        model_polygon = ModelPolygon.from_side_length_and_origin(side_length_parameter, origin_point)
        return self._create_polygon(model_polygon, color, fill_color, fill_opacity, no_animate, voiceover_text)  

    """
    graph_sheet.interior_angle((1,0), (0,0), (0,1))
    If we consider the points as A, B, C, then the internal angle at vertex A is angle BAC not CAB because these points 
    are defined in clockwise direction.
    """
    def interior_angle(self, from_point_or_tuple, vertex_or_tuple, to_point_or_tuple, 
                       color=CURRENT_COLOR_THEME.angle_color(), fill_color=None, fill_opacity=0.3,
                       radius=1,
                       directional_arrow=False,
                       stroke_width=DEFAULT_STROKE_WIDTH, no_animate=False, 
                       voiceover_text=None)->ModelAngle:
        
        if fill_color is None and fill_opacity > 0:
            fill_color = color
            
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.angle_theme(), stroke_width=stroke_width)
        point_from = self._point_from_input(from_point_or_tuple)
        vertex = self._point_from_input(vertex_or_tuple)
        to_point = self._point_from_input(to_point_or_tuple)
        return self._angle(point_from, vertex, to_point, clock_wise=False,
                           style_props=style_props, directional_arrow=directional_arrow,
                          radius=radius, no_animate=no_animate, voiceover_text=voiceover_text)
        
    def angle_between_vectors(self, model_vector_a, model_vector_b, color=CURRENT_COLOR_THEME.angle_color(), 
                              fill_color=None, fill_opacity=0.3, radius=1,
                              directional_arrow=False,
                              stroke_width=DEFAULT_STROKE_WIDTH, no_animate=False, 
                              voiceover_text=None)->ModelAngle:
        return self.angle_between_lines(model_vector_a, model_vector_b, color = color,
                                        fill_color=fill_color, fill_opacity=fill_opacity, 
                                        radius=radius, directional_arrow=directional_arrow,
                                      stroke_width=stroke_width, no_animate=no_animate, voiceover_text=voiceover_text)
        
    def angle_between_lines(self, line_a, line_b, color=CURRENT_COLOR_THEME.angle_color(), 
                            fill_color=None, fill_opacity=0.3, radius=1,
                            directional_arrow=False,
                            stroke_width=DEFAULT_STROKE_WIDTH, 
                            no_animate=False, voiceover_text=None)->ModelAngle:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.angle_theme(), stroke_width=stroke_width)
        model_angle = ModelAngle.angle_between_lines(line_a, line_b)
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

    def exterior_angle(self, point_from_or_tuple, vertex_or_tuple, to_point_or_tuple, color=CURRENT_COLOR_THEME.angle_color(), 
                       fill_color=None, fill_opacity=0.3, radius=1,
                       directional_arrow=False, 
                       stroke_width=DEFAULT_STROKE_WIDTH, 
                       no_animate=False, voiceover_text=None)->ModelAngle:
      
        if fill_color is None and fill_opacity > 0:
            fill_color = color
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.angle_theme(), stroke_width=stroke_width)
        point_from = self._point_from_input(point_from_or_tuple)
        vertex = self._point_from_input(vertex_or_tuple)
        to_point = self._point_from_input(to_point_or_tuple)
        return self._angle(point_from, vertex, to_point, clock_wise=True, style_props=style_props,
                           radius=radius, no_animate=no_animate,
                           directional_arrow=directional_arrow, 
                           voiceover_text=voiceover_text)

    def brace_between_points(self, start, end, color=GREEN, fill_color=None, 
                             fill_opacity=1, no_animate=False, 
                             direction=RIGHT,
                             voiceover_text=None)->ModelDistance:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.distance_marker_theme())
        start = self._point_from_input(start)
        end = self._point_from_input(end)
        model_distance = ModelDistance.from_points(start, end)
        ui_distance = UIDistance(self.geo_mapper, model_distance, 
                                 direction=direction,
                                 style_props=style_props)
        self._register_object(model_distance, ui_distance, no_animate, voiceover_text)
        return model_distance

    def arc_from_center_and_angles(self, center, radius_or_parameter, start_angle_or_parameter, end_angle_or_parameter, 
                                   color=CURRENT_COLOR_THEME.arc_color(), fill_color=None, fill_opacity=1, 
                                   stroke_width=DEFAULT_STROKE_WIDTH, 
                                   no_animate=False, 
                                   voiceover_text=None)->ModelArc:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.arc_theme(), stroke_width=stroke_width)
        center = self._point_from_input(center)
        radius_parameter = self._parameter_from_input(radius_or_parameter)
        start_angle_parameter = self._parameter_from_input(start_angle_or_parameter)
        end_angle_parameter = self._parameter_from_input(end_angle_or_parameter)
        model_arc = ModelArc.from_center_and_angles(center, radius_parameter, start_angle_parameter, end_angle_parameter)
        ui_arc = UIArc(self.geo_mapper, model_arc, style_props=style_props)
        self._register_object(model_arc, ui_arc, no_animate, voiceover_text)
        return model_arc

    def polygon_from_points(self, points, 
                            color=GREEN, fill_color=None, 
                            fill_opacity=0.2, no_animate=False, 
                            voiceover_text=None)->ModelPolygon:
        style_props = self._create_style_props(color, fill_color, 
                                               fill_opacity, UIStyleProps.polygon_theme())
        points = [self._point_from_input(point) for point in points]
        model_polygon = ModelPolygon(points)
        ui_polygon = UIPolygon(self.geo_mapper, model_polygon, style_props=style_props)
        self._register_object(model_polygon, ui_polygon, no_animate, voiceover_text)
        return model_polygon
    
    def dynamic_value(self, source_prop, source_model, var_type=DecimalNumber, 
                         color=BLACK, fill_color=GREEN, fill_opacity=1)->ModelDynamicProperty:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.dynamic_prop_theme())
        model_dynamic_property = ModelDynamicProperty.from_model(
            source_prop=source_prop,
            source_model=source_model
        )
        ui_dynamic_property = UIDynamicSimple(
            self,
            geo_mapper=self.geo_mapper,
            model_dynamic_property=model_dynamic_property,
            var_type=var_type,
            style_props=style_props
        )   
        self._register_text(model_dynamic_property, ui_dynamic_property, no_animate=True)
        return model_dynamic_property
        
    def dynamic_key_value(self, variable_name, source_prop, source_model, var_type=DecimalNumber, 
                         color=BLACK, fill_color=GREEN, fill_opacity=1)->ModelDynamicProperty:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.dynamic_prop_theme())

       
        model_dynamic_property = ModelDynamicProperty.from_model(
            source_prop=source_prop,
            source_model=source_model,
            variable_name=variable_name
        )
        ui_dynamic_property = UIDynamicVariableProperty(
            self,
            geo_mapper=self.geo_mapper,
            model_dynamic_property=model_dynamic_property,
            var_type=var_type,
            style_props=style_props
        )
        self._register_text(model_dynamic_property, ui_dynamic_property, no_animate=True)
        return model_dynamic_property

    def trace_plot(self, plot_expression, value_or_parameter, 
                   substitutions_dict={}, color=CURRENT_COLOR_THEME.trace_color(),
                   fill_color=None, fill_opacity=1, voiceover_text=None)->ModelPlotTrace:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.trace_theme())
        parameter_dict = self._parameter_dict_from_input(substitutions_dict)
        model_plot = ModelPlot.from_expression(plot_expression, subs_dict_of_model_parameters=parameter_dict )
        model_parameter = self._parameter_from_input(value_or_parameter)
        model_plot_trace = ModelPlotTrace.from_plot(model_plot, model_parameter=model_parameter)
        ui_plot_trace = UITrace(self.geo_mapper, model_plot_trace, style_props=style_props)
        self._register_object(model_plot_trace, ui_plot_trace, voiceover_text=voiceover_text)
        return model_plot_trace

    def text(self, text_or_list, scale_factor=1,  color=BLACK,
             fill_color=None,
             fill_opacity=1, no_animate=True, voiceover_text=None)->ModelMixedText:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.text_theme(), scale_factor=scale_factor)
        text_list = [text_or_list] if isinstance(text_or_list, str) else text_or_list       
        model_text = ModelMixedText(text_list)
        ui_text = UIMixedText(model_text=model_text, style_props=style_props)
        self._register_text(model_text, ui_text,  no_animate, voiceover_text)
        return model_text
    
    def math_text(self, text_or_list, scale_factor=0.7,  color=BLACK, fill_color=None,
             fill_opacity=1, no_animate=True, voiceover_text=None)->MathModelText:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.text_theme(), scale_factor=scale_factor)
        text_list = [text_or_list] if isinstance(text_or_list, str) else text_or_list   
        model_text = MathModelText(text_list)
        ui_text = UIMathTex(model_text=model_text, style_props=style_props)
        self._register_text(model_text, ui_text,  no_animate, voiceover_text)
        return model_text
    

    
    def plain_text(self, text, scale_factor=1,  color=BLACK, fill_color=None,
             fill_opacity=1, no_animate=True, voiceover_text=None)->ModelPlainText:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.text_theme(), scale_factor=scale_factor)
        model_text = ModelPlainText(text)
        ui_text = UIPlainText(model_text=model_text, style_props=style_props)
        self._register_text(model_text, ui_text,  no_animate, voiceover_text)
        return model_text

    """
    array is a list of lists
    example:
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    [["\pi", 3], [1, 5]]
    
    """
    def matrix(self, array, bracket_type="[", scale_factor=1, 
               color=BLACK, fill_color=None, 
               fill_opacity=1, no_animate=False, voiceover_text=None)->ModelMatrix:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.text_theme(), scale_factor=scale_factor)
        model_matrix = ModelMatrix(array)
        ui_matrix = UIMatrix(model_matrix, bracket_type=bracket_type, style_props=style_props)
        self._register_object(model_matrix, ui_matrix, no_animate, voiceover_text)
        return model_matrix 
    
    def update_matrix(self, model_matrix, new_array, run_time=1, voiceover_text=None)->ModelMatrix:
        transform_animation = model_matrix.ui_part.update_matrix(new_array)
        self.play(transform_animation, run_time=run_time, voiceover_text=voiceover_text)
        return model_matrix
    
    def aligned_text(self, text, start_point_or_tuple, end_point_or_tuple, direction=UP, reverse_direction=False,   shift=ORIGIN,
                     color=BLACK, scale_factor=1, 
                     fill_color=None, fill_opacity=1, no_animate=False, voiceover_text=None)->ModelAlignedText:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.text_theme(), scale_factor=scale_factor)
        start_point = self._point_from_input(start_point_or_tuple)
        end_point = self._point_from_input(end_point_or_tuple)
        model_text = ModelAlignedText.aligned_to_points(text, start_point, end_point)
        ui_text = UIAlignedText(self.geo_mapper, model_text, style_props=style_props, direction=direction, reverse_direction=reverse_direction, shift=shift)
        self._register_text(model_text, ui_text, no_animate, voiceover_text)
        return model_text
    
    def distance_label_with_arrows(self, text, start_point_or_tuple, end_point_or_tuple, 
                          direction=UP, reverse_direction=False,  
                          buff=0.5,color=ORANGE,
                     scale_factor=0.7,  fill_color=None, fill_opacity=1, no_animate=False, 
                     voiceover_text=None)->ModelLabelWithArrows:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.text_theme(), scale_factor=scale_factor)   
        start_point = self._point_from_input(start_point_or_tuple)
        end_point = self._point_from_input(end_point_or_tuple)
        model_label_with_arrows = ModelLabelWithArrows.from_text_and_points(text, start_point, end_point)
        ui_label_with_arrows = UILabelWithArrows(self.geo_mapper, model_label_with_arrows, style_props=style_props, direction=direction, reverse_direction=reverse_direction, buff=buff)
        self._register_object(model_label_with_arrows, ui_label_with_arrows, no_animate, voiceover_text) 
        return model_label_with_arrows  

   
    def circle_from_equation(self, equation, color=DARK_BROWN, 
                             fill_color=None, fill_opacity=0.2, no_animate=False, voiceover_text=None):
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.circle_theme())
        model_circle = ModelCircle.from_equation(equation)
        self._add_circle(model_circle, style_props=style_props, no_animate=no_animate, voiceover_text=voiceover_text)
        return model_circle


    def perp_line(self, source_line, pass_through_point_or_tuple, color=DARK_BLUE, 
                 fill_color=None, fill_opacity=1, no_animate=False, voiceover_text=None)->ModelLine:
        style_props = self._create_style_props(color, fill_color, 
                                               fill_opacity, UIStyleProps.line_theme())
        source_line = self._line_from_input(source_line)
        pass_through_point = self._point_from_input(pass_through_point_or_tuple)
        perp_line = source_line.perpendicular_line(pass_through_point)
        self._add_line(model_line=perp_line, style_props=style_props, no_animate=no_animate, 
                       voiceover_text=voiceover_text) 
        return perp_line

    def parallel_line(self, source_line, pass_through_point, color=DARK_BLUE, 
                        fill_color=None, fill_opacity=1, no_animate=False, voiceover_text=None)->ModelLine:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.line_theme())
        source_line = self._line_from_input(source_line)
        pass_through_point = self._point_from_input(pass_through_point)
        parallel_line = source_line.parallel_line(pass_through_point)
        self._add_line(model_line=parallel_line, style_props=style_props,
                    no_animate=no_animate, voiceover_text=voiceover_text)
        return parallel_line

    def line_from_general_form_equation(self, equation, segment_length=20, color=DARK_BLUE, 
                                        fill_color=None, fill_opacity=1, no_animate=False,
                                        voiceover_text=None)->ModelLine:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.line_theme())
        model_line = ModelLine.from_general_equation(equation, segment_length=segment_length)
        self._add_line(model_line=model_line, style_props=style_props,
                       no_animate=no_animate, voiceover_text=voiceover_text)    
        return model_line

    def line_from_normal_form_equation(self, equation, segment_length=20, color=DARK_BLUE,
                                       fill_color=None, fill_opacity=1, no_animate=False,
                                       voiceover_text=None)->ModelLine:
        style_props = self._create_style_props(color, fill_color, 
                                               fill_opacity, UIStyleProps.line_theme())
        model_line = ModelLine.from_normal_equation(equation, segment_length=segment_length)
        self._add_line(model_line=model_line, style_props=style_props,
                       no_animate=no_animate, voiceover_text=voiceover_text)
        return model_line

    def line_from_slope_and_intercept(self, slope, intercept, segment_length=20, 
                                      color=DARK_BLUE,   
                                      fill_color=None, fill_opacity=1,
                                      no_animate=False, voiceover_text=None)->ModelLine:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.line_theme())
        slope = self._parameter_from_input(slope)
        intercept = self._parameter_from_input(intercept)
        model_line = ModelLine.from_slope_and_intercept(slope, intercept, segment_length=segment_length)
        self._add_line(model_line=model_line, style_props=style_props,
                       no_animate=no_animate, voiceover_text=voiceover_text)    
        return model_line

      

    
    """
    substitution_dict is a dictionary of parameters to be substituted into the expression
    plot_range is a tuple of the x-axis range
    """
    def plot_function(self, latex_expression, substitutions_dict={}, plot_range=None, 
                      color=CURRENT_COLOR_THEME.plot_color(), fill_color=None, fill_opacity=1, 
                      no_animate=False, voiceover_text=None)->ModelPlot:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.plot_theme())
        parameter_dict = self._parameter_dict_from_input(substitutions_dict)
        model_plot = ModelPlot.from_expression(latex_expression, subs_dict_of_model_parameters=parameter_dict, plot_range=plot_range)
        ui_plot = UIExplicitPlot(self.geo_mapper, model_plot, style_props=style_props) if isinstance(model_plot, ModelExplicitPlot) else UIImplicitPlot(self.geo_mapper, model_plot, style_props=style_props)
        self._register_object(model_plot, ui_plot, no_animate, voiceover_text)
        return model_plot
    
    def plot_lambda_function(self, lambda_function, plot_range=None, color=CURRENT_COLOR_THEME.plot_color(), 
                             fill_color=None, fill_opacity=1, no_animate=False,
                             voiceover_text=None)->ModelExplicitPlot:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.plot_theme())
        model_plot = ModelExplicitPlot.from_lambda_function(lambda_function, plot_range=plot_range)
        ui_plot = UIExplicitPlot(self.geo_mapper, model_plot, style_props=style_props)
        self._register_object(model_plot, ui_plot, no_animate, voiceover_text)  
        return model_plot

    def tangent(self, plot_model, at_plot, color=DARK_BLUE, 
                fill_color=None, fill_opacity=1, no_animate=False, 
                voiceover_text=None)->ModelTanget: 
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.line_theme())
        at_plot = self._parameter_from_input(at_plot)
        model_tangent = ModelTanget.tangent_on_plot(plot_model, at_plot)
        ui_tangent = UITangent(self.geo_mapper, model_tangent, style_props=style_props)
        self._register_object(model_tangent, ui_tangent, no_animate, voiceover_text)
        return model_tangent  
    
    def slope(self, plot, at_plot, 
              color=DARK_BLUE, fill_color=None, fill_opacity=1, 
              no_animate=False, voiceover_text=None)->ModelTangentSlope:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.line_theme())
        x_parameter = self._parameter_from_input(at_plot)
        model_tangent_slope = ModelTangentSlope.tangent_slope(plot, x_parameter)
        ui_tangent_slope = UITangentSlope(self.geo_mapper, model_tangent_slope, style_props=style_props)
        self._register_object(model_tangent_slope, ui_tangent_slope, no_animate, voiceover_text)
        return model_tangent_slope
    
    """ 
    area_range is a tuple (x_min, x_max )
    """
    def area_under_plot(self, model_plot, area_range_parameters, 
                        color=GREEN, fill_color=None, 
                        fill_opacity=1, no_animate=False, voiceover_text=None)->ModelArea:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.polygon_theme())
        area_range_parameters = self._range_parameters_from_input(area_range_parameters)    
        model_area = ModelArea.from_plot_and_range_parameters(model_plot, area_range_parameters)
        ui_area = UIArea(self.geo_mapper, model_area, style_props=style_props)
        self._register_object(model_area, ui_area, no_animate, voiceover_text)
        return model_area
    
    def area_between_curves(self, curve_a:ModelExplicitPlot, curve_b:ModelExplicitPlot, 
                           from_parameter_or_value, to_parameter_or_value, 
                           color=GREEN, fill_color=GREEN, 
                           fill_opacity=0.5, no_animate=False, voiceover_text=None)->ModelAreaBetweenCurves:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.polygon_theme())
        from_parameter = self._parameter_from_input(from_parameter_or_value)
        to_parameter = self._parameter_from_input(to_parameter_or_value)
        model_area_between_curves = ModelAreaBetweenCurves.area_between_curves(curve_a, curve_b, from_parameter, to_parameter)
        ui_area_between_curves = UIAreaBetweenCurves(self.geo_mapper, model_area_between_curves, style_props=style_props)
        self._register_object(model_area_between_curves, ui_area_between_curves, 
                                no_animate, voiceover_text)
        return model_area_between_curves
    
    def image(self, image_path, model_position_or_tuple, scale_factor=1, 
              no_animate=False, voiceover_text=None)->ModelImage:
        model_position = self._point_from_input(model_position_or_tuple)
        model_image = ModelImage.from_path_and_position(image_path, model_position)
        ui_image = UIImage(self.geo_mapper, model_image, scale_factor=scale_factor)
        self._register_image(model_image, ui_image, no_animate, voiceover_text)
        return model_image
    
    """
    sum_range is a tuple (x_min, x_max )
    """
    def reimann_sum(self, model_plot, dx_parameter, sum_range, color=GREEN, 
                    fill_color=None, fill_opacity=1, no_animate=False,
                    voiceover_text=None)->ModelRiemann:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.polygon_theme())
        
        dx_parameter = self._parameter_from_input(dx_parameter)
        model_riemann = ModelRiemann.from_plot_and_parameter(model_plot, dx_parameter, sum_range) 
        ui_riemann = UIReimann(self.scene, self.geo_mapper, model_riemann, style_props=style_props)
        self._register_object(model_riemann, ui_riemann, no_animate, voiceover_text)
        return model_riemann

    def projection_on_axis(self, model_point_or_tuple, color=CURRENT_COLOR_THEME.brace_color(), 
                            no_animate=False, fill_color=None, fill_opacity=1,
                            voiceover_text=None)->ModelAxisLine:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.brace_theme())
        point = self._point_from_input(model_point_or_tuple)
        model_axis_line = ModelAxisLine.axis_line_from_point(point)
        ui_axis_line = UIAxisLines(self.geo_mapper, model_axis_line=model_axis_line, style_props=style_props)
        self._register_object(model_axis_line, ui_axis_line, no_animate, voiceover_text)
        return model_axis_line


    def trace_model(self, model_shape, ratio_parameter, color=CURRENT_COLOR_THEME.trace_color(), 
                    fill_color=None, fill_opacity=1, no_animate=False, 
                    voiceover_text=None)->ModelShapeTrace:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.trace_theme())
        ratio_parameter = self._parameter_from_input(ratio_parameter)
        model_trace = ModelShapeTrace.from_shape(model_shape, ratio_parameter=ratio_parameter)
        ui_trace = UITrace(self.geo_mapper, model_trace, style_props=style_props)
        self._register_trace(model_trace, ui_trace, no_animate, voiceover_text)
        return model_trace
    
    def trace_point(self, model_point:ModelPoint, color=CURRENT_COLOR_THEME.trace_color(), fill_color=None, 
                    fill_opacity=1, no_animate=False, voiceover_text=None)->ModelPointTrace:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.trace_theme())
        model_trace = ModelPointTrace.from_point(model_point)   
        ui_trace = UITrace(self.geo_mapper, model_trace, style_props=style_props)
        self._register_object(model_trace, ui_trace, no_animate, voiceover_text)
        return model_trace

    def plot_parametric(self, latex_expression1, latex_expression2, plot_range, substitutions_dict={}, 
                        color=CURRENT_COLOR_THEME.plot_color(), 
                        fill_color=None, fill_opacity=1, 
                        no_animate=False, voiceover_text=None)->ModelParametricPlot:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.plot_theme())
        parameter_dict = self._parameter_dict_from_input(substitutions_dict)
        model_plot = ModelPlot.plot_parametric(latex_expression1, latex_expression2, plot_range, subs_dict_of_model_parameters=parameter_dict)
        ui_plot = UIParametricPlot(self.geo_mapper, model_plot, plot_range=plot_range, style_props=style_props)
        self._register_object(model_plot, ui_plot, no_animate, voiceover_text)
        return model_plot
    
    def plot_parametric_lambda(self, lambda_function_1, lambda_function_2, plot_range, 
                              color=CURRENT_COLOR_THEME.plot_color(), fill_color=None, 
                              fill_opacity=1, no_animate=False, voiceover_text=None)->ModelParametricPlot:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.plot_theme())
        model_plot = ModelPlot.plot_parametric_lambda(lambda_function_1, lambda_function_2, plot_range)
        ui_plot = UIParametricPlot(self.geo_mapper, model_plot, plot_range=plot_range, style_props=style_props)
        self._register_object(model_plot, ui_plot, no_animate, voiceover_text)
        return model_plot
    
    def ellipse_origin_major_minor(self, origin_point , major, minor, color=CURRENT_COLOR_THEME.ellipse_color(), 
                                   fill_color=None, fill_opacity=1,
                                   no_animate=False, voiceover_text=None)->ModelEllipseParametric:
         style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.ellipse_theme())
         model_point = self._point_from_input(origin_point)
         major = self._parameter_from_input(major)
         minor = self._parameter_from_input(minor)
         model_ellipse = ModelEllipseParametric.from_origin_major_minor(model_point, major, minor)
         ui_ellipse = UIEllipseByParametricFunction(self.geo_mapper, model_ellipse, style_props=style_props)
         self._register_object(model_ellipse, ui_ellipse, no_animate, voiceover_text)
         return model_ellipse
    
    def ellipse_standard_equation(self, equation, color=CURRENT_COLOR_THEME.ellipse_color(), fill_color=None, 
                                  fill_opacity=1, no_animate=False, 
                                  voiceover_text=None)->ModelEllipseParametric:    
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.ellipse_theme())
        model_ellipse = ModelEllipseParametric.from_latex_standard_equation(equation)
        ui_ellipse = UIEllipseByParametricFunction(self.geo_mapper, model_ellipse, style_props=style_props)
        self._register_object(model_ellipse, ui_ellipse, no_animate, voiceover_text)
        return model_ellipse

    def parabola_focus_directrix(self, focus_point, directrix_line, range=3, 
                                 color=DARK_BROWN, fill_color=None, 
                                 fill_opacity=1, no_animate=False, 
                                 voiceover_text=None)->ModelParabolaParametric:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.circle_theme())
        focus_point = self._point_from_input(focus_point)
        directrix_line = self._line_from_input(directrix_line)  
        model_parabola = ModelParabolaParametric.from_focus_and_directrix(focus_point, directrix_line)
        ui_parabola = UIParabolaByParametricFunction(self.geo_mapper, model_parabola, range=range, style_props=style_props)
        self._register_object(model_parabola, ui_parabola, no_animate, voiceover_text)
        return model_parabola
    
    def hyperbola_focus_vertices(self, focus_a_point, focus_b_point, vertex_a_point, vertex_b_point,
                                 color=DARK_BROWN, fill_color=None, fill_opacity=1, 
                                 no_animate=False, voiceover_text=None)->ModelHyperbola:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.circle_theme())
        focus_a_point = self._point_from_input(focus_a_point)
        focus_b_point = self._point_from_input(focus_b_point)
        vertex_a_point = self._point_from_input(vertex_a_point)
        vertex_b_point = self._point_from_input(vertex_b_point)
        model_hyperbola = ModelHyperbola.from_foci_and_vertices(focus_a_point, focus_b_point, vertex_a_point, vertex_b_point)
        ui_hyperbola = UIHyperbola(self.geo_mapper, model_hyperbola, style_props=style_props)
        self._register_object(model_hyperbola, ui_hyperbola, no_animate, voiceover_text)
        return model_hyperbola

    def parameter(self, from_value=0)->ModelParameter:
        model_parameter = ModelParameter(self.scene, from_value)
        ui_parameter = UIParameter(model_parameter)
        self._register_object(model_parameter, ui_parameter)
        return model_parameter
    
    def lambda_parameter(self, lambda_function, from_value=0)->ModelLambdaParameter:
        model_parameter = ModelLambdaParameter(self.scene, lambda_function, from_value)
        ui_parameter = UIParameter(model_parameter)
        self._register_object(model_parameter, ui_parameter)
        return model_parameter
    
    def point_parameter(self, x_lambda_function, y_lambda_function, from_value=0,
                         color=RED, fill_color=None, fill_opacity=1, 
                         no_animate=False, voiceover_text=None)->ModelPointParameter:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        model_parameter = ModelPointParameter(self.scene, x_lambda_function, y_lambda_function, from_value)
        point = UIPoint(self.geo_mapper, model_parameter, style_props=style_props)
        self._register_object(model_parameter, point, no_animate, voiceover_text)
        return model_parameter
    
    def chain_parameters(self, source_parameter, *dependent_parameters)->ModelChainedParameter:
        chained_parameter = ModelChainedParameter(self.scene, source_parameter, *dependent_parameters)
        ui_parameter = UIParameter(chained_parameter)
        self._register_object(chained_parameter, ui_parameter)
        return chained_parameter

    def play_parameter(self, model_parameter:ModelParameter, from_value, to_value, run_time=2, 
                       rate_func=linear, voiceover_text=None)->ModelParameter:
        model_parameter.play(from_value, to_value, run_time, rate_func, voiceover_text)
        return model_parameter

    def sync_parameter_with_model_property(self, model_parameter, target_model, target_prop)->ParameterLambdaUpdater:
        source_model = self._parameter_from_input(model_parameter)
        parameter_lambda_updater = ParameterLambdaUpdater.from_param_change(source_model, "param_value", target_model, target_prop)
        return parameter_lambda_updater

    def intersect_line_line(self, line1, line2, color=RED,
                            fill_color=None, fill_opacity=1, no_animate=False, 
                            voiceover_text=None)->ModelLineToLineIntersection:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        line1 = self._line_from_input(line1)
        line2 = self._line_from_input(line2)
        model_intersection = ModelLineToLineIntersection.from_lines(line1, line2)
        ui_intersection = UIIntersection(self.geo_mapper, model_intersection, style_props=style_props)
        self._register_object(model_intersection, ui_intersection, no_animate, voiceover_text)
        return model_intersection
    
    def intersect_line_circle(self, model_line, model_circle, color=RED,
                              fill_color=None, fill_opacity=1, no_animate=False,
                              voiceover_text=None)->ModelLineToCircleIntersection:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        model_intersection = ModelLineToCircleIntersection.from_line_and_circle(model_line, model_circle)
        ui_intersection = UIIntersection(self.geo_mapper, model_intersection, style_props=style_props)
        self._register_object(model_intersection, ui_intersection, no_animate, voiceover_text)
        return model_intersection
    
    def intersect_circle_circle(self, model_circle1, model_circle2, color=RED,
                                fill_color=None, fill_opacity=1, 
                                no_animate=False, voiceover_text=None)->ModelCircleToCircleIntersection:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        model_intersection = ModelCircleToCircleIntersection.from_circles(model_circle1, model_circle2)
        ui_intersection = UIIntersection(self.geo_mapper, model_intersection, style_props=style_props)
        self._register_object(model_intersection, ui_intersection, no_animate, voiceover_text)
        return model_intersection
    
    def intersect_polygon_polygon(self, model_polygon1, model_polygon2, 
                                  color=RED, fill_color=None, fill_opacity=1, 
                                  no_animate=False, voiceover_text=None)->ModelPolygonToPolygonIntersection:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        model_intersection = ModelPolygonToPolygonIntersection.from_polygons(model_polygon1, model_polygon2)
        ui_intersection = UIIntersection(self.geo_mapper, model_intersection, style_props=style_props)
        self._register_object(model_intersection, ui_intersection, no_animate, voiceover_text)
        return model_intersection
    
    def intersect_region(self, model_shape1, model_shape2, 
                              color=RED, fill_color=None, fill_opacity=1, 
                              no_animate=False, voiceover_text=None)->ModelIntersectionRegion:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        model_intersection = ModelIntersectionRegion.from_shapes(self.geo_mapper, model_shape1, model_shape2)
        ui_intersection = UIIntersectionRegion(model_intersection, style_props=style_props)
        self._register_object(model_intersection, ui_intersection, no_animate, voiceover_text)
        return model_intersection
   
    """
    line is a ModelLine
    poly is a ModelPolygon or ModelTriangle
    
    """ 
    
    def move_camera_down(self, distance=2):
        self.move_camera_to(DOWN*distance)
        
    def show_subscripts(self, math_text_model, word_index=None):
        view = math_text_model.view()
        if word_index is None:
            vgroup =  TextPositionRenderHelper.render_single_mathtex(view)
        else:
            vgroup =  TextPositionRenderHelper.render_single_mathtex(view, word_index)
        self.add(vgroup)
        return vgroup
    
    def compare_subscripts(self, math_text_model1, math_text_model2, word_index_1=0, word_index_2=0):
        view1 = math_text_model1.view()
        view2 = math_text_model2.view()
        vgroup = TextPositionRenderHelper.render_two_mathtex(view1, view2, word_index_1, word_index_2)
        self.add(vgroup)
        return vgroup
    
    def move_camera_to(self, model_object_or_point, voiceover_text=None):
        self.scene.camera.frame.save_state()
        if voiceover_text is not None   :
            with self.scene.voiceover(voiceover_text) as tracker:       
                if isinstance(model_object_or_point, BaseModel):
                    self.scene.play(self.scene.camera.frame.animate.move_to(model_object_or_point.view()), 
                               run_time=tracker.duration)       
                else:
                    self.scene.play(self.scene.camera.frame.animate.move_to(model_object_or_point), 
                               run_time=tracker.duration)      
        else:
            if isinstance(model_object_or_point, BaseModel):
                self.play(self.scene.camera.frame.animate.move_to(model_object_or_point.view()))
            else:
                self.play(self.scene.camera.frame.animate.move_to(model_object_or_point))
            
    def zoom_camera_to(self, model_object_or_point, width=2, voiceover_text=None):
        self.scene.camera.frame.save_state()
        if voiceover_text is not None:
            with self.scene.voiceover(voiceover_text) as tracker:   
                if isinstance(model_object_or_point, BaseModel):
                    self.scene.play(self.scene.camera.frame.animate.move_to(model_object_or_point.view()).set(width=width), 
                               run_time=tracker.duration)   
                else:
                    self.scene.play(self.scene.camera.frame.animate.move_to(model_object_or_point).set(width=width), 
                               run_time=tracker.duration)      
        else:
            if isinstance(model_object_or_point, BaseModel):    
                self.play(self.scene.camera.frame.animate.move_to(model_object_or_point.view()).set(width=width))
            else:
                self.play(self.scene.camera.frame.animate.move_to(model_object_or_point).set(width=width))
        
    def restore_camera(self, voiceover_text=None):
        if voiceover_text is not None: 
            with self.scene.voiceover(voiceover_text) as tracker:   
                self.scene.play(Restore(self.scene.camera.frame), run_time=tracker.duration)
        else:
            self.play(Restore(self.scene.camera.frame))

    def fade_out(self, *model_objects:BaseModel):
        if len(model_objects) == 0: 
            return
        animations = []
        for model_object in model_objects:
            if isinstance(model_object, BaseModel):
                animations.append(FadeOut(model_object.view()))
            else:
               animations.append(FadeOut(model_object))
        self.scene.play(AnimationGroup(*animations, lag_ratio=0))
        
        
    def _fade_in_manim_objects(self, objects_to_fade_in, run_time=2, voiceover_text:str=None):
        animations = []
        for obj in objects_to_fade_in:
            obj.set_opacity(1)
            animations.append(FadeIn(obj))
        if voiceover_text is not None:  
            with self.scene.voiceover(voiceover_text) as tracker:
                self.scene.play(AnimationGroup(*animations, lag_ratio=0), run_time=tracker.duration)
        else:       
            self.scene.play(AnimationGroup(*animations, lag_ratio=0), run_time=run_time)
            
    def _fade_in_manim_object_effect(self, objects_to_fade_in, run_time=2, voiceover_text:str=None):
        def do_func():
            animations = []
            for obj in objects_to_fade_in:
                obj.set_opacity(1)
                animations.append(FadeIn(obj))
            return AnimationGroup(*animations, lag_ratio=0)
        
        def undo_func():
             return Wait(0.1)       
         
         
        return EffectCommand(do_func=do_func, undo_func=undo_func, scene=self.scene, 
                             graph_sheet=self, run_time=run_time, voiceover_text=voiceover_text, remove_on_completion=False)
              
        
    def fade_in(self, *model_objects:BaseModel):
        if len(model_objects) == 0: 
            return
        animations = []
        for model_object in model_objects:
            if isinstance(model_object, BaseModel): 
                model_object.view().set_opacity(1)
                model_object.view().set_fill(opacity=self._given_fill_opacity(model_object))    
                animations.append(FadeIn(model_object.view()))
            else:
                model_object.set_opacity(1)
                model_object.set_fill(opacity=self._given_fill_opacity(model_object))   
                animations.append(FadeIn(model_object))
            
        self.scene.play(AnimationGroup(*animations, lag_ratio=0))
        
    def remove_self(self):
        self.clear_all()
        self.scene.remove(self)
    
    
    def intersect_line_polygon(self, line, poly, color=RED,
                               fill_color=None, fill_opacity=1, no_animate=False, 
                               voiceover_text=None)->ModelLineToPolygonIntersection: 
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.point_theme())
        model_intersection = ModelLineToPolygonIntersection.line_to_polygon_intersection(line, poly)
        ui_intersection = UIIntersection(self.geo_mapper, model_intersection, style_props=style_props)
        self._register_object(model_intersection, ui_intersection, no_animate, voiceover_text)
        return model_intersection

    """
    expressions example: ["x","x^2"]
    range example: [0,10]
    subs_dict example: {x:3}
    """ 
    def table_by_expressions(self, expressions, range, subs_dict={}, edge_position=LEFT, 
                             buff=LARGE_BUFF, color=BLACK, fill_color=None, 
                             fill_opacity=1, no_animate=False, voiceover_text=None)->ModelTable:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.plot_theme())
        model_table = ModelTable.from_expressions(expressions, range, subs_dict)
        ui_table = UITable(model_table, style_props=style_props)
        ui_table.view().to_edge(edge_position, buff=buff)
        self._register_object(model_table, ui_table, no_animate, voiceover_text)
        return model_table
    
    """
    header example: ["x","f(x)=x^2"]
    rows example: [[0,f(0)],[1,f(1)],[2,f(2)]]  
    """
    def table_by_header_and_rows(self, header, rows, edge_position=LEFT,
                                 buff=LARGE_BUFF, color=CURRENT_COLOR_THEME.plot_color(), 
                                 fill_color=None, fill_opacity=1, no_animate=False, 
                                 voiceover_text=None)->ModelTable:
        style_props = self._create_style_props(color, fill_color, fill_opacity, UIStyleProps.plot_theme())
        model_table = ModelTable.from_header_and_rows(header, rows)
        ui_table = UITable(model_table, style_props=style_props)
        ui_table.view().to_edge(edge_position, buff=buff)
        self._register_object(model_table, ui_table, no_animate, voiceover_text)
        return model_table  
    
    
    def bulleted_list(self, items:list[str], color=BLACK, 
                      scale_factor=1, no_animate=True,
                      line_spacing=0.6,
                      voiceover_text=None)->ModelBulletedList:
        style_props = self._create_style_props(
            color=color,    
            fill_color=None, 
            fill_opacity=1, 
            scale_factor=scale_factor,
            default_style=UIStyleProps.text_theme())
        model_bulleted_list = ModelBulletedList(items)
        ui_bulleted_list = UIBulletedList(model_bulleted_list, style_props=style_props)
        self._register_object(model_bulleted_list, ui_bulleted_list, no_animate, voiceover_text=voiceover_text)
        return model_bulleted_list
    
    """
    direction example: LEFT, RIGHT, UP, DOWN
    buff example: SMALL_BUFF, MED_SMALL_BUFF, MED_LARGE_BUFF, LARGE_BUFF
    aligned_edge example: LEFT, RIGHT, UP, DOWN 
    This would make the model and ui objects out of sync
    
    """
    def arrange(self, *model_objects, direction=RIGHT, buff=LARGE_BUFF, aligned_edge=LEFT)->ModelGroup:
        model_group = ModelGroup(*model_objects, direction=direction, buff=buff, aligned_edge=aligned_edge)
        ui_group = UIGroup(self.geo_mapper, model_group)
        self._register_group(model_group, ui_group)
        return model_group
    
    
    def update_arrangement(self, model_group, new_model_object, direction=RIGHT, buff=LARGE_BUFF,
                           voiceover_text=None)->ModelGroup:
        new_model_object.next_to(model_group, direction, buff=buff)
        new_model_object.show()
      
        new_v_group = VGroup()
        for model_object in model_group.model_objects:  
            new_v_group.add(model_object.view())
            
        new_v_group.add(new_model_object.view())
        
        target_positions = [item.get_center() for item in new_v_group.copy().arrange(direction, buff=buff)]
        
        animations = []
        for index in range(len(new_v_group.submobjects)):
            animations.append(new_v_group.submobjects[index].animate.move_to(target_positions[index]))
      
        if voiceover_text is not None:
            self.play(AnimationGroup(*animations, lag_ratio=0), voiceover_text=voiceover_text)
        else:
            self.play(AnimationGroup(*animations, lag_ratio=0))
      
        all_model_objects = model_group.model_objects + [new_model_object]
        new_model_group = ModelGroup(*all_model_objects, direction=direction, buff=buff)
        new_ui_group = UIGroup(self.geo_mapper, new_model_group, existing_ui_group=new_v_group)
        self._register_group(new_model_group, new_ui_group)
        return new_model_group
    
    def grid(self, *model_objects, rows=None, cols=None, buff=0.25, 
             cell_alignment=np.array([0., 0., 0.]),
             row_alignments=None, col_alignments=None, 
             row_heights=None, col_widths=None, flow_order='rd', **kwargs)->ModelGroup:
        model_group = ModelGroup(*model_objects, direction=LEFT, buff=buff)
        ui_group = UIGroup(self.geo_mapper, model_group)
        self._register_group(model_group, ui_group)
        model_group.grid(rows, cols, buff, cell_alignment, row_alignments, col_alignments, row_heights, col_widths, flow_order, **kwargs)
        return model_group

    
    def get_sub_part(self, model_object, from_proportion, to_proportion)->ModelPart:
        sub_part = model_object.view().get_subcurve(from_proportion, to_proportion)
        ui_part = UIPart(sub_part, self.graphsheet, self.geo_mapper, self.scene, style_props=self.style_props)
        return ModelPart(ui_part, self.graphsheet, self.geo_mapper, self.scene, item_row=from_proportion, item_col=to_proportion)    
    
    def zoom_effect(self, model_object_to_focus, width=8, run_time=1, voiceover_text=None ):
        ui_object = model_object_to_focus.view()
        return ZoomEffectCommand(scene=self.scene, 
                                 graph_sheet=self, 
                                 object_to_focus=ui_object, 
                                 width=width, 
                                 run_time=run_time, 
                                 voiceover_text=voiceover_text)
        
        
    """
    Useful for copying and moving text parts to a target location. 
    For example, copying and moving labels from a graphsheet to places in a formula. See sine_law_scene.py  
    Steps:
    1. Create the entire text in the graphsheet.
    2. Cover the text.
    3. Remove the parts where you want targets to set it.
    4. Call the effect with the source  and target models. (The target models are generally the removed parts, it encapsulates the poisition of the target )  
    5.  sin_A_source_parts = [self.label_A, self.height_label, self.side_c]
        sin_A_target_parts = [abh_angle_part, abh_height_part, abh_c_part]
        effect = graph_sheet.move_text_to_text_effect(sin_A_source_parts, sin_A_target_parts)
        graph_sheet.play_effect(effect) 
    """ 
    def move_text_to_text_effect(self, source_parts, target_parts, 
                                 match_shape=True,  
                                run_time=1, voiceover_text=None)->EffectCommand:
        return self.text_animator.move_text_to_text_effect(source_parts=source_parts,
                                                        target_parts=target_parts, 
                                                        run_time=run_time, 
                                                        voiceover_text=voiceover_text,
                                                        match_shape=match_shape)
   
    """
    point_text is object returned from either math_text or text
    target_model - is expected to be in hidden state and will be drawn after move is completed
    Sort of reverse of move_text_to_text_effect 
    """     
    def move_text_to_point_effect(self, text_model, target_model_point, run_time=1, 
                          voiceover_text=None, remove_on_completion=False)->EffectCommand:
        return self.text_animator.move_text_to_point_effect(text_model=text_model,
                                                      target_model_point=target_model_point, 
                                                      run_time=run_time, 
                                                      voiceover_text=voiceover_text,
                                                      remove_on_completion=remove_on_completion)
    """
    Useful when you want to rearrange math equations.
    Example 1:
    source_model = graph_sheet.math_text(["a^2", "+", "b^2", "=", "c^2"], no_animate=True).to_corner(UP+LEFT)
    target_terms = ["a^2", "=", "c^2", "-", "b^2"]
    effect = graph_sheet.text_arrangement_effect(source_model, target_terms)
    graph_sheet.play_effect(effect)
    
    Example 2:
    sine_formula = graph_sheet.math_text([ r'\sin(A)', r'=', r'\frac{h}{c}'])
    target_terms = [r'h', r'=', r'\sin(A) \cdot c']
    effect = graph_sheet.text_arrangement_effect(sine_formula, target_terms)
    graph_sheet.play_effect(effect)
    """
    def text_arrangement_effect(self, source_model, target_terms, key_map={},
                                target_scale=1,
                                run_time=2, voiceover_text=None)->EffectCommand:
        return self.text_animator.text_arrangement_effect(
            source_model=source_model, 
            target_terms=target_terms,   
            key_map=key_map,
            target_scale=target_scale,
            run_time=run_time, 
            voiceover_text=voiceover_text)
    
    """
    Say you have some idenity. You call partial_text method(give 
    thw whole text, but upto index argument will determine the partial text).
    The upto index generally is the lhs of the identity equation.    
    You want to replace the rhs part by part by calling the effect multiple times.
    
    """    
    def replace_text_effect(self, model_text, from_parts_indexes, to_part_indexes, 
                           text_items_to_fade_in=[], run_time=2, voiceover_text=None)->EffectCommand:
        return self.text_animator.replace_text_effect(model_text, from_parts_indexes, to_part_indexes, 
                                                     text_items_to_fade_in = text_items_to_fade_in, run_time = run_time, 
                                                     voiceover_text=voiceover_text) 
        
    def reveal_text_effect(self, model_text, 
                           reveal_from_index, run_time=2, voiceover_text=None)->EffectCommand: 
        return self.text_animator.reveal_text_effect(model_text, 
                                                     reveal_from_index = reveal_from_index, run_time = run_time, 
                                                     voiceover_text=voiceover_text)      
    
    def surround_text_effect(self, text_parts, color=GREEN, buffer_factor=0.1, run_time=2,
                             voiceover_text=None, remove_on_completion=True)->EffectCommand:
        if isinstance(text_parts, list):
            return self.text_animator.surround_text_effect(text_parts, 
                                                           color=color, 
                                                           buffer_factor=buffer_factor, 
                                                           run_time=run_time, 
                                                           voiceover_text=voiceover_text, 
                                                           remove_on_completion=remove_on_completion)   
        else:
            return self.text_animator.surround_text_effect([text_parts], 
                                                           color=color, 
                                                           buffer_factor=buffer_factor, 
                                                           run_time=run_time, 
                                                           voiceover_text=voiceover_text, 
                                                           remove_on_completion=remove_on_completion)   
    
    def circumscribe_text_effect(self, text_parts, color=GREEN, buffer_factor=0.1, run_time=2,
                                 voiceover_text=None, remove_on_completion=True)->EffectCommand:
        if isinstance(text_parts, list):
            return self.text_animator.circumscribe_text(text_parts, 
                                                        color=color, 
                                                        buffer_factor=buffer_factor, 
                                                        run_time=run_time, 
                                                        voiceover_text=voiceover_text, 
                                                        remove_on_completion=remove_on_completion)   
        else:
            return self.text_animator.circumscribe_text([text_parts], 
                                                        color=color, 
                                                        buffer_factor=buffer_factor, 
                                                        run_time=run_time, 
                                                        voiceover_text=voiceover_text, 
                                                        remove_on_completion=remove_on_completion)   
            
    """
    Useful when we want to move a Text
    object to a graph sheet point and then draw a line to that point
   
    """            
    def play_coordinate_move_then_draw(self, point_text, target_point,
                                    model_to_draw, color=BLUE, run_time=1, voiceover_text=None):
        return self.text_animator.play_coordinate_move_then_draw(point_text, target_point, model_to_draw, color=color, run_time=run_time, voiceover_text=voiceover_text)
    
    def draw_effect(self, model_object:BaseModel, run_time=2, voiceover_text=None, 
                    remove_on_completion=False)->EffectCommand:
        return model_object.draw_effect(run_time, voiceover_text, remove_on_completion)
    
    def fade_in_effect(self, model_object:BaseModel, run_time=2,
                        voiceover_text=None, remove_on_completion=True)->EffectCommand:
        return model_object.fade_in_effect(run_time, voiceover_text, remove_on_completion)
    
    def transform_effect(self, source_model, target_model, 
                         run_time=2, voiceover_text=None):
        return self.text_animator.transform_effect(source_model, target_model,
                                        run_time=run_time, 
                                       voiceover_text=voiceover_text)
    
    def compose_effect(self, *effects, voiceover_text=None)->ComposeEffectCommand:
        return ComposeEffectCommand(*effects, 
                                    scene=self.scene, 
                                    graph_sheet=self,   
                                    voiceover_text=voiceover_text)
    
    def pause_effect(self, run_time=1)->EffectCommand:
        def do_func():
            return Wait(run_time=run_time)
        def undo_func():
            pass
        pause_note = f"<break time='{run_time}s'/>"
        return EffectCommand(do_func, undo_func, 
                            scene=self.scene, 
                            graph_sheet=self, 
                            run_time=run_time, 
                            voiceover_text=pause_note)
    
    def undo_effect(self, effect_command, run_time=1, voiceover_text=None)->EffectCommand:
        def do_func():
            return effect_command.clear()
        def undo_func():
            pass
        if voiceover_text is not None:  
            return EffectCommand(do_func, undo_func, 
                                 scene=self.scene, 
                                 graph_sheet=self, run_time=run_time, voiceover_text=voiceover_text)
        else:
            undo_note = f"<break time='{run_time}s'/>"   
            return EffectCommand(do_func, undo_func, 
                                 scene=self.scene, graph_sheet=self, run_time=run_time, voiceover_text=undo_note)
    
    def fill_region_effect(self, model_points:list[ModelPoint] , 
                           stroke_width=DEFAULT_STROKE_WIDTH*2,
                           color=BLUE, fill_opacity=0.3, run_time=2, 
                           voiceover_text=None, remove_on_completion=True)->EffectCommand:
             
        object_render = None
       
        def do_func():
            nonlocal object_render
            ui_points = [self.geo_mapper.model_point_to_ui_point(model_point) for model_point in model_points]  
            object_render =  Polygon(*ui_points, color=color, fill_opacity=fill_opacity)
            object_render.set_z_index(1000)
            return DrawBorderThenFill(object_render, stroke_width=stroke_width)
        
        def undo_func():
            return FadeOut(object_render)
        
        effect_command = EffectCommand(do_func, undo_func, 
                                       scene=self.scene,    
                                       graph_sheet=self, 
                                       run_time=run_time, 
                                       voiceover_text=voiceover_text, 
                                       remove_on_completion=remove_on_completion)
        return effect_command
  
   
    def color_effect(self, model_object:BaseModel, color=BLUE, scale_factor=1.2, run_time=5, 
                     voiceover_text=None,   remove_on_completion=True)->EffectCommand:
        return model_object.color_effect(color, scale_factor, run_time, voiceover_text, remove_on_completion)
    
    def stroke_effect(self, model_object:BaseModel, stroke_width=10, run_time=5, 
                      voiceover_text=None, remove_on_completion=True)->EffectCommand:   
        return model_object.stroke_effect(stroke_width, run_time, voiceover_text, remove_on_completion)
    
    def scale_effect(self, model_object:BaseModel, scale_factor=1.2, run_time=5, 
                      voiceover_text=None, remove_on_completion=True)->EffectCommand:   
        return model_object.scale_effect(scale_factor, run_time, voiceover_text, remove_on_completion)
    
    """
    Say you have an object and you want to move it to the target object, use this effect.
    Generally the moved object and target object will be of same type and dimensions.
    """
    def move_to_target_effect(self, model_object:BaseModel, target_object:BaseModel, run_time=5, voiceover_text=None, 
                              remove_on_completion=True)->EffectCommand:
        def do_func():
            cloned_source_object = model_object.shape_to_trace().copy()
            cloned_source_object.generate_target()
            translation_vector = target_object.shape_to_trace().get_center() - cloned_source_object.get_center()
            cloned_source_object.target.shift(translation_vector)
            return MoveToTarget(cloned_source_object)

        def undo_func():
            pass
        
        return EffectCommand(do_func, undo_func, 
                             scene=self.scene, 
                             graph_sheet=self, 
                             run_time=run_time, 
                             voiceover_text=voiceover_text, 
                             remove_on_completion=remove_on_completion)
    
    def arrow_effect(self, from_model, to_model, color=BLUE, 
                     from_buff=0.3*RIGHT, to_buff=0.3*LEFT,
                     run_time=2, 
                     voiceover_text=None, remove_on_completion=True):
        return self.arrow_animator.arrow_effect(from_model, to_model,
                                                color=color,
                                                from_buff=from_buff,
                                                to_buff=to_buff,    
                                                run_time=run_time, 
                                                voiceover_text=voiceover_text, 
                                                remove_on_completion=remove_on_completion)
        
    
    def surrounding_effect(self, model_object:BaseModel, color=BLUE, buffer=0.1, run_time=5, 
                           voiceover_text=None, remove_on_completion=True)->EffectCommand:
        return model_object.surrounding_effect(color, buffer, run_time, voiceover_text, remove_on_completion)
    
    def indicate_effect(self, model_object:BaseModel, color=BLUE, scale_factor=1.2, run_time=5,
                        voiceover_text=None, remove_on_completion=True)->EffectCommand:
        return model_object.indicate_effect(color, scale_factor, run_time, voiceover_text, remove_on_completion  )
    
    def circumscribe_effect(self, model_object:BaseModel, color=BLUE, run_time=5, 
                            voiceover_text=None, remove_on_completion=True)->EffectCommand:
        return model_object.circumscribe_effect(color, run_time, voiceover_text, remove_on_completion)
    
    def flash_effect(self, model_object:BaseModel, color=BLUE, run_time=5, 
                     voiceover_text=None, remove_on_completion=True)->EffectCommand:    
        return model_object.flash_effect(color, run_time, voiceover_text, remove_on_completion)
    
    def trace_effect(self, model_object:BaseModel, color=RED, run_time=5, 
                     voiceover_text=None, remove_on_completion=True)->EffectCommand:
        return model_object.trace_effect(color, run_time, voiceover_text, remove_on_completion) 
    
    def un_cover_effect(self, model_object:BaseModel, run_time=2, voiceover_text=None, 
                        remove_on_completion=True)->EffectCommand:
        return model_object.un_cover_effect(run_time, voiceover_text, remove_on_completion)
    
    def play_parallel_effects(self, *effects, run_time=3, voiceover_text=None):
        if len(effects) == 0: 
            return  
        self.effect_command_manager.play_parallel(*effects, run_time=run_time, voiceover_text=voiceover_text)
        
    
    def play_effect(self, effect, run_time=2, voiceover_text=None):  
        available_voiceover_text = voiceover_text if voiceover_text is not None else effect.voiceover_text
        self.effect_command_manager.play_parallel(effect, voiceover_text=available_voiceover_text, run_time=run_time)
       
        
    def play_sequence_effects(self, *effects):
        if len(effects) == 0: 
            return
        self.effect_command_manager.play_sequence(*effects)  
        
    def play_with_voice_fragments(self, *effects):
        if len(effects) == 0: 
            return
        self.effect_command_manager.play_with_voice_fragments(*effects)
    
    def clear_effect(self, *effects):
        if len(effects) == 0: 
            return
        self.effect_command_manager.clear(*effects) 
        
    def clear_effects(self, *effects):
        if len(effects) == 0: 
            return
        self.effect_command_manager.clear(*effects)  
        
    def pause_text(self, time=1):
        return f"<break time='{time}s'/>"    
        
    def calculate_numerical_property(self, property:str, models:list[BaseModel]):
        return self.geo_property_calculator.calculate_numerical_property(property, models)    
    
    """"
    Converts a string to a MathTex object
    Examples:
    string_to_math_tex("x^2") -> MathTex object
    string_to_math_tex("sin(x)") -> MathTex object
    string_to_math_tex("3x+2") -> MathTex object
    
    """
    def string_to_math_tex(self, string:str):
        sympy_expression = sympy.sympify(string)
        latex_expression = sympy.latex(sympy_expression)
        return MathTex(latex_expression)    
    
    def evaluate_symbolic_expression(self, expression, subs_dict={}):
         eval_result = FunctionUtils.evaulatable_sympy_expression(expression, subs_dict=subs_dict)
         return sympy.latex(eval_result)
     
    def evaluate_numeric_expression(self, expression, subs_dict={}, precision=1):
        eval_result = FunctionUtils.evaluate_sympy_expression(expression, subs_dict=subs_dict, precision=precision)
        return eval_result
    
    def point_index(self, model, index)->ModelPoint:
        model_point = model.point_index(index)
        return model_point  
    
    def point_at_ratio(self, model, ratio_parameter)->ModelPoint:
        ratio_parameter = self._parameter_from_input(ratio_parameter)
        model_point = ModelPoint.point_at(model, ratio_parameter)
        return model_point   
    
    """
    Use this to get the normal direction of a line segment, vector or between two points
    """
    def get_normal_direction(self, pt1_tuple_or_model, pt2_tuple_or_model, direction:np.array)->np.array:
        model_pt1 = self.geo_mapper.model_point_from_ui_point(pt1_tuple_or_model)
        model_pt2 = self.geo_mapper.model_point_from_ui_point(pt2_tuple_or_model)
        numpy_pt1 = model_pt1.numpy()
        numpy_pt2 = model_pt2.numpy()
        direction = numpy_pt2 - numpy_pt1
        normalized_direction = normalize(direction)
        normal_direction = rotate_vector(normalized_direction, PI/2)
        return normal_direction
    
    def scroll(self, direction:np.array=UP, run_time=2, voiceover_text=None):
        if voiceover_text is not None:
            with self.scene.voiceover(voiceover_text) as tracker:  
                self.play(self.shift.animate(direction), run_time=run_time, 
                          voiceover_text=voiceover_text)
        else:
            self.play(self.shift.animate(direction), run_time=run_time)
    
    
    
                                              
     