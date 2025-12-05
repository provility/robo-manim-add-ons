from graphing.geo.geo_shape_props import ZIndex
from graphing.geo.model.model_text import BaseModelText, MathModelText, ModelMixedText, ModelPlainText
from graphing.geo.ui.base_ui import BaseUI
from graphing.geo.ui.ui_part import UIPart
from graphing.geo.ui.ui_style_props import UIStyleProps
from manim import *

class UIText(BaseUI):   
    def __init__(self, style_props:UIStyleProps) -> None:
        super().__init__(style_props)
        self.text_obj = None
        self.create()
        
    def create(self):
        self.text_obj = self.to_ui_tex()
        self.text_obj.set_color(self.style_props.color)
        self.text_obj.scale(self.style_props.scale_factor)
        self.text_obj.set_z_index(ZIndex.DOT.value)
         
    def update(self):
        original_position = self.text_obj.get_center()  
        new_text_obj = self.to_ui_tex()
        # Preserve the original position
        new_text_obj.move_to(original_position)
        new_text_obj.set_color(self.style_props.color)
        new_text_obj.scale(self.style_props.scale_factor)
        new_text_obj.set_z_index(ZIndex.DOT.value)
        self.text_obj.become(new_text_obj)
       
    def view(self):
        return self.text_obj
    
    def to_ui_tex(self):
        raise NotImplementedError("Subclasses must implement the to_ui_tex method")
    
    def item(self, index, column_index=0):
        shape  = self.element(index, column_index)
        ui_part = UIPart(shape, self.graphsheet, self.geo_mapper, self.scene, style_props=self.style_props)
        return ui_part    
    
    def letter_range(self, word_index, start_index, end_index):
        shape  = self.element_letter_range(word_index,start_index, end_index)
        ui_part = UIPart(shape, self.graphsheet, self.geo_mapper, self.scene, style_props=self.style_props)
        return ui_part  
    
    def word_range(self, from_index, to_index):
        shape  = self.element_word_range(from_index, to_index)
        ui_part = UIPart(shape, self.graphsheet, self.geo_mapper, self.scene, style_props=self.style_props)
        return ui_part  
    
    def remove_part(self, part):
        part_to_remove = part.view()    
        self.text_obj.submobjects = [
            mob for mob in self.text_obj.submobjects if mob != part_to_remove
        ]
    
    def _draw_effect_animation(self, object_render):
        return Write(object_render)  
    
    def element(self, index, column_index=0):
        # ignore column_index for now
        return self.text_obj[index] 
    
    def element_letter_range(self, word_index, start_index, end_index):
        return self.text_obj[word_index][start_index:end_index+1]
    
    def element_word_range(self, from_index, to_index):
        return self.text_obj[from_index:to_index]
    
    
    def replace_view(self, new_view):
        self.text_obj.become(new_view)
        return self
        
    def reveal_word_range(self, from_index, to_index = None, run_time=2, voiceover_text:str=None):
        text_objects = self._get_word_range(from_index=from_index, to_index=to_index)
        self.graphsheet._fade_in_manim_objects(text_objects, run_time, voiceover_text)
    
    def reveal_word_except(self, wordIndices:list[int], run_time=2, voiceover_text:str=None):
        text_objects = self._get_word_except(wordIndices=wordIndices)
        self.graphsheet._fade_in_manim_objects(text_objects, run_time, voiceover_text)      
         
    def reveal_word(self,wordIndices:list[int], run_time=2, voiceover_text:str=None):     
        text_objects = self._get_word(wordIndices=wordIndices)
        self.graphsheet._fade_in_manim_objects(text_objects, run_time, voiceover_text)     
        
    def reveal_word_range_effect(self, from_index, to_index = None, run_time=2, voiceover_text:str=None):
        text_objects = self._get_word_range(from_index=from_index, to_index=to_index)
        return self.graphsheet._fade_in_manim_object_effect(text_objects, run_time, voiceover_text)   
        
    def reveal_word_except_effect(self, wordIndices:list[int], run_time=2, voiceover_text:str=None):
        text_objects = self._get_word_except(wordIndices=wordIndices)
        return self.graphsheet._fade_in_manim_object_effect(text_objects, run_time, voiceover_text)  
        
    def reveal_word_effect(self,wordIndices:list[int], run_time=2, voiceover_text:str=None):     
        text_objects = self._get_word(wordIndices=wordIndices)
        return self.graphsheet._fade_in_manim_object_effect(text_objects, run_time, voiceover_text)      
    
    def reveal_letters(self, letter_items:list[tuple[int, int]], run_time=2, voiceover_text:str=None):
        text_objects = self._get_letter_objects(letter_items)
        self.graphsheet._fade_in_manim_objects(text_objects, run_time, voiceover_text)  
        
    def reveal_letters_effect(self, letter_items:list[tuple[int, int]], run_time=2, voiceover_text:str=None):
        text_objects = self._get_letter_objects(letter_items)
        return self.graphsheet._fade_in_manim_object_effect(text_objects, run_time, voiceover_text)  
        
    def reveal_letters_except(self, letter_items:list[tuple[int, int]], 
                              run_time=2, voiceover_text:str=None):
        text_objects = self._get_letters_except(letter_items)
        self.graphsheet._fade_in_manim_objects(text_objects, run_time, voiceover_text)
        
    def reveal_letters_except_effect(self, letter_items:list[tuple[int, int]], 
                                     run_time=2, voiceover_text:str=None):
        text_objects = self._get_letters_except(letter_items)
        return self.graphsheet._fade_in_manim_object_effect(text_objects, run_time, voiceover_text) 
   
    def _get_letter_objects(self, letter_items:list[tuple[int, int]]):
        text_objects = []
        for row, col in letter_items:
            text_objects.append(self.text_obj[row][col])
            
        return text_objects
   
    def _get_letters_except(self, letter_items:list[tuple[int, int]]):
        text_objects = []
        total_words = len(self.text_obj)
        
        def is_excluded(row, col):
            return (row, col) in letter_items
        
        for row in range(0, total_words):    
            word = self.text_obj[row]
            for col in range(0, len(word)):
                if not is_excluded(row, col):
                    text_objects.append(word[col])
                    
        return text_objects            
   
    def _get_word_except(self, wordIndices:list[int]):
         to_index = len(self.text_obj)
         text_objects = []
         for row in range(0, to_index):
            if row not in wordIndices: 
               text_objects.append(self.text_obj[row])
              
         return text_objects         
     
    def _get_word(self, wordIndices):
        text_objects = []  
        for row in wordIndices:
            text_objects.append(self.text_obj[row])   
            
        return text_objects     
    
    def _get_word_range(self,from_index, to_index = None):
        if to_index is None:    
            to_index = len(self.text_obj)
        text_objects = []    
        for row in range(from_index, to_index):
            text_objects.append(self.text_obj[row])
          
        return text_objects   
    
   
     
