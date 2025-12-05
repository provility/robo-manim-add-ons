
from graphing.helpers.latex_symbols import LatexSymbols


class MatrixGenerator:
    def __init__(self):
        pass
    
    def matrix(self, entries, env_type='pmatrix'):
        """
        Generate LaTeX for a matrix.
        
        Args:
            entries: List of lists containing matrix elements
            env_type: Type of matrix environment ('pmatrix', 'bmatrix', etc.)
        """
        if env_type not in self.matrix_environments:
            raise ValueError(f"Unknown matrix environment: {env_type}")
        
        env, options = self.matrix_environments[env_type]
        rows = []
        for row in entries:
            # Convert row elements to strings and join with &
            rows.append(" & ".join(map(str, row)))
        
        # Join rows with \\
        matrix_content = " \\\\ ".join(rows)
        return f"\\begin{{{env}}}{options}\n{matrix_content}\n\\end{{{env}}}"

    def augmented_matrix(self, left_entries, right_entries):
        """
        Generate LaTeX for an augmented matrix [A|b].
        """
        rows = []
        for left_row, right_row in zip(left_entries, right_entries):
            left_part = " & ".join(map(str, left_row))
            right_part = " & ".join(map(str, right_row))
            rows.append(f"{left_part} \\middle| {right_part}")
        
        matrix_content = " \\\\ ".join(rows)
        return f"\\begin{{bmatrix}}\n{matrix_content}\n\\end{{bmatrix}}"

    def determinant(self, entries):
        """
        Generate LaTeX for a determinant.
        """
        rows = []
        for row in entries:
            rows.append(" & ".join(map(str, row)))
        matrix_content = " \\\\ ".join(rows)
        return f"\\begin{{vmatrix}}\n{matrix_content}\n\\end{{vmatrix}}"

    def matrix_operation(self, operation, matrix, subscript=None):
        """
        Generate LaTeX for matrix operations like transpose, inverse, etc.
        """
        matrix_str = str(matrix)
        if operation == "transpose":
            return f"{matrix_str}{LatexSymbols.TRANSPOSE}"
        elif operation == "inverse":
            return f"{matrix_str}{LatexSymbols.INVERSE}"
        elif operation == "determinant":
            if subscript:
                return f"{LatexSymbols.DETERMINANT}_{{{subscript}}}({matrix_str})"
            return f"{LatexSymbols.DETERMINANT}({matrix_str})"
        elif operation == "trace":
            return f"{LatexSymbols.TRACE}({matrix_str})"
        elif operation == "rank":
            return f"{LatexSymbols.RANK}({matrix_str})"
        else:
            raise ValueError(f"Unknown matrix operation: {operation}")
        
    def jacobian_matrix(self, functions, variables):
        """
        Generate Jacobian matrix elements.
        
        Args:
            functions: List of function names (e.g., ['f', 'g'])
            variables: List of variable names (e.g., ['x', 'y'])
        Returns:
            List of lists containing partial derivative elements
        """
        return [
            [self.partial_derivative_element(f, var) 
             for var in variables]
            for f in functions
        ]
    
    def hessian_matrix(self, function, variables):
        """
        Generate Hessian matrix elements (second partial derivatives).
        
        Args:
            function: Function name (e.g., 'f')
            variables: List of variable names (e.g., ['x', 'y'])
        Returns:
            List of lists containing second partial derivatives
        """
        return [
            [f"\\frac{{\\partial^2 {function}}}{{\\partial {var1}\\partial {var2}}}"
             for var2 in variables]
            for var1 in variables
        ]     
    
    
    def jacobian(self, functions, variables):
        """Add Jacobian matrix."""
        elements = self.jacobian_matrix(functions, variables)
        return self.matrix(elements, "pmatrix")
    
    def hessian(self, function, variables):
        """Add Hessian matrix."""
        elements = self.hessian_matrix(function, variables)
        return self.matrix(elements, "pmatrix")
    
    def gradient(self, function, variables):
        """Add gradient vector."""
        elements = self.gradient_vector(function, variables)
        return self.matrix([[elem] for elem in elements], "pmatrix")          