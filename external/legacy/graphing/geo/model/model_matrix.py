from graphing.geo.model.base_model import BaseModel
from manim import *

from graphing.geo.model.model_part import ModelPart
"""
array is a list of lists
"""
class ModelMatrix(BaseModel):
    def __init__(self, array):
        super().__init__()
        self.array = array
        
    def item(self, row_index, column_index=None):
        ui_part = self.ui_part.item(row_index, column_index)
        return ModelPart(ui_part, ui_part.graphsheet, ui_part.geo_mapper, ui_part.scene, item_row=row_index, item_col=column_index)
   
        
        