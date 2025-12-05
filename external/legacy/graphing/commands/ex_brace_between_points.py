from manim import *
import numpy as np

class ExBraceBetweenPoints(BraceBetweenPoints):
    def __init__(self, point_1, point_2, **kwargs):
        super().__init__(point_1, point_2, **kwargs)
        self.point_1 = point_1
        self.point_2 = point_2

    def shift_brace(self, shift_distance):
        brace_direction = self.point_2 - self.point_1
        normalized_brace_direction = normalize(brace_direction)
        normal_direction = rotate_vector(normalized_brace_direction, PI/2)
        self.shift(normal_direction * (-shift_distance))   
        