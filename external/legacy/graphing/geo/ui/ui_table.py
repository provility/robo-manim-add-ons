from manim import *
from graphing.geo.model.model_table import ModelTable
from graphing.geo.ui.base_ui import BaseUI
from graphing.geo.ui.ui_part import UIPart
from graphing.geo.ui.ui_style_props import UIStyleProps


class UITable(BaseUI):
    def __init__(self, model_table: ModelTable, style_props:UIStyleProps=UIStyleProps.plot_theme() ):
        super().__init__(style_props)
        self.model_table = model_table
        self.table_shape = None
        self.create()   
        
    def create(self):
        self.table_shape = MathTable(
            [
                self.model_table.header,
                *self.model_table.rows
            ],
            include_outer_lines=True,
            h_buff=0.4,v_buff=0.4,line_config={"stroke_width":1}
        )
        self.table_shape.set_color(self.style_props.color)
        self.table_shape.scale(0.8)
        
    def view(self):
        return self.table_shape
    
    def get_cell(self, row: int, col: int):
        entries = self.table_shape.get_entries()
        return entries[row * len(self.model_table.header) + col]
    
    def get_row(self, row: int):
        return VGroup(*[self.get_cell(row, col) for col in range(len(self.model_table.header))])

    def get_col(self, col: int):
        return VGroup(*[self.get_cell(row, col) for row in range(len(self.model_table.rows) + 1)])  # +1 for header
    
    def _element(self, row_index, column_index):
        if row_index is not None and column_index is not None:
           return self.get_cell(row_index, column_index)
        if row_index is not None:
            return self.get_row(row_index)
        if column_index is not None:
            return self.get_col(column_index)   
    
    def item(self, row_index, column_index=None):
        element = self._element(row_index, column_index)
        ui_part = UIPart(element, self.graphsheet, self.geo_mapper, self.scene, style_props=self.style_props)
        return ui_part
       
    

   

