class CameraConfig:
    
    """
    This is the camera configuration for the 3D scene in Manim *ThreedAxes
    
    """
    @staticmethod
    def x_towards_y_right_z_up():
        return {
            "phi": 75,
            "theta": 45,
            "gamma": 0
        }
    
    @staticmethod
    def y_right_z_up_x_towards_origin():
        return {
            "phi": 0,
            "theta": 0,
            "gamma": 0
        }
    
    """
    Giving all angles to 0 will align Y towards the viewer and Z towards UP
    by default, 
    X points to the right
    Y points forward towards the viewer 
    Z points up 
    phi is rotation about the horizontal (X) axis - looking up or down
    theta is rotation about the Vertical (Z) axis - looking left or right
    gamma is rotation about the Depth (Y) axis - roll - rotating the view around the depth axis
    """
    @staticmethod
    def x_right_y_up_z_towards_origin():
        return {
            "phi": 0,    
            "theta": -90,   
            "gamma": 0    
        }

        
        
        
  
        