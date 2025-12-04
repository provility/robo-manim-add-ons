"""
Expression utilities for extracting coordinates from various object types.

Provides functions for extracting x and y coordinates from Manim objects,
numpy arrays, or lists.
"""

import numpy as np
from typing import Union
from manim import Line, Arrow, Dot


def x(obj: Union[object, np.ndarray, list]) -> float:
    """
    Extract the x-coordinate from various object types.

    Args:
        obj: Can be:
            - A Manim object with get_center() method (e.g., Dot, VMobject)
            - A NumPy array [x, y] or [x, y, z]
            - A Python list [x, y] or [x, y, z]

    Returns:
        The x-coordinate (first element) as a float

    Raises:
        TypeError: If the object type is not supported
        IndexError: If the array/list is empty

    Example:
        >>> from manim import Dot, ORIGIN
        >>> from robo_manim_add_ons import x
        >>>
        >>> dot = Dot(ORIGIN)
        >>> x_val = x(dot)  # Returns 0.0
        >>>
        >>> arr = np.array([1.5, 2.0, 0.0])
        >>> x_val = x(arr)  # Returns 1.5
        >>>
        >>> lst = [3.0, 4.0]
        >>> x_val = x(lst)  # Returns 3.0
    """
    # Check if object has get_center method (Manim object like Dot, VMobject, etc.)
    if hasattr(obj, 'get_center'):
        return obj.get_center()[0]
    # Check if it's a numpy array
    elif isinstance(obj, np.ndarray):
        return float(obj[0])
    # Check if it's a list
    elif isinstance(obj, (list, tuple)):
        return float(obj[0])
    else:
        raise TypeError(
            f"Unsupported type {type(obj).__name__}. "
            "Expected object with get_center(), numpy array, or list."
        )


def y(obj: Union[object, np.ndarray, list]) -> float:
    """
    Extract the y-coordinate from various object types.

    Args:
        obj: Can be:
            - A Manim object with get_center() method (e.g., Dot, VMobject)
            - A NumPy array [x, y] or [x, y, z]
            - A Python list [x, y] or [x, y, z]

    Returns:
        The y-coordinate (second element) as a float

    Raises:
        TypeError: If the object type is not supported
        IndexError: If the array/list has less than 2 elements

    Example:
        >>> from manim import Dot, UP
        >>> from robo_manim_add_ons import y
        >>>
        >>> dot = Dot(UP)
        >>> y_val = y(dot)  # Returns 1.0
        >>>
        >>> arr = np.array([1.5, 2.5, 0.0])
        >>> y_val = y(arr)  # Returns 2.5
        >>>
        >>> lst = [3.0, 4.0]
        >>> y_val = y(lst)  # Returns 4.0
    """
    # Check if object has get_center method (Manim object like Dot, VMobject, etc.)
    if hasattr(obj, 'get_center'):
        return obj.get_center()[1]
    # Check if it's a numpy array
    elif isinstance(obj, np.ndarray):
        return float(obj[1])
    # Check if it's a list
    elif isinstance(obj, (list, tuple)):
        return float(obj[1])
    else:
        raise TypeError(
            f"Unsupported type {type(obj).__name__}. "
            "Expected object with get_center(), numpy array, or list."
        )


def st(obj: Union[object, np.ndarray, list]) -> np.ndarray:
    """
    Get the start point from various object types.

    Args:
        obj: Can be:
            - A Manim object with get_start() method (e.g., Line, Arc, etc.)
            - A NumPy array [x, y] or [x, y, z] (returned as-is)
            - A Python list [x, y] or [x, y, z] (converted to numpy array)

    Returns:
        The start point as a numpy array [x, y, z]

    Raises:
        TypeError: If the object type is not supported

    Example:
        >>> from manim import Line, LEFT, RIGHT
        >>> from robo_manim_add_ons import st
        >>>
        >>> line = Line(LEFT, RIGHT)
        >>> start = st(line)  # Returns np.array([-1., 0., 0.])
        >>>
        >>> arr = np.array([1.5, 2.0, 0.0])
        >>> start = st(arr)  # Returns np.array([1.5, 2.0, 0.0])
        >>>
        >>> lst = [3.0, 4.0, 0.0]
        >>> start = st(lst)  # Returns np.array([3.0, 4.0, 0.0])
    """
    # Check if object has get_start method (Manim object like Line, Arc, etc.)
    if hasattr(obj, 'get_start'):
        return obj.get_start()
    # Check if it's a numpy array
    elif isinstance(obj, np.ndarray):
        return obj
    # Check if it's a list
    elif isinstance(obj, (list, tuple)):
        return np.array(obj)
    else:
        raise TypeError(
            f"Unsupported type {type(obj).__name__}. "
            "Expected object with get_start(), numpy array, or list."
        )


