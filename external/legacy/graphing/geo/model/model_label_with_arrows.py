from graphing.geo.model.base_model import BaseModel


class ModelLabelWithArrows(BaseModel):
    def __init__(self, text, start_point, end_point):
        super().__init__()
        self.text = text
        self.start_point = start_point
        self.end_point = end_point
        
    def update(self, text, start_point, end_point):
        self.text = text
        self.start_point = start_point
        self.end_point = end_point
        self.notify()
        
    @staticmethod
    def from_text_and_points(text, start_point, end_point):
        model_label_with_arrows = None
        model_label_with_arrows = ModelLabelWithArrows(text, start_point, end_point)
        
        def update():   
            model_label_with_arrows.update(text, start_point, end_point)
            
        start_point.on_change(update)
        end_point.on_change(update)
        
        return model_label_with_arrows
