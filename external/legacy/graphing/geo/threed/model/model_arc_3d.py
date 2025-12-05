from pydantic import BaseModel

from graphing.geo.threed.base_model_3d import BaseModel3D


class ModelArc3D(BaseModel3D):
    def __init__(self, left_point, right_point, center_point, radius, segments):
        super().__init__()
        self.left_point = left_point
        self.right_point = right_point
        self.center_point = center_point
        self.radius = radius
        self.segments = segments    
        
    @staticmethod    
    def arc_from_points(left_point, right_point, center_point, radius=1, segments=30):
        model_arc_3d = ModelArc3D(left_point, right_point, center_point, radius, segments)
        left_point.on_change(lambda:  model_arc_3d.update())
        right_point.on_change(lambda:  model_arc_3d.update())
        center_point.on_change(lambda:  model_arc_3d.update())
        return model_arc_3d    
