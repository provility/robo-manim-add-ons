from manim import *


from graphing.geo.arg_utils import ArgUtils
from graphing.geo.effect_command import EffectCommand
from graphing.geo.geo_shape_props import ZIndex
from graphing.geo.model.model_part import ModelPart
from graphing.geo.model.model_point import ModelPoint
from graphing.geo.ui.ui_style_props import UIStyleProps
class BaseUI:
    def __init__(self, style_props:UIStyleProps) -> None:
        self.style_props = style_props
        self.graphsheet = None
        self.geo_mapper = None  
        self.scene = None   
        self.custom_display_handler = None
        self.covering_rectangle = None
        
    def set_delegate(self, graphsheet, geo_mapper, scene):
        self.graphsheet = graphsheet
        self.geo_mapper = geo_mapper
        self.scene = scene
        
    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        return self is other  
    
    def view(self):
        raise NotImplementedError("view method not implemented")  
    
    def point_at(self, ratio):
        return self.view().point_from_proportion(ratio)

    
    def update(self):
        raise NotImplementedError("update method not implemented in class name " + self.__class__.__name__) 

    def set_dynamic(self):
        if self.custom_display_handler is not None:
            def updater(mob):   
                self.update()   
                self.custom_display_handler(self)
                
            self.view().add_updater(updater)
        else:
            self.view().add_updater(lambda mob: self.update())
    
    def add_updater(self, updater):
        self.view().add_updater(updater) 
    
    @property    
    def color(self):
        return self.style_props.color
    
    @property    
    def stroke_width(self):
        return self.style_props.stroke_width
    
    @property    
    def fill_color(self):
        return self.style_props.fill_color
    
    @property    
    def fill_opacity(self):
        return self.style_props.fill_opacity
    
   

    def apply_style(self, color=None, fill_color=None, fill_opacity=0.5, stroke_width=None):
        if fill_color is not None:
            self.view().set_fill(color=fill_color, opacity=fill_opacity)
        if stroke_width is not None:
            self.view().set_stroke(width=stroke_width)
        if color is not None:
            self.view().set_color(color)
        if stroke_width is not None:
            self.view().set_stroke(width=stroke_width)    
    
     # the shift org is RIGHT, LEFT, UP, DOWN etc          
    def shift(self, shift_arg):
         numpy_point = ArgUtils.extract_num_py_point(shift_arg)   
         self.view().shift(numpy_point)
    
    # the next org is RIGHT, LEFT, UP, DOWN etc       
    def next_to(self, model_name_or_model_ref, direction, buff=SMALL_BUFF, aligned_edge=ORIGIN):
        if isinstance(model_name_or_model_ref, VMobject):
            m_object = model_name_or_model_ref
        else:
            ui_ref = self.graphsheet._get_ui_object(model_name_or_model_ref)
            m_object  = ui_ref.view()
            
        direction = ArgUtils.extract_num_py_point(direction)   
        self.view().next_to(m_object, direction, buff=buff, aligned_edge = aligned_edge)  
        
    def align_to(self, model_name_or_model_ref, align_org):
        if isinstance(model_name_or_model_ref, VMobject):
            m_object = model_name_or_model_ref
        else:
            ui_ref = self.graphsheet._get_ui_object(model_name_or_model_ref)
            m_object  = ui_ref.view()
        align_org = ArgUtils.extract_num_py_point(align_org)   
        self.view().align_to(m_object, align_org)
        
    def orient_to(self, pt1_name_or_model_or_tuple, pt2_name_or_model_or_tuple, position=0.5, buff=0.1):
        model_point_1 = self.graphsheet._point_from_input(pt1_name_or_model_or_tuple)
        model_point_2 = self.graphsheet._point_from_input(pt2_name_or_model_or_tuple)
        ui_point1 = self.geo_mapper.to_screen_point(model_point_1)
        ui_point2 = self.geo_mapper.to_screen_point(model_point_2)
        line = Line(ui_point1, ui_point2)   
       
         # Get the angle of the line
        angle = line.get_angle()
        
        # Rotate the text to match the line's angle
        self.text_obj.rotate(angle)
        
        # Position the text along the line
        point = line.point_from_proportion(position)
        self.view().move_to(point)
        
        # Optionally, offset the text slightly
        self.view().next_to(point, direction=normalize(line.get_vector()), buff=buff)
        
    def move_to(self, pt_name_or_model_or_tuple):
        if isinstance(pt_name_or_model_or_tuple, VMobject):
            m_object = pt_name_or_model_or_tuple
            self.view().move_to(m_object)
            return
        
        model_point = self.graphsheet._point_from_input(pt_name_or_model_or_tuple)
        if model_point is not None: 
            ui_point = self.geo_mapper.to_screen_point(model_point)
            self.view().move_to(ui_point)     
            return
        
        ref_object = self.graphsheet.get_ui_object(pt_name_or_model_or_tuple)
        m_object = ref_object.view()
        self.view().move_to(m_object)
       
            
    def to_corner(self, corner, buff):
        self.view().to_corner(corner, buff)
        
    def to_edge(self, direction, buff):
        self.view().to_edge(direction, buff)
    
    def anchor(self):
        return self.view().get_center()
    
    @property
    def center(self):
        return self.get_center()    
    
    @property
    def midpoint(self):
        return self.get_midpoint()
    
    @property
    def top(self):
        return self.get_top()   
    
    @property
    def bottom(self):
        return self.get_bottom()    
    
    @property
    def left(self):
        return self.get_left()    
    
    @property
    def right(self):
        return self.get_right()     
    
    
    def get_center(self):
        view_center = self.view().get_center()
        model_coords = self.geo_mapper.ui_to_model(view_center[0], view_center[1], view_center[2])
        return ModelPoint(model_coords[0], model_coords[1])
    
    def get_midpoint(self):
        view_midpoint = self.view().get_midpoint()
        model_coords = self.geo_mapper.ui_to_model(view_midpoint[0], view_midpoint[1], view_midpoint[2])
        return ModelPoint(model_coords[0], model_coords[1]) 
    
    def get_top(self):
        view_top = self.view().get_top()
        model_coords = self.geo_mapper.ui_to_model(view_top[0], view_top[1], view_top[2])
        return ModelPoint(model_coords[0], model_coords[1])
   
    def get_bottom(self):
        view_bottom = self.view().get_bottom()
        model_coords = self.geo_mapper.ui_to_model(view_bottom[0], view_bottom[1], view_bottom[2])
        return ModelPoint(model_coords[0], model_coords[1])
    
    def get_left(self):
        view_left = self.view().get_left()
        model_coords = self.geo_mapper.ui_to_model(view_left[0], view_left[1], view_left[2])
        return ModelPoint(model_coords[0], model_coords[1])
    
    def get_right(self):
        view_right = self.view().get_right()
        model_coords = self.geo_mapper.ui_to_model(view_right[0], view_right[1], view_right[2])
        return ModelPoint(model_coords[0], model_coords[1]) 
    
    def get_corner(self, corner_direction):
        view_corner = self.view().get_corner(corner_direction)
        model_coords = self.geo_mapper.ui_to_model(view_corner[0], view_corner[1], view_corner[2])
        return ModelPoint(model_coords[0], model_coords[1]) 
    
    @property
    def x(self):
        view_center = self.view().get_center()
        np_ui =  self.geo_mapper.ui_to_model(view_center[0], view_center[1])
        return np_ui[0]
    
    @property
    def y(self):
        view_center = self.view().get_center()
        np_ui =  self.geo_mapper.ui_to_model(view_center[0], view_center[1])
        return np_ui[1]
    
    def shape_to_trace(self):
        return self.view()          
    
    def show(self):
        self.view().set_opacity(1)
        
    def cover(self, buffer=SMALL_BUFF, background_color=WHITE):
        view_width =  self.view().get_right()[0] - self.view().get_left()[0] # returns a tuple so get x
        view_height = self.view().get_top()[1] - self.view().get_bottom()[1] # returns a tuple so get y
        
        self.covering_rectangle = Rectangle(
            width=view_width + buffer,  
            height=view_height + buffer
        ).set_fill(background_color, opacity=1).set_stroke(width=0)
        self.covering_rectangle.set_z_index(ZIndex.COVERING_RECTANGLE.value)
        self.covering_rectangle.move_to(self.view())
        self.scene.add(self.covering_rectangle) 
        self.graphsheet.add_covering_rectangle(self.covering_rectangle)
        return self


    def fade_in(self, voiceover_text=None):
        self.graphsheet._play_fade_in(self.view_to_render(), 
                                      fill_opacity=self.fill_opacity,
                                      voiceover_text=voiceover_text)
        
    def un_cover(self, voiceover_text=None):
        self.graphsheet._play_fade_out(self.covering_rectangle, voiceover_text=voiceover_text)  
        
    def fade_out(self, voiceover_text=None):
        self.graphsheet._play_fade_out(self.view(), voiceover_text=voiceover_text)

        
    def scale(self, scale_factor):
        self.view().scale(scale_factor)
        return self
    
    def copy(self):
        return self.view().copy()
           
    def remove(self):
        if isinstance(self.view(), VGroup):   
            for v in self.view():
                self.scene.remove(v)
        else:
            self.scene.remove(self.view())
    
    def hide(self):
        self.view_to_render().set_opacity(0)
        
    def apply_fill(self, fill_opacity):
        self.view_to_render().set_fill(opacity=fill_opacity)
        
    def view_to_render(self):
        return self.view()   
    
    def _draw_effect_animation(self, object_render):
        return Create(object_render) 
        
    def draw_effect(self, run_time=2, voiceover_text=None, remove_on_completion=False):
        object_render = self.view_to_render()
       
        def do_func():
           self.show()
           self.apply_fill(self.fill_opacity)  
           return self._draw_effect_animation(object_render)
        
        def undo_func():
            if remove_on_completion:
                return FadeOut(object_render)
            else:
                return Wait(0)
        
        effect_command = EffectCommand(do_func, undo_func, 
                                       scene=self.scene, 
                                       graph_sheet=self.graphsheet, 
                                       run_time=run_time, 
                                       voiceover_text=voiceover_text)
        return effect_command

        
    
    def fade_in_effect(self, run_time=2, voiceover_text=None, remove_on_completion=True):
        object_render = self.view()
        def do_func():
            object_render.set_opacity(1)
            return FadeIn(object_render)
        
        def undo_func():
            return FadeOut(object_render)
        
        effect_command = EffectCommand(do_func, undo_func,
                                       scene=self.scene, 
                                       graph_sheet=self.graphsheet, 
                                       run_time=run_time, 
                                       voiceover_text=voiceover_text, 
                                       remove_on_completion=remove_on_completion)
        return effect_command
    
    def un_cover_effect(self, run_time=2, voiceover_text=None, remove_on_completion=True):
        def do_func():
            return FadeOut(self.covering_rectangle)
        
        effect_command = EffectCommand(do_func, lambda: None,
                                       scene=self.scene, 
                                       graph_sheet=self.graphsheet, 
                                       run_time=run_time, 
                                       voiceover_text=voiceover_text, 
                                       remove_on_completion=remove_on_completion)
        return effect_command   
    
    def color_effect(self, color, stroke_width=5, run_time=2, voiceover_text=None, remove_on_completion=True):
        current_color = self.view().get_color()
        do_func = lambda: self.view().animate.set_color(color).set_stroke_width(stroke_width)
        undo_func = lambda: self.view().animate.set_color(current_color).set_stroke_width(self.stroke_width)
        effect_command = EffectCommand(do_func, undo_func,
                                       scene=self.scene, 
                                       graph_sheet=self.graphsheet, 
                                       run_time=run_time, 
                                       voiceover_text=voiceover_text, 
                                       remove_on_completion=remove_on_completion)
        return effect_command   
       
    def stroke_effect(self, stroke_width=15, run_time=2, voiceover_text=None, remove_on_completion=True):
        current_stroke_width = self.view().get_stroke_width()
        def do_func():
            return self.view().animate.set_stroke_width(stroke_width)
        
        def undo_func():
            return self.view().animate.set_stroke_width(current_stroke_width)
        
        effect_command = EffectCommand(do_func, undo_func,
                                       scene=self.scene, 
                                       graph_sheet=self.graphsheet, 
                                       run_time=run_time, 
                                       voiceover_text=voiceover_text, 
                                       remove_on_completion=remove_on_completion)
        return effect_command
    
    # Be careful with this one. It scales the object to the new scale and then scales it back to the original scale.
    # This is not a good idea if the object distorts the geometry.
    # Could be useful for point though
    
    def scale_effect(self, scale=1.2, run_time=1, voiceover_text=None, remove_on_completion=True):
        manim_object = self.view()
        original_height = manim_object.get_height()
        
        def do_func():
            return manim_object.animate.scale(scale)
        
        def undo_func():
            current_height = manim_object.get_height()
            scale_back = original_height / current_height
            return manim_object.animate.scale(scale_back)

        effect_command = EffectCommand(do_func, undo_func,
                                       scene=self.scene, 
                                       graph_sheet=self.graphsheet, 
                                       run_time=run_time, 
                                       voiceover_text=voiceover_text, 
                                       remove_on_completion=remove_on_completion)
        return effect_command

    def surrounding_effect(self, color, buffer=SMALL_BUFF, run_time=2, voiceover_text=None, remove_on_completion=True):
        highlight = SurroundingRectangle(self.view(), color=color, buff=buffer)
        do_func = lambda: Create(highlight)
        undo_func = lambda: FadeOut(highlight)
        effect_command = EffectCommand(do_func, undo_func,
                                       scene=self.scene, 
                                       graph_sheet=self.graphsheet, 
                                       run_time=run_time, 
                                       voiceover_text=voiceover_text, 
                                       remove_on_completion=remove_on_completion)
        return effect_command
      
    
     
        
        
    def indicate_effect(self, color=BLUE, scale_factor=1.2, run_time=2, voiceover_text=None, remove_on_completion=True):
        indicate = Indicate(self.view(), scale_factor=1.2, color=color)
        do_func = lambda: indicate
        undo_func = lambda: Wait(0.2) # do nothing
        effect_command = EffectCommand(do_func, undo_func,
                                       scene=self.scene, 
                                       graph_sheet=self.graphsheet, 
                                       run_time=run_time, 
                                       voiceover_text=voiceover_text, 
                                       remove_on_completion=remove_on_completion)
        return effect_command   
     
     
        
    def flash_effect(self, color=BLUE, run_time=2, voiceover_text=None, remove_on_completion=True):
        flash = Flash(self.view(), color=color)
        do_func = lambda: flash 
        undo_func = lambda: Wait(0.2) # do nothing
        effect_command = EffectCommand(do_func, undo_func,
                                       scene=self.scene, 
                                       graph_sheet=self.graphsheet, 
                                       run_time=run_time, 
                                       voiceover_text=voiceover_text, 
                                       remove_on_completion=remove_on_completion)
        return effect_command   
    
    def passing_flash_effect(self, color=BLUE, run_time=2, voiceover_text=None, remove_on_completion=True):
        flash = ShowPassingFlash(self.view(), color=color)
        do_func = lambda: flash 
        undo_func = lambda: Wait(0) # do nothing
        effect_command = EffectCommand(do_func, undo_func,
                                       scene=self.scene, 
                                       graph_sheet=self.graphsheet, 
                                       run_time=run_time, 
                                       voiceover_text=voiceover_text, 
                                       remove_on_completion=remove_on_completion)
        return effect_command   
    
    def circumscribe_effect(self, color=BLUE, run_time=2, fade_out=True, voiceover_text=None, remove_on_completion=True  ):
        def do_func():
            circumscribe_circle = Circumscribe(self.view(), run_time=run_time)
            animations = [Create(circumscribe_circle)]
            if fade_out:
                animations.append(FadeOut(circumscribe_circle, run_time=run_time/2))
            return AnimationGroup(*animations)

        def undo_func():
            return Wait(0)  # No-op for undo

        effect_command = EffectCommand(do_func, undo_func,
                                       scene=self.scene, 
                                       graph_sheet=self.graphsheet, 
                                       run_time=run_time * (1.5 if fade_out else 1), 
                                       voiceover_text=voiceover_text, 
                                       remove_on_completion=remove_on_completion)
        return effect_command  
    
    def trace_effect(self, color=RED, run_time=2, voiceover_text=None, remove_on_completion=True):
        dot = Dot(ORIGIN, color=color).set_radius(1)
        path = self.shape_to_trace()
        do_func = lambda: MoveAlongPath(dot, path)
        undo_func = lambda: FadeOut(dot)
        effect_command = EffectCommand(do_func, undo_func,
                                       scene=self.scene, 
                                       graph_sheet=self.graphsheet, 
                                       run_time=run_time, 
                                       voiceover_text=voiceover_text, 
                                       remove_on_completion=remove_on_completion)
        return effect_command   
        
    def underline_effect(self, color=BLUE, 
                         buff=0.1,
                         stroke_width=2,
                         run_time=2, 
                         voiceover_text=None, 
                         remove_on_completion=True):
        underline = None
        def do_func():
            nonlocal underline
            underline = Line(LEFT, RIGHT)
            underline.set_width(self.view().width)
            underline.next_to(self.view(), DOWN, buff=buff)
            underline.set_color(color)
            underline.set_stroke(width=stroke_width)
            return Create(underline)
        
        def undo_func():
            return FadeOut(underline)
        
        effect_command = EffectCommand(do_func, undo_func, scene=self.scene, graph_sheet=self.graph_sheet, 
                                      run_time=run_time, remove_on_completion=remove_on_completion, 
                                      voiceover_text=voiceover_text)
        return effect_command
        
        
    def transform_effect(self, target_model_or_text, run_time=2, voiceover_text=None, remove_on_completion=True):           
        return self.graphsheet.transform_effect(source_model = self, 
                                    target_model_or_text = target_model_or_text,
                                    run_time = run_time, 
                                    voiceover_text = voiceover_text)
        
        
  



