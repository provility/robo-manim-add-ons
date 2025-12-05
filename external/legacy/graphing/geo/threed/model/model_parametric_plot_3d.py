import numpy as np

from graphing.geo.model.model_plot import ModelPlot

class ModelParametricPlot3D(ModelPlot):
    def __init__(self, eq_lambda, plot_range=None):
        super().__init__(eq_lambda, plot_range)
        
    def point_at(self, at): 
        return np.array([self.eq_lambda(at), at, 0])    