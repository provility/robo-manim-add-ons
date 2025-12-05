

from graphing.commands.base_command import BaseCommand
from manim import *

from graphing.sheets.graphsheet2d import GraphSheet2D

class AddGraphSheet2DCommand(BaseCommand):
    def __init__(self):
        super().__init__()
       
    def do_execute(self, scene):
        scene.add(self.grap_sheet2d)
        scene.grap_sheet2d = GraphSheet2D(scene)
        
class AxesCommand(BaseCommand):
    def __init__(self, x_range, y_range, x_tick_labels, y_tick_labels):
        super().__init__()
        self.x_range = x_range
        self.y_range = y_range
        self.x_tick_labels = x_tick_labels
        self.y_tick_labels = y_tick_labels
        
    def do_execute(self, scene):
        scene.graph_sheet2d.add_axes(
            x_range = self.x_range,
            y_range = self.y_range,
            x_tick_labels = self.x_tick_labels,
            y_tick_labels = self.y_tick_labels
        )           