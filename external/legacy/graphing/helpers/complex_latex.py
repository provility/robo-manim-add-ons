import math
import sympy as sp
from sympy import latex, sqrt, symbols, conjugate
from .latex_generator import LatexGenerator


class ComplexLatex:
    def __init__(self, real, imag, name="z"):
        """
        Initialize with the real and imaginary parts of the complex number.
        """
        self._assign_symbol(real, imag, name)
      
        
    def _assign_symbol(self, real, imag, name="z"):
         # Format real and imag to have at most 2 decimal places
        self.real = int(real) if float(real).is_integer() else round(float(real), 2)
        self.imag = int(imag) if float(imag).is_integer() else round(float(imag), 2)
        self.symbol = symbols(name)
        self.expression = self.real + self.imag * 1j
        self.latex_gen = LatexGenerator()
  
    def set_symbol(self, name):
        self.symbol = symbols(name)
        self.expression = self.real + self.imag * 1j    
        
    def to_latex(self, with_symbol=False,
                 show_zero_terms=True,
                 with_braces=False)->str:
        """
        Return the LaTeX representation of the complex number.
        
        Args:
                with_symbol (bool): Whether to include the symbol (e.g., z =) in output
                show_zero_terms (bool): Whether to show terms that are 0 or coefficients of 1
                with_braces (bool): Whether to add braces around the result
        """
        
        def add_braces(expr: str) -> str:
            return f"({expr})" if with_braces else expr
        
        # Format real and imaginary parts
        real_str = str(int(self.real) if float(self.real).is_integer() else round(float(self.real), 2))
        imag_str = str(int(abs(self.imag)) if float(abs(self.imag)).is_integer() else round(float(abs(self.imag)), 2))
            
        # Handle special cases when show_zero_terms is False
        if not show_zero_terms:
            # Case: pure imaginary number
            if self.real == 0:
                if abs(self.imag) == 1:
                    result = "i" if self.imag > 0 else "-i"
                elif self.imag == 0:
                    result = "0"
                else:
                    result = f"{imag_str}i" if self.imag > 0 else f"-{imag_str}i"
                    
                result = add_braces(result)
                return f"{latex(self.symbol)} = {result}" if with_symbol else result
                
            
        # Default case: show all terms normally
        sign = "+" if self.imag >= 0 else "-"
        result = f"{real_str} {sign} {imag_str}i"
        result = add_braces(result)
        return f"{latex(self.symbol)} = {result}" if with_symbol else result
       
      
    def as_operand_latex(self)->str:
        """
        Return the LaTeX representation of the complex number as an operand.
        """
        return self.to_latex(with_symbol=False, show_zero_terms=True, with_braces=True)
    
    def as_equation_latex(self)->str:
        """
        Return the LaTeX representation of the complex number as an equation.
        """
        return self.to_latex(with_symbol=True, show_zero_terms=True, with_braces=False)
 

    def modulus_latex(self)->str:
        """
        Generate the LaTeX definition of the modulus.
        """
        modulus = (self.real**2 + self.imag**2)**0.5
        modulus_str = str(int(modulus) if float(modulus).is_integer() else round(float(modulus), 2))
        return r"|{}| = {}".format(latex(self.symbol), modulus_str)

    def modulus_squared_latex(self)->str:
        """
        Generate the LaTeX representation of |z|^2 = z * conjugate(z).
        Example: |z|^2 = z * conjugate(z)
        """
        return r"|{}|^2 = {} \cdot \overline{{{}}}".format(
            latex(self.symbol), latex(self.symbol), latex(self.symbol)
        )

    def conjugate_latex(self)->str:
        """
        Generate the LaTeX representation of the conjugate.
        Example: conjugate(z) = x - yi
        """
        conjugate_expr = ComplexLatex(self.real, -self.imag, name=str(self.symbol))
        return r"\overline{{{}}} = {}".format(
            latex(self.symbol), conjugate_expr.to_latex().split("=", 1)[1].strip()
        )

    """
    Methods ending in "expression" return the symbolic expression(sympy) of the complex number.
    These methods are used by complex_latex_operations.py to perform operations on complex numbers. 
    """
    def symbolic_expression(self)->sp.Expr:
        """
        Return the symbolic expression of the complex number.
        """
        return self.expression
    
    def reciprocal_expression(self)->sp.Expr:
        """
        Return the symbolic expression of the reciprocal of the complex number.
        """
        return 1 / self.expression

    def modulus_expression(self)->sp.Expr:
        """
        Return the symbolic expression of the modulus.
        """
        return sqrt(self.real**2 + self.imag**2)

    def modulus_squared_expression(self)->sp.Expr:
        """
        Return the symbolic expression of |z|^2.
        """
        return self.expression * conjugate(self.expression)

    def conjugate_expression(self)->sp.Expr:
        """
        Return the symbolic expression of the conjugate of the complex number.
        """
        return conjugate(self.expression)

    def real_part_latex(self)->str:
        """
        Generate the LaTeX representation of Re(z).
        """
        return r"\text{{Re}}({}) = \frac{{{} + \overline{{{}}}}}{{2}}".format(
            latex(self.symbol), latex(self.symbol), latex(self.symbol)
        )

    def imaginary_part_latex(self)->str:
        """
        Generate the LaTeX representation of Im(z).
        """
        return r"\text{{Im}}({}) = \frac{{{} - \overline{{{}}}}}{{2i}}".format(
            latex(self.symbol), latex(self.symbol), latex(self.symbol)
        )

    def is_real_latex(self)->str:
        """
        Generate the LaTeX representation for checking if z is real.
        """
        return r"{} = \overline{{{}}}".format(latex(self.symbol), latex(self.symbol))

    def is_purely_imaginary_latex(self)->str:
        """
        Generate the LaTeX representation for checking if z is purely imaginary.
        """
        return r"{} = -\overline{{{}}}".format(latex(self.symbol), latex(self.symbol))

    def reciprocal_latex(self)->str:
        """
        Generate the LaTeX representation of the reciprocal of the complex number.
        Example: 1/z
        """
        return r"\frac{{1}}{{{}}}".format(latex(self.symbol))

   

    def real_imag_modulus(self)->tuple[str, str]:
        """
        Generate LaTeX for Re(z) ≤ |z| and Im(z) ≤ |z|.
        """
        re_latex = r"\text{{Re}}({}) \leq |{}|".format(latex(self.symbol), latex(self.symbol))
        im_latex = r"\text{{Im}}({}) \leq |{}|".format(latex(self.symbol), latex(self.symbol))
        return re_latex, im_latex

    def reciprocal_polar_latex(self)->str:
        """
        Generate LaTeX for the reciprocal of a complex number in polar form.
        Example: z^{-1} = \frac{1}{r} (cos(-π/4) + i sin(-π/4))
        """
        r, theta = self.to_polar_form()
        angle_latex = self.latex_gen.radian_to_pi_notation(-theta)  # Negative angle for reciprocal
        return r"{}^{{-1}} = \frac{{1}}{{{}}} (\cos({}) + i \sin({}))".format(
            latex(self.symbol), latex(r), angle_latex, angle_latex
        )


    def to_polar_form(self)->tuple[float, float]:
        """
        Convert complex number to polar form (r, θ).
        Returns (r, θ) where r is the modulus and θ is the argument.
        """
        r = (self.real**2 + self.imag**2)**0.5
        theta = math.atan2(self.imag, self.real)
        return r, theta
    
    def to_polar_form_latex(self)->str:
        """
        Generate LaTeX for the polar form of a complex number.
        Example: z = r (cos(θ) + i sin(θ))
        """
        r, theta = self.to_polar_form()
        return r"{} = {} (\cos({}) + i \sin({}))".format(latex(self.symbol), latex(r), theta, theta)    

    def de_moivre_power_latex(self, n)->str:
        """
        Generate LaTeX for De Moivre's theorem for power n.
        Example: z^n = r^n(cos(nπ/4) + i sin(nπ/4))
        """
        r, theta = self.to_polar_form()
        angle_latex = self.latex_gen.radian_to_pi_notation(n * theta)
        return r"{}^{{{}}} = {}^{{{}}} (\cos({}) + i \sin({}))".format(
            latex(self.symbol), n, latex(r), n, angle_latex, angle_latex
        )

    def reciprocal_modulus_latex(self)->str:
        """
        Generate LaTeX for the modulus of the reciprocal of a complex number.
        Example: |1/z| = 1/|z|
        """
        return r"|\frac{{1}}{{{}}}| = \frac{{1}}{{|{}|}}".format(
            latex(self.symbol), latex(self.symbol)
        )

class ComplexVariable(ComplexLatex):
    def __init__(self, name: str):
        super().__init__(0, 0, name)
        
    def to_latex(self, with_symbol=False, show_zero_terms=True, with_braces=False)->str:
        return latex(self.symbol)   
    
    def as_operand_latex(self)->str:
        return self.to_latex()
    
    def as_equation_latex(self)->str:
        return self.to_latex()  
    
class PureImaginaryVariable(ComplexLatex):
    def __init__(self, imag: float):
        super().__init__(0, imag, "i")
        
    def to_latex(self, with_symbol=False, show_zero_terms=True, with_braces=False)->str:
        return "i" if self.imag > 0 else "-i"
    
    def as_operand_latex(self)->str:
        return self.to_latex()
    
    def as_equation_latex(self)->str:
        return self.to_latex()

class SymbolicComplexVariable(ComplexLatex):
    def __init__(self, real='a', imag='b', name: str='z'):
        super().__init__(real, imag, name)
        
    def _assign_symbol(self, real, imag, name):
        self.real = real
        self.imag = imag
        self.symbol = symbols(name)
        self.expression = self.real + self.imag * 1j
        
