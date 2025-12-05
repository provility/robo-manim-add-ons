from graphing.geo.model.base_model import BaseModel
import numpy as np

from graphing.geo.model.model_point import ModelPoint

class GeoPropertyCalculator:

    
    def calculate_numerical_property(self, property:str, models:list[BaseModel]):
        property = property.lower()
        if property == "distance":
            return self.calculate_distance(models[0], models[1])
        if property == "midpoint":
            return self.calculate_midpoint(models[0], models[1])
        if property == "slope":
            return self.calculate_slope(models[0], models[1])
        if property == "angle":
            return self.calculate_angle(models[0], models[1])  
        if property == "dot product":
            return self.calculate_dot_product(models[0], models[1])

    def calculate_dot_product(self, model1, model2):
        return model1.x * model2.x + model1.y * model2.y + model1.z * model2.z
    
    def calculate_distance(self, model1, model2):
        return np.sqrt((model1.x - model2.x)**2 + (model1.y - model2.y)**2 + (model1.z - model2.z)**2)
    
    def calculate_midpoint(self, model1, model2):
        return ModelPoint((model1.x + model2.x) / 2, (model1.y + model2.y) / 2, (model1.z + model2.z) / 2) 
        
    def calculate_slope(self, model1, model2):
        return (model2.y - model1.y) / (model2.x - model1.x) 

    def calculate_angle(self, model1, model2):
        return np.arctan2(model2.y - model1.y, model2.x - model1.x)

    