def ed(obj: Union[object, np.ndarray, list]) -> np.ndarray:
    """
    Get the end point from various object types.

    Args:
        obj: Can be:
            - A Manim object with get_end() method (e.g., Line, Arc, etc.)
            - A NumPy array [x, y] or [x, y, z] (returned as-is)
            - A Python list [x, y] or [x, y, z] (converted to numpy array)

    Returns:
        The end point as a numpy array [x, y, z]

    Raises:
        TypeError: If the object type is not supported

    Example:
        >>> from manim import Line, LEFT, RIGHT
        >>> from robo_manim_add_ons import ed
        >>>
        >>> line = Line(LEFT, RIGHT)
        >>> end = ed(line)  # Returns np.array([1., 0., 0.])
        >>>
        >>> arr = np.array([1.5, 2.0, 0.0])
        >>> end = ed(arr)  # Returns np.array([1.5, 2.0, 0.0])
        >>>
        >>> lst = [3.0, 4.0, 0.0]
        >>> end = ed(lst)  # Returns np.array([3.0, 4.0, 0.0])
    """
    # Check if object has get_end method (Manim object like Line, Arc, etc.)
    if hasattr(obj, 'get_end'):
        return obj.get_end()
    # Check if it's a numpy array
    elif isinstance(obj, np.ndarray):
        return obj
    # Check if it's a list
    elif isinstance(obj, (list, tuple)):
        return np.array(obj)
    else:
        raise TypeError(
            f"Unsupported type {type(obj).__name__}. "
            "Expected object with get_end(), numpy array, or list."
        )


def mid(obj) -> Dot:
    """
    Get a Dot at the center of an object.

    Args:
        obj: A Manim object with get_center() method (e.g., Line, Circle, VMobject, etc.)

    Returns:
        A Dot at the center of the object

    Raises:
        TypeError: If the object doesn't have get_center() method

    Example:
        >>> from manim import Line, Circle, LEFT, RIGHT
        >>> from robo_manim_add_ons import mid
        >>>
        >>> line = Line(LEFT, RIGHT)
        >>> dot = mid(line)  # Dot at center of line
        >>>
        >>> circle = Circle(radius=2)
        >>> dot = mid(circle)  # Dot at center of circle
    """
    if hasattr(obj, 'get_center'):
        return Dot(obj.get_center())
    else:
        raise TypeError(
            f"Unsupported type {type(obj).__name__}. "
            "Expected object with get_center() method."
        )


def mag(obj: Union[object, np.ndarray, list]) -> float:
    """
    Get the magnitude/length from various object types.

    Args:
        obj: Can be:
            - A Manim object with get_length() method (e.g., Line, Arc, etc.)
            - A NumPy array (calculates magnitude using np.linalg.norm)
            - A Python list (calculates magnitude after converting to array)

    Returns:
        The magnitude/length as a float

    Raises:
        TypeError: If the object type is not supported

    Example:
        >>> from manim import Line, LEFT, RIGHT
        >>> from robo_manim_add_ons import mag
        >>>
        >>> line = Line(LEFT, RIGHT)
        >>> length = mag(line)  # Returns 2.0
        >>>
        >>> arr = np.array([3.0, 4.0, 0.0])
        >>> magnitude = mag(arr)  # Returns 5.0
        >>>
        >>> lst = [1.0, 0.0, 0.0]
        >>> magnitude = mag(lst)  # Returns 1.0
    """
    # Check if object has get_length method (Manim object like Line, Arc, etc.)
    if hasattr(obj, 'get_length'):
        return obj.get_length()
    # Check if it's a numpy array
    elif isinstance(obj, np.ndarray):
        return float(np.linalg.norm(obj))
    # Check if it's a list
    elif isinstance(obj, (list, tuple)):
        return float(np.linalg.norm(np.array(obj)))
    else:
        raise TypeError(
            f"Unsupported type {type(obj).__name__}. "
            "Expected object with get_length(), numpy array, or list."
        )


