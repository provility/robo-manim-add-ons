from manim import *
import numpy as np

from graphing.geo.model.model_point import ModelPoint
from graphing.geo.model.model_vector import ModelVector

class AlphaAnimator:
    def __init__(self, scene):
        self.scene = scene
   
    def rotate_point(self, model_point, angle_in_degrees_parameter, about_point, run_time=2, rate_func=linear, voiceover_text=None):
        start_x, start_y  = model_point.to_x_y()  
        angle_in_degrees = angle_in_degrees_parameter.get_value()    
        if isinstance(about_point, ModelPoint):
             about_point = about_point.to_numpy()    
        
        def update_alpha(alpha):    
            temp_point = ModelPoint(start_x, start_y)
            current_rotation = angle_in_degrees * alpha  
            rotated_point = temp_point.rotate(current_rotation, about_point)
            model_point.set(rotated_point.x, rotated_point.y) # This will notify the observers of the model point 
            
        self._play_value_tracker(update_alpha, run_time, rate_func, voiceover_text)
        
    def rotate_model(self, base_model, angle_in_degrees_parameter, about_point, run_time=2, rate_func=linear, voiceover_text=None):
        all_points = base_model.get_all_points()  
        all_point_values = [(point.to_x_y()) for point in all_points]  # rotate from the original values    
        angle_in_degrees = angle_in_degrees_parameter.get_value()    
        if isinstance(about_point, ModelPoint):
             about_point = about_point.to_numpy()    

         
        def update_alpha(alpha):     
            for index, point in enumerate(all_points):
                temp_point = ModelPoint(all_point_values[index][0], all_point_values[index][1])
                current_rotation = angle_in_degrees * alpha  
                rotated_point = temp_point.rotate(current_rotation, about_point)
                point.set(rotated_point.x, rotated_point.y, notify=False) # This will not notify the observers of the model point 
            base_model.notify()

        self._play_value_tracker(update_alpha, run_time, rate_func, voiceover_text)
        
    def translate_point(self, model_point, vector_translation, run_time=2, rate_func=linear, voiceover_text=None):
        start_x, start_y, start_z = model_point.to_x_y_z()  
      
        def update_alpha(alpha):   
            temp_point = ModelPoint(start_x, start_y, start_z)
            current_translation = vector_translation.scale_vector(alpha)
            translated_point = temp_point.translate(current_translation)
            model_point.set(translated_point.x, translated_point.y, translated_point.z)
            
        self._play_value_tracker(update_alpha, run_time, rate_func, voiceover_text)
        
    def scale_point(self, model_point, scale_factor_parameter, run_time=2, rate_func=linear, voiceover_text=None):
        start_x, start_y, start_z  = model_point.to_x_y_z()
        scale_factor = scale_factor_parameter.get_value() 

        def update_alpha(alpha):    
            temp_point = ModelPoint(start_x, start_y, start_z)
            scaled_point = temp_point.scale(scale_factor * alpha)
            model_point.set(scaled_point.x, scaled_point.y, scaled_point.z) # This will notify the observers of the model point
        
        self._play_value_tracker(update_alpha, run_time, rate_func) 
        
    def scale_model(self, base_model, scale_factor_parameter, run_time=2, rate_func=linear, voiceover_text=None):
        all_points = base_model.get_all_points()    
        all_point_values = [(point.to_x_y_z()) for point in all_points]  # scale from the original values    
        scale_factor = scale_factor_parameter.get_value() 
        
        
        def update_alpha(alpha):     
            for index, point in enumerate(all_points):
                temp_point = ModelPoint(all_point_values[index][0], all_point_values[index][1], all_point_values[index][2])
                scaled_point = temp_point.scale(scale_factor * alpha)
                point.set(scaled_point.x, scaled_point.y, scaled_point.z, notify=False) # This will not notify the observers of the model point   
            base_model.notify()
            
        self._play_value_tracker(update_alpha, run_time, rate_func, voiceover_text)  
        
    def translate_model(self, base_model, vector, run_time=2, rate_func=linear, voiceover_text=None):
        all_points = base_model.get_all_points()    
        all_point_values = [(point.to_x_y_z()) for point in all_points]  # translate from the original values    
        
        def update_alpha(alpha):     
            for index, point in enumerate(all_points):
                temp_point = ModelPoint(all_point_values[index][0], all_point_values[index][1], all_point_values[index][2])
                current_translation = vector.scale_vector(alpha)
                translated_point = temp_point.translate(current_translation)
                point.set(translated_point.x, translated_point.y, translated_point.z, notify=False) # This will not notify the observers of the model point
            base_model.notify()
            
        self._play_value_tracker(update_alpha, run_time, rate_func, voiceover_text)
    

    def rotate_to(self, model_point, target_point, about_point, run_time=2, rate_func=linear, voiceover_text=None):
        start_x, start_y, start_z  = model_point.to_x_y_z()      
        target_x, target_y, target_z = target_point.to_x_y_z()
        if isinstance(about_point, ModelPoint):
            about_point = about_point.to_numpy()        

        # Calculate the angle between source and target point
        start_vector = np.array([start_x - about_point[0], start_y - about_point[1], start_z - about_point[2]])
        target_vector = np.array([target_x - about_point[0], target_y - about_point[1], target_z - about_point[2]])

        # Calculate the angle between these vectors
        dot_product = np.dot(start_vector, target_vector)
        magnitudes = np.linalg.norm(start_vector) * np.linalg.norm(target_vector)
        angle_in_radians = np.arccos(np.clip(dot_product / magnitudes, -1.0, 1.0))
        angle_in_degrees = np.degrees(angle_in_radians)

        # Determine the direction of rotation (clockwise or counterclockwise)
        cross_product = np.cross(start_vector, target_vector)
        if cross_product[2] < 0:
            angle_in_degrees = -angle_in_degrees

        

        def update_alpha(alpha):    
            temp_point = ModelPoint(start_x, start_y, start_z)
            current_rotation = angle_in_degrees * alpha  
            rotated_point = temp_point.rotate(current_rotation, about_point)

            # Snap to target at the end to avoid floating-point errors
            if alpha >= 1:
                rotated_point = ModelPoint(target_x, target_y, target_z)

            model_point.set(rotated_point.x, rotated_point.y, rotated_point.z)  # Update the model point

        self._play_value_tracker(update_alpha, run_time, rate_func, voiceover_text)
        
    def _play_value_tracker(self, updater, run_time, rate_func, voiceover_text=None):
        value_tracker = ValueTracker(0)    
        value_tracker.add_updater(lambda d:updater(value_tracker.get_value()))
        if voiceover_text:    
              with self.scene.voiceover(voiceover_text) as tracker:
                self.scene.play(value_tracker.animate.set_value(1), 
                                run_time=tracker.duration,
                                rate_func=rate_func)
        else:           
            self.scene.play(value_tracker.animate.set_value(1), 
                            run_time=run_time,
                            rate_func=rate_func)
            
        value_tracker.remove_updater(updater)       

           
            