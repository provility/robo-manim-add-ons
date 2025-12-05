from graphing.geo.model.base_model import BaseModel
from graphing.geo.model.model_point import ModelPoint


class ModelPointList(BaseModel):
    """
    Will rececive the max number of points 
    """
    def __init__(self, points:list[ModelPoint]):
        super().__init__()  
        self._points = points
        
         
    @property
    def points(self):
        return self._points
    
    def point_index(self, index):
        if index < len(self.points):
            return self.points[index]
        else:
            raise ValueError("Invalid index for point list")    
    
    def update(self):
        raise NotImplementedError("update method not implemented for ModelPointList, use Merge instead")
    

    def merge(self, new_points):
        # Set all old points to far off-screen position before updating
        for i in range(len(self.points)):
            self.points[i].set(-1000, -1000)
            
        for i in range(len(new_points)):
            self.points[i].set(new_points[i].x, new_points[i].y) 
        
        self.notify()           
           
    @property
    def sympy_points(self):
        return [point.to_sympy() for point in self.points]
        
        
    