from .model_point import ModelPoint
from .base_model import BaseModel
from manim import *
class ModelDynamicProperty(BaseModel):
     def __init__(self, 
                  source_prop, source_model:BaseModel,
                  display_prop_name = None
                  ):
         super().__init__()
         self.display_prop_name = display_prop_name
         self.source_prop = source_prop
         self.source_model = source_model
         self.property_value = self._get_current_variable_value()
         

     def update(self):
         self.property_value = self._get_current_variable_value()
         self.notify()
         
  
     def _get_current_variable_value(self):
         try:
             return getattr(self.source_model, self.source_prop)
         except AttributeError:
             print(f"Property '{self.source_prop}' not found in {self.source_model} model")
             return None
         
    

     @staticmethod   
     def from_model( source_prop, source_model:BaseModel, variable_name=None):
        model_dynamic_property = ModelDynamicProperty(source_prop, source_model, variable_name)
        
        # hook dependencies
        source_model.on_change(model_dynamic_property.update)
        return model_dynamic_property
    
