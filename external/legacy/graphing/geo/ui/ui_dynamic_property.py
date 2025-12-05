from graphing.geo.geo_mapper import GeoMapper
from graphing.geo.model.model_dynamic_property import ModelDynamicProperty
from graphing.geo.ui.base_ui import BaseUI
from graphing.geo.ui.ui_style_props import UIStyleProps
from manim import *

class UIDynamicBaseProperty(BaseUI):
      def __init__(self,  graphsheet, geo_mapper:GeoMapper, 
                   model_dynamic_property:ModelDynamicProperty, 
                   var_type = DecimalNumber,
                   style_props: UIStyleProps=UIStyleProps.dynamic_prop_theme()) -> None:
            super().__init__(style_props)   
            self.graphsheet = graphsheet  
            self.model_dynamic_property = model_dynamic_property
            self.geo_mapper = geo_mapper     
            self.var_type = var_type         

      def get_current_variable_value(self):
          return self.model_dynamic_property.property_value
           
class UIDynamicSimple(UIDynamicBaseProperty):
       def __init__(self,  graphsheet, geo_mapper:GeoMapper, 
                   model_dynamic_property:ModelDynamicProperty, 
                   var_type = DecimalNumber,
                   style_props: UIStyleProps=UIStyleProps.dynamic_prop_theme()) -> None:
            super().__init__(graphsheet, geo_mapper, model_dynamic_property, var_type, style_props)
            self.ui_shape = None
            self.create()
        
       def create(self):
           current_value = self.get_current_variable_value()
           # Convert to integer if the value is a float
           if isinstance(current_value, float):
               current_value = int(round(current_value))
           self.ui_shape = Tex(f"{current_value}")
           self.ui_shape.set_color(self.color)
           
       def update(self):
            current_position = self.ui_shape.get_center()
            current_value = self.get_formatted_value()
            new_shape = Tex(f"{current_value}")
            new_shape.set_color(self.color)
            new_shape.move_to(current_position)
            self.ui_shape.become(new_shape)
            
       def view(self):
            return self.ui_shape
        
       def get_formatted_value(self):
           current_value = self.get_current_variable_value()
           if isinstance(current_value, float):
               current_value = int(round(current_value))
           return current_value
        

class UIDynamicVariableProperty(UIDynamicBaseProperty):
      def __init__(self,  graphsheet, geo_mapper:GeoMapper, 
                   model_dynamic_property:ModelDynamicProperty, 
                   var_type = DecimalNumber,
                   style_props: UIStyleProps=UIStyleProps.dynamic_prop_theme()) -> None:
            super().__init__(graphsheet, geo_mapper,model_dynamic_property, var_type, style_props)
            self.variable = None
            self.var_type = var_type
            self.variable_with_box = None
            self.create()
                 
            
      def create(self):            
          value = self.get_current_variable_value()
          variable = Variable(value,
                                   label=self.model_dynamic_property.display_prop_name, 
                                   var_type=self.var_type,  
                                   num_decimal_places=1)  
          self.variable = variable
          self.variable.set_color(self.style_props.color)   
          
          # Create a RoundedRectangle around the variable
          rounded_rect = RoundedRectangle(corner_radius=0.2, width=self.variable.width + 1, height=self.variable.height + 0.5, color=self.style_props.fill_color, fill_opacity=self.style_props.fill_opacity)

          # Center the variable within the rounded rectangle
          variable.move_to(rounded_rect.get_center())

          # Update the VGroup to ensure proper positioning
          self.variable_with_box = VGroup(rounded_rect, variable)

      def view(self):
           return self.variable_with_box
       
      def update(self):
          new_value = self.get_current_variable_value()
          self.variable.tracker.set_value(new_value) 
     
     
    
     
    
   
            


