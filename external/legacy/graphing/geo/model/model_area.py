from graphing.geo.model.base_model import BaseModel

class ModelArea(BaseModel):
    def __init__(self, model_plot, area_range_parameters):
        super().__init__()       
        self.model_plot = model_plot
        self.area_range_parameters = area_range_parameters
        
    def update_area(self):
        self.notify()
        
    @staticmethod
    def from_plot_and_range_parameters(model_plot, range_parameters):
        model_area = ModelArea(model_plot, range_parameters)
        range_parameters[0].on_param_change(lambda x: model_area.update_area())
        range_parameters[1].on_param_change(lambda x: model_area.update_area())
        return model_area