def uv(obj: Union[object, np.ndarray, list]) -> np.ndarray:
    """
    Get the unit vector from various object types.

    Args:
        obj: Can be:
            - A Manim object with get_unit_vector() method (e.g., Line, Vector, etc.)
            - A NumPy array (normalizes the vector)
            - A Python list (converts to array and normalizes)

    Returns:
        The unit vector as a numpy array

    Raises:
        TypeError: If the object type is not supported
        ValueError: If the vector has zero magnitude

    Example:
        >>> from manim import Line, LEFT, RIGHT
        >>> from robo_manim_add_ons import uv
        >>>
        >>> line = Line(LEFT, RIGHT)
        >>> unit = uv(line)  # Returns np.array([1., 0., 0.])
        >>>
        >>> arr = np.array([3.0, 4.0, 0.0])
        >>> unit = uv(arr)  # Returns np.array([0.6, 0.8, 0.])
        >>>
        >>> lst = [0.0, 5.0, 0.0]
        >>> unit = uv(lst)  # Returns np.array([0., 1., 0.])
    """
    # Check if object has get_unit_vector method (Manim object like Line, Vector, etc.)
    if hasattr(obj, 'get_unit_vector'):
        return obj.get_unit_vector()
    # Check if it's a numpy array
    elif isinstance(obj, np.ndarray):
        magnitude = np.linalg.norm(obj)
        if magnitude == 0:
            raise ValueError("Cannot compute unit vector of zero-magnitude vector")
        return obj / magnitude
    # Check if it's a list
    elif isinstance(obj, (list, tuple)):
        arr = np.array(obj)
        magnitude = np.linalg.norm(arr)
        if magnitude == 0:
            raise ValueError("Cannot compute unit vector of zero-magnitude vector")
        return arr / magnitude
    else:
        raise TypeError(
            f"Unsupported type {type(obj).__name__}. "
            "Expected object with get_unit_vector(), numpy array, or list."
        )


def vec(obj: Union[object, np.ndarray, list]) -> np.ndarray:
    """
    Get the vector from various object types.

    Args:
        obj: Can be:
            - A Manim object with get_vector() method (e.g., Line - returns end - start)
            - A NumPy array (returned as-is)
            - A Python list (converted to numpy array)

    Returns:
        The vector as a numpy array

    Raises:
        TypeError: If the object type is not supported

    Example:
        >>> from manim import Line, LEFT, RIGHT
        >>> from robo_manim_add_ons import vec
        >>>
        >>> line = Line(LEFT, RIGHT)
        >>> vector = vec(line)  # Returns np.array([2., 0., 0.])
        >>>
        >>> arr = np.array([1.5, 2.0, 0.0])
        >>> vector = vec(arr)  # Returns np.array([1.5, 2.0, 0.0])
        >>>
        >>> lst = [3.0, 4.0, 0.0]
        >>> vector = vec(lst)  # Returns np.array([3.0, 4.0, 0.0])
    """
    # Check if object has get_vector method (Manim object like Line, etc.)
    if hasattr(obj, 'get_vector'):
        return obj.get_vector()
    # Check if it's a numpy array
    elif isinstance(obj, np.ndarray):
        return obj
    # Check if it's a list
    elif isinstance(obj, (list, tuple)):
        return np.array(obj)
    else:
        raise TypeError(
            f"Unsupported type {type(obj).__name__}. "
            "Expected object with get_vector(), numpy array, or list."
        )


