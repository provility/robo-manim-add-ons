from manim import *

class RemoveCommandHelper:

    @staticmethod   
    def manage_commands_to_remove_on_completion(scene, *commands):
        remove_animations = []
        for command in commands:
            if command.remove_on_completion:
                undo_command_animation = command.clear()
                if undo_command_animation is not None:
                    remove_animations.append(undo_command_animation)
        if len(remove_animations) > 0:
            scene.play(*remove_animations)
    

class EffectCommand:
    def __init__(self, do_func, undo_func, scene, graph_sheet, run_time=1, 
                 voiceover_text=None, remove_on_completion=False ):
        self.do_func = do_func
        self.undo_func = undo_func
        self.scene = scene
        self.graph_sheet = graph_sheet
        self.run_time = run_time
        self.voiceover_text = voiceover_text
        self.remove_on_completion = remove_on_completion
       
          
    def build(self):
        return self.do_func()
        
    def clear(self):
        return self.undo_func()
    
    def play(self):
        if self.voiceover_text:
            with self.scene.voiceover(self.voiceover_text) as tracker:
                actual_run_time = min(tracker.duration, self.run_time) if tracker.duration else self.run_time
                self.scene.play(self.build(), run_time=actual_run_time)
        else:
            self.scene.play(self.build(), run_time=self.run_time)
            
        RemoveCommandHelper.manage_commands_to_remove_on_completion(self.scene, self)
    
    def remove_effect(self):
        remove_animations = [self.clear()]
        self.scene.play(*remove_animations)
"""
ComposeEffectCommand is used to chain multiple effects in after each other in sequence
"""    
class ComposeEffectCommand(EffectCommand):
    def __init__(self, *effects, scene, graph_sheet, voiceover_text=None, remove_on_completion=False):
        self.effects = effects
        self.scene = scene
        self.graph_sheet = graph_sheet
        self.voiceover_text = voiceover_text
        self.remove_on_completion = remove_on_completion
        
    def build(self):
        animation_group = AnimationGroup(*[effect.build() for effect in self.effects], lag_ratio=1)
        return animation_group
    
    def clear(self):
        animation_group = AnimationGroup(*[effect.clear() for effect in self.effects])
        return animation_group
    
        
class ZoomEffectCommand(EffectCommand):
    def __init__(self, scene, graph_sheet, object_to_focus, width=8, run_time=2, voiceover_text=None, remove_on_completion=False): 
        object_to_focus = object_to_focus
        box_width = width
    
        def do_func():
            scene.camera.frame.save_state()
            return scene.camera.frame.animate.move_to(object_to_focus).set(width=box_width)
            
        def undo_func():
            return Restore(scene.camera.frame)
            
        super().__init__(do_func, undo_func, scene, graph_sheet, run_time, voiceover_text, remove_on_completion)
      
        
       
        
       
class TextTransformEffectCommand(EffectCommand):
    def __init__(self, do_func, scene, graph_sheet, run_time=1, voiceover_text=None, remove_on_completion=False, copied_parts=[]):
        super().__init__(do_func, lambda: Wait(0.1), scene, graph_sheet, run_time, voiceover_text, remove_on_completion)
        self.copied_parts = copied_parts
       
        
class EffectCommandManager:
    def __init__(self, scene):
        self.scene = scene
        
    def play_parallel(self, *commands,  voiceover_text=None, run_time=2, speed=1):
        if voiceover_text:
            with self.scene.voiceover(voiceover_text) as tracker:
                actual_run_time = min(tracker.duration, run_time) if tracker.duration else run_time
                self.scene.play(*[command.build() for command in commands], run_time=actual_run_time)
        else:
            self.scene.play(*[command.build() for command in commands], run_time=run_time)
            
        RemoveCommandHelper.manage_commands_to_remove_on_completion(self.scene, *commands)
            
    def play_group(self, *commands, voiceover_text=None, run_time=2):
        animation_group = AnimationGroup(*[command.build() for command in commands], lag_ratio=1)
        if voiceover_text:
            with self.scene.voiceover(voiceover_text) as tracker:
                actual_run_time = min(tracker.duration, run_time) if tracker.duration else run_time
                self.scene.play(animation_group, run_time=actual_run_time)
        else:
            self.scene.play(animation_group, run_time=run_time)
        
    def play_sequence(self, *commands):
        for command in commands:
            if command.voiceover_text:
                with self.scene.voiceover(command.voiceover_text) as tracker:
                    self.scene.play(command.build(), run_time=tracker.duration)
            else:
                self.scene.play(command.build(), run_time=command.run_time)
            if command.remove_on_completion:
                self.scene.play(command.clear())
                
    def play_with_voice_fragments(self, *commands):
        alphabet_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  
        all_voiceover_texts = self.create_voice_fragments(*[command.voiceover_text for command in commands])
        with self.scene.voiceover(all_voiceover_texts) as tracker:  
             for command_index, command in enumerate(commands):
                self.scene.wait_until_bookmark(alphabet_list[command_index])
                if command_index < len(commands) - 1:
                    next_bookmark = alphabet_list[command_index + 1] 
                    next_run_time = tracker.time_until_bookmark(next_bookmark)
                    self.scene.play(
                        command.build(), run_time=next_run_time
                    )
                else:
                    self.scene.play(command.build(), run_time=tracker.get_remaining_duration(buff=-1))
                    
        RemoveCommandHelper.manage_commands_to_remove_on_completion(self.scene, *commands)
                    
    def create_voice_fragments(self, *voiceover_texts):
        book_mark_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        all_voiceover_ssml = ""
        for index, voiceover_text in enumerate(voiceover_texts):
            book_mark = book_mark_alphabet[index]
            all_voiceover_ssml+="\n"
            all_voiceover_ssml+= f"<bookmark mark='{book_mark}'/>{voiceover_text}"  
            all_voiceover_ssml+="\n"
        return all_voiceover_ssml           

    def clear(self, *commands):
        self.scene.play(*[command.clear() for command in commands])
     
    
        
        
        
        
