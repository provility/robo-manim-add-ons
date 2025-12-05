from graphing.geo.model.model_circle import ModelCircle
from graphing.geo.model.model_line import ModelLine
from graphing.geo.model.model_point_list import ModelPointList
import math
import numpy as np
import sympy as sp
import sympy.geometry as spg
from manim import *

from graphing.geo.model.model_polygon import ModelPolygon
from graphing.geo.model.model_triangle import ModelTriangle
from .model_point import ModelPoint
from .base_model import BaseModel
from shapely.geometry import Polygon
class ModelIntersection(ModelPointList):
      def __init__(self, points:list[ModelPoint]):
          super().__init__(points)
         
        
      def calculate_intersection(self):
          raise NotImplementedError("ModelIntersection Subclass must implement calculate_intersection method")
             
      def update(self):
          self.merge(self.calculate_intersection()) # merge is notifying    
          
      def point_index(self, index):
          if index < len(self.points):
              return self.points[index]
          else:
              raise ValueError("Invalid index for intersection points") 
          
    
class ModelLineToPolygonIntersection(ModelIntersection):
    def __init__(self, line:ModelLine, poly:ModelPolygon|ModelTriangle):
        self.line = line
        self.poly = poly
        self.intersection_points = [ModelPoint(-1000, -1000), ModelPoint(-1000, -1000)]
        super().__init__(self.intersection_points)
        self.update() # the real calculation is done in update
        
    def calculate_intersection(self):
        try:
            model_line = self.line
            model_poly = self.poly
            sympy_line = sp.Line(sp.Point(model_line.start_x, model_line.start_y), sp.Point(model_line.end_x, model_line.end_y))    
            if isinstance(model_poly, ModelPolygon):
                sympy_polygon = model_poly.sympy_polygon
            elif isinstance(model_poly, ModelTriangle):
                sympy_polygon = model_poly.sympy_triangle
            intersections = sympy_line.intersection(sympy_polygon)
        except spg.GeometryError:
            return ModelPoint.from_sym_points([])
        
        return ModelPoint.from_sym_points(intersections)    
    
    @staticmethod
    def line_to_polygon_intersection(line:ModelLine, poly)->ModelIntersection:
        model_intersection = ModelLineToPolygonIntersection(line, poly)
                
        def update():   
            nonlocal model_intersection
            model_intersection.update()
            
        # hook dependencies, when the input points change, the angle should update
        line.on_change(lambda: update())
        poly.on_change(lambda: update())
        return model_intersection
    
    
    
class ModelIntersectionRegion(BaseModel):
    def __init__(self, geoMapper, baseModel:BaseModel, otherModel:BaseModel):
        super().__init__()  
        self.geoMapper = geoMapper
        self.baseModel = baseModel
        self.otherModel = otherModel
        self.intersection = self.calculate_intersection()
        
    def update(self):
        self.intersection = self.calculate_intersection()
        self.notify()
     
        
    def calculate_intersection(self):
        view1 = self.baseModel.ui_part.view()
        view2 = self.otherModel.ui_part.view()
        return Intersection(view1, view2)
        
       
    @staticmethod    
    def from_shapes(geoMapper, baseModel:BaseModel, otherModel:BaseModel):
        model_intersection = ModelIntersectionRegion(geoMapper, baseModel, otherModel)
                    
        def update():   
            nonlocal model_intersection
            model_intersection.update()
                
        # hook dependencies, when the input points change, the angle should update
        baseModel.on_change(lambda: update())
        otherModel.on_change(lambda: update())
        return model_intersection
        
        

class ModelLineToLineIntersection(ModelIntersection):
    def __init__(self, line1:ModelLine, line2:ModelLine):
        self.line1 = line1
        self.line2 = line2
        self.intersection_points = [ModelPoint(-1000, -1000)]
        super().__init__(self.intersection_points)
        self.update() # the real calculation is done in update
    
    def calculate_intersection(self):
        # This is sympy line
        line1 = sp.Line(sp.Point(self.line1.start_x,self.line1.start_y), sp.Point(self.line1.end_x,self.line1.end_y))
        line2 = sp.Line(sp.Point(self.line2.start_x,self.line2.start_y), sp.Point(self.line2.end_x,self.line2.end_y))
        try:    
            intersections = line1.intersection(line2)
        except spg.GeometryError:
            return ModelPoint.from_sym_points([])
        
        return ModelPoint.from_sym_points(intersections)  
       
        
    @staticmethod    
    def from_lines(line1:ModelLine, line2:ModelLine)->ModelIntersection:
        model_intersection = None
        
        def create():
            nonlocal model_intersection  
            model_intersection = ModelLineToLineIntersection(line1, line2)
            
        def update():   
            nonlocal model_intersection
            model_intersection.update()
            
        create()
        
        # hook dependencies, when the input points change, the angle should update
        line1.on_change(lambda: update())
        line2.on_change(lambda: update())
        return model_intersection
    
    
