from graphing.geo.model.base_model import BaseModel


class BaseModel3D(BaseModel):
    def __init__(self):
        super().__init__()
        
    @property
    def z(self):
        return self.ui_part.z      
        