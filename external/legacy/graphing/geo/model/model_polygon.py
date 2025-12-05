from graphing.geo.model.base_model import BaseModel
import sympy as sp
import sympy.geometry as spg
import math
from graphing.geo.model.model_line import ModelLine
from graphing.geo.model.model_point import ModelPoint

class ModelPolygon(BaseModel):
    def __init__(self, points:list[ModelPoint]):
        super().__init__()
        self.points = points
        self.sympy_polygon = spg.Polygon(*[p.to_sympy() for p in self.points])
        self.sides = [ModelLine(self.points[i].x, self.points[i].y, self.points[i+1].x, self.points[i+1].y)
                for i in range(len(self.points)-1)] + [ModelLine(self.points[-1].x, self.points[-1].y, self.points[0].x, self.points[0].y)]    

    def update_points(self, new_points: list[ModelPoint]):
        if len(new_points) != len(self.points):
            raise ValueError("The number of new points must match the current number of points.")
        
        for i, new_point in enumerate(new_points):
            self.points[i].set(new_point.x, new_point.y)
            
        self.sympy_polygon = spg.Polygon(*[p.to_sympy() for p in self.points])
        self.notify()
   

    def point_index(self, index):
        if index < len(self.points):
            return self.points[index]
        else:
            raise ValueError("Invalid index for polygon points")    
        
    def side_index(self, index):
        if index < len(self.sides):
            return self.sides[index]
        else:
            raise ValueError("Invalid index for polygon side")   
            
    
    def get_all_points(self):
        return self.points  
    
    @property
    def area(self):
        return self.sympy_polygon.area
    
    @property
    def centroid(self):
        return self.sympy_polygon.centroid
    
    @property
    def angles(self):
        return self.sympy_polygon.angles
    
    @staticmethod
    def polygon_by_sides(side_size_parameters, origin_point):
        model_polygon = None
     
        def computation():
            points = [ModelPoint(origin_point.x, origin_point.y, origin_point.z)]
            current_x, current_y, current_z = origin_point.x, origin_point.y, origin_point.z
            angle = 0

            for i, side in enumerate(side_size_parameters[:-1]):
                side_value = side.get_value()
                current_x += side_value * math.cos(angle)
                current_y += side_value * math.sin(angle)
                points.append(ModelPoint(current_x, current_y, current_z))

                if i < len(side_size_parameters) - 2:
                    next_side = side_size_parameters[i + 1].get_value()
                    last_side = side_size_parameters[-1].get_value()
                    # This angle calculation is based on the law of cosines
                    # It determines the angle between two sides of the polygon
                    # given the lengths of three sides forming a triangle
                    # It is used to calculate the next angle in the polygon
                    # The result is the angle in radians
                    
                    angle += math.acos((side_value**2 + next_side**2 - last_side**2) / (2 * side_value * next_side))

            return points

        def create():
            nonlocal model_polygon
            model_points = computation()
            model_polygon = ModelPolygon(model_points)

        create()

        def update():
            nonlocal model_polygon
            new_points = computation()
            model_polygon.update_points(new_points)

        for side in side_size_parameters:
            side.on_param_change(lambda d: update())

        return model_polygon
    
    @staticmethod
    def from_side_length_and_origin(side_length_param, origin):
        model_polygon = None    
        
        def computation():
            # use origin as the first point and create 4 sides using side length parameter, should be created in counterclockwise direction 
            # the last side should be connected to the first side
            side_length = side_length_param.get_value()
            points = [origin]
            # Create 4 points in counterclockwise direction using side_length
            points.append(ModelPoint(origin.x + side_length, origin.y))  # Right
            points.append(ModelPoint(origin.x + side_length, origin.y + side_length))  # Top-right
            points.append(ModelPoint(origin.x, origin.y + side_length))  # Top-left
            points.append(ModelPoint(origin.x, origin.y))  # Bottom-left
            return points   
  
        def create():
            nonlocal model_polygon
            model_points = computation()
            model_polygon = ModelPolygon(model_points)
        
        create()
        
        def update():
            nonlocal model_polygon
            new_points = computation()
            model_polygon.update_points(new_points)
        
        #hook up the parameter to the square
        origin.on_change(lambda : update()) 
        side_length_param.on_param_change(lambda m: update())
        
        return model_polygon
    
    @staticmethod
    def from_width_and_height(width_param, height_param, origin):
        model_polygon = None   
        
        def computation():
            width = width_param.get_value()
            height = height_param.get_value()
            points = [origin]     
            points.append(ModelPoint(origin.x + width, origin.y))  # Right
            points.append(ModelPoint(origin.x + width, origin.y + height))  # Top-right
            points.append(ModelPoint(origin.x, origin.y + height))  # Top-left
            points.append(ModelPoint(origin.x, origin.y))  # Bottom-left
            return points
        
        def create():
            nonlocal model_polygon
            model_points = computation()
            model_polygon = ModelPolygon(model_points)
        
        create()
        
        def update():
            nonlocal model_polygon
            new_points = computation()
            model_polygon.update_points(new_points)
        
        origin.on_change(lambda : update()) 
        width_param.on_param_change(lambda m: update())
        height_param.on_param_change(lambda m: update())
        
        return model_polygon
        
  