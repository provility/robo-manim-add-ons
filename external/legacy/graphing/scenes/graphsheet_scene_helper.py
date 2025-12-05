from re import T
from manim import *

from graphing.sheets.axes_builder import AxesBuilder
from graphing.sheets.graphsheet2d import GraphSheet2D
from graphing.sheets.graphsheet3d import Graphsheet3D
from graphing.sheets.static_graphsheet2d import StaticGraphSheet2D


class GraphSheetSceneHelper():  
    def __init__(self, scene):
        super().__init__()
        self.scene = scene
        self.graph_sheet_2d_instances = []
        self.graph_sheet_3d_instances = []
   
    """
    range_val is the range of the axes, which is twice the length of the axes. 
    """     
    def square_axes(self, range_val=10, factor=1, axis_color=BLACK, include_numbers=False, tips=False, opacity=1)->Axes:
        axes = AxesBuilder.create_square_axes(range_val, factor, axis_color, include_numbers, tips)
        axes.set_opacity(opacity)
        return axes
    
    def number_plane(self, range_val=10, axis_color=BLACK, include_numbers=False, tips=False, opacity=1)->Axes:
        number_plane = AxesBuilder.number_plane(range_val, axis_color, include_numbers, tips)
        number_plane.set_opacity(opacity)
        return number_plane
    
    def log_axes(self, x_range=[0.001, 6], y_range=[-8, 2], x_length=5, y_length=3, axis_color=BLACK, include_numbers=False, tips=False, opacity=1)->Axes:
        log_axes = AxesBuilder.log_axes(x_range, y_range, x_length, y_length, axis_color, include_numbers, tips)
        log_axes.set_opacity(opacity)
        return log_axes
    
    def number_line(self, x_range=[0, 10], unit_size=1, include_numbers=True, axis_color=BLACK)->Axes:
        number_line = AxesBuilder.number_line(x_range, unit_size, include_numbers, axis_color)
        return number_line
    
    def complex_plane(self,  axis_color=BLACK, tips=True, opacity=1, x_range=[-6, 6, 1], y_range=[-6, 6, 1])->Axes:
        complex_plane = AxesBuilder.complex_plane(
            axis_color = axis_color, 
            x_range = x_range, 
            y_range = y_range, 
            tips = tips)
        complex_plane.set_opacity(opacity)
        return complex_plane
    
    def polar_plane(self, axis_color=BLACK, azimuth_units="PI radians", size=6)->Axes:
        polar_plane = AxesBuilder.polar_plane(axis_color, azimuth_units, size)
        return polar_plane
    
    def first_quadrant_axes(self, x_range = [-2, 8, 1], y_range = [-2, 8, 1 ], include_numbers=True, 
                            factor=1, tips=False, opacity=1, axis_color=BLACK)->Axes:
        axes = AxesBuilder.first_quadrant_axes(
            x_range = x_range, 
            y_range = y_range,  
            include_numbers=include_numbers,    
            factor = factor,
            tips=tips,
            axis_color=axis_color)
        axes.set_opacity(opacity)
        return axes
    
    def equal_spacing_axes(self, x_range = [-5, 5, 1], 
                                y_range = [-3, 7, 1],    
                                unit_size=1,
                                include_numbers=True, 
                                tips=False, 
                                opacity=1,
                                axis_color=BLACK)->Axes:
        axes = AxesBuilder.equal_spacing_axes(x_range, y_range, unit_size, include_numbers, tips, opacity, axis_color)
        return axes
    
    def top_quadrant_axes(self, x_range = [-5, 5, 1], 
                                y_range = [-3, 7, 1],    
                              length = 10, 
                              factor = 1,
                              include_numbers=True, 
                              tips=False, 
                              opacity=1,
                              axis_color=BLACK)->Axes:
        axes = AxesBuilder.top_quadrant_axes(
            x_range = x_range, 
            y_range = y_range, 
            length = length,    
            factor = factor,    
            include_numbers=include_numbers,    
            tips=tips,
            axis_color=axis_color)
        axes.set_opacity(opacity)
        return axes 
    
    def right_quadrant_axes(self, x_range = [-2, 8, 1], 
                              y_range = [-5, 5, 1], 
                              length = 10,
                              factor = 1,
                              include_numbers=True, 
                              tips=False, 
                              opacity=1,
                              axis_color=BLACK):
        axes = AxesBuilder.right_quadrant_axes(
            x_range = x_range, 
            y_range = y_range, 
            length = length,
            factor = factor,
            include_numbers=include_numbers,    
            tips=tips)
        axes.set_opacity(opacity)
        return axes  
    
    def create_axis(self, x_range, y_range, x_length, y_length, axis_color=BLACK, include_numbers=True, tips=False, opacity=1)->Axes:
        axes = AxesBuilder.create_axis(x_range, y_range, x_length, y_length, axis_color, include_numbers, tips)
        axes.set_opacity(opacity)
        return axes
    
    def trig_axes(self, x_range=[-2*PI, 2*PI, PI/2], y_range=[-2.5, 2.5, 1], x_length=12, y_length=8, axis_color=BLACK, include_numbers=True, 
                         tips=False, x_axis_name=r"\theta", y_axis_name=r"y", opacity=1):
        axes = AxesBuilder.create_trig_axes(x_range, y_range, x_length, y_length, axis_color, include_numbers, tips, x_axis_name, y_axis_name)
        axes.set_opacity(opacity)
        return axes

    def graph_sheet_2d(self,  axes:Axes, add_to_scene=True, hide_axes=False)->GraphSheet2D:
        graph_sheet = GraphSheet2D(self, axes, hide_axes=hide_axes)
        self.graph_sheet_2d_instances.append(graph_sheet)
        if add_to_scene:
            self.scene.add(graph_sheet)
        return graph_sheet
    
    def static_graph_sheet_2d(self,  axes:Axes, add_to_scene=True, hide_axes=False)->StaticGraphSheet2D:
        graph_sheet = StaticGraphSheet2D(self, axes, hide_axes=hide_axes)
        self.graph_sheet_2d_instances.append(graph_sheet)
        if add_to_scene:
            self.scene.add(graph_sheet)
        return graph_sheet
    
    def graph_sheet_3d(self, axes:Axes, add_to_scene=True)->Graphsheet3D:
        graph_sheet = Graphsheet3D(self, axes)
        self.graph_sheet_3d_instances.append(graph_sheet)
        if add_to_scene:
            self.scene.add(graph_sheet)
        return graph_sheet
    
   
   