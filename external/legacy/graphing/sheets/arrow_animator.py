from manim import *

from graphing.geo.effect_command import EffectCommand
from graphing.geo.model.base_model import BaseModel
class ArrowAnimator:
    def __init__(self, graphsheet, scene):
        self.graphsheet = graphsheet
        self.scene = scene
        
    def arrow_effect(self, from_model, to_model, color=BLUE, 
                     from_buff=0.3*RIGHT, to_buff=0.3*LEFT,
                     run_time=2, voiceover_text=None, remove_on_completion=True):
        arrow = Arrow(start=from_model.view().get_center() + from_buff, end=to_model.view().get_center() + to_buff).set_color(color)
        do_func = lambda: GrowArrow(arrow)
        undo_func = lambda: FadeOut(arrow)
        effect_command = EffectCommand(do_func, undo_func,
                                       scene=self.scene, 
                                       graph_sheet=self.graphsheet, 
                                       run_time=run_time, 
                                       voiceover_text=voiceover_text, 
                                       remove_on_completion=remove_on_completion)
        return effect_command  
    