def ang(obj: Union[object, np.ndarray, list]) -> float:
    """
    Get the angle from various object types.

    Args:
        obj: Can be:
            - A Manim object with get_angle() method (e.g., Line)
            - A NumPy array (calculates angle using np.arctan2(y, x))
            - A Python list (calculates angle after converting to array)

    Returns:
        The angle in radians as a float

    Raises:
        TypeError: If the object type is not supported

    Example:
        >>> from manim import Line, LEFT, RIGHT, UP
        >>> from robo_manim_add_ons import ang
        >>>
        >>> line = Line(LEFT, RIGHT)
        >>> angle = ang(line)  # Returns 0.0 (horizontal line)
        >>>
        >>> arr = np.array([1.0, 1.0, 0.0])
        >>> angle = ang(arr)  # Returns π/4 (45 degrees)
        >>>
        >>> lst = [0.0, 1.0, 0.0]
        >>> angle = ang(lst)  # Returns π/2 (90 degrees)
    """
    # Check if object has get_angle method (Manim object like Line, etc.)
    if hasattr(obj, 'get_angle'):
        return obj.get_angle()
    # Check if it's a numpy array
    elif isinstance(obj, np.ndarray):
        return float(np.arctan2(obj[1], obj[0]))
    # Check if it's a list
    elif isinstance(obj, (list, tuple)):
        arr = np.array(obj)
        return float(np.arctan2(arr[1], arr[0]))
    else:
        raise TypeError(
            f"Unsupported type {type(obj).__name__}. "
            "Expected object with get_angle(), numpy array, or list."
        )


def slope(obj: Union[object, np.ndarray, list]) -> float:
    """
    Get the slope from various object types.

    Args:
        obj: Can be:
            - A Manim object with get_slope() method (e.g., Line)
            - A NumPy array (calculates slope as y/x)
            - A Python list (calculates slope after converting to array)

    Returns:
        The slope as a float

    Raises:
        TypeError: If the object type is not supported
        ValueError: If x-component is zero (vertical line)

    Example:
        >>> from manim import Line, ORIGIN, UP + RIGHT
        >>> from robo_manim_add_ons import slope
        >>>
        >>> line = Line(ORIGIN, UP + RIGHT)
        >>> slp = slope(line)  # Returns 1.0 (45 degree line)
        >>>
        >>> arr = np.array([2.0, 4.0, 0.0])
        >>> slp = slope(arr)  # Returns 2.0
        >>>
        >>> lst = [1.0, 3.0, 0.0]
        >>> slp = slope(lst)  # Returns 3.0
    """
    # Check if object has get_slope method (Manim object like Line, etc.)
    if hasattr(obj, 'get_slope'):
        return obj.get_slope()
    # Check if it's a numpy array
    elif isinstance(obj, np.ndarray):
        if obj[0] == 0:
            return float('inf') if obj[1] > 0 else float('-inf')
        return float(obj[1] / obj[0])
    # Check if it's a list
    elif isinstance(obj, (list, tuple)):
        arr = np.array(obj)
        if arr[0] == 0:
            return float('inf') if arr[1] > 0 else float('-inf')
        return float(arr[1] / arr[0])
    else:
        raise TypeError(
            f"Unsupported type {type(obj).__name__}. "
            "Expected object with get_slope(), numpy array, or list."
        )


def val(obj: Union[object, float, int]) -> float:
    """
    Get the value from various object types.

    Args:
        obj: Can be:
            - A Manim object with get_value() method (e.g., ValueTracker, Variable)
            - A numeric value (int or float, returned as-is)

    Returns:
        The value as a float

    Raises:
        TypeError: If the object type is not supported

    Example:
        >>> from manim import ValueTracker
        >>> from robo_manim_add_ons import val
        >>>
        >>> tracker = ValueTracker(5.0)
        >>> value = val(tracker)  # Returns 5.0
        >>>
        >>> num = 3.14
        >>> value = val(num)  # Returns 3.14
        >>>
        >>> integer = 42
        >>> value = val(integer)  # Returns 42.0
    """
    # Check if object has get_value method (Manim object like ValueTracker, Variable, etc.)
    if hasattr(obj, 'get_value'):
        return obj.get_value()
    # Check if it's already a numeric value
    elif isinstance(obj, (int, float)):
        return float(obj)
    else:
        raise TypeError(
            f"Unsupported type {type(obj).__name__}. "
            "Expected object with get_value() or numeric value."
        )


