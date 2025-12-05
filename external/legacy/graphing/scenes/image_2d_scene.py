from manim import *
from manim.constants import DEFAULT_WAIT_TIME

from graphing.scenes.graphsheet_scene_helper import GraphSheetSceneHelper

class Image2DScene(Scene, GraphSheetSceneHelper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        GraphSheetSceneHelper.__init__(self, self)  
         
    def pause(self, duration):
        pass
        
    def setup(self):
        Scene.setup(self)  
        
    def wait(self, duration):
        pass
    
    def render(self, *args, **kwargs):
        return Scene.render(self, *args, **kwargs)