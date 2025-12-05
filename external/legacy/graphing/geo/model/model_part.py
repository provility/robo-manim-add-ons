from graphing.geo.model.base_model import BaseModel


class ModelPart(BaseModel):
    def __init__(self, ui_part, graphsheet, geo_mapper, scene, item_row=None, item_col=None):
        super().__init__()
        self.graphsheet = graphsheet
        self.geo_mapper = geo_mapper
        self.scene = scene
        self.ui_part = ui_part
        self.item_row = item_row
        self.item_col = item_col
        
    def item_index(self):
        return (self.item_row, self.item_col)   
  
    
        