from graphing.geo.model.model_line import ModelLine
from graphing.geo.model.model_point import ModelPoint
import numpy as np

class ModelVector(ModelLine):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2) # represents a vector from point (x1, y1) to point (x2, y2)    
    
    def reverse(self):
        return ModelVector(self.end_x, self.end_y, self.start_x, self.start_y)  
    
    @staticmethod    
    def as_translation_vector(a:ModelPoint, b:ModelPoint):
        return ModelVector(0, 0, b.x - a.x, b.y - a.y)
    
    @staticmethod
    def position_vector(a:ModelPoint):
        return ModelVector(0, 0, a.x, a.y) 
  
    def unit_vector_numpy(self):
        length = self.length
        return np.array([self.x / length, self.y / length, self.z / length])
  
    @property
    def x(self):
        return self.end_x - self.start_x
    
    @property
    def y(self):
        return self.end_y - self.start_y
    
    @property
    def z(self):
        return 0
    
    @property
    def length(self):
        return np.sqrt((self.end_x - self.start_x)**2 + (self.end_y - self.start_y)**2) 
    
    def scale_vector(self, scale_factor):
        scaled_vector = ModelVector(self.start_x, self.start_y, self.end_x * scale_factor, self.end_y * scale_factor)
        return scaled_vector
     
    def translate_vector(self, vector):
        return ModelVector(self.start_x + vector.x, self.start_y + vector.y, 
                                        self.end_x + vector.x, self.end_y + vector.y)        
    
    def reverse_vector(self):
        return ModelVector(self.end_x, self.end_y, self.start_x, self.start_y)
    
    def parallel_vector(self, from_vector):
        x_diff = self.x
        y_diff = self.y
        return ModelVector(from_vector.end_x, from_vector.end_y, 
                                                 from_vector.end_x + x_diff,  # the difference between the end points of the vectors    
                                                 from_vector.end_y + y_diff)
        
    def perpendicular_vector(self, from_vector):   
        return ModelVector(from_vector.end_x, from_vector.end_y, 
                                                 from_vector.end_x + self.y, 
                                                 from_vector.end_y - self.x)   
        
    def unit_vector(self):
        length = self.length
        return ModelVector(self.start_x, self.start_y, self.x / length, self.y / length)
    
    @staticmethod   
    def from_end_points(a:ModelPoint, b:ModelPoint):
         model_vector = ModelVector (a.x, a.y, b.x, b.y)
         a.on_change(lambda:  model_vector.update(a.x, a.y, b.x, b.y))
         b.on_change(lambda:  model_vector.update(a.x, a.y, b.x, b.y))
         return model_vector
     
    @staticmethod
    def reversed_vector(source_vector):
        model_vector = None
       
        def create():
            nonlocal model_vector
            model_vector = source_vector.reverse_vector()   
            return model_vector
        
        def update():
            nonlocal model_vector   
            new_vector = source_vector.reverse_vector() 
            model_vector.update(new_vector.start_x, new_vector.start_y,
                                 new_vector.end_x, new_vector.end_y)     
            
        create()
        source_vector.on_change(update)
        return model_vector
    
    @staticmethod
    def perped_vector(start_vector, source_vector):
        model_vector = None
        def computation():
            perpendicular_vector = source_vector.perpendicular_vector(start_vector)
            return perpendicular_vector
            
        def create():
            nonlocal model_vector
            model_vector = computation()
            
        def update():
            nonlocal model_vector
            new_vector = computation()  
            model_vector.update(new_vector.start_x, new_vector.start_y,
                                 new_vector.end_x, new_vector.end_y)     
            
        create()
        start_vector.on_change(update)
        source_vector.on_change(update)
        return model_vector
    
    @staticmethod
    def scaled_vector(model_vector, scale_factor_parameter):
        scaled_vector = None
        def create():
            nonlocal scaled_vector
            scale_value = scale_factor_parameter.get_value()
            scaled_vector = model_vector.scale_vector(scale_value)  
            return scaled_vector    
        
        def update():   
            nonlocal scaled_vector  
            scale_value = scale_factor_parameter.get_value()    
            new_vector = model_vector.scale_vector(scale_value)
            scaled_vector.update(new_vector.start_x, new_vector.start_y,
                                 new_vector.end_x, new_vector.end_y)     
            
        create()
        model_vector.on_change(update)
        scale_factor_parameter.on_param_change(lambda d: update())
        return scaled_vector    
               
    @staticmethod
    def add_vector(vector_a, vector_b):
        sum_vector = None

        def create():
            nonlocal sum_vector
            sum_vector = ModelVector(vector_a.start_x, vector_a.start_y, vector_a.end_x + vector_b.end_x, vector_a.end_y + vector_b.end_y)
            return sum_vector
        
        def update():
            sum_vector.update(vector_a.start_x, vector_a.start_y, vector_a.end_x + vector_b.end_x, vector_a.end_y + vector_b.end_y)
            
        create()
        vector_a.on_change(update)
        vector_b.on_change(update)
        return sum_vector
    
    @staticmethod
    def subtract_vector(vector_a, vector_b):    
        difference_vector = None

        def create():
            nonlocal difference_vector
            difference_vector = ModelVector(vector_a.start_x, vector_a.start_y, vector_a.end_x - vector_b.end_x, vector_a.end_y - vector_b.end_y)
            return difference_vector
        
        def update():
            difference_vector.update(vector_a.start_x, vector_a.start_y, vector_a.end_x - vector_b.end_x, vector_a.end_y - vector_b.end_y)
            
        create()
        vector_a.on_change(update)
        vector_b.on_change(update)
        return difference_vector   
        
    @staticmethod
    def parallelled_vector(from_vector, source_vector):
        target_parallel_vector = None

        def create():
            nonlocal target_parallel_vector 
            target_parallel_vector = source_vector.parallel_vector(from_vector)   
            return target_parallel_vector
        
        def update():   
            nonlocal target_parallel_vector
            new_vector = source_vector.parallel_vector(from_vector)
            target_parallel_vector.update(new_vector.start_x, new_vector.start_y, new_vector.end_x, new_vector.end_y)
            
        create()
        from_vector.on_change(update)
        source_vector.on_change(update)
        return target_parallel_vector   
        
        
  
 
    
    @staticmethod
    def scaled_vector(model_vector, scale_factor_or_parameter):
        scaled_vector= None
        
        def create():
            nonlocal scaled_vector  
            scale_value = scale_factor_or_parameter.get_value()
            scaled_vector = ModelVector(model_vector.start_x, model_vector.start_y, model_vector.end_x * scale_value, model_vector.end_y * scale_value)
            return scaled_vector
        
        def update():
            scale_value = scale_factor_or_parameter.get_value()
            scaled_vector.update(model_vector.start_x, model_vector.start_y, model_vector.end_x * scale_value, model_vector.end_y * scale_value)
            
        create()
        model_vector.on_change(update)
        scale_factor_or_parameter.on_param_change(lambda d: update())
        return scaled_vector
        
      
     
    
      
       

   