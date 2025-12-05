from graphing.helpers.complex_latex import ComplexLatex
from .base_model import BaseModel
import math
import numpy as np
import sympy as sp
from manim import *
class ModelPoint(BaseModel):
    def __init__(self, x, y, z=0):
        super().__init__()
        self._x = x
        self._y = y
        self._z = z
        
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self)->str:
        return f"ModelPoint({self.x}, {self.y}, {self.z})"
    
    def move_right(self, x_offset)->'ModelPoint':
        return ModelPoint(self.x + x_offset, self.y, self.z)
    
    def move_left(self, x_offset)->'ModelPoint':
        return ModelPoint(self.x - x_offset, self.y, self.z)
    
    def move_up(self, y_offset)->'ModelPoint'   :
        return ModelPoint(self.x, self.y + y_offset, self.z)
    
    def move_down(self, y_offset)->'ModelPoint':
        return ModelPoint(self.x, self.y - y_offset, self.z)
    
    def move_in(self, z_offset)->'ModelPoint':
        return ModelPoint(self.x, self.y, self.z + z_offset)    
    
    def move_x_y(self, x_offset, y_offset)->'ModelPoint':
        return ModelPoint(self.x + x_offset, self.y + y_offset, self.z) 
    
    def move_by_angle(self, angle_in_degrees, distance)->'ModelPoint':
        angle_in_radians = math.radians(angle_in_degrees)
        return ModelPoint(self.x + distance * math.cos(angle_in_radians), self.y + distance * math.sin(angle_in_radians), self.z)   
    
    
    def animate_translate_to(self, target_point, run_time=2, voiceover_text=None)->'ModelPoint':
        self.graphsheet.translate_to(self, target_point, run_time, voiceover_text)
    
    def animate_translate_by_vector(self, vector, run_time=2, voiceover_text=None)->'ModelPoint':
        self.graphsheet.translate_by_vector(self, vector, run_time, voiceover_text)
    
    def animate_rotate_by_angle(self, angle_in_degrees, about_point=ORIGIN, run_time=2, voiceover_text=None)->'ModelPoint':
        self.graphsheet.rotate_point_by_angle(self, angle_in_degrees, about_point, run_time, voiceover_text)
    
    def animate_rotate_to(self, target_point, run_time=2, voiceover_text=None)->'ModelPoint':
        self.graphsheet.rotate_to(self, target_point, run_time, voiceover_text)
    
    """
    Move the point in the direction of the direction_vector by the distance
    direction_vector is a numpy array with two elements [x, y]   
    """
    def move_direction(self, direction_vector, distance)->'ModelPoint':
        return ModelPoint(self.x + direction_vector[0] * distance, self.y + direction_vector[1] * distance, self.z) 


    @property
    def complex_coordinate(self, as_operand=False, 
                           with_zero_terms=True, 
                           lhs = None)->str:
         complex_latex = ComplexLatex(self.x, self.y)
         if lhs is not None:
             complex_latex.set_symbol(lhs)  
         return complex_latex.to_latex(
             with_brackets=as_operand,
             with_zero_terms=with_zero_terms,
             with_symbol=lhs is not None
         )
         
    def coordinate(self, as_operand=False, 
                   precision=1,
                   lhs = None)->str:
        pts_str = f"({self.x:.{precision}f}, {self.y:.{precision}f})"   
        if lhs is not None:
            pts_str = f"{lhs} = {pts_str}"
            
        if as_operand:
            pts_str = f"({pts_str})"
        return pts_str
       
    
    def to_numpy(self)->np.array: 
        return np.array([self.x, self.y, self.z], dtype=float)
    
    
    def to_sympy(self)->sp.Point:
        return sp.Point(self.x, self.y)
        
    def set(self, x, y, z=0, notify=True):
        self._x = x
        self._y = y
        self._z = z
        if notify:
            self.notify()
    
        
    def to_x_y(self)->tuple:
        return self.x, self.y    
                      
    def point_index(self, index)->float:
        return self[index]
    
    def get_all_points(self)->list['ModelPoint']:
        return [self]
        
    @property
    def x(self)->float:
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value
        self.notify()
        
    @property
    def y(self)->float:
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value
        self.notify()
    
    @property
    def z(self)->float:
        return self._z
    
    @z.setter
    def z(self, value):
        self._z = value
        self.notify()
    
    
    @staticmethod    
    def from_array(point_array)->'ModelPoint':
        if len(point_array) == 2:
            return ModelPoint(point_array[0], point_array[1])
        elif len(point_array) == 3:
            return ModelPoint(point_array[0], point_array[1], point_array[2])
        else:
            raise ValueError("Invalid array length")
    
    @staticmethod
    def from_sym_point(point)->'ModelPoint':
        return ModelPoint(point.x, point.y)
    
    @staticmethod    
    def from_sym_points(points)->list['ModelPoint']:
        return [ModelPoint(point.x, point.y) for point in points]    
    
    @staticmethod   
    def from_x_y(x, y)->'ModelPoint':
        return ModelPoint(x, y)
    
    def to_x_y(self)->tuple:
        return self.x, self.y
    
    def to_numpy_array(self)->np.array:
        return np.array([self.x, self.y, self.z])   
    
    def to_x_y_z(self)->tuple:
        return self.x, self.y, self.z
    
    def from_x_y_z(self, x, y, z)->'ModelPoint':
        return ModelPoint(x, y, z)  
    
    def translate(self, model_vector)->'ModelPoint':
        return ModelPoint(self.x + model_vector.x, self.y + model_vector.y, self.z + model_vector.z)
    
    def scale(self, scale_factor):
        return ModelPoint(self.x * scale_factor, self.y * scale_factor, self.z * scale_factor)
    
    def rotate(self, angle_in_degrees, about=ORIGIN)->'ModelPoint':
        dot = Dot(np.array([self.x, self.y, self.z]))
        angle_in_radians = math.radians(angle_in_degrees)
        new_point = rotate_vector(dot.get_center(), angle=angle_in_radians)
        dot.move_to(new_point)  
        rotated_point = dot.get_center()
        return ModelPoint(rotated_point[0], rotated_point[1], rotated_point[2])
    
    
    @staticmethod
    def next_to_model(model:BaseModel, off_set=ORIGIN)->'ModelPoint':
        new_point = ModelPoint(0,0, 0)
        def create():
            nonlocal new_point
            new_x = model.x + off_set[0]
            new_y = model.y + off_set[1]
            new_z = model.z + off_set[2]
            new_point = ModelPoint(new_x, new_y, new_z)
        
        def update():
            nonlocal new_point
            new_x = model.x + off_set[0]
            new_y = model.y + off_set[1]    
            new_z = model.z + off_set[2]
            new_point.set(new_x, new_y, new_z)
        
        create()
        
        model.on_change(update)
        
        return new_point
    
    @staticmethod
    def from_polar(radius_param, theta_param)->'ModelPoint':
        model_point = None  
        
        def create():
            nonlocal model_point
            parameter_value = radius_param.get_value()
            model_point = ModelPoint(parameter_value * math.cos(theta_param.get_value()), parameter_value * math.sin(theta_param.get_value()))
            
        def update():
            nonlocal model_point
            parameter_value = radius_param.get_value()
            model_point.set(parameter_value * math.cos(theta_param.get_value()), parameter_value * math.sin(theta_param.get_value()))
            
        create()
        radius_param.on_param_change(lambda d: update())
        theta_param.on_param_change(lambda d: update())
        return model_point  
    
    @staticmethod
    def from_complex_latex(complex_latex:ComplexLatex)->'ModelPoint':
        return ModelPoint(complex_latex.real, complex_latex.imag)
    
    @staticmethod
    def point_at(model:BaseModel, ratio_parameter)->'ModelPoint':
        new_point = ModelPoint(0,0, 0)
        def create():
            nonlocal new_point
            ratio = ratio_parameter.get_value()
            np_array_pt = model.point_at(ratio)
            new_point = ModelPoint(np_array_pt[0], np_array_pt[1], np_array_pt[2])
        
        def update():
            nonlocal new_point
            ratio = ratio_parameter.get_value()
            np_array_pt = model.point_at(ratio)
            new_point.set(np_array_pt[0], np_array_pt[1], np_array_pt[2])
        
        create()
        
        model.on_change(update)
        ratio_parameter.param_on_change(lambda d: update())
        return new_point
    
    @staticmethod
    def synch_translate(modelPoint, vector)->'ModelPoint':
         model_point = None
         
         def create():
             nonlocal model_point
             model_point = ModelPoint(modelPoint.x + vector.x, modelPoint.y + vector.y, modelPoint.z + vector.z)
             
         def update():
             nonlocal model_point
             model_point.set(modelPoint.x + vector.x, modelPoint.y + vector.y, modelPoint.z + vector.z)
             
         create()
         modelPoint.on_change(update)
         return model_point
        
        
    @staticmethod
    def rotate_about_point(model_point, angle_in_degrees_param, about_point):
        new_point = ModelPoint(0,0, 0)
        
        def create():
            nonlocal new_point
            new_point = model_point.rotate(angle_in_degrees_param.get_value(), about_point)
            
        def update():
            nonlocal new_point
            updated_point = model_point.rotate(angle_in_degrees_param.get_value(), about_point)
            new_point.set(updated_point.x, updated_point.y, updated_point.z)
            
        create()
        model_point.on_change(update)
        about_point.on_change(update)   
        angle_in_degrees_param.on_param_change(lambda d: update())
        return new_point
        
        
    @staticmethod
    def from_function(parameter_model, x_lambda_function, y_lambda_function):
        model_point = ModelPoint(0,0,0)
        
        def create():
            nonlocal model_point
            x_value = x_lambda_function(parameter_model.get_value())
            y_value = y_lambda_function(parameter_model.get_value())
            model_point = ModelPoint(x_value, y_value)
            
        def update():
            nonlocal model_point
            x_value = x_lambda_function(parameter_model.get_value())
            y_value = y_lambda_function(parameter_model.get_value())
            model_point.set(x_value, y_value)
            
        create()
        parameter_model.on_param_change(lambda d: update())   
        return model_point
    
    
   
    
    
    @staticmethod
    def from_property(reference_model, property_name):
        model_point = None
        
        def computation():
            try:
                return getattr(reference_model, property_name)
            except AttributeError:
             print(f"Property '{property_name }' not found in {reference_model} model")
             return None   
        
        def create():
            nonlocal model_point
            value = computation()
            model_point = ModelPoint(value.x, value.y, value.z)
            
        def update():
            nonlocal model_point
            value = computation()
            model_point.set(value.x, value.y, value.z)
            
        create()
        reference_model.on_change(update)
        return model_point
            
         
      
    @staticmethod
    def _get_x_value(reference_model, x_direction, x_offset):
        ui_part = reference_model.ui_part
        if np.array_equal(x_direction, LEFT):
            return ui_part.get_left().x + x_offset 
        elif np.array_equal(x_direction, RIGHT):
            return ui_part.get_right().x + x_offset
        elif np.array_equal(x_direction, ORIGIN):
            return ui_part.get_center().x + x_offset
        else:
            raise ValueError("Invalid x_direction")
    
    @staticmethod
    def _get_y_value(reference_model, y_direction, y_offset):
        ui_part = reference_model.ui_part
        if np.array_equal(y_direction, ORIGIN):
            return ui_part.get_center().y + y_offset
        elif np.array_equal(y_direction, UP):
            return ui_part.get_top().y + y_offset
        elif np.array_equal(y_direction, DOWN):
            return ui_part.get_bottom().y + y_offset
        else:
            raise ValueError("Invalid y_direction")
        
        
        
        
   