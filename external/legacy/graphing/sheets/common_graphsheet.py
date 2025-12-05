from manim import *
from typing import Optional, Tuple, List

from graphing.geo.model.base_model import BaseModel
from graphing.geo.model.model_line import ModelLine
from graphing.geo.model.model_parameter import ModelParameter
from graphing.geo.model.model_plot import ModelPlot
from graphing.geo.model.model_point import ModelPoint
from graphing.geo.model.model_vector import ModelVector
from graphing.geo.ui.ui_style_props import UIStyleProps
from manim import ORIGIN
CENTER = ORIGIN

class CommonGraphSheet(VGroup):
    def __init__(self, scene, **kwargs):
        super().__init__(**kwargs)
        self.scene = scene
        self.model_to_ui = {}
        self.ui_to_model = {}
        
    def add_default_models(self):
        self.x_axis_model_line = ModelLine.from_points(ModelPoint(0,0,0), ModelPoint(1,0,0))
        self.y_axis_model_line = ModelLine.from_points(ModelPoint(0,0,0), ModelPoint(0,1,0)) 
        self.z_axis_model_line = ModelLine.from_points(ModelPoint(0,0,0), ModelPoint(0,0,1))
        
    def x_axis_line(self) -> ModelLine:   
        return self.x_axis_model_line
 
    def y_axis_line(self) -> ModelLine:
        return self.y_axis_model_line
    
    def z_axis_line(self) -> ModelLine:
        return self.z_axis_model_line
        
    def wait(self, time):
        self.scene.wait(time)
        
    def _from_property(self, reference_model: BaseModel, property_name: str):
        try:
            return getattr(reference_model, property_name)
        except AttributeError:
            print(f"Property '{property_name}' not found in {reference_model} model")
            return None

    def _get_ui_object(self, model_object: BaseModel):
        if model_object in self.model_to_ui:
            return self.model_to_ui[model_object]
        raise ValueError(f"No UI object found for model object: {model_object}")

    def _create_style_props(self, color, fill_color, fill_opacity, default_style, 
                           dashed=False, scale_factor=1, stroke_width=DEFAULT_STROKE_WIDTH) -> UIStyleProps:
        return UIStyleProps(
            color=color or default_style.color,
            fill_color=fill_color or default_style.fill_color,
            fill_opacity=fill_opacity if fill_opacity is not None else default_style.fill_opacity,
            dashed=dashed or default_style.dashed,
            scale_factor=scale_factor,
            stroke_width=stroke_width
        )

    def set_dynamic(self, model_object: BaseModel):
        if model_object in self.model_to_ui:
            self.model_to_ui[model_object].set_dynamic()

    def make_dynamic(self, *model_objects: BaseModel):
        for model_object in model_objects:
            self.set_dynamic(model_object)

    def play(self, *args, subcaption=None, subcaption_duration=None, 
             subcaption_offset=0, **kwargs):
        self.scene.play(*args, 
                       subcaption=subcaption, 
                       subcaption_duration=subcaption_duration,
                       subcaption_offset=subcaption_offset,
                       **kwargs)

    def play_create(self, mobject, voiceover_text=None, **kwargs):
        if hasattr(mobject, "custom_create_animation"):
            if voiceover_text:
                with self.scene.voiceover(voiceover_text) as tracker:
                    self.scene.play(mobject.custom_create_animation(**kwargs), 
                                  run_time=tracker.duration)
            else:
                self.scene.play(mobject.custom_create_animation(**kwargs))
        else:   
            self.scene.play(Create(mobject, **kwargs))

    def direct_add(self, object):
        self.scene.add(object)

    def play_write(self, mobject, voiceover_text=None, **kwargs):
        if hasattr(mobject, "custom_create_animation"):
            if voiceover_text:
                with self.scene.voiceover(voiceover_text) as tracker:
                    self.scene.play(mobject.custom_create_animation(**kwargs), 
                                  run_time=tracker.duration)
            else:
                self.scene.play(mobject.custom_create_animation(**kwargs))
        else:
            if voiceover_text:
                with self.scene.voiceover(voiceover_text) as tracker:
                    self.scene.play(Write(mobject, **kwargs), run_time=tracker.duration)
            else:
                self.scene.play(Write(mobject, **kwargs))

    def _set_opacity(self, mobject, opacity):
        actual_m_object = mobject.view() if isinstance(mobject, BaseModel) else mobject
        if hasattr(actual_m_object, "set_opacity"):
            actual_m_object.set_opacity(opacity)
     
    def _set_fill_opacity(self, mobject, opacity):
        actual_m_object = mobject.view() if isinstance(mobject, BaseModel) else mobject
        if isinstance(actual_m_object, ImageMobject):
            actual_m_object.set_opacity(opacity)
        elif hasattr(actual_m_object, "set_fill"):
            actual_m_object.set_fill(opacity=opacity)
            
            
    def _play_fade_in(self, mobject, 
                      voiceover_text=None, 
                      fill_opacity=0.3,
                      **kwargs):
        if voiceover_text:
            with self.scene.voiceover(voiceover_text) as tracker:
                if isinstance(mobject, BaseModel):
                    self._set_opacity(mobject, 1)
                    self._set_fill_opacity(mobject, self._given_fill_opacity(mobject))
                    self.scene.play(FadeIn(mobject.view(), **kwargs), run_time=tracker.duration)
                else:
                    self._set_opacity(mobject, 1)
                    self._set_fill_opacity(mobject, fill_opacity)
                    self.scene.play(FadeIn(mobject, **kwargs), run_time=tracker.duration)
        else:
            if isinstance(mobject, BaseModel):
                self._set_opacity(mobject, 1)
                self._set_fill_opacity(mobject, self._given_fill_opacity(mobject))
                self.scene.play(FadeIn(mobject.view(), **kwargs))
            else:
                self._set_opacity(mobject, 1)
                self._set_fill_opacity(mobject, fill_opacity)
                self.scene.play(FadeIn(mobject, **kwargs))
                
    def _given_fill_opacity(self, mobject):
        if isinstance(mobject, BaseModel):  
            return mobject.fill_opacity
        else:
            return 1

    def _play_fade_out(self, mobject, voiceover_text=None, **kwargs):
        if voiceover_text:
            with self.scene.voiceover(voiceover_text) as tracker:
                if isinstance(mobject, BaseModel):
                    self.scene.play(FadeOut(mobject.view(), **kwargs), run_time=tracker.duration)
                else:
                    self.scene.play(FadeOut(mobject, **kwargs), run_time=tracker.duration)
        else:
            if isinstance(mobject, BaseModel):
                self.scene.play(FadeOut(mobject.view(), **kwargs))
            else:
                self.scene.play(FadeOut(mobject, **kwargs))  
                
                
    def _play_animation(self, animation, run_time=2, voiceover_text=None):            
        if voiceover_text:
            with self.scene.voiceover(voiceover_text) as tracker:
                self.scene.play(animation, run_time=tracker.duration)
        else:
            self.scene.play(animation, run_time=run_time)

   

    def show(self, model_object: BaseModel):
        if model_object in self.model_to_ui:
            fill_opacity = self._given_fill_opacity(model_object)
            self.model_to_ui[model_object].view().set_opacity(1)
            self.model_to_ui[model_object].view().set_fill(opacity=fill_opacity)

    def hide(self, *model_objects: BaseModel):
        for model_object in model_objects:
            if model_object in self.model_to_ui:
                self.model_to_ui[model_object].view().set_opacity(0)

    def _register_object(self, model_object: BaseModel, ui_object, 
                        no_animate: bool = False, 
                        voiceover_text: Optional[str] = None) -> BaseModel:
        if ui_object.view() is not None:
            if no_animate:
                self.direct_add(ui_object.view())
            else:
                self.play_write(ui_object.view(), voiceover_text=voiceover_text)
        return self._do_register_object(model_object, ui_object)
    
  
    def _register_group(self, model_object: BaseModel, ui_object) -> BaseModel:
        return self._register_object(model_object, ui_object, no_animate=True)
    
    def _register_in_background(self, model_object: BaseModel, ui_object,
                               no_animate: bool = False, 
                               voiceover_text: Optional[str] = None) -> BaseModel:
        if no_animate:
            self.direct_add(ui_object.view())
            self.scene.bring_to_back(ui_object.view())
        else:
            self.direct_add(ui_object.view().set_opacity(0))
            self.scene.bring_to_back(ui_object.view())
            self._play_fade_in(ui_object.view(), 
                               fill_opacity=ui_object.fill_opacity,  
                               voiceover_text=voiceover_text)
        return self._do_register_object(model_object, ui_object)    

    def _register_image(self, model_object: BaseModel, ui_object,
                       no_animate: bool = False, 
                       voiceover_text: Optional[str] = None) -> BaseModel:
        if no_animate:
            self.direct_add(ui_object.view())
        else:
            self._play_fade_in(ui_object.view(), 
                                fill_opacity=ui_object.fill_opacity,  
                               voiceover_text=voiceover_text)
        return self._do_register_object(model_object, ui_object)

    def _register_text(self, model_object: BaseModel, ui_object,
                      no_animate: bool = False, 
                      voiceover_text: Optional[str] = None, partial=False) -> BaseModel:
        view = ui_object.view() if not partial else ui_object.partial_view()
        if no_animate:
            self.direct_add(view)
        else:
            self._play_fade_in(view, 
                               fill_opacity=ui_object.fill_opacity, 
                               voiceover_text=voiceover_text)
        return self._do_register_object(model_object, ui_object)

    def _register_arrow(self, model_object: BaseModel, ui_object,
                       no_animate: bool = False, 
                       voiceover_text: Optional[str] = None) -> BaseModel:
        if no_animate:
            self.direct_add(ui_object.view())
        else:
            self._play_fade_in(ui_object.view(), 
                               fill_opacity=ui_object.fill_opacity, 
                               voiceover_text=voiceover_text)
        return self._do_register_object(model_object, ui_object)
    
    def _register_trace(self, model_object: BaseModel, ui_object,
                       no_animate: bool = False, 
                       voiceover_text: Optional[str] = None) -> BaseModel:
        if no_animate:
            self.direct_add(ui_object.view())
        else:
            self.play_create(ui_object.view(), voiceover_text=voiceover_text)
        return self._do_register_object(model_object, ui_object)    

    def _do_register_object(self, model_object: BaseModel, ui_object) -> BaseModel:
        self.model_to_ui[model_object] = ui_object
        self.ui_to_model[ui_object] = model_object
        model_object.set_delegate(
            graphsheet=self,
            geo_mapper=self.geo_mapper,
            scene=self.scene,
            ui_part=ui_object
        )
        ui_object.set_delegate(
            graphsheet=self,
            geo_mapper=self.geo_mapper,
            scene=self.scene
        )
        return model_object


    def _range_parameters_from_input(self, parameters):
        model_parameters = []
        for parameter in parameters:
            if isinstance(parameter, (float, int)):
                model_parameters.append(ModelParameter(self.scene, parameter))
            elif isinstance(parameter, ModelParameter):
                model_parameters.append(parameter)
            else:
                raise ValueError(f"Invalid parameter: {parameter}")
        return model_parameters

 

    def _parameter_from_input(self, parameter) -> ModelParameter:
        if isinstance(parameter, (float, int)):
            return ModelParameter(self.scene, parameter)
        if isinstance(parameter, ModelParameter):
            return parameter    
        raise ValueError(f"Invalid parameter: {parameter}")

    def _parameter_dict_from_input(self, substitutions: dict) -> dict:
        return {name: self._parameter_from_input(value) for name, value in substitutions.items()}

    def _point_from_input(self, point) -> ModelPoint:
        if isinstance(point, ModelPoint):
            return point
        if isinstance(point, tuple):
            if len(point) == 2:
                return ModelPoint(point[0], point[1], 0)
            elif len(point) == 3:
                return ModelPoint(*point)
            raise ValueError("Point tuple must have 2 or 3 components")
        if isinstance(point, np.ndarray):
            if len(point) == 2:
                return ModelPoint(point[0], point[1], 0)
            elif len(point) == 3:
                return ModelPoint(*point)
            raise ValueError("Point array must have 2 or 3 components")
        if isinstance(point, dict) and 'x' in point and 'y' in point:
            return ModelPoint(point['x'], point['y'])
        raise ValueError(f"Invalid point input: {point}")

    def _line_from_input(self, line) -> ModelLine:
        if isinstance(line, ModelLine):
            return line
        if isinstance(line, tuple):
            a = ModelPoint.from_x_y(line[0], line[1])
            b = ModelPoint.from_x_y(line[2], line[3])
            return ModelLine(a.x, a.y, b.x, b.y)
        raise ValueError(f"Invalid line input: {line}")

    def _translate_vector_from_input(self, vector) -> ModelVector:
        if isinstance(vector, ModelVector):
            return vector
        if isinstance(vector, np.ndarray):
            if len(vector) == 2:
                a = ModelPoint.from_x_y(vector[0], vector[1], 0)
                return ModelVector.position_vector(a)
            elif len(vector) == 3:
                a = ModelPoint(vector[0], vector[1], vector[2])
                return ModelVector.position_vector(a)
            raise ValueError("Vector array must have 2 or 3 components")
        if isinstance(vector, tuple):
            if len(vector) == 3:
                a = ModelPoint(vector[0], vector[1], vector[2])
                return ModelVector.position_vector(a)
            elif len(vector) == 2:
                a = ModelPoint(vector[0], vector[1], 0)
                return ModelVector.position_vector(a)
            raise ValueError("Vector tuple must have 2 or 3 components")
        raise ValueError(f"Invalid vector input: {vector}")

    def _vector_from_input(self, vector) -> ModelVector:
        return self._translate_vector_from_input(vector)

    def point_at_ratio(self, model: BaseModel, ratio_parameter) -> ModelPoint:
        ratio_parameter = self._parameter_from_input(ratio_parameter)
        return ModelPoint.point_at(model, ratio_parameter)
