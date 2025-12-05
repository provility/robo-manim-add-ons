from manim import *

from graphing.geo.ui.ui_style_props import UIStyleProps
class ArrowTextAnnotation:
    def __init__(self):
        super().__init__()
        self.text_elements = []
        self.text_group =  VGroup()
        self.arrow =  Arrow(ORIGIN,ORIGIN)
        
      
    def add_text(self, text:str):
        self.text_elements.append(Text(text))
     
    def add_math_text(self, text:str):
        self.text_elements.append(MathTex(text))
        
    def build(self):
        objects = self.text_elements
        for i in range(len(objects)-1):
            objects[i+1].next_to(objects[i],RIGHT, buff=0.1, aligned_edge=UP)
        self.text_group.add(*objects)
     
    def arrow_direction(self, source, destination): 
        self.arrow.become(Arrow(source, destination))
    
    def text_placement(self, location):
        self.text_group.move_to(location)    
        
    def write(self, scene):
        pass
    
    def animate(self, scene):
        self.play(GrowArrow(self.arrow))
        self.play(FadeIn(self.text_group))   
        
    def fade(self):
        self.play(FadeOut(self.arrow), FadeOut(self.text_group))    
        
        
        