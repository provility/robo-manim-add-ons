import sympy
from manim import *
import math
import numpy as np

class BaseVGroup(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) 
        
    def label(self): 
        if self.label is not None:
            return self.label
        return None 
    
    def set_dynamic(self): 
        raise NotImplementedError("set_dynamic method not implemented")
    
    def position_label(self, direction):
        if self.label:
            self.label.next_to(self, direction)
        else:
            raise ValueError("Label not found")
        
    def point_at(self, x):
        raise NotImplementedError("This method should be implemented by the subclass")    
        
  