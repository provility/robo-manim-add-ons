import math
import sympy as sp
import numpy as np

class GeometryUtils:
    
    
    @staticmethod # direction vector is a sympy point  
    def get_slope_line(point, direction_vector, length):
        # Normalize the direction vector
        direction_length = math.sqrt(direction_vector[0]**2 + direction_vector[1]**2)
        normalized_vector = (direction_vector[0] / direction_length, direction_vector[1] / direction_length)
        
        # Calculate half-length
        half_length = length / 2
        
        # Calculate the endpoints
        start_point = sp.Point(point.x - half_length * normalized_vector[0], point.y - half_length * normalized_vector[1])
        end_point = sp.Point(point.x + half_length * normalized_vector[0], point.y + half_length * normalized_vector[1])
        
        return start_point, end_point
    
    @staticmethod
    def from_sympy_to_numpy(point):
        return np.array([point.x, point.y,0])
     
    
    @staticmethod
    def from_numpy_to_sympy(numpy_array):
        return sp.Point(numpy_array[0], numpy_array[1])
    
    @staticmethod
    def create_shading_strips(points, direction='vertical', step_size=0.1):
        # Convert direction to a vector
        if direction == 'vertical':
            dir_vector = sp.Point(0, 1)
        elif direction == 'horizontal':
            dir_vector = sp.Point(1, 0)
        else:
            raise ValueError("Direction must be 'vertical' or 'horizontal'")

        # Create polygon
        polygon = sp.Polygon(*points)

        # Find bounding box
        x_coords = [p.x for p in points]
        y_coords = [p.y for p in points]
        min_x, max_x = min(x_coords), max(x_coords)
        min_y, max_y = min(y_coords), max(y_coords)

        # Create shading lines
        shading_lines = []
        if direction == 'vertical':
            for x in np.arange(min_x, max_x, step_size):
                line = sp.Line(sp.Point(x, min_y - 1), sp.Point(x, max_y + 1))
                intersections = polygon.intersection(line)
                if len(intersections) >= 2:
                    shading_lines.append(sp.Segment(intersections[0], intersections[-1]))
        else:  # horizontal
            for y in np.arange(min_y, max_y, step_size):
                line = sp.Line(sp.Point(min_x - 1, y), sp.Point(max_x + 1, y))
                intersections = polygon.intersection(line)
                if len(intersections) >= 2:
                    shading_lines.append(sp.Segment(intersections[0], intersections[-1]))

        return shading_lines
    
        

   