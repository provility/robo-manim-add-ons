from graphing.geo.model.base_model import BaseModel
from graphing.geo.model.model_point import ModelPoint

class ModelImage(BaseModel):
    def __init__(self, image_path, model_position:ModelPoint):
        super().__init__()
        self.image_path = image_path
        self.model_position = model_position
        
    def get_image(self):
        return self.image_path
    
    def update(self):
        self.notify()
        
    @staticmethod
    def from_path_and_position(image_path, model_position:ModelPoint):
        model_image = ModelImage(image_path, model_position)
        model_position.on_change(model_image.update)
        return model_image
        