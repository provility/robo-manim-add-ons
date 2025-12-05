from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.model.model_group import ModelGroup
from graphing.geo.ui.base_ui import BaseUI
from manim import *

from graphing.geo.ui.ui_style_props import UIStyleProps

class UIGroup(BaseUI):
    def __init__(self, geo_mapper:GeoMapper, model_group:ModelGroup, existing_ui_group=None):
        super().__init__(UIStyleProps.point_theme())
        self._geo_mapper = geo_mapper
        self._model_group = model_group
        self.ui_group = existing_ui_group if existing_ui_group is not None else None   
        if self.ui_group is None:
           self.create()
        
    def create(self):
        self.ui_group = VGroup()
        for model_object in self._model_group.model_objects:
            self.ui_group.add(model_object.view())
      
        """
        This will adjust the positions of the ui objects based on the direction and buff
        """      
        self.ui_group.arrange(direction=self._model_group.direction,
                              buff=self._model_group.buff,
                              aligned_edge=self._model_group.aligned_edge)
        
    def view(self):
        return self.ui_group
    
    def add_item(self, ui_part):
        self.ui_group.add(ui_part.view())
        self.ui_group.arrange(direction=self._model_group.direction,
                              buff=self._model_group.buff,
                              aligned_edge=self._model_group.aligned_edge)  
        return self 
        
    def grid(self, rows=None, cols=None, buff=0.25, cell_alignment=np.array([0., 0., 0.]),
             row_alignments=None, col_alignments=None, row_heights=None, 
             col_widths=None, flow_order='rd', **kwargs):
        self.ui_group.arrange_in_grid(rows, cols, buff, cell_alignment, row_alignments, col_alignments, 
                                      row_heights, col_widths, flow_order, **kwargs)
        return self
        
    def scroll(self, direction=UP):
        # Create animation for smooth scrolling
        self.ui_group.generate_target()
        self.ui_group.target.shift(direction)
        self.ui_group.become(self.ui_group.target)
        return self
    
    def item(self, item_index):
       return self.ui_group[item_index]
       
