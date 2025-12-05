from .base_model import BaseModel
import math
import numpy as np
import sympy as sp
from sympy import Point, Segment
from manim import *
from .model_point import ModelPoint

class ModelDistance(BaseModel):
    def __init__(self, start_x, start_y, end_x, end_y):
        super().__init__()
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.distance_value = math.sqrt((self.end_x - self.start_x)**2 + (self.end_y - self.start_y)**2)
        self.model_points = [ModelPoint(self.start_x, self.start_y), ModelPoint(self.end_x, self.end_y)]    
        
    def update(self, start_x, start_y, end_x, end_y):
         self.start_x = start_x
         self.start_y = start_y
         self.end_x = end_x
         self.end_y = end_y
         self.distance_value = math.sqrt((self.end_x - self.start_x)**2 + (self.end_y - self.start_y)**2)
         self.model_points[0].set(self.start_x, self.start_y)    
         self.model_points[1].set(self.end_x, self.end_y)
         self.notify()
         
    @property     
    def start(self): 
        return [self.start_x, self.start_y]    
    
    def point_index(self, index):
        if index == 0:
            return self.model_points[0]
        elif index == 1:
            return self.model_points[1]
        else:
            raise ValueError("Invalid index for distance points")
    @property     
    def end(self): 
        return [self.end_x, self.end_y] 
    
    @property   
    def distance(self):
        return self.distance_value
    
   
        
    @staticmethod        
    def from_points(a:ModelPoint, b:ModelPoint):
         model_distance = ModelDistance(a.x, a.y, b.x, b.y)
         a.on_change(lambda:  model_distance.update(a.x, a.y, b.x, b.y))
         b.on_change(lambda:  model_distance.update(a.x, a.y, b.x, b.y))
         return model_distance
    
    
     
     
   