def pt(x: float, y: float, z: float = 0) -> np.ndarray:
    """
    Create a point as a numpy array from x, y, and optional z coordinates.

    Args:
        x: The x-coordinate
        y: The y-coordinate
        z: The z-coordinate (default: 0)

    Returns:
        A numpy array [x, y, z]

    Example:
        >>> from robo_manim_add_ons import pt
        >>>
        >>> point = pt(1, 2)  # Returns np.array([1, 2, 0])
        >>>
        >>> point = pt(3.5, 4.5)  # Returns np.array([3.5, 4.5, 0])
        >>>
        >>> point = pt(1, 2, 3)  # Returns np.array([1, 2, 3])
    """
    return np.array([x, y, z])


def m2v(axes, x: float, y: float) -> Dot:
    """
    Convert model coordinates to view coordinates and return as a Dot.

    Args:
        axes: The Axes object with c2p method
        x: The x-coordinate in model space
        y: The y-coordinate in model space

    Returns:
        A Dot at the screen point corresponding to the model coordinates

    Example:
        >>> from manim import Axes
        >>> from robo_manim_add_ons import m2v
        >>>
        >>> axes = Axes(x_range=[-5, 5], y_range=[-5, 5])
        >>> dot = m2v(axes, 2, 3)  # Dot at screen coordinates for (2, 3) in model space
    """
    return Dot(axes.c2p(x, y))


def v2m(axes, x: float, y: float) -> Dot:
    """
    Convert view coordinates (screen point) to model coordinates and return as a Dot.

    Args:
        axes: The Axes object with p2c method
        x: The x-coordinate in screen space
        y: The y-coordinate in screen space

    Returns:
        A Dot at the model coordinates corresponding to the screen point

    Example:
        >>> from manim import Axes
        >>> from robo_manim_add_ons import v2m
        >>>
        >>> axes = Axes(x_range=[-5, 5], y_range=[-5, 5])
        >>> dot = v2m(axes, 1.5, 2.0)  # Dot at model coordinates for screen point (1.5, 2.0)
    """
    return Dot(axes.p2c(pt(x, y)))


def x2v(axes, graph, x: float) -> Dot:
    """
    Get a Dot on a graph at a given x-value.

    This is a wrapper for axes.i2gp(x, graph) that returns a Dot.

    Args:
        axes: The Axes object with i2gp method
        graph: The ParametricFunction (graph) object
        x: The x-value on the graph

    Returns:
        A Dot at the point on the graph corresponding to the x-value

    Example:
        >>> from manim import Axes
        >>> from robo_manim_add_ons import x2v
        >>>
        >>> axes = Axes(x_range=[-5, 5], y_range=[-5, 5])
        >>> parabola = axes.plot(lambda x: x**2)
        >>> dot = x2v(axes, parabola, 2)  # Dot on parabola at x=2
    """
    return Dot(axes.i2gp(x, graph))


def vl(x: float, y1: float = -20, y2: float = 20) -> Line:
    """
    Create a vertical line at x-coordinate from y1 to y2.

    Args:
        x: The x-coordinate of the vertical line
        y1: The starting y-coordinate (default: -20)
        y2: The ending y-coordinate (default: 20)

    Returns:
        A Line object representing the vertical line

    Example:
        >>> from robo_manim_add_ons import vl
        >>>
        >>> line = vl(2)         # Vertical line at x=2 from y=-20 to y=20
        >>> line = vl(2, -3, 3)  # Vertical line at x=2 from y=-3 to y=3
        >>> line = vl(0, 0, 5)   # Vertical line at x=0 from y=0 to y=5
    """
    return Line(pt(x, y1), pt(x, y2))


def hl(y: float, x1: float = -20, x2: float = 20) -> Line:
    """
    Create a horizontal line at y-coordinate from x1 to x2.

    Args:
        y: The y-coordinate of the horizontal line
        x1: The starting x-coordinate (default: -20)
        x2: The ending x-coordinate (default: 20)

    Returns:
        A Line object representing the horizontal line

    Example:
        >>> from robo_manim_add_ons import hl
        >>>
        >>> line = hl(3)         # Horizontal line at y=3 from x=-20 to x=20
        >>> line = hl(3, -2, 2)  # Horizontal line at y=3 from x=-2 to x=2
        >>> line = hl(0, 0, 5)   # Horizontal line at y=0 from x=0 to x=5
    """
    return Line(pt(x1, y), pt(x2, y))


