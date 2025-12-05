from graphing.geo.model.base_model import BaseModel
from graphing.geo.model.model_plot import ModelExplicitPlot


class ModelAreaBetweenCurves(BaseModel):
    def __init__(self, curve_a:ModelExplicitPlot, curve_b:ModelExplicitPlot,
                 from_x, to_x):
        super().__init__()
        self.curve_a = curve_a
        self.curve_b = curve_b
        self.from_x = from_x
        self.to_x = to_x    
      
  
    def update(self, curve_a, curve_b, from_x, to_x):
        self.curve_a = curve_a  
        self.curve_b = curve_b
        self.from_x = from_x
        self.to_x = to_x
        self.notify()
        
    
    @staticmethod    
    def area_between_curves(curve_a:ModelExplicitPlot, curve_b:ModelExplicitPlot,
                 from_parameter, to_parameter):
        model_area_between_curves = None
        
        model_area_between_curves = ModelAreaBetweenCurves(curve_a, curve_b,
                 from_parameter.get_value(), to_parameter.get_value())
        
        def update():
            nonlocal model_area_between_curves
            from_x_value = from_parameter.get_value()
            to_x_value = to_parameter.get_value()
            model_area_between_curves.update(curve_a=curve_a, curve_b=curve_b, 
                                             from_x=from_x_value, to_x=to_x_value)
           
         
        
        from_parameter.on_param_change(lambda d: update)
        to_parameter.on_param_change(lambda d: update)
        return model_area_between_curves
            
        
            
        
    
        
    
        