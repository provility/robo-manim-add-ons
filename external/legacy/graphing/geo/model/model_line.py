from graphing.geo.model.model_parameter import ModelParameter
from graphing.math.function_expression_utils import FunctionUtils
from .base_model import BaseModel
import math
import numpy as np
import sympy as sp
import sympy.geometry as spg
from sympy import Point, Segment, Rational, latex, symbols, Eq, solve
from manim import *
from .model_point import ModelPoint

class ModelLine2Points(BaseModel):
      def __init__(self, from_point:ModelPoint, to_point:ModelPoint):
        super().__init__()
        self.from_point = from_point
        self.to_point = to_point
        self.model_points = [from_point, to_point]
        self.sympy_segment = self.create_segment()  

      def create_segment(self):
          return sp.Segment2D(sp.Point(self.from_point.x,self.from_point.y), sp.Point(self.to_point.x,self.to_point.y))
      
      def update(self):
          self.sympy_segment = self.create_segment()
          self.notify()
          
      def end_model_point(self):
          return self.to_point
      
      def start_model_point(self):
          return self.from_point
          
      def update_points(self, from_point:ModelPoint, to_point:ModelPoint):
          self.from_point.set(from_point.x, from_point.y)
          self.to_point.set(to_point.x, to_point.y) 
          self.sympy_segment = self.create_segment()
          self.notify()
          
      def update_end_point(self, to_point:ModelPoint):
          self.to_point.set(to_point.x, to_point.y) 
          self.sympy_segment = self.create_segment()
          self.notify()
          
      @property     
      def start(self): 
          return [self.from_point.x, self.from_point.y]    
    
      @property     
      def end(self): 
          return [self.to_point.x, self.to_point.y] 
      
      @property
      def start_x(self):
          return self.from_point.x
      
      @property
      def start_y(self):
          return self.from_point.y
      
      @property 
      def end_x(self):
          return self.to_point.x
      
      @property
      def end_y(self):
          return self.to_point.y
      
      @property
      def length(self):
          return self.sympy_segment.length
    
      @property
      def distance(self):
          return self.sympy_segment.length
   
      def point_index(self, index):
        if index == 0:
            return self.model_points[0] # start point
        elif index == 1:
            return self.model_points[1] # end point
        else:
            raise ValueError("Invalid index for line points")
        
      def get_all_points(self):
        return self.model_points
   
      def as_points(self):
        return [self.from_point.x, self.from_point.y, self.to_point.x, self.to_point.y]
    
      def sympy_line(self):
          return self.sympy_segment
    
      @property
      def mid_point(self):
          return ModelPoint((self.from_point.x + self.to_point.x) / 2, (self.from_point.y + self.to_point.y) / 2)
    
      @property
      def perpendicular_bisector(self):
          perpendicular_bisector = sp.Line(sp.Point(self.from_point.x,self.from_point.y), sp.Point(self.to_point.x,self.to_point.y)).perpendicular_bisector()
          return ModelLine2Points(ModelPoint(perpendicular_bisector.p1.x, perpendicular_bisector.p1.y), ModelPoint(perpendicular_bisector.p2.x, perpendicular_bisector.p2.y))
    
      def point_at(self, at): # This is just for calculation. 
          line_from_manim = Line(np.array([self.from_point.x, self.from_point.y, 0]), np.array([self.to_point.x, self.to_point.y, 0]))
          return line_from_manim.point_from_proportion(at)
      
      def model_point_at(self, at):
          self.point_at(at)
          return ModelPoint()

      def _update_model_points(self):
          self.model_points[0].set(self.from_point.x, self.from_point.y)
          self.model_points[1].set(self.to_point.x, self.to_point.y)
    
      def point_at_x(self, x):
        # Create a SymPy Line object
        line = sp.Line(sp.Point(self.from_point.x, self.from_point.y), sp.Point(self.to_point.x, self.to_point.y))
        
        # Calculate the point using the parametric form of the line equation
        point = line.arbitrary_point()
        x, y = point.x.subs('t', x), point.y.subs('t', x)
        
        # Return as a ModelPoint
        return ModelPoint(float(x), float(y))
    
     
      @property
      def midpoint(self):
          mid_x = (self.from_point.x + self.to_point.x) / 2
          mid_y = (self.from_point.y + self.to_point.y) / 2
          return ModelPoint(mid_x, mid_y)

      def contains_point(self, model_point: ModelPoint):
          line = sp.Line(sp.Point(self.from_point.x, self.from_point.y), sp.Point(self.to_point.x, self.to_point.y))
          point = model_point.to_sympy()
          return line.contains(point)

      def distance_to_point(self, model_point: ModelPoint):
          line = sp.Line(sp.Point(self.from_point.x, self.from_point.y), sp.Point(self.to_point.x, self.to_point.y))
          point = model_point.to_sympy()
          return line.distance(point)

      @property
      def slope_fraction(self):
          if self.to_point.x - self.from_point.x == 0:
              return r"\infty"  # Vertical line
        
          rise = self.to_point.y - self.from_point.y
          run = self.to_point.x - self.from_point.x
        
          # Use sympy's Rational for exact fraction representation
          fraction = Rational(rise, run)
        
          # Convert to LaTeX string
          if fraction.q == 1:  # If denominator is 1, just return the numerator
              return str(fraction.p)
          else:
              return latex(fraction)
        
      @property
      def slope(self):
          if self.to_point.x - self.from_point.x == 0:
              return float('inf')  # Vertical line
          return (self.to_point.y - self.from_point.y) / (self.to_point.x - self.from_point.x)

      @property
      def y_intercept(self):
          if self.slope == float('inf'):
            return r"\text{undefined}"  # Vertical line has no y-intercept
          y_intercept = self.from_point.y - self.slope * self.from_point.x
          return latex(y_intercept)
    
      def is_parallel(self, other_line):
          line1 = sp.Line(sp.Point(self.from_point.x, self.from_point.y), sp.Point(self.to_point.x, self.to_point.y))
          line2 = sp.Line(sp.Point(other_line.from_point.x, other_line.from_point.y), sp.Point(other_line.to_point.x, other_line.to_point.y))
          return line1.is_parallel(line2)


      @property
      def slope_intercept_form_latex(self):
          x, y = symbols('x y')
          m = self.slope
          b = self.y_intercept
          if m == float('inf'):
              return r"x = " + latex(self.from_point.x)
          eq = Eq(y, m*x + b)
          return latex(eq)

      @property
      def point_slope_form_latex(self):
          x, y = symbols('x y')
          x1, y1 = self.from_point.x, self.from_point.y
          m = self.slope
          if m == float('inf'):
            return r"x = " + latex(x1)
          eq = Eq(y - y1, m*(x - x1))
          return latex(eq)

      @property
      def general_form_latex(self):
          x, y = symbols('x y')
          A = self.from_point.y - self.to_point.y
          B = self.to_point.x - self.from_point.x
          C = self.from_point.x * self.to_point.y - self.to_point.x * self.from_point.y
          eq = Eq(A*x + B*y + C, 0)
          return latex(eq)

      @property
      def two_point_form_latex(self):
          x, y = symbols('x y')
          x1, y1 = self.from_point.x, self.from_point.y
          x2, y2 = self.to_point.x, self.to_point.y
          eq = Eq((y - y1)*(x2 - x1), (y2 - y1)*(x - x1))
          return latex(eq)

      @property
      def intercept_form_latex(self):
          x, y = symbols('x y')
          if self.slope == 0:
              return r"y = " + latex(self.from_point.y)
          elif self.slope == float('inf'):
              return r"x = " + latex(self.from_point.x)
          else:
              x_intercept = -self.y_intercept / self.slope
              y_intercept = self.from_point.y - self.slope * self.from_point.x
              eq = Eq(x/x_intercept + y/y_intercept, 1)
              return latex(eq)

      @property
      def parametric_form_latex(self):
          x, y = symbols('x y')
          t = symbols('t')
          x0, y0 = self.from_point.x, self.from_point.y
          dx, dy = self.to_point.x - self.from_point.x, self.to_point.y - self.from_point.y
          eq = Eq(x, x0 + t*dx)
          eq = Eq(y, y0 + t*dy)   
          return latex(eq)

      @property
      def symmetric_form_latex(self):
          x, y = symbols('x y')
          x1, y1 = self.from_point.x, self.from_point.y
          x2, y2 = self.to_point.x, self.to_point.y
          eq = Eq((x - x1)/(x2 - x1), (y - y1)/(y2 - y1))
          return latex(eq)
  
    
      def projection(self, model_point:ModelPoint):
          try:
              line = sp.Line(sp.Point(self.from_point.x,self.from_point.y), sp.Point(self.to_point.x,self.to_point.y))
              point = model_point.to_sympy()
              projection = line.projection(point)
              return ModelPoint(projection.x, projection.y)
          except spg.GeometryError:
            return None
            
      def intersection(self, other):
          try:
              line1 = sp.Line(sp.Point(self.from_point.x,self.from_point.y), sp.Point(self.to_point.x,self.to_point.y))
              line2 = sp.Line(sp.Point(other.from_point.x,other.from_point.y), sp.Point(other.to_point.x,other.to_point.y))
              intersection_points = line1.intersection(line2)
              if isinstance(intersection_points[0], sp.Line2D): # if the points are same, the intersection returns a Line2D object
                  intersection_point =  intersection_points[0].p1
              else:
                  intersection_point = intersection_points[0]
              return ModelPoint(intersection_point.x, intersection_point.y)
          except spg.GeometryError:
              return None
    
      def reflection(self, model_point:ModelPoint):
          line = sp.Line(sp.Point(self.from_point.x,self.from_point.y), sp.Point(self.to_point.x,self.to_point.y))
          point = model_point.to_sympy()
          # SymPy Line doesn't have a reflection method, but we can calculate it
          projection = line.projection(point)
          reflection = 2 * projection - point
          return ModelPoint(reflection.x, reflection.y, 0)   
    
      def parallel_line(self, model_point:ModelPoint):
          model_line = None
          
          def computation():
            # This is sympy line
            line = sp.Line(sp.Point(self.from_point.x,self.from_point.y), sp.Point(self.to_point.x,self.to_point.y))
            parallel = line.parallel_line(model_point.to_sympy())
            p1, p2 = parallel.points
            return p1, p2
        
          def create():
              nonlocal model_line  
              p1, p2 = computation()
              model_line = ModelLine2Points(ModelPoint(p1.x, p1.y), ModelPoint(p2.x, p2.y))
            
          def update():   
              nonlocal model_line  
              p1, p2 = computation()
              model_line.update_points(ModelPoint(p1.x, p1.y), ModelPoint(p2.x, p2.y))

          create()
          
          # hook dependencies, when the input line and the point change, 
          # the output line should get change
          self.on_change(lambda: update())
          model_point.on_change(lambda: update())
          return model_line
        
      def perpendicular_line(self, model_point:ModelPoint):
        model_line = None
        
        def computation():
            line = sp.Line(sp.Point(self.from_point.x,self.from_point.y), sp.Point(self.to_point.x,self.to_point.y))
            perpendicular = line.perpendicular_line(model_point.to_sympy())
            p1, p2 = perpendicular.points
            return p1, p2
        
        def create():
            nonlocal model_line  
            p1, p2 = computation()
            model_line = ModelLine2Points(ModelPoint(p1.x, p1.y), ModelPoint(p2.x, p2.y))
            
        def update():   
            nonlocal model_line  
            p1, p2 = computation()
            model_line.update_points(ModelPoint(p1.x, p1.y), ModelPoint(p2.x, p2.y))
            
        create()
        
        # hook dependencies, when the input line and the point change, 
        # the output line should get changed as well
        self.on_change(lambda: update())
        model_point.on_change(lambda: update())
        return model_line 
    
