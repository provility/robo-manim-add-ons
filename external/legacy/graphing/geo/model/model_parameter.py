from pyee import EventEmitter

from graphing.geo.model.model_point import ModelPoint
from graphing.geo.parameter_lambda_updater import ParameterLambdaUpdater
from .base_model import BaseModel
from manim import *


class BaseModelParameter():
    def __init__(self, scene, from_value=None):
        self.scene = scene
        self.from_value = from_value
        self.to_value = None
        self.value_tracker = None
        if from_value is not None:
            self.value_tracker = ValueTracker(from_value) 
        self.param_change_event_emitter = EventEmitter()
        self.param_change_lambda_updater = None 
        
    def get_value(self):
        return self.value_tracker.get_value()
          
    def value_updater_callback(self):
        pass
       
    def value_updater_callback_with_value(self, value):
        pass
          
    def play(self, from_value, to_value, run_time=2, rate_func=linear, voiceover_text=None):
        self.from_value = from_value
        self.to_value = to_value
        self.run_time = run_time
        self.rate_func = rate_func  
        if self.value_tracker is not None:
            self.value_tracker.clear_updaters()
            self.value_tracker = None
         
        self.value_tracker = ValueTracker(from_value)    
        self.value_tracker.add_updater(lambda d: self.value_updater_callback())
        if voiceover_text:    
              with self.scene.voiceover(voiceover_text) as tracker:
                self.scene.play(self.value_tracker.animate.set_value(self.to_value), 
                                run_time=tracker.duration,
                                rate_func=self.rate_func)
        else:
              self.scene.play(self.value_tracker.animate.set_value(self.to_value), 
                          run_time=self.run_time,
                          rate_func=self.rate_func)
          
    def on_param_change(self, callback):
        self.param_change_event_emitter.on("param_change", callback)
          
    def off_param_change(self, callback):
        self.param_change_event_emitter.off("param_change", callback)
          
    @property     
    def param_value(self):
        return self.get_value()   
          
          
    def add_change_setter(self, source_model, source_attribute, target_model, target_attribute):
        self.param_change_lambda_updater = ParameterLambdaUpdater(source_model, source_attribute, target_model, target_attribute)

    def _update_param_change_lambda_updater(self):
        if self.param_change_lambda_updater is not None:
            self.param_change_lambda_updater.update()    
      
"""
This class doesnt have any UI part, it is just a model class, which allows us
to animate a value from one to another
"""
class ModelParameter(BaseModel, BaseModelParameter):
      def __init__(self, scene, from_value=None):
          BaseModelParameter.__init__(self, scene, from_value)
          BaseModel.__init__(self)
          
      def value_updater_callback(self):
          self.param_change_event_emitter.emit("param_change", self.get_value())    
          self._update_param_change_lambda_updater()
          self.notify()    

      def value_updater_callback_with_value(self, value):   
        self.param_change_event_emitter.emit("param_change", value)    
        self._update_param_change_lambda_updater()
        self.notify()  

"""
A point that is defined by a lambda function. Wherever point is used,
the lambda function will be called to get the x and y values.
"""
class ModelPointParameter(ModelPoint, BaseModelParameter):
    def __init__(self, scene, x_lambda_function, y_lambda_function, from_value):
        BaseModelParameter.__init__(self, scene, from_value)
        ModelPoint.__init__(self, x_lambda_function(from_value), y_lambda_function(from_value))
        self.x_lambda_function = x_lambda_function
        self.y_lambda_function = y_lambda_function 
        self.current_parameter_value = from_value
        
    @property
    def x(self):
        return self.x_lambda_function(self.current_parameter_value)
    
    @property
    def y(self):
        return self.y_lambda_function(self.current_parameter_value)
    
    @property
    def z(self):
        return 0
    
    @x.setter
    def x(self, value):
        raise NotImplementedError("Cannot set values directly on a parameter point. Update the parameter instead.")
        
    @y.setter 
    def y(self, value):
        raise NotImplementedError("Cannot set values directly on a parameter point. Update the parameter instead.")
        
    @z.setter
    def z(self, value):
        raise NotImplementedError("Cannot set values directly on a parameter point. Update the parameter instead.")
    
    def set(self, x, y, z=0, notify=True):
        raise NotImplementedError("Cannot set values directly on a parameter point. Update the parameter instead.")

    def update(self, x, y, z=0, notify=True):
        raise NotImplementedError("Cannot update a parameter point directly. Update the parameter instead.")    

    def value_updater_callback_with_value(self, value):   
        self.current_parameter_value = value
        self.param_change_event_emitter.emit("param_change", value)    
        self._update_param_change_lambda_updater()
        self.notify()  


class ModelLambdaParameter(ModelParameter):
    def __init__(self, scene, lambda_function, from_value):
        super().__init__(scene, lambda_function(from_value))
        self.lambda_function = lambda_function  
        self.current_parameter_value = from_value
        
    def get_value(self):
        return self.lambda_function(self.current_parameter_value) 
    
    """
    If directly played - should still work
    """
    def value_updater_callback_with_value(self, value):   
        self.current_parameter_value = value
        self.param_change_event_emitter.emit("param_change", self.lambda_function(value))    
        self._update_param_change_lambda_updater()
        self.notify()       
        
               
    

class ModelChainedParameter(ModelParameter):
    def __init__(self, scene, source_parameter, *dependent_parameters):
        super().__init__(scene, source_parameter.get_value())
        self.source_parameter = source_parameter
        self.dependent_parameters = dependent_parameters
        self.chain_parameters(source_parameter, *dependent_parameters)
        
    def chain_parameters(self, source_parameter, *dependent_parameters):
        
        def source_parameter_callback(value):
            for dependent_parameter in dependent_parameters:
                dependent_parameter.value_updater_callback_with_value(value)
            
        source_parameter.on_param_change(source_parameter_callback)
         
       
           
        
        