class UIPlainText(UIText):
    def __init__(self, model_text:ModelPlainText, style_props:UIStyleProps) -> None:
        self.model_text = model_text
        super().__init__(style_props)
        
    def to_ui_tex(self):
        return Text(self.model_text.text) 
    
  
    
class UIMixedText(UIText):
    def __init__(self, model_text:ModelMixedText, style_props:UIStyleProps) -> None:
        self.model_text = model_text
        super().__init__(style_props)
        
    def to_ui_tex(self):
        return Tex(*self.model_text.text)    
    
   
    
class UIMathTex(UIText):
    def __init__(self, model_text:MathModelText, style_props:UIStyleProps) -> None:
        self.model_text = model_text
        super().__init__(style_props)
        
    def to_ui_tex(self):
        # text is a list of string for math tex
        return MathTex(*self.model_text.text)
    
    
    
    def _ui_parts_from_text_objects(self, text_objects):
        return [UIPart(text_item, self.graphsheet, geo_mapper=self.geo_mapper, scene=self.scene, style_props=self.style_props) for text_item in text_objects]
       
            
        
class UIPartialMathTex(UIMathTex):
    def __init__(self, model_text:MathModelText, style_props:UIStyleProps, upto_index:int) -> None:
        self.upto_index = upto_index
        super().__init__(model_text, style_props)

    def view(self):
        return self.text_obj
    
    def partial_view(self):
        return self.text_obj[:self.upto_index]    
    
    def view_to_render(self):
        return self.partial_view()  
    
    
    
 
         
    
    
   
    

