
from .graphsheet2d import GraphSheet2D
from manim import linear

class StaticGraphSheet2D(GraphSheet2D):
    def __init__(self, scene, axes, hide_axes=False, **kwargs):
        super().__init__(scene=scene, axes=axes, hide_axes=hide_axes, **kwargs)
        
    def play_create(self, mobject, voiceover_text=None, **kwargs):
        self.scene.add(mobject, **kwargs)  
        
    def play_write(self, mobject, voiceover_text=None, **kwargs):
        self.scene.add(mobject, **kwargs)
        
    def _play_fade_in(self, mobject, voiceover_text=None, **kwargs):
        self.scene.add(mobject)
        
     
        
    # do nothing
    def wait(self, duration):
        pass
    
   
    
    def play_parameter(self, param, from_value, to_value, run_time=2, rate_func=linear):
        pass
    
    
    