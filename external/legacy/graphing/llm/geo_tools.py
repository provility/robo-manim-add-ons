tools_list = """

1. **Point**
   - **Function**: `Point[x, y]`
   - **Arguments**: Coordinates x and y for the point.

2. **Point on Object**
   - **Function**: `Point[m]`
   - **Arguments**: An object m (such as a line, curve, or segment) on which to place the point.

3. **Intersect**
   - **Function**: `Intersection[m, n]`
   - **Arguments**: Two objects m and n to find their intersection point(s).

4. **Midpoint or Centre**
   - **Function**: `Midpoint[A, B]`
   - **Arguments**: Two points A and B to find the midpoint.

5. **Attach / Detach Point**
   - **Function**: `Attach[A, m]` / `Detach[A]`
   - **Arguments**: A point A to attach to an object m or to detach from its current object.

6. **Complex Number**
   - **Function**: `Complex[a, b]`
   - **Arguments**: Real part a and imaginary part b of the complex number.

7. **Extremum**
   - **Function**: `Extremum[f]`
   - **Arguments**: A function f to find its extremum points.

8. **Roots**
   - **Function**: `Roots[f]`
   - **Arguments**: A function f to find its roots (where f(x) = 0).

9. **Line**
   - **Function**: `Line[A, B]`
   - **Arguments**: Two points A and B to define the line.

10. **Segment**
   - **Function**: `Segment[A, B]`
   - **Arguments**: Two points A and B to create the line segment.

11. **Segment with Given Length**
   - **Function**: `Segment[A, length]`
   - **Arguments**: A point A and a specified length for the segment.

12. **Ray**
   - **Function**: `Ray[A, B]`
   - **Arguments**: A starting point A and a direction point B to create the ray.

13. **Polyline**
   - **Function**: `Polyline[A, B, C, ...]`
   - **Arguments**: A list of points A, B, C, etc., to create the polyline.

14. **Vector**
   - **Function**: `Vector[A, B]`
   - **Arguments**: Two points A and B to define the vector from A to B.

15. **Vector from Point**
   - **Function**: `Vector[v]`
   - **Arguments**: A vector v defined by its components or from a point.


16. **Perpendicular Line**
   - **Function**: `PerpendicularLine[m, A]`
   - **Arguments**: A line m and a point A to create a line perpendicular to m through A.

17. **Parallel Line**
   - **Function**: `ParallelLine[m, A]`
   - **Arguments**: A line m and a point A to create a line parallel to m through A.

18. **Perpendicular Bisector**
   - **Function**: `PerpendicularBisector[A, B]`
   - **Arguments**: Two points A and B to create the perpendicular bisector of the segment connecting A and B.

19. **Angle Bisector**
   - **Function**: `AngleBisector[A, B, C]`
   - **Arguments**: Three points A, B, and C to create the angle bisector of the angle formed at point B.

20. **Tangents**
   - **Function**: `Tangent[C, P]`
   - **Arguments**: A circle C and a point P outside the circle to create the tangent line from P to C.

21. **Polar or Diameter Line**
   - **Function**: `Polar[A, C]`
   - **Arguments**: A point A and a circle C to create the polar line of A with respect to C.

22. **Best Fit Line**
   - **Function**: `BestFitLine[{A, B, C, ...}]`
   - **Arguments**: A list of points {A, B, C, ...} to create a line of best fit for the given points.

23. **Locus**
   - **Function**: `Locus[A, m]`
   - **Arguments**: A point A and a moving object m to create the locus of A as m moves.
   
24. **Polygon**
   - **Function**: `Polygon[A, B, C, ...]`
   - **Arguments**: A list of points A, B, C, etc., to create a polygon defined by these vertices.

25. **Regular Polygon**
   - **Function**: `RegularPolygon[n, A]`
   - **Arguments**: An integer n for the number of sides and a point A for the center to create a regular polygon with n sides.

26. **Rigid Polygon**
   - **Function**: `RigidPolygon[A, B, C, ...]`
   - **Arguments**: A list of points A, B, C, etc., to create a rigid polygon that maintains its shape and size when moved.

27. **Vector Polygon**
   - **Function**: `VectorPolygon[A, B, C, ...]`
   - **Arguments**: A list of points A, B, C, etc., to create a polygon where the sides are represented as vectors.   
   
28. **Circle with Centre through Point**
   - **Function**: `Circle[A, B]`
   - **Arguments**: A center point A and a point B on the circumference to create a circle.

29. **Circle with Centre and Radius**
   - **Function**: `Circle[A, r]`
   - **Arguments**: A center point A and a radius r to create a circle with the specified radius.

30. **Compasses**
   - **Function**: `Compass[A, B]`
   - **Arguments**: A center point A and a point B to create a circle using a compass tool.

31. **Circle through 3 Points**
   - **Function**: `Circle[A, B, C]`
   - **Arguments**: Three points A, B, and C to create a circle that passes through all three points.

32. **Semicircle through 2 Points**
   - **Function**: `Semicircle[A, B]`
   - **Arguments**: Two points A and B to create a semicircle with endpoints at A and B.

33. **Circular Arc**
   - **Function**: `Arc[A, B, C]`
   - **Arguments**: Three points A, B, and C to create a circular arc from A to B with C as a point on the arc.

34. **Circumcircular Arc**
   - **Function**: `CircumcircularArc[A, B, C]`
   - **Arguments**: Three points A, B, and C to create a circumcircular arc that passes through these points.

35. **Circular Sector**
   - **Function**: `Sector[A, B, C]`
   - **Arguments**: Three points A (center), B (on the circle), and C (on the circle) to create a circular sector defined by these points.

36. **Circumcircular Sector**
   - **Function**: `CircumcircularSector[A, B, C]`
   - **Arguments**: Three points A, B, and C to create a circumcircular sector defined by the circumcircle of triangle ABC.   

37. **Ellipse**
   - **Function**: `Ellipse[A, B, c]`
   - **Arguments**: Two foci points A and B, and a distance c (the sum of the distances from any point on the ellipse to the two foci) to create an ellipse.

38. **Hyperbola**
   - **Function**: `Hyperbola[A, B, c]`
   - **Arguments**: Two foci points A and B, and a distance c (the difference of the distances from any point on the hyperbola to the two foci) to create a hyperbola.

39. **Parabola**
   - **Function**: `Parabola[A, B]`
   - **Arguments**: A focus point A and a directrix line B to create a parabola that opens towards the focus.

40. **Conic through 5 Points**
   - **Function**: `Conic[A, B, C, D, E]`
   - **Arguments**: Five points A, B, C, D, and E to create a conic section that passes through all five points.
   
41. **Angle**
   - **Function**: `Angle[A, B, C]`
   - **Arguments**: Three points A, B, and C, where B is the vertex, to create the angle ∠ABC.

42. **Angle with Given Size**
   - **Function**: `Angle[A, B, size]`
   - **Arguments**: A point A (the vertex), a point B (on one side of the angle), and a size (the measure of the angle in degrees) to create an angle of the specified size.

43. **Distance or Length**
   - **Function**: `Distance[A, B]`
   - **Arguments**: Two points A and B to calculate the distance between them.

44. **Area**
   - **Function**: `Area[Object]`
   - **Arguments**: An object (such as a polygon or circle) to calculate its area.

45. **Slope**
   - **Function**: `Slope[Line]`
   - **Arguments**: A line to calculate its slope.

46. **List**
   - **Function**: `List[{A, B, C, ...}]`
   - **Arguments**: A list of objects (points, segments, etc.) to create a list containing these elements.  
   

47. **Dilate from Point Tool**
   - **Function**: `Dilate[A, k]`
   - **Arguments**: A point A (the center of dilation) and a scale factor k to dilate an object from the point A by the factor k.

48. **Reflect about Circle Tool**
   - **Function**: `Reflect[Object, Circle]`
   - **Arguments**: An object (such as a point, line, or shape) and a circle to reflect the object across the given circle.

49. **Reflect about Line Tool**
   - **Function**: `Reflect[Object, Line]`
   - **Arguments**: An object (such as a point, line, or shape) and a line to reflect the object across the given line.

50. **Reflect about Point Tool**
   - **Function**: `Reflect[Object, Point]`
   - **Arguments**: An object (such as a point, line, or shape) and a point to reflect the object across the given point.

51. **Rotate around Point Tool**
   - **Function**: `Rotate[Object, angle, Point]`
   - **Arguments**: An object to rotate, an angle (in degrees), and a point around which to rotate the object.

52. **Translate by Vector Tool**
   - **Function**: `Translate[Object, Vector]`
   - **Arguments**: An object to translate and a vector that defines the direction and distance of the translation. 
   
53. **Graphing Tool**
   - **Function**: `Graph[f(x)]`
   - **Arguments**: A function f(x) to plot its graph in the Cartesian coordinate system.

54. **Parametric Curve Tool**
   - **Function**: `Curve[f(t), g(t), t, a, b]`
   - **Arguments**: Two functions f(t) and g(t) for the x and y coordinates, and the interval [a, b] for the parameter t to plot a parametric curve.

55. **Polar Curve Tool**
   - **Function**: `Curve[r(θ), θ, a, b]`
   - **Arguments**: A function r(θ) for the radius in polar coordinates and the interval [a, b] for the angle θ to plot a polar curve.

56. **Inequality Tool**
   - **Function**: `Inequality[f(x) < g(x)]`
   - **Arguments**: Two functions f(x) and g(x) to graph the region where the inequality holds.

57. **Implicit Curve Tool**
   - **Function**: `ImplicitCurve[f(x, y) = 0]`
   - **Arguments**: An equation f(x, y) = 0 to graph an implicit curve in the coordinate plane.

58. **Function Inspector Tool**
   - **Function**: `f(x) = expression`
   - **Arguments**: An expression to define a function, which can then be analyzed and graphed using the Function Inspector.

59. **Tangent Line Tool**
   - **Function**: `Tangent[f(x), a]`
   - **Arguments**: A function f(x) and a point a to create the tangent line to the graph of the function at that point.

60. **Intersection Tool**
   - **Function**: `Intersection[Object1, Object2]`
   - **Arguments**: Two objects (such as curves or lines) to find and plot their intersection points.
   
   
"""