from graphing.geo.model.base_model import BaseModel
from manim import *
import numpy as np

from graphing.geo.model.model_part import ModelPart

class ModelGroup(BaseModel):
    def __init__(self, *model_objects, direction=DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT):
        super().__init__()
        self.model_objects = [model_object for model_object in model_objects]
        self.direction = direction
        self.buff = buff   
        self.aligned_edge = aligned_edge
    
    """
    rows (int | None) The number of rows in the grid.

    cols (int | None) The number of columns in the grid.

    buff (float | tuple[float, float]) The gap between grid cells. To specify a different buffer in the horizontal and vertical directions, a tuple of two values can be given - (row, col).

    cell_alignment (Vector3D) The way each submobject is aligned in its grid cell.

    row_alignments (str | None) The vertical alignment for each row (top to bottom). Accepts the following characters: "u" - up, "c" - center, "d" - down.

    col_alignments (str | None) The horizontal alignment for each column (left to right). Accepts the following characters "l" - left, "c" - center, "r" - right.

    row_heights (Iterable[float | None] | None) Defines a list of heights for certain rows (top to bottom). If the list contains None, the corresponding row will fit its height automatically based on the highest element in that row.

    col_widths (Iterable[float | None] | None) Defines a list of widths for certain columns (left to right). If the list contains None, the corresponding column will fit its width automatically based on the widest element in that column.

    flow_order (str) The order in which submobjects fill the grid. Can be one of the following values: “rd”, “dr”, “ld”, “dl”, “ru”, “ur”, “lu”, “ul”. (“rd” -> fill rightwards then downwards)
    
    """
    
        
    def grid(self, rows=None, cols=None, buff=0.25, cell_alignment=np.array([0., 0., 0.]), row_alignments=None, col_alignments=None, row_heights=None, col_widths=None, flow_order='rd', **kwargs):
        self.ui_part.grid(rows, cols, buff, cell_alignment, row_alignments, col_alignments, row_heights, col_widths, flow_order, **kwargs)
        return self
    
    def add_item(self, model_object):
        self.model_objects.append(model_object)
        self.ui_part.add_item(model_object.ui_part)
        return self
    
    def num_objects(self):
        return len(self.model_objects)  
    
    def view_item(self, index):
        return self.model_objects[index].view()
    
    def scroll(self, direction=UP):
        self.ui_part.scroll(direction)
        return self
    
    def item(self, item_index)->ModelPart:
        ui_part = self.ui_part.item(item_index)
        return ModelPart(ui_part, ui_part.graphsheet, ui_part.geo_mapper, ui_part.scene,
                         item_row=item_index, item_col=0)