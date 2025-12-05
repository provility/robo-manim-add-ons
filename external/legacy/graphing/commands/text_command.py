from graphing.commands.base_command import BaseCommand
from manim import *

class TextCommand(BaseCommand):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def do_execute(self, scene):
        scene.add(Tex(self.text))
        
class MathTextCommand(BaseCommand):
    def __init__(self, latex):
        super().__init__()
        self.latex = latex

    def do_execute(self, scene):
        scene.add(MathTex(self.latex))        