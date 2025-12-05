from manim import *

from graphing.geo.model.model_point import ModelPoint

class GeoMapper:
      def __init__(self, axes:Axes) -> None:
          self._axes = axes
             
      def model_to_ui(self, x, y=0, z=0):
          if isinstance(x, ModelPoint):
              return self.axes.c2p(x.x, x.y)
          else: 
              return self.axes.c2p(x, y)
      
      def model_point_to_ui_point(self, model_point:ModelPoint):
          return self.model_to_ui(model_point.x, model_point.y) 
      
      def to_screen_point(self, model_point_or_x_or_tuple, y=None):
          if isinstance(model_point_or_x_or_tuple, ModelPoint):
              return self.model_point_to_ui_point(model_point_or_x_or_tuple)
          elif isinstance(model_point_or_x_or_tuple, tuple) or isinstance(model_point_or_x_or_tuple, list):
              return self.model_to_ui(model_point_or_x_or_tuple[0], model_point_or_x_or_tuple[1])   
          elif y is not None:
              return self.model_to_ui(model_point_or_x_or_tuple, y)
          else:
              raise ValueError("Invalid input. Provide either a ModelPoint or x and y coordinates.")
     
      
      def ui_to_model(self, ux, uy, z=0):
          model_values  = self.axes.p2c(np.array([ux, uy, z]))
          return model_values
      
      def ui_numpy_array_list_to_model_point(self, ui_array_list):
          return [ self.ui_to_model(np_point_array[0], np_point_array[1]) for np_point_array in ui_array_list]
      
      def distance_between_points(self, p1_x, p1_y, p2_x, p2y):
          ui_point_1 = self.model_to_ui(p1_x, p1_y)
          ui_point_2 = self.model_to_ui(p2_x, p2y)
          return  np.linalg.norm(ui_point_1 - ui_point_2)
      
      def model_radius_to_ui(self, radius):
          ui_point_1 = self.model_to_ui(0,0)
          ui_point_2 = self.model_to_ui(radius,0)
        
          return  np.linalg.norm(ui_point_1 - ui_point_2)
    
      @property
      def axes(self):
          return self._axes      