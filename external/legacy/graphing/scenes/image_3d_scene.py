from manim import *

from graphing.scenes.graphsheet_scene_helper import GraphSheetSceneHelper

class Image3DScene(ThreeDScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.graph_sheet_scene_helper = GraphSheetSceneHelper(self)       
        
    def construct(self):
        pass