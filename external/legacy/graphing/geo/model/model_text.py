
from graphing.geo.model.base_model import BaseModel
from graphing.geo.model.model_part import ModelPart
from graphing.math.function_expression_utils import FunctionUtils
from manim import FadeIn, AnimationGroup
class BaseModelText(BaseModel):
    def __init__(self):
        super().__init__()
        
    @property       
    def text(self):
        raise NotImplementedError("Subclasses must implement the text property")
    
    def item(self, row_index, column_index=None)->ModelPart:
        ui_part = self.ui_part.item(row_index, column_index)
        return ModelPart(ui_part, ui_part.graphsheet, ui_part.geo_mapper, ui_part.scene,
                         item_row=row_index, item_col=column_index)
        
    def letter_range(self, word_index, letter_start, letter_end)->ModelPart:
        ui_part = self.ui_part.letter_range(word_index, letter_start, letter_end)
        return ModelPart(ui_part, ui_part.graphsheet, ui_part.geo_mapper, ui_part.scene,
                         item_row=letter_start, item_col=letter_end)
        
    def word_range(self, from_index, to_index)->ModelPart:
        ui_part = self.ui_part.word_range(from_index, to_index)
        return ModelPart(ui_part, ui_part.graphsheet, ui_part.geo_mapper, ui_part.scene,
                         item_row=from_index, item_col=to_index)
    
    def update_text(self, new_text):    
        raise NotImplementedError("Subclasses must implement the update_text method")
    
    def reveal_word_range(self, from_index, to_index = None, run_time=2, voiceover_text:str=None):
        self.ui_part.reveal_word_range(from_index, to_index, run_time, voiceover_text)
    
    def reveal_word_except(self, wordIndices:list[int], run_time=2, voiceover_text:str=None):   
        if isinstance(wordIndices, int):
           wordIndices = [wordIndices]     
        self.ui_part.reveal_word_except(wordIndices, run_time, voiceover_text)
        
    def reveal_word(self,wordIndices:list[int], run_time=2, voiceover_text:str=None): 
        if isinstance(wordIndices, int):
             wordIndices = [wordIndices] 
        self.ui_part.reveal_word(wordIndices, run_time, voiceover_text)   
        
    def reveal_word_range_effect(self, from_index, to_index = None, run_time=2, voiceover_text:str=None):
         return self.ui_part.reveal_word_range_effect(from_index, to_index, run_time, voiceover_text)
        
    def reveal_word_except_effect(self, wordIndices:list[int], run_time=2, voiceover_text:str=None):
        if isinstance(wordIndices, int):
            wordIndices = [wordIndices] 
        return self.ui_part.reveal_word_except_effect(wordIndices, run_time, voiceover_text) 
        
    def reveal_word_effect(self,wordIndices:list[int], run_time=2, voiceover_text:str=None):     
        if isinstance(wordIndices, int):
            wordIndices = [wordIndices] 
        return self.ui_part.reveal_word_effect(wordIndices, run_time, voiceover_text)   
        
    def reveal_letters_except(self, letter_items:list[tuple[int, int]], run_time=2, voiceover_text:str=None):
        return self.ui_part.reveal_letters_except(letter_items, run_time, voiceover_text)      

        
    def reveal_letters(self, letter_items:list[tuple[int, int]], run_time=2, voiceover_text:str=None):
        self.ui_part.reveal_letters(letter_items, run_time, voiceover_text)
        
    def reveal_letters_except(self, letter_items:list[tuple[int, int]], 
                              run_time=2, voiceover_text:str=None):
        return self.ui_part.reveal_letters_except(letter_items, run_time, voiceover_text)
        
    def reveal_letters_except_effect(self, letter_items:list[tuple[int, int]], 
                                     run_time=2, voiceover_text:str=None):
        return self.ui_part.reveal_letters_except_effect(letter_items, run_time, voiceover_text)         
    
   
    
    def show_subscripts(self, word_index=None):
        self.graphsheet.show_subscripts(self.ui_part,
                                        word_index = word_index)   
        return self
    
    def replace_view(self, new_view):
        self.ui_part.replace_view(new_view)
        return self
  
   
    

class ModelPlainText(BaseModelText):
    def __init__(self, text:str):
        super().__init__()
        self._text = text   
        
    @property       
    def text(self):
        return self._text
    
    def update_text(self, new_text):
        if isinstance(new_text, str):
            new_text = [new_text]
        self._text = new_text 
        self.notify()
        
class ModelMixedText(BaseModelText):
    def __init__(self, text_list:list[str]):
        super().__init__()
        self._text_list = text_list
        
    @property       
    def text(self):
        return self._text_list
     
    def update_text(self, new_text):
        if isinstance(new_text, str):
            new_text = [new_text]
        self._text_list = new_text
        self.notify()
    
        
class MathModelText(BaseModelText):
    def __init__(self, text_list:list[str]):
        super().__init__()
        self._text_list = text_list
    
    
    def update_text(self, new_text):
        if isinstance(new_text, str):
            new_text = [new_text]   
        self._text_list = new_text
        self.notify()
        
    @property       
    def text(self):
        return self._text_list
    
  
        
        
       
   
class  ModelPartialMathText(MathModelText):
    def __init__(self, text_list:list[str]):
        super().__init__(text_list)
       
    def partial_view(self):
        return self.ui_part.partial_view()  
      
        

        
        
        