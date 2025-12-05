
from sympy import Line3D, Segment3D
from graphing.geo.model.base_model import BaseModel
from graphing.geo.model.model_line import ModelLine
import sympy as sp
import numpy as np
from graphing.geo.model.model_point import ModelPoint

class ModelLine3D(BaseModel):
    def __init__(self, start_x, start_y, start_z, end_x, end_y, end_z):
        super().__init__()
        self.start_x = start_x
        self.start_y = start_y
        self.start_z = start_z
        self.end_x = end_x  
        self.end_y = end_y
        self.end_z = end_z
        self.model_points = [ModelPoint(start_x, start_y, start_z), ModelPoint(end_x, end_y, end_z)]
        
    def create_segment(self):
        p1 = sp.Point3D(self.start_x, self.start_y, self.start_z)
        p2 = sp.Point3D(self.end_x, self.end_y, self.end_z)
        return sp.Segment3D(p1, p2)          
    
    def create_sympy_line(self):
        p1 = sp.Point3D(self.start_x, self.start_y, self.start_z)
        p2 = sp.Point3D(self.end_x, self.end_y, self.end_z)
        return sp.Line3D(p1, p2)       
    
    def update(self, x1, y1, z1, x2, y2, z2):
        self.start_x = x1
        self.start_y = y1
        self.start_z = z1
        self.end_x = x2
        self.end_y = y2
        self.end_z = z2
        self.model_points[0].set(x1, y1, z1)
        self.model_points[1].set(x2, y2, z2)

        self.notify()
        
    
       
    def point_at(self, at): # This is just for calculation. 
        line_from_manim = Line3D(np.array([self.start_x, self.start_y, self.start_z]), np.array([self.end_x, self.end_y, self.end_z]))
        return line_from_manim.point_from_proportion(at) 
    

    def reflection(self, model_point:ModelPoint):
        line = sp.Line3D(sp.Point3D(self.start_x,self.start_y, self.start_z), sp.Point3D(self.end_x,self.end_y, self.end_z))
        point = model_point.to_sympy()
        # SymPy Line doesn't have a reflection method, but we can calculate it
        projection = line.projection(point)
        reflection = 2 * projection - point
        return ModelPoint(reflection.x, reflection.y, reflection.z)   
    
    
    @staticmethod        
    def from_points(a:ModelPoint, b:ModelPoint):
        model_line_3d = ModelLine3D(a.x, a.y, a.z, b.x, b.y, b.z)
        a.on_change(lambda:  model_line_3d.update(a.x, a.y, a.z, b.x, b.y, b.z))
        b.on_change(lambda:  model_line_3d.update(a.x, a.y, a.z, b.x, b.y, b.z))
        return model_line_3d    