def lra(radius: float, angle: float, from_x: float = 0, from_y: float = 0) -> Line:
    """
    Create a line using polar coordinates (radius and angle).

    Args:
        radius: The radius (distance from starting point)
        angle: The angle in degrees
        from_x: The x-coordinate of the starting point (default: 0)
        from_y: The y-coordinate of the starting point (default: 0)

    Returns:
        A Line object from (from_x, from_y) to the point at radius and angle

    Example:
        >>> from robo_manim_add_ons import lra
        >>>
        >>> line = lra(2, 45)        # Line from origin, radius 2 at 45 degrees
        >>> line = lra(3, 90, 1, 1)  # Line from (1,1), radius 3 at 90 degrees
        >>> line = lra(1, 0, 2, 0)   # Line from (2,0), radius 1 at 0 degrees
    """
    angle_rad = np.radians(angle)
    dx = radius * np.cos(angle_rad)
    dy = radius * np.sin(angle_rad)
    return Line(pt(from_x, from_y), pt(from_x + dx, from_y + dy))


def vra(radius: float, angle: float, from_x: float = 0, from_y: float = 0) -> Arrow:
    """
    Create an arrow using polar coordinates (radius and angle).

    Args:
        radius: The radius (distance from starting point)
        angle: The angle in degrees
        from_x: The x-coordinate of the starting point (default: 0)
        from_y: The y-coordinate of the starting point (default: 0)

    Returns:
        An Arrow object from (from_x, from_y) to the point at radius and angle

    Example:
        >>> from robo_manim_add_ons import vra
        >>>
        >>> arrow = vra(2, 45)        # Arrow from origin, radius 2 at 45 degrees
        >>> arrow = vra(1, 90, 1, 1)  # Arrow from (1,1), radius 1 at 90 degrees
        >>> arrow = vra(3, 0, 2, 0)   # Arrow from (2,0), radius 3 at 0 degrees
    """
    angle_rad = np.radians(angle)
    dx = radius * np.cos(angle_rad)
    dy = radius * np.sin(angle_rad)
    start_point = np.array([from_x, from_y, 0])
    end_point = np.array([from_x + dx, from_y + dy, 0])
    return Arrow(start=start_point, end=end_point)


def r2p(obj, proportion: float) -> Dot:
    """
    Get a point at a proportion along an object and return it as a Dot.

    Args:
        obj: A Manim object with point_from_proportion method (e.g., Line, Arc, VMobject)
        proportion: The proportion along the object (0 = start, 1 = end)

    Returns:
        A Dot at the point corresponding to the given proportion

    Example:
        >>> from manim import Line, LEFT, RIGHT
        >>> from robo_manim_add_ons import r2p
        >>>
        >>> line = Line(LEFT, RIGHT)
        >>> dot = r2p(line, 0.5)   # Dot at midpoint of line
        >>> dot = r2p(line, 0.25)  # Dot at 25% along the line
        >>> dot = r2p(line, 1)     # Dot at end of line
    """
    point = obj.point_from_proportion(proportion)
    return Dot(point)


class Exp:
    """
    Expression utility class for extracting coordinates and properties from various types.

    This class provides the same functionality as the standalone x, y, st, ed, mid, mag, uv, vec, ang, slope, val, pt, m2v, v2m, x2v, vl, hl, lra, vra, and r2p functions,
    but in a class-based interface for those who prefer it.
    """
    x = staticmethod(x)
    y = staticmethod(y)
    st = staticmethod(st)
    ed = staticmethod(ed)
    mid = staticmethod(mid)
    mag = staticmethod(mag)
    uv = staticmethod(uv)
    vec = staticmethod(vec)
    ang = staticmethod(ang)
    slope = staticmethod(slope)
    val = staticmethod(val)
    pt = staticmethod(pt)
    m2v = staticmethod(m2v)
    v2m = staticmethod(v2m)
    x2v = staticmethod(x2v)
    vl = staticmethod(vl)
    hl = staticmethod(hl)
    lra = staticmethod(lra)
    vra = staticmethod(vra)
    r2p = staticmethod(r2p)
