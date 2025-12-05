from manim import *

def intersection_circles(circle_1: Circle, circle_2: Circle) -> tuple[np.ndarray, np.ndarray]:
    o1 = circle_1.get_center()
    o2 = circle_2.get_center()
    r1 = circle_1.radius
    r2 = circle_2.radius
    l = Line(o1, o2).get_length()

    if l > r1 + r2 + 0.02:
        raise Exception('Circles do not intersect')

    x1 = Dot(Line(o1, o2).set_length_about_point(o1, r1).get_end())
    x2 = x1.copy()

    alpha = np.arccos(round((r2 ** 2 - r1 ** 2 - l ** 2) / (-2 * r1 * l), 4))
    x1.rotate(about_point=o1, angle=alpha)
    x2.rotate(about_point=o1, angle=-alpha)

    return x1.get_center(), x2.get_center()


def intersection_line_and_circle(line: Line, circle: Circle) -> tuple[np.ndarray, np.ndarray]:
    o, r = circle.get_center(), circle.radius
    h = Line(line.get_projection(o), o).get_length()
    alpha = np.arccos(round(h / r, 4))
    x1 = Dot(Line(o, line.get_projection(o)).set_length_about_point(o, r).get_end())
    x2 = x1.copy()
    x1.rotate(about_point=o, angle=alpha)
    x2.rotate(about_point=o, angle=-alpha)
    return x1.get_center(), x2.get_center()