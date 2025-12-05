from manim import *
import re

class MatrixUtils:
    
    """
      latex_matrix = r"\begin{bmatrix} 1 & 4 & 3 \\ 3 & 5 & 2 \\ 5 & 2 & 3 \end{bmatrix}"
        
    """
    @staticmethod
    def manim_matrix_from_latex(latex_str):
        # Remove any whitespace and newlines
        latex_str = latex_str.replace('\n', '').replace(' ', '')
        
        # Check if it's a bmatrix or array environment
        if '\\begin{bmatrix}' in latex_str:
            pattern = r'\\begin{bmatrix}(.*?)\\end{bmatrix}'
        elif '\\begin{array}' in latex_str:
            pattern = r'\\left\((.*?)\\right\)'
        else:
            raise ValueError("Unsupported matrix format")
        
        # Extract the matrix content
        content = re.search(pattern, latex_str, re.DOTALL).group(1)
        # Split into rows and then elements
        rows = content.strip().split('\\\\')
        elements = [row.strip().split('&') for row in rows]
        return Matrix(elements)
    
  