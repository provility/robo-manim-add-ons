import sympy as sp
import numpy as np
import re
from sympy.parsing.latex import parse_latex
from manim import ParametricFunction
from sympy import Point, Segment, Ellipse, symbols, Eq, parse_expr, expand, solve, N, Matrix
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor

transformations = (standard_transformations +
                               (implicit_multiplication_application,) +
                               (convert_xor,))
 
 
class FunctionUtils:
    
    @staticmethod
    def latex_patterns():
        return  [
            r'\\[a-zA-Z]+',     # Matches LaTeX commands like \frac, \sin, etc.
            r'\{[^{}]*\}',      # Matches curly braces with content inside
            r'\$',              # Matches the dollar sign for inline math
            r'\\\[',            # Matches \[ for display math
            r'\\\(',            # Matches \( for inline math
            r'\\\)',            # Matches \) for inline math
            r'\\text\{'     # Matches \text{ for text
        ]
    
    @staticmethod
    def is_latex(input_str):
        # Check for common LaTeX patterns
       # General LaTeX syntax detection using common LaTeX symbols
        latex_pattern_items = FunctionUtils.latex_patterns()
        return any(re.search(pattern, input_str) for pattern in latex_pattern_items)
    
    @staticmethod
    def is_math(input_str):
        latex_pattern_items = FunctionUtils.latex_patterns()
        math_operator_pattern =  [ r'[+\-*/^]' ]         # Matches any arithmetic operator (+, -, *, /, ^)
        all_patterns = latex_pattern_items + math_operator_pattern
        return any(re.search(pattern, input_str) for pattern in all_patterns) 
    
    # Function to safely get coefficients
    @staticmethod
    def get_coefficients(expr_or_eq):
        # Check if the object is an Equality object (an equation)
        if isinstance(expr_or_eq, sp.Equality):
            # Use the left-hand side of the equation
            expanded_eq = expr_or_eq.lhs - expr_or_eq.rhs
            return expanded_eq.as_coefficients_dict()
        else:
            # Directly call as_coefficients_dict on the expression
            return expr_or_eq.as_coefficients_dict() 
    
    """
    Ensures that the input string is a valid SymPy expression.
    If the input is a LaTeX string, it tries to parse it.
    If the input is an equation, it converts it to a SymPy expression.
    Otherwise, it parses the input string directly.
    """
    @staticmethod
    def ensure_expression(input_str):
        if FunctionUtils.is_latex(input_str):
            try:
                expr = parse_latex(input_str)
            except Exception as e:
                print(f"Error parsing LaTeX: {e}")
                return None
        else:
            if "=" in input_str:
                left, right =  input_str.split("=")
                left_expr = parse_expr(left, transformations=transformations)   
                right_expr = parse_expr(right, transformations=transformations)
                expr = left_expr - right_expr
            else:
                expr = parse_expr(input_str, transformations=transformations)
                
        # If it's an equation, convert it to an expression  
        if isinstance(expr, sp.Equality):
            expr = expr.lhs - expr.rhs  
        return expr
    
    @staticmethod
    def as_equation(input_str):
        expr = FunctionUtils.ensure_expression(input_str)
        return sp.Eq(expr, 0)


    """
    Remove left-hand side if the expression is in the form x= or y= or f(x)=
    """
    @staticmethod
    def remove_function_notation(expression):
        if '=' in expression:
            lhs, rhs = expression.split('=', 1)
            lhs = lhs.strip() # checks function notation like f(x), g(x), etc.
            if lhs in ['x', 'y'] or (lhs[0].isalpha() and lhs.startswith(lhs[0]) and lhs.endswith(')')):
                expression = rhs.strip()
        return expression
    
    @staticmethod
    def evaulatable_sympy_expression(expression, subs_dict={}):
        expression = FunctionUtils.remove_function_notation(expression)
        sympy_expression = FunctionUtils.ensure_expression(expression)          
        sympy_expression = sympy_expression.subs(subs_dict)
        return sympy_expression
    
    @staticmethod
    def evaluate_sympy_expression(expression, subs_dict={}, precision=1):
        eval_result = FunctionUtils.evaulatable_sympy_expression(expression, subs_dict=subs_dict)
        # Format the result with precision
        if isinstance(eval_result, sp.Expr):
            # If it's a symbolic expression, evaluate it numerically
            numeric_result = eval_result.evalf()
        else:
            numeric_result = eval_result

        # Format the numeric result to 6 decimal places
        formatted_result = "{:."+str(precision)+"f}".format(float(numeric_result))
        
        # Remove trailing zeros after the decimal point
        formatted_result = formatted_result.rstrip('0').rstrip('.')
        
        return formatted_result
        
    @staticmethod
    def general_form_coefficients_from_expression(input_str):
        x, y = symbols('x y')
        expr = FunctionUtils.ensure_expression(input_str)
        expanded = expand(expr)
        
        coeffs = FunctionUtils.get_coefficients(expanded)
        A = coeffs.get(x**2, 0)
        B = coeffs.get(x*y, 0)
        C = coeffs.get(y**2, 0)
        D = coeffs.get(x, 0)
        E = coeffs.get(y, 0)
        F = coeffs.get(1, 0)
        
        return A, B, C, D, E, F
    
    @staticmethod
    def latex_to_plot_function(latex_expression, subs_dict={}, free_variable='x'):
        latex_expression = FunctionUtils.ensure_expression(latex_expression)
        free_variable_symbol = sp.Symbol(free_variable)
        sympy_expression = parse_latex(latex_expression)
        sympy_expression = sympy_expression.subs(subs_dict)
            
        # If the expression is an equation, solve for y
        if isinstance(sympy_expression, sp.Equality):
            lhs, rhs = sympy_expression.lhs, sympy_expression.rhs
            sympy_expression = sp.solve(lhs - rhs, sp.Symbol('y'))[0]
                
            sympy_expression = sympy_expression.subs(subs_dict)

            # Convert SymPy expression to a lambda function for plotting
            plot_function = sp.lambdify(free_variable_symbol, sympy_expression, 'numpy')
            
            return plot_function
        
        
        
    @staticmethod
    def is_explicit_function(latex_or_str_expression, variables=['x','y','z']):
        
        expression = FunctionUtils.ensure_expression(latex_or_str_expression)
        
        # Check if the expression is an equality
        """ 
        Determine if an equation is explicit for any of the specified variables or implicit.
    
        Parameters:
        equation (sympy expression): The equation to check.
        variables (list of sympy symbols): The variables to solve for.
    
        Returns:
        str: 'explicit in {var}' if the equation can be solved for any specified variable,
             'implicit' if it cannot be solved for any of the specified variables.
        """
        # Attempt to solve for each specified variable
        for var in variables:
            try: # Sumpy is smart enough to handle the case where the expression is not an equation 
                solution = sp.solve(expression, var)
                if solution:
                    return True
            except (sp.SolveFailed, ValueError):
                pass
    
        # If none of the specified variables can be isolated,
        # the equation is implicit
        return False    
    
    @staticmethod     
    def find_x_given_y(expression_str, y_value, subs_dict={}):
              # Define symbols
         x, y = sp.symbols('x y')
    
        # Parse the input string
         if FunctionUtils.is_latex(expression_str):
             expression_or_eq = parse_latex(expression_str)
         else:
    
         # Check if the input is an equation (contains '=')
          if '=' in expression_str:
            left, right = expression_str.split('=')
            left_expr = parse_expr(left.strip(), transformations=transformations)
            right_expr = parse_expr(right.strip(), transformations=transformations)
            # Assuming the equation is of the form 'y = ...', just use the right side
            if left_expr == x:
                expression_or_eq = right_expr
            else:
                # Create the equation for solving
                expression_or_eq = left_expr - right_expr
          else:
            # If it's an expression, parse it directly
            expression_or_eq = parse_expr(expression_str, transformations=transformations)
    
         expression_or_eq = expression_or_eq.subs(subs_dict)
         x_values = []
        # If it's an equation to be solved, solve for y
         if isinstance(expression_or_eq, sp.Basic) and expression_or_eq.has(x):
            solutions = sp.solve(expression_or_eq, x)
            # Substitute x_value into each solution and return the results
            x_values = [sol.subs(y, y_value) for sol in solutions]
         
         else:
            # Directly substitute x into the expression
            x_values = [expression_or_eq.subs(y, y_value)]
            
         results = []
         for x_value in x_values:
            if isinstance(x_value, sp.Expr):
                 results.append(float(x_value.evalf()))
            else:
                 results.append(x_value)
                 
         return results

    """
    Find the y-values given an x-value for a function.
    "y = x^2 + 2x + 1", 3 -> [16]
    "y = 4sin(2x)", 3 -> [4sin(6)]
    """
    @staticmethod
    def find_y_given_x(expression_str, x_value, subs_dict={}):
         # Define symbols
         x, y = sp.symbols('x y')
        # Parse the input string
         if FunctionUtils.is_latex(expression_str):
             expression_or_eq = parse_latex(expression_str)
         else:
    
         # Check if the input is an equation (contains '=')
          if '=' in expression_str:
            left, right = expression_str.split('=')
            left_expr = parse_expr(left.strip(), transformations=transformations)
            right_expr = parse_expr(right.strip(), transformations=transformations)
            # Assuming the equation is of the form 'y = ...', just use the right side
            if left_expr == y:
                expression_or_eq = right_expr
            else:
                # Create the equation for solving
                expression_or_eq = left_expr - right_expr
          else:
            # If it's an expression, parse it directly
            expression_or_eq = parse_expr(expression_str, transformations=transformations)
    
         expression_or_eq = expression_or_eq.subs(subs_dict)
         y_values = []   
        # If it's an equation to be solved, solve for y
         if isinstance(expression_or_eq, sp.Basic) and expression_or_eq.has(y):
            solutions = sp.solve(expression_or_eq, y)
            
            # Substitute x_value into each solution and return the results
            y_values = [sol.subs(x, x_value) for sol in solutions]
            
         else:
            # Directly substitute x into the expression
            y_values = [expression_or_eq.subs(x, x_value)]
    
            
         # Evaluate y_values if they are symbolic, otherwise return as is
         results = []
         for y_value in y_values:
             if isinstance(y_value, sp.Expr):
                 results.append(float(y_value.evalf()))
             else:
                 results.append(y_value)
                 
         return results
        

  
       
