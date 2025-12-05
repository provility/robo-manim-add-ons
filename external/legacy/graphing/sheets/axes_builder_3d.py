from manim import *

class AxesBuilder3D:
    def __init__(self, scene,  x_range=[-2, 7, 1],
            y_range=[-2, 7, 1],
            z_range=[-2, 7, 1],
            x_length=9,
            y_length=9,
            z_length=9, 
            add_coordinates=False, 
            show_axes_labels=False):
        self.x_range = x_range
        self.y_range = y_range
        self.z_range = z_range
        self.x_length = x_length
        self.y_length = y_length
        self.z_length = z_length
        self.add_coordinates = add_coordinates
        self.show_axes_labels = show_axes_labels
        self.scene = scene
        self.axes = None
        self.axes_group = None  
        self.build_axes()
       
        
    def build_axes(self):
        self.axes = ThreeDAxes(x_range=self.x_range, y_range=self.y_range, z_range=self.z_range, x_length=self.x_length, y_length=self.y_length, z_length=self.z_length)
        self.axes_group = VGroup() 
        self.axes_group.add(self.axes)
        if self.add_coordinates:
            self.axes.add_coordinates()
        if self.show_axes_labels:   
            x_label = self.axes.get_x_axis_label(Tex("X").scale(0.7).set_color(RED))
            y_label = self.axes.get_y_axis_label(Tex("Y").scale(0.7).set_color(GREEN))
            z_label = self.axes.get_z_axis_label(Tex("Z").scale(0.7).set_color(BLUE))
            self.axes_group.add(x_label, y_label, z_label)
        self.scene.add(self.axes_group)

    
        
    
    