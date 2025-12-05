from manim import *
"""
This class contains static methods for geometric calculations.
"""
class GeomUtils:
    
    """
    Returns a intersection point (np.array) between two lines
    """
    @staticmethod
    def get_intersection_between_lines(l1: Line,l2: Line):
        return line_intersection(
            (l1.get_start_and_end()),(l2.get_start_and_end())
        )
    
    """
    Returns the angle in radians between two lines
    """
    @staticmethod    
    def angle_betweeb_lines(l1: Line, l2: Line):
       return angle_between_vectors(l1.get_vector(),l2.get_vector())
   
