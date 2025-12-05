from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.model.model_matrix import ModelMatrix
from graphing.geo.model.model_point import ModelPoint
from graphing.geo.ui.base_ui import BaseUI
from graphing.geo.ui.ui_part import UIPart
from graphing.geo.ui.ui_style_props import UIStyleProps
from manim import *


class UIMatrix(BaseUI):
    def __init__(self, 
                 model_matrix: ModelMatrix, 
                 bracket_type:str="[",
                 style_props: UIStyleProps = UIStyleProps.ellipse_theme()):
        super().__init__(style_props)
        self.model_matrix = model_matrix
        self.bracket_type = bracket_type
        self.matrix_shape = None
        self.left_bracket = None
        self.right_bracket = None
        self._create_bracket()
        self.create()
        
    def create(self):
        array = self.model_matrix.array
        self.matrix_shape = Matrix(array, left_bracket=self.left_bracket, right_bracket=self.right_bracket)   
        self.matrix_shape.set_color(self.style_props.color)
        self.matrix_shape.scale(self.style_props.scale_factor)
        self.matrix_shape.set_z_index(100)
        
        
    def update_matrix(self, array):
        original_position = self.matrix_shape.get_center()  
        self.model_matrix.array = array 
        new_matrix_shape = Matrix(array, left_bracket=self.left_bracket, right_bracket=self.right_bracket)
        new_matrix_shape.set_color(self.style_props.color)
        new_matrix_shape.scale(self.style_props.scale_factor)
        new_matrix_shape.set_z_index(100)
        new_matrix_shape.move_to(original_position)
        # Create a Transform animation for smooth transition
        transform_animation = Transform(self.matrix_shape, new_matrix_shape)
        return transform_animation
    
    
    def view(self):
        return self.matrix_shape
    
    def _create_bracket(self):
        if self.bracket_type == "[":
            self.left_bracket = "["
            self.right_bracket = "]"
        elif self.bracket_type == "(":
            self.left_bracket = "("
            self.right_bracket = ")"
        elif self.bracket_type == "{":
            self.left_bracket = "{"
            self.right_bracket = "}"
            
    
  
    def _element(self, row_index, column_index):
        part_to_highlight = None
        if row_index is not None and column_index is not None:
            num_cols = len(self.model_matrix.array[0])
            index = row_index * num_cols + column_index
            element = self.matrix_shape.get_entries()[index] 
            return element  
        if row_index is not None:
            rows = self.matrix_shape.get_rows()
            part_to_highlight = rows[row_index]
        if column_index is not None:
            columns = self.matrix_shape.get_columns()
            part_to_highlight = columns[column_index]   
        return part_to_highlight
    
    def item(self, row_index, column_index=None):
        element = self._element(row_index, column_index)
        ui_part = UIPart(element, self.graphsheet, self.geo_mapper, self.scene, style_props=self.style_props)
        return ui_part
       
        
        
        
        
        
        