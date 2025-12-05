from typing import Any
from sympy import Point, Triangle, cos, sin, pi

import math
from graphing.geo.model.model_angle import ModelAngle
from graphing.geo.model.model_line import ModelLine
from graphing.geo.model.model_parameter import ModelParameter
from .base_model import BaseModel
from .model_point import ModelPoint
class ModelTriangle(BaseModel):
      def __init__(self, model_point_a:ModelPoint, model_point_b:ModelPoint, model_point_c:ModelPoint) -> Any:
            super().__init__()
            self.model_point_a = model_point_a
            self.model_point_b = model_point_b
            self.model_point_c = model_point_c
            self.sympy_triangle =  Triangle(model_point_a.to_sympy(), model_point_b.to_sympy(), model_point_c.to_sympy())
            self._side_a = None
            self._side_b = None
            self._side_c = None
            self._angle_a = None
            self._angle_b = None
            self._angle_c = None
            self.create_dependencies()
            
      def update(self):
          self.notify()
          self.sympy_triangle =  Triangle(self.model_point_a.to_sympy(), self.model_point_b.to_sympy(), self.model_point_c.to_sympy())    
          
      def update_from_points(self, model_point_a, model_point_b, model_point_c):
          self.model_point_a.set(*model_point_a.to_x_y())
          self.model_point_b.set(*model_point_b.to_x_y())
          self.model_point_c.set(*model_point_c.to_x_y())
          self.update()
          
      """
      use the same point references for all the dependencies
      """
      def create_dependencies(self):
          # when points change, the lines should also get updated, so dont create ModelLine with constructor version, 
          # as far as ModelAngle is concerned, it will be updated when the points change, 
          # so constructor version is fine.
          self._side_a = ModelLine.from_points(self.model_point_a, self.model_point_b)
          self._side_b = ModelLine.from_points(self.model_point_b, self.model_point_c)
          self._side_c = ModelLine.from_points(self.model_point_c, self.model_point_a)
          self._angle_a = ModelAngle(self.model_point_b, self.model_point_a, self.model_point_c)
          self._angle_b = ModelAngle(self.model_point_c, self.model_point_b, self.model_point_a)
          self._angle_c = ModelAngle(self.model_point_a, self.model_point_c, self.model_point_b)
          
    
      def point_index(self, index):
          if index == 0:
              return self.model_point_a
          elif index == 1:
              return self.model_point_b
          elif index == 2:
              return self.model_point_c
          else: 
              raise ValueError("Invalid index for triangle points") 
          
      def get_all_points(self):
          return [self.model_point_a, self.model_point_b, self.model_point_c]
      

      @property    
      def area(self):
          return self.sympy_triangle.area
    
      @property
      def perimeter(self):
          return self.sympy_triangle.perimeter
    
      @property
      def centroid(self):
          return self.sympy_triangle.centroid
      
      @property
      def incenter(self):
          return self.sympy_triangle.incenter
    
      @property
      def circumcenter(self):
          return self.sympy_triangle.circumcenter
    
      @property
      def orthocenter(self):
          return self.sympy_triangle.orthocenter
      
      @property
      def point_a(self):
          return self.model_point_a
      
      @property
      def point_b(self):
          return self.model_point_b
      
      @property
      def point_c(self):
          return self.model_point_c 
      
      @property
      def side_a(self):
          return self._side_a
      
      @property
      def side_b(self):
          return self._side_b
      
      @property
      def side_c(self):
          return self._side_c
      
      @property
      def angle_a(self):
          return self._angle_a
      
      @property
      def angle_b(self):
          return self._angle_b
      
      @property
      def angle_c(self):
          return self._angle_c
    
      @staticmethod
      def from_points(self, model_point_a, model_point_b, model_point_c):
          model_triangle = ModelTriangle(model_point_a, model_point_b, model_point_c)
        
          def update():
             nonlocal model_triangle
             model_triangle.update()

          # Hook dependencies
          model_point_a.on_change(lambda: update())
          model_point_b.on_change(lambda: update())
          model_point_c.on_change(lambda: update())

          return model_triangle
    
  
      @staticmethod
      def triangle_from_angle_and_side(angle:ModelParameter, side_a:ModelParameter, side_b:ModelParameter   ):
       
          def computation():
              # Convert angle to radians
              angle_rad = angle.get_value() * pi / 180

              # Construct the triangle using SymPy
              A = Point(0, 0)
              B = Point(side_a.get_value(), 0)
              C = Point(side_b.get_value() * cos(angle_rad), side_b.get_value() * sin(angle_rad))

              # Create a SymPy Triangle
              sympy_triangle = Triangle(A, B, C)

              # Extract points from the SymPy Triangle
              points = sympy_triangle.vertices

              # Create ModelPoints
              model_point_a = ModelPoint(float(points[0].x), float(points[0].y))
              model_point_b = ModelPoint(float(points[1].x), float(points[1].y))
              model_point_c = ModelPoint(float(points[2].x), float(points[2].y))

              return model_point_a, model_point_b, model_point_c

          # Compute initial points
          point_a, point_b, point_c = computation()

          # Create ModelTriangle
          model_triangle = ModelTriangle(point_a, point_b, point_c)

          def update():
              nonlocal model_triangle
              new_point_a, new_point_b, new_point_c = computation()
              model_triangle.update_from_points(new_point_a, new_point_b, new_point_c)

          # Hook dependencies (assuming angle, side_a, and side_b are ModelParameters)
          angle.on_change(lambda: update())
          side_a.on_change(lambda: update())
          side_b.on_change(lambda: update())

          return model_triangle
  
      @staticmethod
      def from_base_and_height(base:ModelParameter, height:ModelParameter):
          model_triangle = None
          def computation():
              base_value = base.get_value()
              height_value = height.get_value()

                # Calculate the coordinates of the points
              A = Point(0, 0)
              B = Point(base_value, 0)
              C = Point(base_value / 2, height_value)

            # Create ModelPoints
              model_point_a = ModelPoint(float(A.x), float(A.y))
              model_point_b = ModelPoint(float(B.x), float(B.y))
              model_point_c = ModelPoint(float(C.x), float(C.y))
            
              model_triangle = ModelTriangle(model_point_a, model_point_b, model_point_c)   

          def update():
              nonlocal model_triangle
              new_point_a, new_point_b, new_point_c = computation()
              model_triangle.update_from_points(new_point_a, new_point_b, new_point_c)

          # Hook dependencies
          base.on_change(lambda: update())
          height.on_change(lambda: update())
          return model_triangle
          
          
      @staticmethod
      def from_three_sides(a, b, c, origin_point):
          model_triangle = None
          model_point_a = None
          model_point_b = None
          model_point_c = None  
          def computation():
              # Convert ModelParameters to SymPy parameters
              a_value = a.get_value()
              b_value = b.get_value()
              c_value = c.get_value()
              
              # create the points from the origin point and the sides
              point_a = ModelPoint(origin_point.x, origin_point.y)
              point_b = ModelPoint(origin_point.x + a_value, origin_point.y)
              # Calculate the angle using the law of cosines
              angle_rad = math.acos((a_value**2 + b_value**2 - c_value**2) / (2 * a_value * b_value))
              point_c = ModelPoint(origin_point.x + b_value * math.cos(angle_rad), origin_point.y + b_value * math.sin(angle_rad))
              return point_a, point_b, point_c
          
          def create():
              nonlocal model_triangle, model_point_a, model_point_b, model_point_c
              # Compute initial points
              point_a, point_b, point_c = computation()   
              model_point_a, model_point_b, model_point_c = point_a, point_b, point_c
              model_triangle = ModelTriangle(model_point_a, model_point_b, model_point_c)

          # Create ModelTriangle
          create()

          def update():
              nonlocal model_triangle
              new_point_a, new_point_b, new_point_c = computation()
              model_triangle.update_from_points(new_point_a, new_point_b, new_point_c)

          # Hook dependencies   
          a.on_change(lambda: update())
          b.on_change(lambda: update())
          c.on_change(lambda: update())
          model_point_a.on_change(lambda: update())
          model_point_b.on_change(lambda: update())
          model_point_c.on_change(lambda: update()) 
          origin_point.on_change(lambda: update())
          
          return model_triangle 
