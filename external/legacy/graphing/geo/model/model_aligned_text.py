from graphing.geo.model.base_model import BaseModel
from graphing.geo.model.model_point import ModelPoint
from graphing.geo.model.model_text import MathModelText

class ModelAlignedText(MathModelText):
    def __init__(self, text:str,start_point:ModelPoint, end_point:ModelPoint,) -> None:
        super().__init__([text])
        self.start_point = start_point
        self.end_point = end_point  
        
    @staticmethod
    def aligned_to_points(text: str, start_point: ModelPoint, end_point: ModelPoint):
        model_aligned_text = ModelAlignedText(text, start_point, end_point)
        start_point.on_change(lambda: model_aligned_text.update())
        end_point.on_change(lambda: model_aligned_text.update())
        return model_aligned_text
   
    def update(self):
        self.notify()
        