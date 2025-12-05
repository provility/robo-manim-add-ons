from graphing.geo.model.base_model import BaseModel
from graphing.math.conic_utils import ConicUtils


class ModelHyperbola(BaseModel):
    def __init__(self, focus_a, focus_b, vertex_a, vertex_b, hyperbola_implicit_function):
        super().__init__()
        self.focus_a = focus_a
        self.focus_b = focus_b
        self.vertex_a = vertex_a
        self.vertex_b = vertex_b
        self.hyperbola_implicit_function = hyperbola_implicit_function
       
        
    def update(self, focus_a, focus_b, vertex_a, vertex_b, hyperbola_implicit_function):    
        self.focus_a = focus_a
        self.focus_b = focus_b
        self.vertex_a = vertex_a
        self.vertex_b = vertex_b
        self.hyperbola_implicit_function = hyperbola_implicit_function

    @staticmethod    
    def from_foci_and_vertices(focus_a_point, focus_b_point, vertex_a_point, vertex_b_point):
        model_hyperbola = None
        
        def compute():  
            # Convert points to tuples
            vertices = (vertex_a_point.x, vertex_a_point.y), (vertex_b_point.x, vertex_b_point.y)
            foci = (focus_a_point.x, focus_a_point.y), (focus_b_point.x, focus_b_point.y)   
            hyperbola_implicit_function = ConicUtils.hyperbola_implicit_function(vertices, foci)
            return hyperbola_implicit_function
        
        def create():
            nonlocal model_hyperbola
            hyperbola_implicit_function = compute()
            model_hyperbola = ModelHyperbola(focus_a_point, focus_b_point, vertex_a_point, vertex_b_point, hyperbola_implicit_function)    
        
        create()
        
        def update():
            nonlocal model_hyperbola
            hyperbola_implicit_function = compute()
            model_hyperbola.update(focus_a_point, focus_b_point, vertex_a_point, vertex_b_point, hyperbola_implicit_function)
        
        focus_a_point.on_change(update)
        focus_b_point.on_change(update)
        vertex_a_point.on_change(update)
        vertex_b_point.on_change(update)    
        
        return model_hyperbola
        
        