from graphing.geo.model.model_point import ModelPoint
from graphing.geo.threed.model.model_vector_3d import ModelVector3D


class ModelPlane3D:
    def __init__(self, normal_vector:ModelVector3D, point_on_plane:ModelPoint):
        self.normal_vector = normal_vector
        self.point_on_plane = point_on_plane
        
    def update(self):
       self.notify()
        
    @staticmethod    
    def from_point_and_normal(normal_vector:ModelVector3D, point_on_plane:ModelPoint,):    
        model_plane = ModelPlane3D(normal_vector, point_on_plane)
        
        normal_vector.on_change(model_plane.update)
        point_on_plane.on_change(model_plane.update) 
        return model_plane
        
   
