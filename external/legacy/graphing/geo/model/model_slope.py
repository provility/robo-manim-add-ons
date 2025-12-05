from graphing.geo.model.base_model import BaseModel
from graphing.geo.model.model_plot import ModelExplicitPlot
from graphing.geo.model.model_point import ModelPoint


class ModelTangentSlope(BaseModel):
    def __init__(self, model_plot:ModelExplicitPlot, model_x:float):
        self.model_plot = model_plot
        self.model_x = model_x
        super().__init__()
        
    def update(self, model_plot, model_x):
        self.model_plot = model_plot
        self.model_x = model_x
        self.notify()   
        
    def plot_shape(self):
        return self.model_plot.plot_shape()    
        
    @staticmethod
    def tangent_slope(model_plot:ModelExplicitPlot, model_x_parameter):
        model_tangent_slope = ModelTangentSlope(model_plot, model_x_parameter.get_value())
        
        def update():
            model_tangent_slope.update(model_plot, model_x_parameter.get_value())
            
        model_x_parameter.on_param_change(lambda d: update())
        model_plot.on_change(update)
        return model_tangent_slope
         