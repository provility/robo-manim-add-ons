from graphing.geo.ui.ui_style_props import UIStyleProps
from .base_ui import BaseUI
from ..model.model_point import ModelPoint
from ..model.model_angle import ModelAngle
from ..geo_mapper import GeoMapper
from ..geo_shape_props import ZIndex
from manim import *


class UIAngle(BaseUI):
      def __init__(self, geo_mapper: GeoMapper, 
                   model_angle:ModelAngle, 
                   radius=0.8,
                   style_props =UIStyleProps.angle_theme()) -> None:
         super().__init__(style_props)
         self.geo_mapper = geo_mapper
         self.model_angle = model_angle 
         self.radius = radius
         self.angle_value = None
         self.angle_shape = None
       
             
             
      def create(self):
         self.angle_value = self.model_angle.angle_value()
         self._do_create()
       
            
      def _do_create(self):
         raise NotImplementedError("Subclasses must implement _do_create method")
      
      def is_right_angle(self):
         return abs(self.angle_value - 90) < 1e-6  # Tolerance of 1e-6  
             
      def model_to_ui_angle(self):
         self.angle_value = self.model_angle.angle_value()  
         if self.is_right_angle():
            angle_mob = self.create_right_angle()
         else:
            angle_mob = self.create_angle_shape()
         angle_mob.set_z_index(ZIndex.ANGLE.value)
         return angle_mob
     
    
      def update(self):
         try:
            self.angle_value = self.model_angle.angle_value()
            if self.angle_value < 1e-6:
               self.angle_shape.set_opacity(0)
               return self.angle_shape
            else:
               self.angle_shape.set_opacity(1)  
               
            new_angle = self.model_to_ui_angle()
            if self.angle_shape is not None and len(self.angle_shape.points) > 0: 
               self.angle_shape.become(new_angle) 
            else:
               self.angle_shape.set_points(new_angle.points)   
            self.angle_shape.set_z_index(ZIndex.ANGLE.value)
         except Exception as e:
            pass

      def view(self):
         return self.angle_shape
      
      def create_angle_shape(self):
           raise NotImplementedError("Subclasses must implement create_angle_shape method")
      
            
      def create_right_angle(self):
          model_angle = self.model_angle
          ui_vertex = self.geo_mapper.model_to_ui(*model_angle.vertex.to_x_y())
          ui_point_from = self.geo_mapper.model_to_ui(*model_angle.point_from.to_x_y())
          ui_to_point = self.geo_mapper.model_to_ui(*model_angle.to_point.to_x_y())
          line1 = Line(ui_vertex, ui_point_from)
          line2 = Line(ui_vertex, ui_to_point)
          # Create a custom right angle using a square
          square_size = self.radius * 0.5
          square = Square(side_length=square_size, color=self.color, fill_opacity=self.fill_opacity)
          # Shift the square so its corner (not center) aligns with vertex
          square.shift(square_size * np.array([-0.5, -0.5, 0]))  # Move corner to origin
          square.move_to(ui_vertex, aligned_edge=np.array([-1, -1, 0]))  # Align corner with vertex
          # Rotate the square to align with both lines
          angle = line1.get_angle()
          square.rotate(angle, about_point=ui_vertex)
          # Check if we need to flip the square based on line2's direction
          if (line2.get_angle() - line1.get_angle()) % (2 * PI) > PI:
                  square.rotate(PI, about_point=ui_vertex)
           
          return square
     
     
      

class UISectorAngle(UIAngle):
      def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.create()
         
      def _do_create(self):
          try:  
               self.angle_shape   = self.model_to_ui_angle()
               self.angle_shape.set_z_index(ZIndex.ANGLE.value)
          except Exception as e:
               self.angle_shape = VMobject()
         
      def create_angle_shape(self):
          try:
               model_angle = self.model_angle
               ui_point_from = self.geo_mapper.model_to_ui(*model_angle.point_from.to_x_y())
               ui_vertex = self.geo_mapper.model_to_ui(*model_angle.vertex.to_x_y())
               ui_to_point = self.geo_mapper.model_to_ui(*model_angle.to_point.to_x_y())
               interior_angle_mob  = Angle.from_three_points(ui_point_from, ui_vertex, ui_to_point,
                                                radius=self.radius,
                                                color=self.color, 
                                                fill_opacity=self.fill_opacity,
                                                other_angle=model_angle.clock_wise)

               # Create a filled sector to represent the angle
               angle_line = Line(ui_vertex, ui_point_from)
               angle_mob = Sector(
                        arc_center=ui_vertex,
                        start_angle=angle_line.get_angle(),
                        angle=interior_angle_mob.get_value(),
                        outer_radius=self.radius,
                        color=self.color,
                        fill_opacity=self.fill_opacity,
                        stroke_width=self.stroke_width   
                  )
               return angle_mob          
          except Exception as e:
               return self.angle_shape 
          

class UIArrowAngle(UIAngle):
      def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.create()
         
      def _do_create(self):
          try:  
               self.angle_shape   = self.model_to_ui_angle()
               self.angle_shape.set_z_index(ZIndex.ANGLE.value)
          except Exception as e:
               self.angle_shape = VGroup(VMobject(), VMobject())
      
      def update(self):
         try:
            self.angle_value = self.model_angle.angle_value()
            if self.angle_value < 1e-6:
               self.angle_shape.set_opacity(0)
               return self.angle_shape
            else:
               self.angle_shape.set_opacity(1)  
               
            new_angle = self.model_to_ui_angle()
            if self.angle_shape is not None and len(self.angle_shape[0].points) > 0: 
               self.angle_shape[0].become(new_angle[0]) 
            else:
               self.angle_shape[0].set_points(new_angle[0].points)   
               self.angle_shape.set_z_index(ZIndex.ANGLE.value)
         except Exception as e:
            pass
         
      def create_angle_shape(self):
          model_angle = self.model_angle
          ui_point_from = self.geo_mapper.model_to_ui(*model_angle.point_from.to_x_y())
          ui_vertex = self.geo_mapper.model_to_ui(*model_angle.vertex.to_x_y())
          ui_to_point = self.geo_mapper.model_to_ui(*model_angle.to_point.to_x_y())
          interior_angle_mob  = Angle.from_three_points(ui_point_from, ui_vertex, ui_to_point,
                                                radius=self.radius,
                                                color=self.color, 
                                                fill_opacity=self.fill_opacity,
                                                other_angle=model_angle.clock_wise)

          angle_mob = VGroup()
          arc = ArcBetweenPoints(interior_angle_mob.get_start(),
                                         interior_angle_mob.get_end(), 
                                         color=self.color, 
                                         fill_opacity=0,
                                         radius=self.radius)
          arc.add_tip(tip_shape=StealthTip, tip_length=0.2, tip_width=0.05).set_color(self.color).set_fill(opacity=0)
          angle_mob.add(arc)
          return angle_mob
       

     