class ModelLine(ModelLine2Points):
    def __init__(self, start_x, start_y, end_x, end_y):
        super().__init__(ModelPoint(start_x, start_y), ModelPoint(end_x, end_y))
  
    def update(self, start_x, start_y, end_x, end_y):
         self.from_point.set(start_x, start_y)
         self.to_point.set(end_x, end_y)
         self.sympy_segment = self.create_segment() 
         self.notify()
         

        
    @staticmethod        
    def from_points(a:ModelPoint, b:ModelPoint):
        model_line = ModelLine2Points(a,b)
        a.on_change(lambda:  model_line.update())
        b.on_change(lambda:  model_line.update())
        return model_line
    
    @staticmethod
    def from_slope_and_intercept(slope_paramter:ModelParameter, 
                                 intercept_paramter:ModelParameter, segment_length:float):
        model_line = None   
        
        def computation():
            start_x = -segment_length / 2  # Use half of the segment length for start_x
            start_y = slope_paramter.get_value() * start_x + intercept_paramter.get_value()
            end_x = segment_length / 2  # Use half of the segment length for end_x
            end_y = slope_paramter.get_value() * end_x + intercept_paramter.get_value()
            return start_x, start_y, end_x, end_y

        def create():
            nonlocal model_line
            start_x, start_y, end_x, end_y = computation()
            model_line = ModelLine(start_x, start_y, end_x, end_y)
        
        def update():
            nonlocal model_line
            start_x, start_y, end_x, end_y = computation()
            model_line.update(start_x, start_y, end_x, end_y)
        
        create()
        
        # Hook dependencies
        slope_paramter.on_change(lambda: update())
        intercept_paramter.on_change(lambda: update())  
        return model_line   
    
    @staticmethod
    def from_slope_and_point(slope_paramter:ModelParameter, point:ModelPoint):
        model_line = None
        
        def computation():
            # Calculate the y-intercept using the point-slope form
            y_intercept = point.y - slope_paramter.get_value() * point.x
            
            # Calculate two points on the line
            x1 = point.x - 0.5  # Arbitrary point to the left
            y1 = slope_paramter.get_value() * x1 + y_intercept
            x2 = point.x + 0.5  # Arbitrary point to the right
            y2 = slope_paramter.get_value() * x2 + y_intercept
            
            return x1, y1, x2, y2
        
        def create():
            nonlocal model_line
            x1, y1, x2, y2 = computation()
            model_line = ModelLine(x1, y1, x2, y2)
        
        def update():
            nonlocal model_line
            x1, y1, x2, y2 = computation()
            model_line.update(x1, y1, x2, y2)
        
        create()
        
        # Hook dependencies
        slope_paramter.on_change(lambda: update())
        point.on_change(lambda: update())
        return model_line
    
    @staticmethod
    def from_general_equation( general_equation : str, segment_length: float = 12):
        model_line = None
        
        # Parse the equation string
        x, y = sp.symbols('x y')
       
        expression = FunctionUtils.ensure_expression(general_equation)
        
        # Extract coefficients A, B, and C from Ax + By + C = 0
     
        A = expression.coeff(x)
        B = expression.coeff(y)
        C = expression.as_coeff_add(x, y)[0]
        
        def create():
            nonlocal model_line
            if B != 0:
                m = -A / B
                b = -C / B
                x1, x2 = -segment_length / 2, segment_length / 2
                y1, y2 = m * x1 + b, m * x2 + b
            else:
                # Vertical line
                x1 = x2 = -C / A
                y1, y2 = -segment_length / 2, segment_length / 2
            
            model_line = ModelLine(x1, y1, x2, y2)
        
        create()
        return model_line
    
    # normal form of line equation is y=mx+c  
    @staticmethod  
    def from_normal_equation(normal_equation: str, segment_length: float = 10):
       
        expression = FunctionUtils.ensure_expression(normal_equation)
        
        # Extract coefficients m and c from the equation
        m = expression.coeff(sp.Symbol('x'))
        c = expression.as_coeff_add(sp.Symbol('x'), sp.Symbol('y'))[0]
        
        # Calculate two points on the line
        x1 = -segment_length / 2
        y1 = m * x1 + c
        x2 = segment_length / 2
        y2 = m * x2 + c
        
        return ModelLine(x1, y1, x2, y2)
    
    
    @staticmethod
    def reflect_over_line(model_line, point_to_reflect:ModelPoint):
        model_point = None
        
        
        def computation():
            return model_line.reflection(point_to_reflect)
        
        def create():
            nonlocal model_point
            model_point = computation()   
            
        def update():
            nonlocal model_point
            new_point = computation()
            model_point.update(new_point.x, new_point.y)
            
        create()
        
        point_to_reflect.on_change(lambda: update())
        model_line.on_change(lambda: update())
        return model_point
    
    @staticmethod    
    def projection_on_line(point_to_project:ModelPoint, line_to_project_onto):
        projected_point = None
       
        def computation():
            line = line_to_project_onto.sympy_line()
            point = point_to_project.to_sympy()
            try:    
                projection = line.projection(point)
            except spg.GeometryError:
                return None
            return projection   
           
        
        def create():
            nonlocal projected_point  
            point = computation()
            if point is None:
                projected_point.set(10000, 10000, 0)
            else:    
                projected_point = ModelPoint.from_sym_point(point)
             
            
        def update():   
            nonlocal projected_point   
            point = computation()   
            if point is None:
                projected_point.set(10000, 10000, 0)
            else:    
                 projected_point.set(point.x, point.y, 0)
                         
            
        create()
        
        # hook dependencies, when the input line and the point change, 
        # the output line should get changed as well
        line_to_project_onto.on_change(lambda: update())
        point_to_project.on_change(lambda: update())
        return projected_point
        
    @staticmethod
    def point_on_line(model_line, parameter_or_value):
        model_point = None

        def create():
            nonlocal model_point
            model_point = model_line.point_at(parameter_or_value)   
            
        def update():
            nonlocal model_point
            new_point = model_line.point_at(parameter_or_value)
            model_point.set(new_point.x, new_point.y, 0)
            
        create()
        parameter_or_value.on_param_change(lambda d: update())
        model_line.on_change(lambda: update())
        return model_point  
    
    
    @staticmethod    
    def projection_line_on_line(point_to_project:ModelPoint, line_to_project_onto):
        projection_line = None
       
        def computation():
            line = line_to_project_onto.sympy_line()
            point = point_to_project.to_sympy()
            try:    
                projection = line.projection(point)
                if projection is not None:
                    return ModelPoint(projection.x, projection.y)
            except spg.GeometryError:
                return ModelPoint(-10000, -10000)     
            return ModelPoint(-10000, -10000)   
           
        
        def create():
            nonlocal projection_line  
            projected_point = computation()
            projection_line =  ModelLine2Points(point_to_project, projected_point);   
      
            
        def update():   
            nonlocal projection_line   
            projected_point = computation()
            projection_line.update_end_point(projected_point)
                         
            
        create()
        
        # hook dependencies, when the input line and the point change, 
        # the output line should get changed as well
        line_to_project_onto.on_change(lambda: update())
        point_to_project.on_change(lambda: update())
        return projection_line
    
    
    