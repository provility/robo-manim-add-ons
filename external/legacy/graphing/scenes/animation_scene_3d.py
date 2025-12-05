import dotenv
from manim import *
from dotenv import load_dotenv
import numpy as np

from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from graphing.scenes.graphsheet_scene_helper import GraphSheetSceneHelper


class AnimationScene3D(ThreeDScene, VoiceoverScene, GraphSheetSceneHelper):
    def __init__(self, **kwargs):
        VoiceoverScene.__init__(self, **kwargs)
        ThreeDScene.__init__(self, **kwargs)
        dotenv.load_dotenv()
        self.set_speech_service(GTTSService())
        GraphSheetSceneHelper.__init__(self, self)
        
    def setup(self):
        VoiceoverScene.setup(self)  
    
    def render(self, *args, **kwargs):
        return VoiceoverScene.render(self, *args, **kwargs)
    
    