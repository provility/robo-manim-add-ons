import numpy as np
from manim import *

class AxesBuilder:
    
      """
      Using the same length for both x and y ensures that the aspect ratio is 1:1.  
      """ 
      @staticmethod
      def create_square_axes(range_val, factor=1, axis_color=BLACK, 
                             include_numbers=False, 
                             tips=False, 
                             x_axis_name=None, 
                             y_axis_name=None,  **kwargs):
          x_range = [-range_val, range_val, 1]
          y_range = [-range_val, range_val, 1]
          x_range = [x_range[0] * factor, x_range[1] * factor, x_range[2]]
          y_range = [y_range[0] * factor, y_range[1] * factor, y_range[2]]   
          length = range_val * factor
            
          axis_config = {
              "color": axis_color,
              "include_numbers": include_numbers,
              "decimal_number_config": {
                  "num_decimal_places": 0,
                  "color": axis_color  # Tick label color
              }
          }
          # Update axis_config with any additional kwargs
          axis_config.update(kwargs)
         
   
          length =  range_val * 2   
          axes = Axes(
              x_range=x_range,
              y_range=y_range,
              x_length= length,
              y_length= length,   
              axis_config=axis_config,
              tips=tips
          )
          
          AxesBuilder.add_axes_labels(axes, x_axis_name, y_axis_name, color=axis_color)     
          if include_numbers:
              AxesBuilder.set_tick_colors(axes, axis_color)
          return axes
     
      @staticmethod
      def set_tick_colors(axes, axis_color):
          if hasattr(axes, 'ticks'):
              for tick in axes.ticks:
                  tick.set_color(axis_color)

        # Customize label color
          if hasattr(axes, 'numbers'):
              for label in axes.numbers:
                  label.set_color(axis_color)
                  
          if hasattr(axes, "coordinate_labels"):
              for label in axes.coordinate_labels:
                  label.set_color(axis_color)
                  
          if hasattr(axes, "x_lines"):
              for line in axes.x_lines:
                  line.set_color(axis_color)
                  
          if hasattr(axes, "y_lines"):
              for line in axes.y_lines:
                  line.set_color(axis_color)
                  
          if hasattr(axes, "axes"):
               for line in axes.axes:
                  line.set_color(axis_color)
               
         
                           
      
      """
      NumberLine is not an Axes object.
      """
      @staticmethod 
      def number_line(x_range=[0, 10], unit_size=1, include_numbers=True, axis_color=BLACK):
          number_line = NumberLine(x_range=x_range,
                            unit_size=unit_size, include_numbers=include_numbers, color=axis_color)
          AxesBuilder.set_tick_colors(number_line, axis_color)
          return number_line
      
      
      @staticmethod
      def log_axes(x_range=[0.001, 6], y_range=[-8, 2], x_length=5, 
                   y_length=3, 
                   axis_color=BLACK, 
                   tips=False, 
                   x_axis_name=None, 
                   y_axis_name=None, 
                   **kwargs):
           axis_config = {
                "color": axis_color,
                "tips": tips
           }
           # Update axis_config with any additional kwargs
           axis_config.update(kwargs)
           axes = Axes(
                x_range=x_range,
                y_range=y_range,
                x_length=x_length,
                y_length=y_length,
                axis_config=axis_config
            )
           AxesBuilder.set_tick_colors(axes, axis_color)
           return axes
      
      @staticmethod
      def number_plane(range_val=10, unit_size=1, color=BLACK,  tips=False):
            axis_config = {
                "color": color,
                "x_range": [-range_val, range_val, unit_size],
                "y_range": [-range_val, range_val, unit_size],
                "tips": tips    
            }
            axes = NumberPlane(**axis_config)
            AxesBuilder.set_tick_colors(axes, color)
            return axes
     
     
      @staticmethod 
      def complex_plane(axis_color=BLACK, x_range=[-10, 10, 1], y_range=[-10, 10, 1], tips=False):
           axis_config = {
                "color": axis_color,
                "x_range": x_range,
                "y_range": y_range,
                "tips": tips,
                "background_line_style": {
                    "stroke_width": 0.2,
                    "stroke_opacity": 0.5
                }
            }
           axes = ComplexPlane(**axis_config).add_coordinates()   
           axes.background_lines.set_opacity(0)  
           AxesBuilder.set_tick_colors(axes, axis_color)
           return axes
      
      @staticmethod
      def polar_plane(axis_color=BLACK, azimuth_units="PI radians", size=6):
           axis_config = {
                "color": axis_color,
                "azimuth_units": azimuth_units, 
                "size": size
            }
           polarplane_pi = PolarPlane(**axis_config)
           return polarplane_pi
       
       
      @staticmethod
      def create_axes(x_range = [-5, 5, 1], 
                              y_range = [-5, 5, 1], 
                              x_length = 10, 
                              y_length = 10, 
                              axis_color=BLACK, 
                              include_numbers=False, 
                              tips=False, 
                              x_axis_name=None, 
                              y_axis_name=None, 
                              **kwargs):
           axis_config={
                "color": axis_color,
                "include_numbers": include_numbers
                }  
           # Update axis_config with any additional kwargs
           axis_config.update(kwargs)
           axes = Axes(
           x_range=x_range,
           y_range=y_range,
           x_length=x_length,
           y_length=y_length,
           axis_config=axis_config, 
           tips=tips 
           )
           
           AxesBuilder.add_axes_labels(axes, x_axis_name, y_axis_name, color=axis_color)
           if include_numbers:
               AxesBuilder.set_tick_colors(axes, axis_color)
           return axes  
      
      """
      Example:
      x_range=[-2, 8]
      y_range=[-2, 8]
      length=10
      tips=False
      include_numbers=True
      axis_color=BLACK
      """

      @staticmethod
      def first_quadrant_axes(x_range = [-2, 8, 1], 
                              y_range = [-2, 8, 1], 
                              length = 10, 
                              factor = 1,
                              tips=False,
                              include_numbers=True, 
                              axis_color=BLACK,
                              x_axis_name=None,
                              y_axis_name=None, 
                              **kwargs):
          
            if len(x_range)==2:
                x_range.append(1)
            if len(y_range)==2:
                y_range.append(1)   
                
            x_range = [x_range[0] * factor, x_range[1] * factor, x_range[2]]
            y_range = [y_range[0] * factor, y_range[1] * factor, y_range[2]]   
            length = length * factor    
            axes = AxesBuilder.create_axes(x_range, y_range, length, length, axis_color, 
                                           include_numbers = include_numbers, 
                                           tips = tips,
                                           x_axis_name = x_axis_name, 
                                           y_axis_name = y_axis_name, 
                                           **kwargs)
            AxesBuilder.set_tick_colors(axes, axis_color)
            return axes
           
      @staticmethod
      def top_quadrant_axes(x_range = [-5, 5, 1], 
                              y_range = [-2, 8, 1], 
                              length = 10,      
                              tips=False,
                              factor = 1,
                              include_numbers=True, 
                              axis_color=BLACK,
                              x_axis_name=None,
                              y_axis_name=None, 
                              **kwargs):
           x_range = [x_range[0] * factor, x_range[1] * factor]
           y_range = [y_range[0] * factor, y_range[1] * factor]   
           length = length * factor    
           axes = AxesBuilder.create_axes(x_range, y_range, length, length, axis_color, 
                                           include_numbers = include_numbers, 
                                           tips = tips,
                                           x_axis_name = x_axis_name, 
                                           y_axis_name = y_axis_name, 
                                           **kwargs)
           AxesBuilder.set_tick_colors(axes, axis_color)
           return axes           

      @staticmethod
      def right_quadrant_axes(x_range = [-2, 8, 1], 
                              y_range = [-5, 5, 1], 
                              length = 10,          
                              tips=False,
                              factor = 1,
                              include_numbers=True, 
                              axis_color=BLACK,
                              x_axis_name=None,
                               y_axis_name=None, 
                              **kwargs):
           x_range = [x_range[0] * factor, x_range[1] * factor]
           y_range = [y_range[0] * factor, y_range[1] * factor]   
           length = length * factor    
           axes = AxesBuilder.create_axes(x_range, y_range, length, length, axis_color, 
                                           include_numbers = include_numbers, 
                                           tips = tips,
                                           x_axis_name = x_axis_name, 
                                           y_axis_name = y_axis_name, 
                                           **kwargs)
           AxesBuilder.set_tick_colors(axes, axis_color)
           return axes    
       
       
       
      """
      Example:
      x_range=[0, 4 * PI, PI / 2]
      y_range=[-1.5, 1.5, 0.5]
      x_length=10
      y_length=10
      axis_color=BLACK
      include_numbers=True
      tips=False
      
      Example 2:
      x_range=[-2, 2, 1]
      y_range=[-2, 2, 1]
      x_length=10
      y_length=10
      axis_color=BLACK
      include_numbers=True
      tips=False
      """    
      @staticmethod
      def create_axis(x_range = [-5, 5, 1], 
                              y_range = [-5, 5, 1], 
                              x_length = 10, 
                              y_length = 10, 
                              axis_color=BLACK, 
                              include_numbers=False, 
                              tips=False, 
                              x_axis_name=None, 
                              y_axis_name=None, 
                              **kwargs):
           axis_config={
                "color": axis_color,
                "include_numbers": include_numbers
                }     
           # Update axis_config with any additional kwargs
           axis_config.update(kwargs)
           axes = Axes(
           x_range=x_range,
           y_range=y_range,
           x_length=x_length,
           y_length=y_length,
           tips=tips,
           axis_config=axis_config      
           )
           AxesBuilder.add_axes_labels(axes, x_axis_name, y_axis_name, color=axis_color)
           AxesBuilder.set_tick_colors(axes, axis_color)
           return axes
       
      @staticmethod
      def create_trig_axes(x_range, y_range, x_length, y_length, 
                           axis_color=BLACK, 
                           include_numbers=True, 
                           tips=False, 
                           x_axis_name=None, 
                           y_axis_name=None, 
                           **kwargs):
           axis_config={
                "color": axis_color,
                "include_numbers": include_numbers
                }     
           # Update axis_config with any additional kwargs
           axis_config.update(kwargs)
           
           x_axis_config={
                    "include_numbers": False
                    }
           
           y_axis_config={
                    "include_numbers": include_numbers
                }
            
           axes = Axes(
           x_range=x_range,
           y_range=y_range, 
           x_length=x_length,
           y_length=y_length,
           axis_config=axis_config,
           x_axis_config=x_axis_config,
           y_axis_config=y_axis_config,
           tips=tips
           )
           
           AxesBuilder.add_axes_labels(axes, x_axis_name, y_axis_name, color=axis_color)
           AxesBuilder.set_tick_colors(axes, axis_color)
           x_axis = axes.get_x_axis()
          
           # Add labels to the axes
           labels =  {   PI: r"\pi",
                PI/2: r"\frac{\pi}{2}", 
                -PI: r"-\pi", 
                -PI/2: r"-\frac{\pi}{2}",
                2*PI: r"2\pi",
                -2*PI: r"-2\pi",
                3*PI/2: r"\frac{3\pi}{2}",
                -3*PI/2: r"-\frac{3\pi}{2}",
                4*PI: r"4\pi",
                -4*PI: r"-4\pi",
                5*PI/2: r"\frac{5\pi}{2}",
                -5*PI/2: r"-\frac{5\pi}{2}",
                6*PI: r"6\pi",
                -6*PI: r"-6\pi",
                7*PI/2: r"\frac{7\pi}{2}",
                -7*PI/2: r"-\frac{7\pi}{2}",
                8*PI: r"8\pi",  
                
            }
           
           # Filter labels based on x_range
           x_min, x_max = x_range[0], x_range[1]
           filtered_labels = {x: label for x, label in labels.items() if x_min <= x <= x_max}
           
           # Sort the filtered labels to ensure they are added in order
           sorted_labels = dict(sorted(filtered_labels.items()))
           
           # Update the labels dictionary with the filtered and sorted labels
           labels = sorted_labels
            
           for x_val, label in filtered_labels.items():
               x_axis.add(MathTex(label).next_to(x_axis.n2p(x_val), DOWN))
          
             
           
           return  axes  
       
     
      @staticmethod
      def add_axes_labels(axes, x_axis_name, y_axis_name, color=BLUE):
          if x_axis_name is not None:  
               x_label = MathTex(x_axis_name).next_to(axes.x_axis.get_end(), RIGHT)
               x_label.set_color(color)
               x_label.shift(DOWN*0.2).shift(LEFT*0.5)
               x_label.scale(0.5)
               axes.add(x_label)
          if y_axis_name is not None:
               y_label = MathTex(y_axis_name).next_to(axes.y_axis.get_end(), UP)
               y_label.set_color(color)
               y_label.shift(RIGHT*0.2).shift(DOWN*0.5)
               y_label.scale(0.5)
               axes.add(y_label)
               
      @staticmethod
      def equal_spacing_axes(x_range, 
                             y_range, 
                             unit_scale=1, 
                             color=BLACK,
                             include_numbers=True,
                             tick_size=0.1,
                             **kwargs):
           x_length = (x_range[1] - x_range[0]) * unit_scale
           y_length = (y_range[1] - y_range[0]) * unit_scale
           # Create axes with the calculated lengths
           axes = Axes(
                x_range=x_range,
                y_range=y_range,
                x_length=x_length,
                y_length=y_length,
                axis_config={
                "include_numbers": include_numbers,  # Add numbers
                "tick_size": tick_size,         # Tick size
                },
                **kwargs
           )
           axes.set_color(color)
           return axes
      
      @staticmethod
      def add_axes_labels(axes, x_axis_name, y_axis_name, x_label_color=BLUE, y_label_color=BLUE):
           x_label = axes.get_x_axis_label(x_axis_name)
           y_label = axes.get_y_axis_label(y_axis_name)
           axes.add(x_label, y_label)
           x_label.set_color(x_label_color)
           y_label.set_color(y_label_color)
         
       