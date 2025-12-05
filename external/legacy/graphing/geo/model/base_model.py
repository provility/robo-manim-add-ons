from pyee import EventEmitter
from manim import *
class BaseModel:
    def __init__(self):
        self._ee = EventEmitter()
        self.graphsheet = None
        self.geo_mapper = None
        self.scene = None
        self.ui_part = None 
        self.identifier = None  
        self.custom_display_handler = None 
        
    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        return self is other
    
    def __str__(self):
        return f"{self.__class__.__name__} at {id(self)}"   
    
    def __repr__(self):
        return f"{self.__class__.__name__} at {id(self)}"
    
    def on_display(self, custom_display_handler):
        self.custom_display_handler = custom_display_handler

    def on_change(self, handler):
        self._ee.on('change', handler)
        
    def notify(self):
        self._ee.emit('change')
     
 
        
    def on_remove(self, handler):
        """
        The corresponding UI object will remove itself
        """
        self._ee.on('destroy', handler)
        
    def anchor(self):
        return self.ui_part.anchor()

    
    def point_index(self, index ):
        raise NotImplementedError("Subclass must implement abstract point_index method  ")    
        
    def get_all_points(self):
        raise NotImplementedError("Subclass must implement abstract get_all_points method  ")    
    
    def remove(self):
        self.ui_part.remove()
        self._ee.emit('remove')    
        return self 
        
    def set_delegate(self, graphsheet, geo_mapper, scene, ui_part):
         self.graphsheet = graphsheet
         self.geo_mapper = geo_mapper
         self.scene = scene
         self.ui_part = ui_part
         
         
    def num_objects(self):
        return 1
    
    def item(self, row_index, column_index=None):
        return self
         
    def view(self):
        return self.ui_part.view()
    
    def shape_to_trace(self):
        return self.ui_part.shape_to_trace()
    
    @property    
    def color(self):
        return self.ui_part.color
    
    @property    
    def stroke_width(self):
        return self.ui_part.stroke_width
    
    @property    
    def fill_color(self):
        return self.ui_part.fill_color
    
    @property    
    def fill_opacity(self):
        return self.ui_part.fill_opacity
    
    def fade_in(self, voiceover_text:str=None)->'BaseModel':
        self.ui_part.fade_in(voiceover_text)
        return self 
    
    def un_cover(self, voiceover_text:str=None)->'BaseModel':
        self.ui_part.un_cover(voiceover_text)
        return self 
    
    def un_cover_effect(self, run_time=2, voiceover_text:str=None, remove_on_completion=True)->'BaseModel':
        return self.ui_part.un_cover_effect(run_time, voiceover_text, remove_on_completion)
    
    def fade_out(self, voiceover_text:str=None)->'BaseModel':
        self.ui_part.fade_out(voiceover_text)
        return self 
    
    def point_at(self, ratio):
        return self.ui_part.point_at(ratio)
    
         
    def shift(self, shift_arg)->'BaseModel':
         self.ui_part.shift(shift_arg) 
         return self.ui_part  
    
    def get_center(self):
        return self.ui_part.get_center()    
    
    """
    Midpoint is the mid of curve, return a ModelPoint
    unline get_center which is the center of the bounding box 
    """
    def get_midpoint(self):
        return self.ui_part.get_midpoint()
    
    """
    return a ModelPoint
    """
    def get_top(self):
        return self.ui_part.get_top()
    
    """
    return a ModelPoint
    """
    def get_bottom(self):
        return self.ui_part.get_bottom()
    
    """
    return a ModelPoint
    """
    def get_left(self):
        return self.ui_part.get_left()
    
    def get_right(self):
        return self.ui_part.get_right()
    
    """
    corner_directions ares UR, UL, DR, DL
    """
    def get_corner(self, corner_direction=UR):
        return self.ui_part.get_corner(corner_direction)
 
    def orient_to(self, model_pt_1, model_pt_2, position=0.5, buff=0.1):
         self.ui_part.orient_to(model_pt_1, model_pt_2, position, buff)
         return self.ui_part
     
    def show(self)->'BaseModel':
       self.ui_part.show()
       return self
   
    def hide(self)->'BaseModel':
        self.ui_part.hide()
        return self
    
    def scale(self, scale_factor)->'BaseModel':
        self.ui_part.scale(scale_factor)
        return self
    
    def cover(self, color=WHITE, buffer=SMALL_BUFF)->'BaseModel':
        self.ui_part.cover(buffer, color)
        return self
    
    def save_state(self):
        return self.view().save_state()
    
    def add_updater(self, updater):
        self.ui_part.add_updater(updater) 
    
    def restore_state(self):
        return self.view().restore_state()
    
    def rotate(self, angle, about_point=ORIGIN):
        return self.view().rotate(angle, about_point)
    
    def view_center(self):
        return self.view().get_center() 
  
    def always_redraw(self, method):
        return self.view().always_redraw(method)
    
    def match_width(self, model, stretch=True):
        return self.view().match_width(model.view(), stretch)
    
    def match_height(self, model, stretch=True):
        return self.view().match_height(model.view(), stretch)
    
    def match_style(self, model):
        return self.view().match_style(model.view())    
    
    def animate_move_to_target(self, 
                       target_model,
                       run_time=2,
                       voiceover_text=None,
                        path_arc=30 * DEGREES):
        self.view().generate_target()
        self.view().target.move_to(target_model.view())
        move_to_target_animation = MoveToTarget(
            self.view(),
            path_arc=path_arc,
        )
        self.graphsheet._play_animation(move_to_target_animation, 
                                        run_time=run_time,  
                                        voiceover_text=voiceover_text)
        
    
   
    def draw_effect(self, run_time=2, voiceover_text=None, remove_on_completion=False):
        return self.ui_part.draw_effect(run_time, voiceover_text, remove_on_completion)

    
    def fade_in_effect(self, run_time=2, voiceover_text=None, remove_on_completion=True):
        return self.ui_part.fade_in_effect(run_time, voiceover_text, remove_on_completion)
        
    def color_effect(self, color, stroke_width=5, run_time=2, voiceover_text=None, remove_on_completion=True):
        return self.ui_part.color_effect(color, stroke_width, run_time, voiceover_text, remove_on_completion)
    
    def stroke_effect(self, stroke_width=10, run_time=2, voiceover_text=None, remove_on_completion=True):
        return self.ui_part.stroke_effect(stroke_width, run_time, voiceover_text, remove_on_completion)
    
    def scale_effect(self, scale=1.2, run_time=2, voiceover_text=None, remove_on_completion=True):
        return self.ui_part.scale_effect(scale, run_time, voiceover_text, remove_on_completion)
    
    def surrounding_effect(self, color, buffer=SMALL_BUFF, run_time=2, voiceover_text=None, remove_on_completion=True):
        return self.ui_part.surrounding_effect(color =color, buffer=buffer, run_time=run_time, voiceover_text=voiceover_text, remove_on_completion=remove_on_completion)
    
    
    def indicate_effect(self, color=BLUE, scale_factor=1.2, run_time=2, voiceover_text=None, remove_on_completion=True):
        return self.ui_part.indicate_effect(color, scale_factor, run_time, voiceover_text, remove_on_completion)   
        
        
    def flash_effect(self, color=BLUE, run_time=2, voiceover_text=None, remove_on_completion=True):
        return self.ui_part.flash_effect(color, run_time, voiceover_text, remove_on_completion)
        
    def trace_effect(self, color=RED,run_time=2, voiceover_text=None, remove_on_completion=True):
        return self.ui_part.trace_effect(color, run_time, voiceover_text, remove_on_completion)
    
    def passing_flash_effect(self, color=BLUE, run_time=2, voiceover_text=None, remove_on_completion=True):
        return self.ui_part.passing_flash_effect(color, run_time, voiceover_text, remove_on_completion)
    
    def circumscribe_effect(self, color=BLUE, run_time=2, fade_out=True, voiceover_text=None, remove_on_completion=True):
        return self.ui_part.circumscribe_effect(color, run_time, fade_out, voiceover_text, remove_on_completion)   
    
    def underline_effect(self, color=BLUE, 
                         buff=0.1,
                         stroke_width=2,
                         run_time=2, 
                         voiceover_text=None, 
                         remove_on_completion=True):
        return self.ui_part.underline_effect(color = color, 
                                             buff = buff, 
                                             stroke_width = stroke_width, 
                                             run_time = run_time, 
                                             voiceover_text = voiceover_text, 
                                             remove_on_completion = remove_on_completion)
        
    def transform_effect(self, target_model_or_text, run_time=2, voiceover_text=None, remove_on_completion=True):
        return self.ui_part.transform_effect(target_model_or_text, run_time, voiceover_text, remove_on_completion)
    
    # overriden by ModelPoint
    @property
    def x(self):
        return self.ui_part.x
    
    @property
    def y(self):
        return self.ui_part.y   
    
    @property
    def z(self):
        return self.ui_part.z
    
    def view(self):
        return self.ui_part.view()
    

    
    @property
    def center(self):
        return self.ui_part.center
    
    @property
    def top(self):
        return self.ui_part.top   
    
    @property
    def bottom(self):
        return self.ui_part.bottom    
    
    @property
    def left(self):
        return self.ui_part.left    
    
    @property
    def right(self):
        return self.ui_part.right 
    
    def apply_style(self, color=None, fill_color=None, fill_opacity=0.5, stroke_width=None):
        self.ui_part.apply_style(color, fill_color, fill_opacity, stroke_width)
        return self
    
    def copy(self):
        return self.ui_part.copy()
        
    """
    direction example: UP, DOWN, LEFT, RIGHT
    """
    def next_to(self, other_model, direction=UP, buff=SMALL_BUFF, aligned_edge=ORIGIN)->'BaseModel':
        self.ui_part.next_to(other_model, direction, buff, aligned_edge)
        return self    
    
    """
    alignment_vector example: UP, DOWN, LEFT, RIGHT
    """     
    def align_to(self, other_model, alignment_vector)->'BaseModel':
        self.ui_part.align_to(other_model, alignment_vector)
        return self    
     
    def move_to(self, other_model_or_tuple_or_numpy_array)->'BaseModel':
        self.ui_part.move_to(other_model_or_tuple_or_numpy_array)
        return self    
    
    def to_edge(self, direction=UP, buff=0):
        self.ui_part.to_edge(direction, buff)
        return self 
    
    """
    corner example: UR, UL, DR, DL or Give combination of UP, DOWN, LEFT, RIGHT
    """
    def to_corner(self, corner=UR, buff=0.3)->'BaseModel':
        self.ui_part.to_corner(corner, buff)
        return self 
    
    def shift(self, shift_arg):
        self.ui_part.shift(shift_arg)
        return self 
    
  
  
    
    
  
       
    
  