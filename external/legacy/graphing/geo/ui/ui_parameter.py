from graphing.geo.model.model_parameter import ModelParameter
from graphing.geo.ui.base_ui import BaseUI


# Just a dummy class, acts as placeholder for now   
class UIParameter(BaseUI):
      def __init__(self, model_parameter:ModelParameter):
          self.model_parameter = model_parameter
    
   
      def view(self):
          return None
   
     
   
 
        