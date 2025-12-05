import numpy as np
from pydantic import BaseModel

class ModelPlot3D(BaseModel):
    def __init__(self, eq_lambda, plot_range=None):
        self.eq_lambda = eq_lambda
        self.plot_range = plot_range
        
    def point_at(self, at):
        return None   