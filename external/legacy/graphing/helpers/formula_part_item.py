from manim import MathTex

class FormulaPartsItem:
    def __init__(self, formula_parts: list, equal_index: int):
        """
        Store formula parts array and index of equals sign for formula transformations.
        
        Args:
            formula_parts: List of LaTeX formula components
            equal_index: Index where "=" appears in formula_parts
        """
        self.formula_parts = formula_parts
        self.equal_index = equal_index
        
    def to_latex_string(self)->str:
        return "".join(self.formula_parts)
    
    def to_math_tex(self)->MathTex:
        return MathTex("".join(self.formula_parts))