class ModelLineToCircleIntersection(ModelIntersection):
    def __init__(self, model_line:ModelLine, model_circle:ModelCircle):
        self.model_line = model_line
        self.model_circle = model_circle
        self.intersection_points = [ModelPoint(-1000, -1000), ModelPoint(-1000, -1000)]
        super().__init__(self.intersection_points)
        self.update() # the real calculation is done in update
    
    def calculate_intersection(self):
        # This is sympy line
        sympy_line = sp.Line(sp.Point(self.model_line.start_x,self.model_line.start_y), sp.Point(self.model_line.end_x,self.model_line.end_y))
        center = self.model_circle.center
        radius = self.model_circle.radius
        sympy_circle = sp.Circle(sp.Point(center.x, center.y), radius)
        try:    
            intersections = sympy_line.intersection(sympy_circle)
        except spg.GeometryError:
            return ModelPoint.from_sym_points([])
        
        return ModelPoint.from_sym_points(intersections)  
       
        
    @staticmethod    
    def from_line_and_circle(model_line:ModelLine, model_circle:ModelCircle)->ModelIntersection:
        model_intersection = None
        
        def create():
            nonlocal model_intersection  
            model_intersection = ModelLineToCircleIntersection(model_line, model_circle)
            
        def update():   
            nonlocal model_intersection
            model_intersection.update()
            
        create()
        
        # hook dependencies, when the input points change, the angle should update
        model_line.on_change(lambda: update())
        model_circle.on_change(lambda: update())
        return model_intersection
     
 
class ModelCircleToCircleIntersection(ModelIntersection): 
    def __init__(self, model_circle1:ModelCircle, model_circle2:ModelCircle):
        self.model_circle1 = model_circle1
        self.model_circle2 = model_circle2
        self.intersection_points = [ModelPoint(-1000, -1000), ModelPoint(-1000, -1000)]
        super().__init__(self.intersection_points)
        self.update() # the real calculation is done in update      
        
    def calculate_intersection(self):
        circle1 = self.model_circle1.sympy_circle
        circle2 = self.model_circle2.sympy_circle
        try:    
            intersections = circle1.intersection(circle2)
        except spg.GeometryError:
            return ModelPoint.from_sym_points([])

        return ModelPoint.from_sym_points(intersections)
    
    @staticmethod    
    def from_circles(model_circle1:ModelCircle, model_circle2:ModelCircle)->ModelIntersection:
        model_intersection = ModelCircleToCircleIntersection(model_circle1, model_circle2)
        model_circle1.on_change(lambda: model_intersection.update())
        model_circle2.on_change(lambda: model_intersection.update())
        return model_intersection   



class ModelPolygonToPolygonIntersection(ModelIntersection): 
    def __init__(self, point_list1:list[ModelPoint], point_list2:list[ModelPoint], max_points=10  ):
        self.point_list1 = point_list1
        self.point_list2 = point_list2
        self.max_points = max_points
        self.intersection_points = [ModelPoint(-1000, -1000) for _ in range(max_points)]
        super().__init__(self.intersection_points)
        self.update() # the real calculation is done in update   
        
    def calculate_intersection(self):
        symy_points_1 = [point.to_sympy() for point in self.point_list1]    
        symy_points_2 = [point.to_sympy() for point in self.point_list2]
        sympy_polygon1 = sp.Polygon(*symy_points_1)
        sympy_polygon2 = sp.Polygon(*symy_points_2)
        try:    
            intersections = sympy_polygon1.intersection(sympy_polygon2)
        except spg.GeometryError:
            return ModelPoint.from_sym_points([])   
        
        return ModelPoint.from_sym_points(self.extract_points_from_intersection(intersections))
    
    def extract_points_from_intersection(self, intersection_list):
        points = []
        for element in intersection_list:
            if isinstance(element, sp.Point2D):
                points.append(element)
            elif isinstance(element, sp.Segment2D):
                # Get the start and end points of the segment
                points.append(element.p1)
                points.append(element.p2)
        return points
    
    """
    Could be ModelPolygon or ModelTriangle. Expects get_all_points  method to exist
    """
    @staticmethod    
    def from_polygons(model_polygon1, model_polygon2)->ModelIntersection:
        model_intersection = None
        
        def create():
            nonlocal model_intersection
            model_1_points = model_polygon1.get_all_points()
            model_2_points = model_polygon2.get_all_points()
            model_intersection = ModelPolygonToPolygonIntersection(model_1_points, model_2_points)
            
        def update():   
            nonlocal model_intersection
            model_intersection.update()
            
        create()
        model_polygon1.on_change(lambda: update())
        model_polygon2.on_change(lambda: update())
        return model_intersection