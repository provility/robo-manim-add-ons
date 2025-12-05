import dotenv
import os
from manim import *
from dotenv import load_dotenv
import numpy as np

from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService
  
from manim_voiceover.services.gtts import GTTSService
from graphing.scenes.graphsheet_scene_helper import GraphSheetSceneHelper
from graphing.voices import VoiceConfig


class AnimationScene2D(VoiceoverScene, MovingCameraScene,
                       GraphSheetSceneHelper):   
    def __init__(self, **kwargs):
        VoiceoverScene.__init__(self, **kwargs)
        MovingCameraScene.__init__(self, **kwargs)
        GraphSheetSceneHelper.__init__(self, self)
        self.background_color(WHITE)
        
    def setup(self):
        VoiceoverScene.setup(self)  
        
    def background_color(self, color):
        self.camera.background_color = color
    
    def render(self, *args, **kwargs):
        return VoiceoverScene.render(self, *args, **kwargs)
    
    def clear_scene(self):
        objects_to_fade = [m for m in self.mobjects]
        self.play(FadeOut(*objects_to_fade))
        self.remove(*objects_to_fade)
        
    
    def set_up_voiceover(self, config: VoiceConfig = VoiceConfig.TARA):
       
        dotenv.load_dotenv()
        self.set_speech_service(self.elevenlabs_speech_service(config))
     
    def set_free_voiceover(self):
        self.set_speech_service(GTTSService())   
        
    def bootstrap(self):
        # Add Robogebra logo to top right corner
        logo = SVGMobject("robogebra-logo.svg")
        logo.scale(0.2)
        logo.to_corner(UR, buff=0.2)
        self.add(logo)
         

    def openai_speech_service(self):
        return OpenAIService(
            voice="alloy",
            style="tts-1-hd"
        )
        
    def elevenlabs_speech_service(self, config: VoiceConfig = VoiceConfig.TARA):
        from manim_voiceover.services.elevenlabs import ElevenLabsService 
        return ElevenLabsService(
            voice=config.voice_name,
            voice_id=config.voice_id,   
            language="en",  
            model="eleven_multilingual_v2"
        )    
    
    def pause(self, duration):
        self.wait(duration) 
        
   