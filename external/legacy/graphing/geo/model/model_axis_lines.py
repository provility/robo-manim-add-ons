from graphing.geo.model.base_model import BaseModel
from graphing.geo.model.model_point import ModelPoint


class ModelAxisLine(BaseModel):
      def __init__(self, model_point:ModelPoint):
          super().__init__()
          self.model_point = model_point
          
      def axis_point(self):
         return self.model_point
     
      def update(self):
         self.notify()
    
      @staticmethod
      def axis_line_from_point(model_point:ModelPoint):
          model_axis_line = None
          
        
          def create():
            nonlocal model_axis_line  
            model_axis_line = ModelAxisLine(model_point=model_point)
            
          def update():   
            nonlocal model_axis_line  
            model_axis_line.update()
            
          create()
        
          model_point.on_change(lambda: update())
          return model_axis_line
           
     
     
          