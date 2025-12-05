from graphing.helpers.complex_latex import ComplexLatex

class ComplexResult:
    
    """
    A class to hold the result of a complex operation.
    latex_equation is the LaTeX String representation of the equation that was solved to get the result.
    result is the actual result of the operation - a ComplexLatex object.    
    """
    def __init__(self,  latex_equation, result:ComplexLatex):
       
        self.latex_equation = latex_equation
        self.result = result