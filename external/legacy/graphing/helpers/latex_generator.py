from cmath import isclose
from fractions import Fraction
from sympy import latex, pi, Rational, simplify
from graphing.helpers.latex_symbols import LatexSymbols



class LatexGenerator:
    
    def __init__(self):
        self.matrix_environments = {
            'pmatrix': ('pmatrix', ''),  # parentheses
            'bmatrix': ('bmatrix', ''),  # square brackets
            'Bmatrix': ('Bmatrix', ''),  # curly braces
            'vmatrix': ('vmatrix', ''),  # single vertical lines
            'Vmatrix': ('Vmatrix', ''),  # double vertical lines
            'matrix': ('matrix', '')      # no delimiters
        }
    
    def text(self, text):
        return f"\\text{{{text}}}"
    
    def complex_number(self, real_part, imaginary_part, variable=None):
        if variable is None:
            return f"{real_part} + {imaginary_part}i"
        else:
            return f"{variable} = {real_part} + {imaginary_part}i"  

    def power(self, base, exponent):
        return f"{base}^{{{exponent}}}" 
    
    def fraction(self, numerator, denominator):
        return f"{LatexSymbols.FRACTION}{{{numerator}}}{{{denominator}}}"

    def square_root(self, value):
        return f"{LatexSymbols.SQUARE_ROOT}{{{value}}}"

    def absolute_value(self, value):
        opening, closing = LatexSymbols.ABSOLUTE_VALUE
        return f"{opening}{value}{closing}"

    # Logic Symbols
    def for_all(self, expr):
        return f"{LatexSymbols.FOR_ALL} {expr}"

    def exists(self, expr):
        return f"{LatexSymbols.EXISTS} {expr}"

    def not_symbol(self, expr):
        return f"{LatexSymbols.NOT} {expr}"

    def therefore(self):
        return LatexSymbols.THEREFORE

    def because(self):
        return LatexSymbols.BECAUSE
    
    def overline(self, expr):
        return f"{LatexSymbols.OVERLINE}{{{expr}}}"
    
    def underbrace(self, expr):
        return f"{LatexSymbols.UNDERBRACE}{{{expr}}}"
    
    def overbrace(self, expr):
        return f"{LatexSymbols.OVERBRACE}{{{expr}}}"    
    
    def triangle(self, expr):
        return f"{LatexSymbols.TRIANGLE}{{{expr}}}"
    
    def quad(self, expr):
        return f"{LatexSymbols.QUAD}{{{expr}}}"
    
    def cube_root(self, expr):
        return f"{LatexSymbols.CUBE_ROOT}{{{expr}}}"
    
    def nth_root(self, expr, n):
        return f"{LatexSymbols.NTH_ROOT}{{{n}}}{{{expr}}}"  
    
    def real_part(self, expr):
        return f"{LatexSymbols.REAL_PART}{{{expr}}}"
    
    def imaginary_part(self, expr):
        return f"{LatexSymbols.IMAGINARY_PART}{{{expr}}}"
    
    def complex_conjugate(self, expr):
        return f"{LatexSymbols.COMPLEX_CONJUGATE}{{{expr}}}"
    
    def eulers_constant(self, expr):
        return f"{LatexSymbols.EULERS_CONSTANT}{{{expr}}}"
    
    def rectangular_form(self, real_part, imaginary_part):
        return f"{real_part} + {imaginary_part}{LatexSymbols.IMAGINARY_UNIT}"
    
    def polar_form(self, magnitude, angle):
        return f"{magnitude}\\left({angle}\\right)"
    
    def euler_form(self, magnitude, angle="\\theta"):
        """Returns expression in Euler form: re^(iθ)
        Example: euler_form("r", "\\theta") -> "re^{i\\theta}" """
        return f"{magnitude}{LatexSymbols.EULERS_CONSTANT}^{{i{angle}}}"
    
    def euler_expanded_form(self, magnitude, angle = "\\theta"):
        """Returns expanded Euler form: r(cos θ + i sin θ)
        Example: euler_expanded_form("r", "\\theta") -> "r(\\cos\\theta + i\\sin\\theta)" """
        return f"{magnitude}\\left({LatexSymbols.COS}{angle} + i{LatexSymbols.SIN}{angle}\\right)"
  
    """
    Allowed types: "quad", "qquad", "small", "medium", "large"
    """
    def space(self, type="quad"):
        """Add space of specified type."""
        spaces = {
            "quad": "\\quad",
            "qquad": "\\qquad",
            "small": "\\,",
            "medium": "\\:",
            "large": "\\;"
        }
        return spaces.get(type, "\\quad")

    def new_line(self):
        """Add new line."""
        return "\\\\"

    def wrap_parentheses(self, *values, join_with=" "):
        """
        Wraps multiple expressions in parentheses.
        Example: wrap_parentheses("x", "+", "y") -> "\\left(x + y\\right)"
        """
        expression = join_with.join(values)  # Concatenate all values with a space
        return f"\\left({expression}\\right)"

    def wrap_square_brackets(self, *values, join_with=" "):
        """
        Wraps multiple expressions in square brackets.
        Example: wrap_square_brackets("x", "+", "y") -> "\\left[x + y\\right]"
        """
        expression = join_with.join(values)  # Concatenate all values with a space
        return f"\\left[{expression}\\right]"

    def wrap_curly_braces(self, *values, join_with=" "):
        """
        Wraps multiple expressions in curly braces.
        Example: wrap_curly_braces("x", "+", "y") -> "\\{x + y\\}"
        """
        expression = join_with.join(values)  # Concatenate all values with a space
        opening, closing = LatexSymbols.CURLY_BRACES
        return f"{opening}{expression}{closing}"

    # Additional Mathematical Notation
    def angle(self, expr):
        """Returns angle symbol followed by the expression.
        Example: angle("ABC") -> "\\angle ABC" """
        return f"{LatexSymbols.ANGLE} {expr}"

    def parallel(self, lhs, rhs):
        """Returns two expressions separated by parallel symbol.
        Example: parallel("l", "m") -> "l \\parallel m" """
        return f"{lhs} {LatexSymbols.PARALLEL} {rhs}"

    def perpendicular(self, lhs, rhs):
        """Returns two expressions separated by perpendicular symbol.
        Example: perpendicular("l", "m") -> "l \\perp m" """
        return f"{lhs} {LatexSymbols.PERPENDICULAR} {rhs}"

    @staticmethod
    def radian_to_pi_notation(theta_in_radians):
        """
        Converts a radian value to a LaTeX-compatible string representing it in terms of multiples of π,
        ensuring proper fractions or integers are produced, and omits "1π" for simplicity.
        """
        # Tolerance for floating-point comparisons
        tolerance = 1e-10

        # Handle the edge case for 0
        if isclose(theta_in_radians, 0, abs_tol=tolerance):
            return "0"

        # Convert radians to a multiplier of π
        multiplier = theta_in_radians / pi

        # Define the closest denominator to approximate the fraction
        closest_denominator = 12  # You can change this to increase or decrease precision
        numerator = round(multiplier * closest_denominator)
        denominator = closest_denominator

        # Simplify the fraction using the greatest common divisor
        gcd = LatexGenerator.greatest_common_divisor(abs(numerator), denominator)
        numerator //= gcd
        denominator //= gcd

        # Handle cases for fractions and integers
        sign = "-" if numerator < 0 else ""
        numerator = abs(numerator)

        # Case 1: Integer multiple of π
        if denominator == 1:
            if numerator == 1:
                return f"{sign}\\pi"  # Omit "1π"
            else:
                return f"{sign}{numerator}\\pi"

        # Case 2: Fractional multiple of π
        if numerator == 1:
            return f"{sign}\\frac{{\\pi}}{{{denominator}}}"  # Handle "1π" in fractions
        else:
            return f"{sign}\\frac{{{numerator}\\pi}}{{{denominator}}}"
    
    @staticmethod
    def greatest_common_divisor(a, b):
        """
        Returns the greatest common divisor of two numbers using Euclid's algorithm.
        """
        while b != 0:
            a, b = b, a % b
        return a         
    

    def length(self, point1, point2):
        """
        Generates LaTeX for length notation between two points.
        Example: length("A", "B") -> "\\overline{AB}"
        """
        return f"{LatexSymbols.OVERLINE}{{{point1}{point2}}}"

    def length_equals(self, point1, point2, value):
        """
        Generates LaTeX for length equality.
        Example: length_equals("A", "B", "5") -> "\\overline{AB} = 5"
        """
        length_notation = self.length(point1, point2)
        return self.equals(length_notation, value)

    def length_comparison(self, point1, point2, operator, value):
        """
        Generates LaTeX for length comparisons.
        Example: length_comparison("A", "B", "<", "5") -> "\\overline{AB} < 5"
        """
        length_notation = self.length(point1, point2)
        # Map comparison operators to their corresponding methods
        operators = {
            "<": LatexSymbols.LESS_THAN,
            ">": LatexSymbols.GREATER_THAN,
            "<=": LatexSymbols.LESS_THAN_OR_EQUAL_TO,
            ">=": LatexSymbols.GREATER_THAN_OR_EQUAL_TO,
            "=": LatexSymbols.EQUALS,
            "!=": LatexSymbols.NOT_EQUALS
        }
        return f"{length_notation} {operators[operator]} {value}"
    
 
        
    def subscript(self, expr, subscript):
        """Generate LaTeX for subscripts."""
        return f"{expr}_{{{subscript}}}"
    
    def superscript(self, expr, superscript):
        """Generate LaTeX for superscripts."""
        return f"{expr}^{{{superscript}}}"
        
    def derivative(self, expr, var="x", order=1):
        """Generate LaTeX for derivatives."""
        if order == 1:
            return f"\\frac{{d}}{{d{var}}}({expr})"
        return f"\\frac{{d^{order}}}{{d{var}^{order}}}({expr})"

    def mixed_partial(self, expr, vars=["x", "y"], orders=[1, 1]):
        """Generate LaTeX for mixed partial derivatives."""
        numerator = "\\partial^{" + str(sum(orders)) + "}"
        denominator = "".join([f"\\partial {var}^{{{order}}}" 
                             for var, order in zip(vars, orders)])
        return f"\\frac{{{numerator}}}{{{denominator}}}({expr})"

    def indefinite_integral(self, expr, var="x"):
        """Generate LaTeX for indefinite integral."""
        return f"\\int {expr}\\,d{var}"

    def definite_integral(self, expr, var="x", lower="a", upper="b"):
        """Generate LaTeX for definite integral."""
        return f"\\int_{{{lower}}}^{{{upper}}} {expr}\\,d{var}"

    def double_integral(self, expr, vars=["x", "y"], bounds=None):
        """Generate LaTeX for double integral."""
        if bounds:
            (x_lower, x_upper), (y_lower, y_upper) = bounds
            return f"\\iint_{{{y_lower} \\leq y \\leq {y_upper}}}^{{{x_lower} \\leq x \\leq {x_upper}}} {expr}\\,d{vars[0]}\\,d{vars[1]}"
        return f"\\iint {expr}\\,d{vars[0]}\\,d{vars[1]}"

    def triple_integral(self, expr, vars=["x", "y", "z"], bounds=None):
        """Generate LaTeX for triple integral."""
        if bounds:
            return f"\\iiint_{{{bounds}}} {expr}\\,d{vars[0]}\\,d{vars[1]}\\,d{vars[2]}"
        return f"\\iiint {expr}\\,d{vars[0]}\\,d{vars[1]}\\,d{vars[2]}"

    def line_integral(self, expr, var="s", curve="C"):
        """Generate LaTeX for line integral."""
        return f"\\oint_{{{curve}}} {expr}\\,d{var}"

    def surface_integral(self, expr, vars=["S"], bounds=None):
        """Generate LaTeX for surface integral."""
        return f"\\oiint_{{{bounds if bounds else vars[0]}}} {expr}\\,dS"

    def limit(self, expr, var="x", approach="a", side=None):
        """Generate LaTeX for limit."""
        if side == "left":
            return f"\\lim_{{{var} \\to {approach}^-}} {expr}"
        elif side == "right":
            return f"\\lim_{{{var} \\to {approach}^+}} {expr}"
        return f"\\lim_{{{var} \\to {approach}}} {expr}"

    def sum(self, expr, index="i", start=0, end="\\infty"):
        """Generate LaTeX for summation."""
        return f"\\sum_{{{index}={start}}}^{{{end}}} {expr}"

    def product(self, expr, index="i", start=1, end="n"):
        """Generate LaTeX for product."""
        return f"\\prod_{{{index}={start}}}^{{{end}}} {expr}"   
    
    def equation(self, lhs, rhs, relation="="):
        """
        Generate LaTeX for a single equation.
        
        Args:
            lhs: Left-hand side expression
            rhs: Right-hand side expression
            relation: Relation symbol (=, <, >, ≤, ≥, etc.)
        """
        relations = {
            "=": "=",
            "<": "<",
            ">": ">",
            "<=": "\\leq",
            ">=": "\\geq",
            "!=": "\\neq"
        }
        rel = relations.get(relation, relation)
        return f"{lhs} {rel} {rhs}"

    def linear_equation(self, coefficients, variables, rhs):
        """
        Generate LaTeX for a linear equation.
        
        Args:
            coefficients: List of coefficients
            variables: List of variable names
            rhs: Right-hand side value
        """
        terms = []
        for coeff, var in zip(coefficients, variables):
            if coeff == 0:
                continue
            if coeff == 1:
                terms.append(var)
            elif coeff == -1:
                terms.append(f"-{var}")
            else:
                terms.append(f"{coeff}{var}")
                
        lhs = " + ".join(terms).replace("+ -", "- ")
        return self.equation(lhs, rhs)

    def system_of_equations(self, equations, system_type="cases"):
        """
        Generate LaTeX for a system of equations.
        
        Args:
            equations: List of equations
            system_type: Type of system display ("cases", "align", "gather")
        """
        if system_type == "cases":
            equations_str = " \\\\ ".join(equations)
            return f"\\begin{{cases}}\n{equations_str}\n\\end{{cases}}"
        elif system_type == "align":
            equations_str = " \\\\ ".join(f"{eq} &" for eq in equations)
            return f"\\begin{{align*}}\n{equations_str}\n\\end{{align*}}"
        else:  # gather
            equations_str = " \\\\ ".join(equations)
            return f"\\begin{{gather*}}\n{equations_str}\n\\end{{gather*}}"

    def partial_derivative_element(self, f, var):
        """Generate partial derivative element."""
        return f"\\frac{{\\partial {f}}}{{\\partial {var}}}"
    
   
    
    def gradient_vector(self, function, variables):
        """
        Generate gradient vector elements.
        
        Args:
            function: Function name
            variables: List of variable names
        Returns:
            List of partial derivatives
        """
        return [self.partial_derivative_element(function, var) 
                for var in variables]
      
    
    def increment(self, var="x", increment_type="delta"):
        """Generate LaTeX for incremented variable like x+Δx or x+h
        Args:
            var: The variable being incremented
            increment_type: Type of increment ('delta', 'h', etc.)
        Returns:
            LaTeX string representing the increment
        """
        if increment_type == "delta":
            return f"{var}+\\delta {var}"
        
        return f"{var}+{increment_type}"
    
    def decrement(self, var="x", decrement_type="delta"):
        """Generate x-Δx or x-h notation
        Examples: x-Δx, y-Δy, x-h"""
        if decrement_type == "delta":
            return f"{var}-\\delta {var}"
        return f"{var}-{decrement_type}"

    def difference(self, var="x", index1="i+1", index2="i"):
        """Generate difference notation like x_{i+1} - x_i
        Example: x_{i+1} - x_i"""
        return f"{var}_{{{index1}}} - {var}_{{{index2}}}"

    def evaluated_at(self, expr, upper, lower):
        """Generate evaluation notation like expr|_{lower}^{upper}
        Example: x^2|_{0}^{1}"""
        return f"{expr}\\big|_{{{lower}}}^{{{upper}}}"

    def infinitesimal(self, var="x"):
        """Generate dx or dy notation for infinitesimals
        Example: dx, dy"""
        return f"d{var}"

    def partial_infinitesimal(self, var="x"):
        """Generate ∂x or ∂y notation for partial derivatives
        Example: ∂x, ∂y"""
        return f"\\partial {var}"

    def sequence_element(self, var="x", index="n"):
        """Generate sequence notation like x_n
        Example: x_n, a_i"""
        return f"{var}_{{{index}}}"
    
    def vector(self, name):
        return f"\\vec{{{name}}}"   
    
    def unit_vector(self, var="x"):
        """Generate unit vector notation like \\hat{x}
        Example: \\hat{x}, \\hat{y}"""
        return f"\\hat{{{var}}}"
    

    def vector_component(self, var="v", index="i"):
        """Generate vector component notation like v_i
        Example: v_i, w_j"""
        return f"{var}_{{{index}}}"

    def evaluated_function(self, f="f", var="x", at="0"):
        """Generate function evaluation notation like f(x)|_{x=0}
        Example: f(x)|_{x=0}"""
        return f"{f}({var})\\big|_{{{var}={at}}}"

    def interval(self, start, end, left_open=False, right_open=False):
        """Generate interval notation like [a,b] or (a,b)
        Example: [0,1], (0,∞)"""
        left = "(" if left_open else "["
        right = ")" if right_open else "]"
        return f"{left}{start},{end}{right}"

    def function_with_condition(self, f="f", var="x", condition="x > 0"):
        """Generate function with condition like f(x), x > 0
        Example: f(x), x > 0"""
        return f"{f}({var}),\\; {condition}"
    
    def function(self, name="f", expression="x"):
        """Create a function with given expression
        Example: function("f", generator.increment("x")) -> "f(x+\\delta x)" """
        return f"{name}({expression})"

    def inner_product(self, x="x", y="y"):
        """Generate inner product notation like ⟨x,y⟩
        Example: ⟨x,y⟩"""
        return f"\\langle {x},{y}\\rangle"


    
    
    def mapsto(self, domain, codomain):
        """Generate function mapping notation"""
        return f"{domain} {LatexSymbols.MAPSTO} {codomain}"
    
    def function_space(self, domain, codomain, arrow_type="FUNCTION_ARROW"):
        """Generate function space notation with different arrow types"""
        arrow = getattr(LatexSymbols, arrow_type)
        return f"{domain} {arrow} {codomain}"
    
    def differential_operator(self, operator, function):
        """Generate differential operator notation"""
        return f"{operator}({function})"
    
    def closed_integral(self, expression, var="x"):
        """Generate closed line integral"""
        return f"{LatexSymbols.CLOSED_INTEGRAL} {expression} d{var}"
    
    def surface_integral(self, expression):
        """Generate surface integral"""
        return f"{LatexSymbols.SURFACE_INTEGRAL} {expression} dS"
    
    def volume_integral(self, expression):
        """Generate volume integral"""
        return f"{LatexSymbols.VOLUME_INTEGRAL} {expression} dV"
    
    def tensor_product(self, a, b):
        """Generate tensor product notation"""
        return f"{a} {LatexSymbols.TENSOR_PRODUCT} {b}"
    
    def direct_sum(self, a, b):
        """Generate direct sum notation"""
        return f"{a} {LatexSymbols.DIRECT_SUM} {b}"
    
    def composition(self, f, g):
        """Generate function composition notation"""
        return f"{f} {LatexSymbols.COMPOSITION} {g}"
    
    def set_builder(self, variable, condition):
        """Generate set builder notation"""
        return f"\\{{{variable} : {condition}\\}}"
    
    def partial_derivative(self, f, var, order=1):
        """Generate partial derivative notation"""
        if order == 1:
            return f"\\frac{{{LatexSymbols.PARTIAL_DIFFERENTIAL}}}{{{LatexSymbols.PARTIAL_DIFFERENTIAL}{var}}} {f}"
        return f"\\frac{{{LatexSymbols.PARTIAL_DIFFERENTIAL}^{order}}}{{{LatexSymbols.PARTIAL_DIFFERENTIAL}{var}^{order}}} {f}"
    
    def norm(self, expression, type=""):
        """Generate norm notation with optional type"""
        if type:
            return f"\\|{expression}\\|_{{{type}}}"
        return f"\\|{expression}\\|"
    
    def commutator(self, a, b):
        """Generate commutator bracket notation"""
        return f"[{a}, {b}]"
    
    def matrix_norm(self, matrix, type=""):
        """Generate matrix norm notation"""
        if type:
            return f"\\|{matrix}\\|_{{{type}}}"
        return f"\\|{matrix}\\|"
    
    @staticmethod
    def split_terms(latex_text):
        """Split the latex text into terms and return a list of terms"""
        terms = []
        current_term = ""
        for char in latex_text:
            if char in ['+', '-', '=', '.']:
                if current_term:
                    terms.append(current_term.strip())
                terms.append(char)
                current_term = ""
            else:
                current_term += char
        return terms
        
