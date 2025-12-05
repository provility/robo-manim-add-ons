from graphing.geo.model.base_model import BaseModel
from graphing.geo.model.model_point import ModelPoint


class ModelPolyLineArrow(BaseModel):
    def __init__(self, points:list[ModelPoint]):
        super().__init__()
        self.points = points
        
    def update(self, points:list[ModelPoint]):
        self.points = points
        self.notify()
        
    @staticmethod
    def from_points(points:list[ModelPoint]):
         model_poly_line_arrow = None
         
         def create():
             nonlocal model_poly_line_arrow
             model_poly_line_arrow = ModelPolyLineArrow(points)
        
         def update():
             nonlocal model_poly_line_arrow
             model_poly_line_arrow.update(points)

         create()
         
         for point in points:
             point.on_change(update)
         
         return model_poly_line_arrow
         
        