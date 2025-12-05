from graphing.geo.model.base_model import BaseModel
from graphing.geo.model.model_point import ModelPoint
from graphing.geo.threed.model.model_line_3d import ModelLine3D
import numpy as np  

class ModelVector3D(ModelLine3D):
    def __init__(self, x1, y1, z1, x2, y2, z2):
        super().__init__(x1, y1, z1, x2, y2, z2)
      
   
    @staticmethod
    def position_vector(a:ModelPoint):
        return ModelVector3D(0, 0, 0, a.x, a.y, a.z) 
    
    @staticmethod
    def scale_vector(a, scale_factor):
        return ModelVector3D(0, 0, 0, a.x * scale_factor, a.y * scale_factor, a.z * scale_factor)  
    
    @property
    def x(self):
        return self.end_x - self.start_x
    
    @property
    def y(self):
        return self.end_y - self.start_y
    
    @property
    def z(self):
        return self.end_z - self.start_z    
    
    @property
    def start(self):
        return self.start_x, self.start_y, self.start_z
    
    @property
    def end(self):
        return self.end_x, self.end_y, self.end_z   
    
    def get_as_numpy_array(self):
        return np.array([self.x, self.y, self.z])
    
    @staticmethod   
    def from_points(a:ModelPoint, b:ModelPoint):
        model_vector = ModelVector3D (a.x, a.y, a.z, b.x, b.y, b.z)
        a.on_change(lambda:  model_vector.update(a.x, a.y, a.z, b.x, b.y, b.z))
        b.on_change(lambda:  model_vector.update(a.x, a.y, a.z, b.x, b.y, b.z))
        return model_vector    