from manim import *

from graphing.geo.effect_command import  ComposeEffectCommand, EffectCommand,TextTransformEffectCommand


class TextAnimator:
    def __init__(self, scene, graph_sheet):
        self.scene = scene
        self.graph_sheet = graph_sheet
        self.implicitly_created_objects = []    
        
 
    def play_coordinate_move_then_draw(self, text_model, target_model_point,
                          model_to_draw, color=BLUE, run_time=2, voiceover_text=None):
        move_effect = self.move_text_to_point_effect(
            text_model=text_model, 
            target_model_point=target_model_point, 
            run_time=run_time, 
            voiceover_text=voiceover_text, 
            remove_on_completion=False)
        axis_lines_effect = self.axis_lines_effect(target_model_point,
                                                   model_to_draw, 
                                                   color=color,
                                                   run_time=run_time,
                                                   voiceover_text=voiceover_text, 
                                                   remove_on_completion=False)
        
        draw_effect =  model_to_draw.draw_effect(run_time=run_time,
                                                  remove_on_completion=False)
        
        self.graph_sheet.play_sequence_effects(move_effect, axis_lines_effect, draw_effect)
        self.graph_sheet.wait(2)
        self.graph_sheet.clear_effects(move_effect, axis_lines_effect)
        
    """
    Useful for transforming equations or expressions
    """
    def text_arrangement_effect(self, source_model, target_terms, key_map={}, target_scale=None, run_time=2, voiceover_text=None):
        def do_func():
            target_math_text = MathTex(*target_terms)
            target_math_text.match_style(source_model.view())       
            if target_scale is not None:
                target_math_text.scale(target_scale)  # Match scale based on width
            target_math_text.move_to(source_model.view())    
            self.implicitly_created_objects.append(target_math_text)    
            return TransformMatchingShapes(source_model.view(), target_math_text, key_map=key_map)
        effect_command = TextTransformEffectCommand(do_func,
                                                    scene=self.scene, 
                                                    graph_sheet=self.graph_sheet, 
                                                    run_time=run_time, 
                                                    voiceover_text=voiceover_text)
        return effect_command
        

    def move_text_to_text_effect(self, source_parts, target_parts,
                                 match_shape=True, run_time=2, voiceover_text=None):
        copied_parts = []   
        def do_func():
            nonlocal copied_parts
            for source in source_parts:
                copied_parts.append(source.copy())  # comprehension will create a list  so use append     
            
            self.implicitly_created_objects.extend(copied_parts)
            copy_move_transforms = []   
            if match_shape:
                copy_move_transforms = [TransformMatchingShapes(copied_item, target.view(), replace_mobject_with_target_in_scene=True) for copied_item, target in zip(copied_parts, target_parts)]
            else:
                copy_move_transforms = [Transform(copied_item, target.view(), replace_mobject_with_target_in_scene=True) for copied_item, target in zip(copied_parts, target_parts)]
            return AnimationGroup(*copy_move_transforms, lag_ratio=0)
        effect_command = TextTransformEffectCommand(do_func, 
                                                    scene=self.scene, 
                                                    graph_sheet=self.graph_sheet, 
                                                    run_time=run_time, 
                                                    voiceover_text=voiceover_text, 
                                                    copied_parts=copied_parts)
        return effect_command

    def surround_text_effect(self, text_parts, color=GREEN, buffer_factor=0.1,
                             run_time=2, voiceover_text=None, remove_on_completion=True):
        surrounding_rectangles =[]
        def do_func():
            nonlocal surrounding_rectangles
            surrounding_rectangles = [SurroundingRectangle(text_part.view(), buff=buffer_factor, color=color) for text_part in text_parts]
            animations = [Create(rectangle) for rectangle in surrounding_rectangles]
            return AnimationGroup(*animations, lag_ratio=0)
           
        def undo_func():
            return AnimationGroup(*[FadeOut(rect) for rect in surrounding_rectangles], lag_ratio=0)
    
        effect_command = EffectCommand(do_func, undo_func, 
                                      scene=self.scene, 
                                      graph_sheet=self.graph_sheet, 
                                      run_time=run_time, 
                                      voiceover_text=voiceover_text, 
                                      remove_on_completion=remove_on_completion)
        return effect_command
    
    def circumscribe_text(self, text_parts, color=GREEN, buffer_factor=0.2, run_time=2, voiceover_text=None, remove_on_completion=True):
        circles = []
        
        def do_func():
            nonlocal circles
            circles = [Circle(color=color).surround(text_part.view(), buffer_factor=buffer_factor) for text_part in text_parts]
            animations = [Create(circle) for circle in circles]
            return AnimationGroup(*animations, lag_ratio=0)
        
        def undo_func():
            nonlocal circles
            return AnimationGroup(*[FadeOut(circle) for circle in circles], lag_ratio=0)
        
        effect_command = EffectCommand(do_func, undo_func, 
                                      scene=self.scene, 
                                      graph_sheet=self.graph_sheet, 
                                      run_time=run_time, 
                                      voiceover_text=voiceover_text, 
                                      remove_on_completion=remove_on_completion)
        return effect_command   
  
    def move_text_to_point_effect(self, text_model, target_model_point, run_time=2, 
                          voiceover_text=None, remove_on_completion=True):
        cloned_text_model = text_model.copy()
        self.implicitly_created_objects.append(cloned_text_model)
       
        def move_func():
            nonlocal cloned_text_model
            geo_mapper = self.graph_sheet.geo_mapper
            target_ui_point = geo_mapper.model_point_to_ui_point(target_model_point)
            return cloned_text_model.animate.move_to(target_ui_point)
        
        def undo_func():
            return FadeOut(cloned_text_model)
        
        effect_command = EffectCommand(move_func, undo_func, scene=self.scene, 
                             graph_sheet=self.graph_sheet, 
                             run_time=run_time, remove_on_completion=remove_on_completion,
                             voiceover_text=voiceover_text) 
        return effect_command
        
        
    def axis_lines_effect(self, target_model_point, axis_lines, 
                          color=BLUE,
                          run_time=1, voiceover_text=None, remove_on_completion=True):
        axis_lines = None
        
        def do_func():
            nonlocal axis_lines
            geo_mapper = self.graph_sheet.geo_mapper
            axes = geo_mapper.axes  
            target_ui_point = geo_mapper.model_point_to_ui_point(target_model_point)    
            axis_lines = axes.get_lines_to_point(target_ui_point)
            axis_lines.set_color(color)
            axis_lines.set_stroke(width=2)
            return Create(axis_lines)
        
        def undo_func():
            return FadeOut(axis_lines)
        
        effect_command = EffectCommand(do_func, undo_func, scene=self.scene, graph_sheet=self.graph_sheet, 
                                      run_time=run_time, remove_on_completion=remove_on_completion, 
                                      voiceover_text=voiceover_text)
        return effect_command
        

    def reveal_text_effect(self, model_text, 
                           reveal_from_index,
                           run_time=2, voiceover_text=None):
        
        def do_func():
            tex = model_text.view()  
            objects_to_fade_in = tex[reveal_from_index:]
            self.implicitly_created_objects.extend(objects_to_fade_in)
            return FadeIn(*objects_to_fade_in)
        
        def undo_func():
            return Wait(0.1)
        
        effect_command = EffectCommand(do_func, undo_func, scene=self.scene, graph_sheet=self.graph_sheet, 
                                      run_time=run_time, remove_on_completion=False, 
                                      voiceover_text=voiceover_text)
        return effect_command
    
    """
    Useful for replacing parts of a math text
    model_text Must be a PartialMathModelText created by partial_math_text method     
    """
    
    def replace_text_effect(self, model_text, from_parts_indexes, 
                           to_part_indexes, 
                           text_items_to_fade_in=[],
                           run_time=2, voiceover_text=None):
        
        def do_func():
            tex = model_text.view()  
            replace_transforms =  [
                ReplacementTransform(tex[i].copy(),tex[j],run_time=run_time)
                for i,j in zip(from_parts_indexes,to_part_indexes)]
            for item_index in  text_items_to_fade_in:
                replace_transforms.append(FadeIn(tex[item_index]))
            self.implicitly_created_objects.extend(tex[item_index] for item_index in  text_items_to_fade_in)    
            return AnimationGroup(*replace_transforms, lag_ratio=0)  
        
        def undo_func():
            return Wait(0.1)
        
        effect_command = EffectCommand(do_func, undo_func, scene=self.scene, graph_sheet=self.graph_sheet, 
                                      run_time=run_time, remove_on_completion=False, 
                                      voiceover_text=voiceover_text)
        return effect_command
    
    
    def clear_implicitly_created_objects(self):
        for obj in self.implicitly_created_objects:
            if obj in self.scene.mobjects or any(sub in self.scene.mobjects for sub in obj.submobjects):
                 self.scene.remove(obj)

        self.implicitly_created_objects = []    
        
        
    def transform_effect(self, source_model, target_model,
                    run_time=2, voiceover_text=None)->EffectCommand:
        target_moObject_copy= None
        def do_func():
            nonlocal target_moObject_copy
            target_moObject_copy= target_model.view().copy()
            original_position = source_model.view().get_center()  
            self.implicitly_created_objects.append(target_moObject_copy)   
            target_moObject_copy.set_color(source_model.view().get_color())
            target_moObject_copy.set_z_index(100)
            target_moObject_copy.move_to(original_position)
            target_moObject_copy.set_opacity(1)
            # Create a Transform animation for smooth transition
            
            transform_animation = Transform(source_model.view(), target_moObject_copy)
            return transform_animation

        def undo_func():
            return FadeOut(target_moObject_copy)
        
        effect_command = EffectCommand(do_func, undo_func, scene=self.scene, graph_sheet=self.graph_sheet, 
                                      run_time=run_time, remove_on_completion=False, 
                                      voiceover_text=voiceover_text)
        return effect_command
    
    
    def underline_text_effect(self, text_model, color=BLUE, run_time=2, voiceover_text=None):
        underline = None
        def do_func():
            nonlocal underline
            underline = Line(LEFT, RIGHT)
            underline.set_width(text_model.view().width)
            underline.next_to(text_model.view(), DOWN, buff=0.1)
            underline.set_color(color)
            underline.set_stroke(width=2)
            return Create(underline)
        
        def undo_func():
            return FadeOut(underline)
        
        effect_command = EffectCommand(do_func, undo_func, scene=self.scene, graph_sheet=self.graph_sheet, 
                                      run_time=run_time, remove_on_completion=False, 
                                      voiceover_text=voiceover_text)
        return effect_command
