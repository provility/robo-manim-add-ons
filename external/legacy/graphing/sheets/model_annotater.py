from manim import *

class AnnotationGroup:
    def __init__(self, *model_objects):
        self.model_objects = model_objects
        
    def draw_effect(self):
        all_draw_effects = []
        for model_object in self.model_objects:
            all_draw_effects.append(model_object.draw_effect())
        return all_draw_effects
        
class ModelAnnotater:
    def __init__(self, graph_sheet):
        self.graph_sheet = graph_sheet
    
    """
    Returns an AnnotationGroup containing the side labels 
    """
    def annotate_triangle_side_labels(self, triangle_model, *side_names, color=BLACK, directions=[DOWN, DOWN, DOWN]):
         side_text_a = self.graph_sheet.aligned_text(side_names[0], triangle_model.point_a, triangle_model.point_b, no_animate=True, direction=directions[0]).hide()
         side_text_b = self.graph_sheet.aligned_text(side_names[1], triangle_model.point_b, triangle_model.point_c, no_animate=True, direction=directions[1]).hide()
         side_text_c = self.graph_sheet.aligned_text(side_names[2], triangle_model.point_c, triangle_model.point_a, no_animate=True, direction=directions[2]).hide()
         return AnnotationGroup(side_text_a, side_text_b, side_text_c)
    
    """"
    Returns an AnnotationGroup containing the angles and their labels   
    """ 
    def annotate_triangle_angles(self, triangle_model, *angle_names, colors=[BLUE, GREEN, RED], radius=0.8, fill_opacity=0.3, directional_arrow=False):
        angle_B = self.graph_sheet.interior_angle(triangle_model.point_b,triangle_model.point_a,triangle_model.point_c, color=colors[0], radius=radius, fill_opacity=fill_opacity, no_animate=True, directional_arrow=directional_arrow).hide()
        angle_C = self.graph_sheet.interior_angle(triangle_model.point_c,triangle_model.point_b,triangle_model.point_a, color=colors[1], radius=radius, fill_opacity=fill_opacity, no_animate=True, directional_arrow=directional_arrow).hide()
        angle_A = self.graph_sheet.interior_angle(triangle_model.point_a,triangle_model.point_c,triangle_model.point_b, color=colors[2], radius=radius, fill_opacity=fill_opacity, no_animate=True, directional_arrow=directional_arrow).hide()     
        return AnnotationGroup(angle_B, angle_C, angle_A)
        
