from manim import *

from graphing.geo.model.model_part import ModelPart
from graphing.math.function_expression_utils import FunctionUtils
from .base_model import BaseModel
import sympy as sp
import numpy as np
from sympy.parsing.latex import parse_latex

# header example: ["x","f(x)=x^2"]
# rows example: [[0,f(0)],[1,f(1)],[2,f(2)]]    
class ModelTable(BaseModel):
    def __init__(self, header, rows ):
        super().__init__()
        self.header = header
        self.rows = rows
       
    def get_cell_ui(self, row: int, col: int):
        return self.ui_part.get_cell(row, col)  
    
    def get_row_ui(self, row: int):
        return self.ui_part.get_row(row)  

    def get_col_ui(self, col: int):
        return self.ui_part.get_col(col)  

    def get_cell_text(self, row: int, col: int):
        return self.rows[row][col]
    
    def get_row_text(self, row: int):
        return self.rows[row]
    
    def get_col_text(self, col: int):
        return [row[col] for row in self.rows]
    
    def item(self, row_index, column_index=None):
        ui_part = self.ui_part.item(row_index, column_index)
        return ModelPart(ui_part, ui_part.graphsheet, ui_part.geo_mapper, ui_part.scene, item_row=row_index, item_col=column_index)

    """
    Example:
    expressions = [x, a*x^2, sin(x), cos(x)]
    range = (0, 10, 1)
    subs = { a: 1}
    variable = 'x'
    """  
    @staticmethod    
    def from_expressions(expresssions, range, subs, variable = None):
        sym_var = None
        if variable is None:    
            sym_var = sp.symbols('x')
        else:
            # Convert the variable to a sympy symbol
            sym_var = sp.Symbol(variable)
    
        # Use FunctionUtil to create sympy expressions
        sympy_expressions = [FunctionUtils.evaulatable_sympy_expression(expr, subs) for expr in expresssions]

        # Create lambdified functions for each expression
        lambda_funcs = [sp.lambdify(sym_var, sp.sympify(expr), modules=['numpy']) for expr in sympy_expressions]

        # Generate the range values
        start, end, step = range
        x_values = np.arange(start, end + step, step)

        # Evaluate each function for the range values
        rows = []
        for x in x_values:
            row = []
            for func in lambda_funcs:
                try:
                    # Evaluate the function and substitute values
                    result = func(x)
                    if isinstance(result, np.ndarray):
                        result = result.item()  # Convert numpy scalar to Python scalar
                    result = sp.sympify(result).subs(subs)
                    row.append(result)
                except Exception as e:
                    row.append(f"Error: {str(e)}")
            rows.append(row)

        return ModelTable(header = expresssions, rows = rows)
    
    @staticmethod
    def from_header_and_rows(header, rows):
        return ModelTable(header = header, rows = rows)
     