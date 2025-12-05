from graphing.geo.model.base_model import BaseModel

class ModelRiemann(BaseModel):
    def __init__(self, model_plot, dx_parameter, sum_range):
        super().__init__()      
        self.model_plot = model_plot
        self.dx_parameter = dx_parameter
        self.sum_range = sum_range 
       
    def update(self):
        self.notify()
       
    @staticmethod
    def from_plot_and_parameter(model_plot, dx_parameter, sum_range):
        model_reimann = ModelRiemann(model_plot, dx_parameter, sum_range)
        
        #hook up the parameter to the plot
        dx_parameter.on_param_change(lambda m: model_reimann.update())
    
        return model_reimann
    
    
