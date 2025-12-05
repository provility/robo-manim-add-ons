from graphing.commands.base_command import BaseCommand
from manim import *

class FunctionPlot2D(BaseCommand):
    def __init__(self, latex_expression, free_variable = 'x', subs_dict={}):
        super().__init__()
        self.latex_expression = latex_expression
        self.sub_dicts = subs_dict
        self.free_variable = free_variable

    def do_execute(self, scene):
        scene.add(Tex(self.text))
     