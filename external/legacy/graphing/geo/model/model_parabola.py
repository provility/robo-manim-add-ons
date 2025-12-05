from graphing.geo.model.base_model import BaseModel
from graphing.math.function_expression_utils import FunctionUtils
from graphing.math.conic_utils import ConicUtils
from .base_model import BaseModel
import numpy as np
import sympy as sp
from sympy import Point, Segment, Ellipse, symbols, Eq, parse_expr, expand, solve, N, Matrix
from .model_point import ModelPoint
from .model_line import ModelLine
from sympy.parsing.latex import parse_latex

class AbstractParabola(BaseModel):
    def __init__(self, sympy_parabola):
        super().__init__()
        self.sympy_parabola = sympy_parabola

    
class ModelParabolaParametric(AbstractParabola):
    def __init__(self, sympy_parabola, x_parametric, y_parametric):
        super().__init__(sympy_parabola)
        self.x_parametric = x_parametric
        self.y_parametric = y_parametric
        
     
    def update(self, sympy_parabola, x_parametric, y_parametric):
        self.sympy_parabola = sympy_parabola
        self.x_parametric = x_parametric
        self.y_parametric = y_parametric
        self.notify()
        
    def point_at(self, t):
        return np.array([self.x_parametric(t), self.y_parametric(t), 0])
    
    def intersect_with_line(self, line:ModelLine, index=0):
        sympy_line = sp.Line2D(sp.Point(line.start[0], line.start[1]), sp.Point(line.end[0], line.end[1]))
        intersections  =  self.sympy_parabola.intersection(sympy_line)
        return ModelPoint(intersections[index][0].evalf(), intersections[index][1].evalf())
    
    def point_at_x(self, x):
        # Get the equation of the parabola
        equation = self.sympy_parabola.equation()
        
        # Create a symbol for y
        y = sp.Symbol('y')
        
        # Substitute the given x into the equation
        eq_at_x = equation.subs('x', x)
        
        # Solve for y
        solutions = sp.solve(eq_at_x, y)
        
        # There might be multiple solutions, but for a parabola, we typically want the real solution
        y_value = next((sol for sol in solutions if sol.is_real), None)
        
        if y_value is None:
            raise ValueError(f"No real y value found for x = {x}")
        
        return ModelPoint(x, float(y_value))
  
    @property
    def eccentricity(self):
        return self.sympy_parabola.eccentricity
  
    @property
    def vertex(self):
        vertex_point = self.sympy_parabola.vertex
        return ModelPoint(vertex_point[0].evalf(), vertex_point[1].evalf())
    
    @property
    def focus(self):
        focus_point = self.sympy_parabola.focus
        return ModelPoint(focus_point[0].evalf(), focus_point[1].evalf())
    
    @property
    def directrix(self):
         directrix_lines = self.sympy_parabola.directrix
         points = directrix_lines.points
         return  ModelLine(points[0][0].evalf(),points[0][1].evalf(), points[1][0].evalf(), points[1][1].evalf())
       
    @property
    def axis_of_symmetry(self):
        axis_of_symmetry_line = self.sympy_parabola.axis_of_symmetry
        points = axis_of_symmetry_line.points
        return  ModelLine(points[0][0].evalf(),points[0][1].evalf(), points[1][0].evalf(), points[1][1].evalf())
    
    @staticmethod
    def from_focus_and_directrix(focus_point, directrix_line):
        model_parabola_parametric = None    
        def compute():
            nonlocal model_parabola_parametric
            sympy_focus = sp.Point2D(focus_point.x, focus_point.y)
            direct_start = directrix_line.start
            direct_end = directrix_line.end
            sympy_directrix = sp.Line2D(sp.Point(direct_start[0], direct_start[1]), sp.Point(direct_end[0], direct_end[1]))
            sympy_parabola = sp.Parabola(sympy_focus, sympy_directrix)
            x_parametric, y_parametric = ConicUtils.parabola_parametric_functions(sympy_parabola)
            return sympy_parabola, x_parametric, y_parametric
        
        def create():
            nonlocal model_parabola_parametric
            sympy_parabola, x_parametric, y_parametric = compute()  
            model_parabola_parametric = ModelParabolaParametric(sympy_parabola, x_parametric, y_parametric)
            
        def update():
            nonlocal model_parabola_parametric
            sympy_parabola, x_parametric, y_parametric = compute()  
            model_parabola_parametric.update(sympy_parabola, x_parametric, y_parametric)
            
        create()    
        #hook dependencies
        focus_point.on_change(update)
        directrix_line.on_change(update)    
        
        return model_parabola_parametric
    
    
