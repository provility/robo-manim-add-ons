import sympy as sp
import numpy as np

class ConicUtils:
    
    @staticmethod
    def parabola_parametric_functions(parabola):
        """
        Given a SymPy Parabola object, return two lambda functions for parametric graphing.
        
        Parameters:
            parabola (sympy.geometry.Parabola): A SymPy Parabola object.
            
        Returns:
            tuple: (x(t), y(t)) lambda functions representing parametric equations for the parabola.
        """
        # Extract the focus and vertex of the parabola
        vertex = parabola.vertex  # Vertex of the parabola
        focus = parabola.focus  # Focus of the parabola
        directrix = parabola.directrix  # Directrix of the parabola

        # Calculate the direction of the parabola from the focus and vertex
        slope = directrix.slope
        if slope == 0:
            # The directrix is horizontal (parabola opens upwards or downwards)
            p = abs(focus.y - vertex.y)  # Distance between focus and vertex
            
            # Check if it opens upward or downward
            if focus.y > vertex.y:
                # Upward opening
                x_t = lambda t: vertex.x + t
                y_t = lambda t: (1 / (4 * p)) * t**2 + vertex.y
            else:
                # Downward opening
                x_t = lambda t: vertex.x + t
                y_t = lambda t: vertex.y - (1 / (4 * p)) * t**2
        
        else:
            # The directrix is vertical (parabola opens left or right)
            p = abs(focus.x - vertex.x)  # Distance between focus and vertex
            
            # Check if it opens right or left
            if focus.x > vertex.x:
                # Right opening
                x_t = lambda t: (1 / (4 * p)) * t**2 + vertex.x
                y_t = lambda t: vertex.y + t
            else:
                # Left opening
                x_t = lambda t: vertex.x - (1 / (4 * p)) * t**2
                y_t = lambda t: vertex.y + t
        
        return x_t, y_t
    


    @staticmethod
    def hyperbola_branches(vertices, foci):
        (vx1, vy1), (vx2, vy2) = vertices
        (fx1, fy1), (fx2, fy2) = foci

        # Center and distances
        center_x = (vx1 + vx2) / 2
        center_y = (vy1 + vy2) / 2
        a = np.sqrt((vx2 - vx1)**2 + (vy2 - vy1)**2) / 2
        c = np.sqrt((fx2 - fx1)**2 + (fy2 - fy1)**2) / 2
        b = np.sqrt(c**2 - a**2)
        
        def upper_branch(x):
            if abs(x - center_x) >= a:
                expression = (x - center_x)**2 / a**2 - 1
                if expression >= 0:
                    y = center_y + np.sqrt(expression * b**2)
                    return (x, y)
            return (x, np.nan)
        
        def lower_branch(x):
            if abs(x - center_x) >= a:
                expression = (x - center_x)**2 / a**2 - 1
                if expression >= 0:
                    y = center_y - np.sqrt(expression * b**2)
                    return (x, y)
            return (x, np.nan)

        return upper_branch, lower_branch
    
    @staticmethod
    def compute_hyperbola_range(vertices, foci, scale_factor=2):
        (vx1, vy1), (vx2, vy2) = vertices
        (fx1, fy1), (fx2, fy2) = foci
        
        # Calculate the center of the hyperbola (midpoint of the vertices)
        center_x = (vx1 + vx2) / 2
        
        # Calculate distance 'a' (half the distance between vertices)
        a = np.sqrt((vx2 - vx1)**2 + (vy2 - vy1)**2) / 2
        
        # Calculate distance 'c' (half the distance between foci)
        c = np.sqrt((fx2 - fx1)**2 + (fy2 - fy1)**2) / 2
        
        # The range should extend beyond the foci
        range_extension = scale_factor * c  # Extend the range by a factor of the distance to foci
        
        # Set the x-range symmetrically around the center
        min_x = center_x - (2 * a + range_extension)
        max_x = center_x + (2 * a + range_extension)
        
        return min_x, max_x
    
    @staticmethod
    def create_valid_x_values(vertices, foci, x_range_padding=2, num_points=100):
        """
        Create valid x-values for hyperbola by excluding the region between the vertices.
        
        Args:
        vertices (tuple): Two tuples representing the vertices of the hyperbola ((vx1, vy1), (vx2, vy2)).
        foci (tuple): Two tuples representing the foci of the hyperbola ((fx1, fy1), (fx2, fy2)).
        x_range_padding (float): Padding to extend the valid range beyond the vertices.
        num_points (int): Number of points to generate for the valid x-values.

        Returns:
        numpy.ndarray: Array of valid x-values for the hyperbola.
        """
        (vx1, vy1), (vx2, vy2) = vertices
        (fx1, fy1), (fx2, fy2) = foci

        # Calculate the center of the hyperbola (midpoint of the vertices)
        center_x = (vx1 + vx2) / 2
        
        # Calculate distance 'a' (half the distance between vertices)
        a = np.sqrt((vx2 - vx1)**2 + (vy2 - vy1)**2) / 2
        
        # Calculate distance 'c' (half the distance between foci)
        c = np.sqrt((fx2 - fx1)**2 + (fy2 - fy1)**2) / 2
        
        # Ensure that c >= a
        if c < a:
            raise ValueError("Foci should be further apart than the vertices for a valid hyperbola.")
        
        # Define the boundary where x-values become invalid
        left_bound = center_x - a
        right_bound = center_x + a
        
        # Generate x-values left of the left vertex and right of the right vertex
        left_x_values = np.linspace(left_bound - x_range_padding * a, left_bound, num_points // 2)
        right_x_values = np.linspace(right_bound, right_bound + x_range_padding * a, num_points // 2)
        
        # Concatenate the valid ranges together
        valid_x_values = np.concatenate((left_x_values, right_x_values))
        
        return valid_x_values
    
    @staticmethod
    def hyperbola_implicit_function(vertices, foci):
        """
        Generates a lambda function representing the implicit equation of a hyperbola
        given the vertices and foci.

        Args:
        vertices (tuple): Two tuples representing the vertices of the hyperbola ((vx1, vy1), (vx2, vy2)).
        foci (tuple): Two tuples representing the foci of the hyperbola ((fx1, fy1), (fx2, fy2)).

        Returns:
        lambda: A lambda function representing the implicit equation of the hyperbola.
        """
        (vx1, vy1), (vx2, vy2) = vertices
        (fx1, fy1), (fx2, fy2) = foci

        # Calculate the center of the hyperbola (midpoint of the vertices)
        center_x = (vx1 + vx2) / 2
        center_y = (vy1 + vy2) / 2

        # Calculate distance 'a' (half the distance between vertices)
        a = np.sqrt((vx2 - vx1)**2 + (vy2 - vy1)**2) / 2

        # Calculate distance 'c' (half the distance between foci)
        c = np.sqrt((fx2 - fx1)**2 + (fy2 - fy1)**2) / 2

        # Ensure that c >= a
        if c < a:
            raise ValueError("Foci must be further apart than the vertices for a valid hyperbola.")
        
        # Calculate 'b' using the relation c^2 = a^2 + b^2
        b_squared = c**2 - a**2

        # Return the lambda function for the implicit equation
        return lambda x, y: ((x - center_x)**2 / a**2) - ((y - center_y)**2 / b_squared) - 1
