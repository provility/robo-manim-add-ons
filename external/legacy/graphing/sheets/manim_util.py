import numpy as np
import sympy as sp
import sympy.geometry as spg
from manim import *

class ManimUtil:
    
    @staticmethod
    def circle(center:np.array, radius:float, color:ManimColor=RED)->Circle:
        return Circle(radius=radius, color=color).move_to(center)
    
    @staticmethod
    def line(pt1:np.array, pt2:np.array, color:ManimColor=RED)->Line:
        return Line(start=pt1, end=pt2, color=color)
    
    @staticmethod
    def find_polygon_intersections(line, polygon)->list[Dot]:
        """
        Find the intersection points between a line and a polygon.
        
        Parameters:
            line: Manim Line object.
            polygon: Manim Polygon object.
        
        Returns:
            A list of intersection points as NumPy arrays.
        """
        intersection_dots = []
        # Get the vertices of the polygon
        poly_points = polygon.get_vertices()
        num_points = len(poly_points)
        
        # Iterate over each edge of the polygon
        for i in range(num_points):
            start = poly_points[i]
            end = poly_points[(i + 1) % num_points]  # Wrap around to the first vertex
            edge = Line(start, end)
            
            # Find the intersection of the line with this edge
            intersection_dot = ManimUtil.get_line_intersection(line, edge)
            if intersection_dot is not None:
                intersection_dots.append(intersection_dot)
        
        return intersection_dots
    
    @staticmethod   
    def get_line_intersection(line1, line2):
        """
        Find the intersection of two infinite lines.
        
        Parameters:
            line1, line2: Manim Line objects
            
        Returns:
            The intersection point as a NumPy array, or None if the lines are parallel.
        """
        # Extract start and end points of both lines
        p1, p2 = line1.get_start_and_end()
        q1, q2 = line2.get_start_and_end()
        
        # Solve for intersection using linear algebra
        A = np.array([
            [p2[0] - p1[0], q1[0] - q2[0]],
            [p2[1] - p1[1], q1[1] - q2[1]]
        ])
        b = np.array([q1[0] - p1[0], q1[1] - p1[1]])
        
        try:
            t, u = np.linalg.solve(A, b)
        except np.linalg.LinAlgError:
            return None  # Lines are parallel or coincident
        
        # Compute the intersection point using t
        intersection = p1 + t * (p2 - p1)
        return Dot(intersection)
     
    @staticmethod
    def get_normal_direction(direction:np.array)->np.array:
        normalized_direction = normalize(direction)
        normal_direction = rotate_vector(normalized_direction, PI/2)
        return normal_direction 