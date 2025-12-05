from manim import *
import numpy as np

class Arc3d(VMobject):
    
    def __init__(self, A=None, B=None, center=None, radius=1, segments=40, **kwargs):
        super().__init__(**kwargs)
        start = center + (A-center)*radius/np.linalg.norm(A-center) 
        end   = center + (B-center)*radius/np.linalg.norm(B-center) 
        self.set_points([start])
        for i in np.linspace(0,1,segments,endpoint=True):
            dotonline = start + i*(end-start)
            radline = dotonline-center
            dotonarc = center + radline/np.linalg.norm(radline)*radius
            self.add_smooth_curve_to(dotonarc)