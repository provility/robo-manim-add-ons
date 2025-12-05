from graphing.helpers.complex_latex import ComplexLatex
from sympy import latex
import math
from graphing.helpers.complex_result import ComplexResult
from graphing.helpers.latex_symbols import LatexSymbols
from graphing.helpers.latex_builder import LatexBuilder

class ComplexLatexOperations:

    @staticmethod
    def multiply(c1: ComplexLatex, c2: ComplexLatex, resultant_name: str)->ComplexResult:
        """
        Multiply two complex numbers and return their symbolic and LaTeX representations.
        """
        real_part = float(c1.real * c2.real - c1.imag * c2.imag)
        imag_part = float(c1.real * c2.imag + c1.imag * c2.real)
        
        # Format the parts
        real_part = int(real_part) if real_part.is_integer() else round(real_part, 2)
        imag_part = int(imag_part) if imag_part.is_integer() else round(imag_part, 2)
        result = ComplexLatex(real_part, imag_part)
        
        product_expr = ( LatexBuilder().append(c1.as_operand_latex())
                        .append(LatexSymbols.DOT_PRODUCT)
                        .append(c2.as_operand_latex())
                        .build()
        )
        equation = (LatexBuilder().append(resultant_name)
                    .append(LatexSymbols.EQUALS)
                    .append(product_expr)
                    .append(LatexSymbols.EQUALS)   
                    .append(result.to_latex())
                    .build())
        
        print(equation)
        
        return ComplexResult(
            latex_equation=equation,
            result=result
        )
    @staticmethod
    def add(*operands: ComplexLatex)->ComplexResult:
        """
        Add multiple complex numbers and return their symbolic and LaTeX representations.
        """
        real_sum = float(sum(o.real for o in operands))
        imag_sum = float(sum(o.imag for o in operands))
        
        # Format the sums
        real_sum = int(real_sum) if real_sum.is_integer() else round(real_sum, 2)
        imag_sum = int(imag_sum) if imag_sum.is_integer() else round(imag_sum, 2)
        
        # Build LaTeX components using LatexBuilder
        latex_builder = LatexBuilder()
        for o in operands:
            latex_builder.append(o.as_operand_latex())
            if o != operands[-1]:  # Add plus sign between operands
                latex_builder.append(LatexSymbols.PLUS)
        
        # Final result in LaTeX
        result_latex = ComplexLatex(real_sum, imag_sum).to_latex()
        latex_builder.append(LatexSymbols.EQUALS)
        latex_builder.append(result_latex)
        
        equation = latex_builder.build()
        
        return ComplexResult(
            latex_equation=equation,
            result=ComplexLatex(real_sum, imag_sum)
        )

    @staticmethod
    def divide(c1: ComplexLatex, c2: ComplexLatex, resultant_name: str)->ComplexResult:
        """
        Divide two complex numbers and return their symbolic and LaTeX representations.
        """
        if c2.real == 0 and c2.imag == 0:
            raise ValueError("Division by zero is not allowed.")
        
        denominator = float(c2.real**2 + c2.imag**2)
        real_part = float((c1.real * c2.real + c1.imag * c2.imag) / denominator)
        imag_part = float((c1.imag * c2.real - c1.real * c2.imag) / denominator)
        
        # Format the parts
        real_part = int(real_part) if real_part.is_integer() else round(real_part, 2)
        imag_part = int(imag_part) if imag_part.is_integer() else round(imag_part, 2)
        
        # Build LaTeX components using LatexBuilder
        latex_builder = LatexBuilder()
        latex_builder.append(resultant_name)
        latex_builder.append(LatexSymbols.EQUALS)
        latex_builder.append(c1.as_operand_latex())
        latex_builder.append(LatexSymbols.DIVISION)
        latex_builder.append(c2.as_operand_latex())
        latex_builder.append(LatexSymbols.EQUALS)
        latex_builder.append(ComplexLatex(real_part, imag_part).to_latex())
        
        equation = latex_builder.build()
        
        return ComplexResult(
            latex_equation=equation,
            result=ComplexLatex(real_part, imag_part)
        )

    

    @staticmethod
    def subtract_reciprocals(c1: ComplexLatex, c2: ComplexLatex, resultant_name: str)->ComplexResult:
        """
        Subtract reciprocals of two complex numbers and return their symbolic and LaTeX representations.
        """
        if (c1.real == 0 and c1.imag == 0) or (c2.real == 0 and c2.imag == 0):
            raise ValueError("Division by zero is not allowed.")
            
        # Calculate denominators
        denom1 = float(c1.real**2 + c1.imag**2)
        denom2 = float(c2.real**2 + c2.imag**2)
        
        # Calculate real and imaginary parts of result
        real_part = float(c2.real/denom2 - c1.real/denom1)
        imag_part = float(-c2.imag/denom2 + c1.imag/denom1)
        
        # Format the parts
        real_part = int(real_part) if real_part.is_integer() else round(real_part, 2)
        imag_part = int(imag_part) if imag_part.is_integer() else round(imag_part, 2)
        
        # Build LaTeX components using LatexBuilder
        latex_builder = LatexBuilder()
        latex_builder.append(resultant_name)
        latex_builder.append(LatexSymbols.EQUALS)
        latex_builder.append(LatexSymbols.FRACTION_START)
        latex_builder.append(LatexSymbols.ONE)
        latex_builder.append(LatexSymbols.DIVISION)
        latex_builder.append(c2.as_operand_latex())
        latex_builder.append(LatexSymbols.MINUS)
        latex_builder.append(LatexSymbols.ONE)
        latex_builder.append(LatexSymbols.DIVISION)
        latex_builder.append(c1.as_operand_latex())
        latex_builder.append(LatexSymbols.FRACTION_END)
        latex_builder.append(LatexSymbols.EQUALS)
        latex_builder.append(ComplexLatex(real_part, imag_part).to_latex())
        
        equation = latex_builder.build()
        
        return ComplexResult(
            latex_equation=equation,
            result=ComplexLatex(real_part, imag_part)
        )



    @staticmethod
    def modulus_product(*operands: ComplexLatex)->ComplexResult:
        """
        Generate LaTeX for the product of moduli: |z1 * z2 * ...| = |z1| * |z2| * ....
        """
        lhs = r"|{}|".format(r" \cdot ".join(latex(o.symbol) for o in operands))
        rhs = r" \cdot ".join(rf"|{latex(o.symbol)}|" for o in operands)
        equation = rf"{lhs} = {rhs}"
        
        # Calculate the actual product of moduli
        modulus = float(1)
        for o in operands:
            modulus *= (o.real**2 + o.imag**2)**0.5
            
        # Format the modulus
        modulus = int(modulus) if modulus.is_integer() else round(modulus, 2)
        
        # Calculate the symbolic product
        prod = 1
        for o in operands:
            prod *= o.symbolic_expression()
            
        return ComplexResult(
            latex_equation=equation,
            result=ComplexLatex(modulus, 0)  # Result is real number
        )


    @staticmethod
    def subtract(c1: ComplexLatex, c2: ComplexLatex, resultant_name: str)->ComplexResult:
        """
        Subtract two complex numbers and return their symbolic and LaTeX representations.
        """
        real_part = c1.real - c2.real
        imag_part = c1.imag - c2.imag
        symbolic_expr = c1.symbolic_expression() - c2.symbolic_expression()
        latex_repr = ComplexLatex(real_part, imag_part).to_latex()
        equation = (LatexBuilder().append(resultant_name)
                    .append(LatexSymbols.EQUALS)
                    .append(latex_repr)
                    .build())
        return ComplexResult(
            latex_equation=equation,
            result=ComplexLatex(real_part, imag_part)
        )
        
    @staticmethod
    def subtract_reciprocals(c1: ComplexLatex, c2: ComplexLatex, resultant_name: str)->ComplexResult:
        """
        Subtract reciprocals of two complex numbers and return their symbolic and LaTeX representations.
        """
        if c1.real == 0 and c1.imag == 0 or c2.real == 0 and c2.imag == 0:
            raise ValueError("Division by zero is not allowed.")
            
        # Calculate reciprocals first
        denom1 = float(c1.real**2 + c1.imag**2)
        denom2 = float(c2.real**2 + c2.imag**2)
        
        # Real and imaginary parts of 1/z1 - 1/z2
        real_part = float(c1.real/denom1) - float(c2.real/denom2)
        imag_part = float(-c1.imag/denom1) - float(-c2.imag/denom2)
        
        symbolic_expr = 1/c1.symbolic_expression() - 1/c2.symbolic_expression()
        
        # Construct LaTeX representation
        numerator = f"{latex(c2.real * denom1 - c1.real * denom2)} + {latex(c2.imag * denom1 - c1.imag * denom2)}i"
        denominator_latex = f"{latex(denom1 * denom2)}"
        latex_repr = rf"\frac{{{numerator}}}{{{denominator_latex}}}"
        
        equation = (LatexBuilder().append(resultant_name)
                    .append(LatexSymbols.EQUALS)
                    .append(latex_repr)
                    .build())
        
        return ComplexResult(
            latex_equation=equation,
            result=ComplexLatex(real_part, imag_part)
        )
        
        
    @staticmethod
    def modulus_division(c1: ComplexLatex, c2: ComplexLatex)->ComplexResult:
        """
        Generate LaTeX for the division of moduli: |z1 / z2| = |z1| / |z2|.
        """
        if c2.real == 0 and c2.imag == 0:
            raise ValueError("Division by zero is not allowed.")
        lhs = rf"|{latex(c1.symbol / c2.symbol)}|"
        rhs = rf"\frac{{|{latex(c1.symbol)}|}}{{|{latex(c2.symbol)}|}}"
        equation = rf"{lhs} = {rhs}"
        
        # Calculate actual modulus
        modulus1 = float((c1.real**2 + c1.imag**2)**0.5)
        modulus2 = float((c2.real**2 + c2.imag**2)**0.5)
        result = modulus1 / modulus2
        
        # Format the result
        result = int(result) if result.is_integer() else round(result, 2)
        
        return ComplexResult(
            latex_equation=equation,
            result=ComplexLatex(result, 0)  # Result is real number
        )

    @staticmethod
    def modulus_power(c: ComplexLatex, n: int)->ComplexResult:
        """
        Generate LaTeX for the power of modulus: |z^n| = |z|^n.
        """
        lhs = rf"|{latex(c.symbol**n)}|"
        rhs = rf"|{latex(c.symbol)}|^{n}"
        equation = rf"{lhs} = {rhs}"
        
        # Calculate actual modulus
        modulus = (c.real**2 + c.imag**2)**(n/2)
        
        return ComplexResult(
            latex_equation=equation,
            result=ComplexLatex(modulus, 0)  # Result is real number
        )


    
    @staticmethod
    def conjugate_addition(c1: ComplexLatex, c2: ComplexLatex)->ComplexResult:
        """
        Generate LaTeX for: conjugate(z1 + z2) = conjugate(z1) + conjugate(z2).
        """
        lhs = rf"\overline{{{latex(c1.symbol + c2.symbol)}}}"
        rhs = rf"\overline{{{latex(c1.symbol)}}} + \overline{{{latex(c2.symbol)}}}"
        equation = rf"{lhs} = {rhs}"
        result = ComplexLatex(c1.real + c2.real, -(c1.imag + c2.imag))
        return ComplexResult(
            latex_equation=equation,
            result=result
        )

    @staticmethod
    def conjugate_subtraction(c1: ComplexLatex, c2: ComplexLatex)->ComplexResult:
        """
        Generate LaTeX for: conjugate(z1 - z2) = conjugate(z1) - conjugate(z2).
        """
        lhs = rf"\overline{{{latex(c1.symbol - c2.symbol)}}}"
        rhs = rf"\overline{{{latex(c1.symbol)}}} - \overline{{{latex(c2.symbol)}}}"
        equation = rf"{lhs} = {rhs}"
        result = ComplexLatex(c1.real - c2.real, -(c1.imag - c2.imag))
        return ComplexResult(
            latex_equation=equation,
            result=result
        )

    @staticmethod
    def conjugate_product(c1: ComplexLatex, c2: ComplexLatex)->ComplexResult:
        """
        Generate LaTeX for: conjugate(z1 * z2) = conjugate(z1) * conjugate(z2).
        """
        prod_symbol = latex(c1.symbol * c2.symbol)
        conj1 = latex(c1.symbol)
        conj2 = latex(c2.symbol)
        
        lhs = rf"\overline{{{prod_symbol}}}"
        rhs = (rf"\overline{{{conj1}}} " +
               LatexSymbols.MULTIPLICATION + r" " +
               r"\overline{" + conj2 + r"}")
        
        equation = rf"{lhs} {LatexSymbols.EQUALS} {rhs}"
        
        # Calculate result
        result = ComplexLatex(
            c1.real * c2.real - c1.imag * c2.imag,
            -(c1.real * c2.imag + c1.imag * c2.real)
        )
        
        return ComplexResult(
            latex_equation=equation,
            result=result
        )

    @staticmethod
    def conjugate_division(c1: ComplexLatex, c2: ComplexLatex, resultant_name: str)->ComplexResult:
        """
        Generate LaTeX for: conjugate(z1 / z2) = conjugate(z1) / conjugate(z2).
        """
        if c2.real == 0 and c2.imag == 0:
            raise ValueError("Division by zero is not allowed.")
        
        denominator = c2.real**2 + c2.imag**2
        real_part = (c1.real * c2.real + c1.imag * c2.imag) / denominator
        imag_part = -(c1.imag * c2.real - c1.real * c2.imag) / denominator
        
        # Build LaTeX components using LatexBuilder
        latex_builder = LatexBuilder()
        latex_builder.append(resultant_name)
        latex_builder.append(LatexSymbols.EQUALS)
        latex_builder.append(LatexSymbols.CONJUGATE_START)
        latex_builder.append(c1.as_operand_latex())
        latex_builder.append(LatexSymbols.DIVISION)
        latex_builder.append(c2.as_operand_latex())
        latex_builder.append(LatexSymbols.CONJUGATE_END)
        latex_builder.append(LatexSymbols.EQUALS)
        latex_builder.append(ComplexLatex(real_part, imag_part).to_latex())
        
        equation = latex_builder.build()
        
        return ComplexResult(
            latex_equation=equation,
            result=ComplexLatex(real_part, imag_part)
        )

    @staticmethod
    def conjugate_power(c: ComplexLatex, n: int)->ComplexResult:
        """
        Generate LaTeX for: conjugate(z^n) = (conjugate(z))^n.
        """
        lhs = rf"\overline{{{latex(c.symbol**n)}}}"
        rhs = rf"\left(\overline{{{latex(c.symbol)}}}\\right)^{n}"
        equation = rf"{lhs} = {rhs}"
        # For conjugate power, we need polar form calculations for accurate results
        result = ComplexLatex(c.real, -c.imag)**n
        return ComplexResult(
            latex_equation=equation,
            result=result
        )
    
    @staticmethod
    def add_reciprocals(*operands: ComplexLatex, resultant_name: str)->ComplexResult:
        """
        Generate LaTeX for the sum of reciprocals of multiple complex numbers.
        """
        for o in operands:
            if o.real == 0 and o.imag == 0:
                raise ValueError("Division by zero is not allowed.")
        
        # Calculate actual result
        real_part = sum((o.real/(o.real**2 + o.imag**2)) for o in operands)
        imag_part = sum((-o.imag/(o.real**2 + o.imag**2)) for o in operands)
        actual = ComplexLatex(real_part, imag_part)

        # Build LaTeX components using LatexBuilder
        latex_builder = LatexBuilder()
        latex_builder.append(resultant_name)
        latex_builder.append(LatexSymbols.EQUALS)
        for o in operands:
            latex_builder.append(LatexSymbols.FRACTION_START)
            latex_builder.append(LatexSymbols.ONE)
            latex_builder.append(LatexSymbols.DIVISION)
            latex_builder.append(o.as_operand_latex())
            latex_builder.append(LatexSymbols.FRACTION_END)
            if o != operands[-1]:
                latex_builder.append(LatexSymbols.PLUS)
        latex_builder.append(LatexSymbols.EQUALS)
        latex_builder.append(actual.to_latex())

        equation = latex_builder.build()
        
        return ComplexResult(
            latex_equation=equation,
            result=actual
        )
        
    @staticmethod
    def multiply_polar_latex(c1: ComplexLatex, c2: ComplexLatex, resultant_name: str)->ComplexResult:
        """
        Generate LaTeX for the multiplication of two complex numbers in polar form.
        """
        # Get polar form components for both numbers
        r1, theta1 = c1.to_polar_form()
        r2, theta2 = c2.to_polar_form()
        
        # Build the LaTeX representation showing multiplication in polar form
        latex_builder = LatexBuilder()
        latex_builder.append(resultant_name)
        latex_builder.append(LatexSymbols.EQUALS)
        latex_builder.append(c1.as_operand_latex())
        latex_builder.append(LatexSymbols.MULTIPLICATION)
        latex_builder.append(c2.as_operand_latex())
        latex_builder.append(LatexSymbols.EQUALS)
        latex_builder.append(f"{r1 * r2} (\\cos({theta1 + theta2}) + i \\sin({theta1 + theta2}))")
        
        # The actual result is the same as regular multiplication
        result = ComplexLatexOperations.multiply(c1, c2).result
        latex_builder.append(LatexSymbols.EQUALS)
        latex_builder.append(result.to_latex())

        equation = latex_builder.build()
        
        return ComplexResult(
            latex_equation=equation,
            result=result
        )

    @staticmethod
    def modulus_polar_product(*operands: ComplexLatex, resultant_name: str)->ComplexResult:
        """
        Generate LaTeX for the product of moduli in polar form: |z1 * z2 * ...| = |z1| * |z2| * ....
        """
        # Calculate the actual product of moduli
        modulus = 1
        for o in operands:
            modulus *= (o.real**2 + o.imag**2)**0.5

        # Build LaTeX components using LatexBuilder
        latex_builder = LatexBuilder()
        latex_builder.append(resultant_name)
        latex_builder.append(LatexSymbols.EQUALS)
        latex_builder.append(LatexSymbols.ABSOLUTE)
        for o in operands:
            latex_builder.append(o.as_operand_latex())
            if o != operands[-1]:
                latex_builder.append(LatexSymbols.MULTIPLICATION)
        latex_builder.append(LatexSymbols.ABSOLUTE)
        latex_builder.append(LatexSymbols.EQUALS)
        latex_builder.append(str(round(modulus, 2)))

        equation = latex_builder.build()
        
        return ComplexResult(
            latex_equation=equation,
            result=ComplexLatex(modulus, 0)  # Result is real number
        )

    @staticmethod
    def de_moivre_power(c: ComplexLatex, n: int, resultant_name: str)->ComplexResult:
        """
        Apply De Moivre's theorem to raise a complex number to power n.
        Returns symbolic and LaTeX representations.
        """
        r, theta = c.to_polar_form() 
        
        # Format the radius
        r = int(r) if r.is_integer() else round(r, 2)
        
        # Pre-compute theta in LaTeX notation
        theta_latex = c.latex_gen.radian_to_pi_notation(theta)

        # Calculate the result components
        result_real = r**n * math.cos(n * theta)
        result_imag = r**n * math.sin(n * theta)

        # Build the LaTeX representation using LatexBuilder
        latex_builder = LatexBuilder()
        latex_builder.append(resultant_name)
        latex_builder.append(LatexSymbols.EQUALS)
        latex_builder.append(r"{0}^{{{1}}}(\cos({1}{2}) + i\sin({1}{2}))".format(
            latex(r), n, theta_latex))
        latex_builder.append(LatexSymbols.EQUALS)
        latex_builder.append(ComplexLatex(result_real, result_imag).to_latex())

        equation = latex_builder.build()
        
        return ComplexResult(
            latex_equation=equation,
            result=ComplexLatex(result_real, result_imag)
        )

    @staticmethod
    def de_moivre_sum_reciprocal(c: ComplexLatex, n: int, resultant_name: str)->ComplexResult:
        """
        Generate expressions for z^n + 1/z^n.
        Returns symbolic and LaTeX representations.
        """
        if n == 0:
            return ComplexResult(
                latex_equation=f"{resultant_name} = z^0 + \\frac{{1}}{{z^0}} = 2",
                result=ComplexLatex(2, 0)
            )
        
        r, theta = c.to_polar_form()
        
        # Using De Moivre's theorem: z^n + 1/z^n = 2cos(nθ)
        result = 2 * math.cos(n * theta)
        
        # Pre-compute theta in LaTeX notation
        theta_latex = c.latex_gen.radian_to_pi_notation(n * theta)

        # Build the LaTeX representation using LatexBuilder
        latex_builder = LatexBuilder()
        latex_builder.append(resultant_name)
        latex_builder.append(LatexSymbols.EQUALS)
        latex_builder.append(c.as_operand_latex())
        latex_builder.append(f"^{{{n}}} + \\frac{{1}}{{")
        latex_builder.append(c.as_operand_latex())
        latex_builder.append(f"^{{{n}}}}}")
        latex_builder.append(LatexSymbols.EQUALS)
        latex_builder.append(f"2\\cos({theta_latex})")

        equation = latex_builder.build()
        
        return ComplexResult(
            latex_equation=equation,
            result=ComplexLatex(result, 0)
        )

    @staticmethod
    def de_moivre_difference_reciprocal(c: ComplexLatex, n: int, resultant_name: str)->ComplexResult:
        """
        Generate expressions for z^n - 1/z^n.
        Returns symbolic and LaTeX representations.
        """
        if n == 0:
            return ComplexResult(
                latex_equation=f"{resultant_name} = z^0 - \\frac{{1}}{{z^0}} = 0",
                result=ComplexLatex(0, 0)
            )
        
        r, theta = c.to_polar_form()

        # Using De Moivre's theorem: z^n - 1/z^n = 2i*sin(nθ)
        result = 2 * math.sin(n * theta)
        
        # Pre-compute theta in LaTeX notation
        theta_latex = c.latex_gen.radian_to_pi_notation(n * theta)

        # Build the LaTeX representation using LatexBuilder
        latex_builder = LatexBuilder()
        latex_builder.append(resultant_name)
        latex_builder.append(LatexSymbols.EQUALS)
        latex_builder.append(c.as_operand_latex())
        latex_builder.append(f"^{{{n}}} - \\frac{{1}}{{")
        latex_builder.append(c.as_operand_latex())
        latex_builder.append(f"^{{{n}}}}}")
        latex_builder.append(LatexSymbols.EQUALS)
        latex_builder.append(f"2i\\sin({theta_latex})")

        equation = latex_builder.build()
        
        return ComplexResult(
            latex_equation=equation,
            result=ComplexLatex(0, result)
        )
     
     
    
        # Add to ComplexLatexOperations class:

    @staticmethod
    def nth_root_unity(n: int, k: int, resultant_name: str)->ComplexResult:
        """
        Generate LaTeX for kth nth root of unity using:
        omega_k = cos(2πk/n) + i*sin(2πk/n)
        """
        import math
        angle = 2 * math.pi * k / n
        result = ComplexLatex(math.cos(angle), math.sin(angle))
        
        # Build LaTeX components using LatexBuilder
        latex_builder = LatexBuilder()
        latex_builder.append(resultant_name)
        latex_builder.append(LatexSymbols.EQUALS)
        latex_builder.append(r"\omega_{{{0}}} = \cos\left(\frac{{2\pi {1}}}{{{2}}}\right) + i\sin\left(\frac{{2\pi {1}}}{{{2}}}\right)".format(k, k, n))
        
        equation = latex_builder.build()
        
        return ComplexResult(
            latex_equation=equation,
            result=result
        )

    @staticmethod
    def nth_roots_complex(z: ComplexLatex, n: int, resultant_name: str)->ComplexResult:
        """
        Generate LaTeX for finding nth roots using de Moivre's formula:
        z^(1/n) = r^(1/n)(cos((θ + 2πk)/n) + i*sin((θ + 2πk)/n))
        """
        r, theta = z.to_polar_form()
        r_nth = r ** (1 / n)
        n_minus_1 = n - 1  # Pre-calculate n-1
        
        r_nth = int(r_nth) if r_nth.is_integer() else round(r_nth, 2)  # Format the radius
        
        # Build LaTeX components using LatexBuilder
        latex_builder = LatexBuilder()
        latex_builder.append(resultant_name)
        latex_builder.append(LatexSymbols.EQUALS)
        for k in range(n):
            angle = (theta + 2 * math.pi * k) / n
            real_part = r_nth * math.cos(angle)
            imag_part = r_nth * math.sin(angle)
            root_latex = ComplexLatex(real_part, imag_part).to_latex()
            latex_builder.append(root_latex)
            if k != n_minus_1:
                latex_builder.append(", ")
        
        equation = latex_builder.build()
        
        return ComplexResult(
            latex_equation=equation,
            result=ComplexLatex(r_nth * math.cos(theta / n), r_nth * math.sin(theta / n))  # Example root
        )


    @staticmethod
    def unity_roots_sum(n: int, resultant_name: str)->ComplexResult:
        """
        Generate LaTeX for sum of nth roots of unity property:
        1 + ω + ω² + ... + ω^(n-1) = 0
        """
        if n <= 0:
            raise ValueError("n must be positive")
        
        # Build LaTeX components using LatexBuilder
        latex_builder = LatexBuilder()
        latex_builder.append(resultant_name)
        latex_builder.append(LatexSymbols.EQUALS)
        latex_builder.append("1")
        for k in range(1, n):
            latex_builder.append(f" + \\omega^{{{k}}}")
        latex_builder.append(" = 0, \\ ")
        latex_builder.append(r"\omega = e^{{2\pi i/{0}}}".format(n))
        
        equation = latex_builder.build()
        latex_eq = (
            r"1 + \omega + \omega^2 + \cdots + \omega^{{{0}-1}} = 0, \\ "
            r"\omega = e^{{2\pi i/{0}}}".format(n)
        )
        
        result = ComplexLatex(0, 0)
        
        return ComplexResult(
            latex_equation=latex_eq,
            result=result
        )

    @staticmethod
    def unity_roots_product(n: int)->ComplexResult:
        """
        Generate LaTeX for product of nth roots of unity property:
        1 * ω * ω² * ... * ω^(n-1) = (-1)^(n-1)
        """
        if n <= 0:
            raise ValueError("n must be positive")
        
        n_minus_1 = n - 1  # Pre-calculate n-1
        latex_eq = (
            r"\omega^0 \cdot \omega^1 \cdot \omega^2 \cdots \omega^{{{0}}} = (-1)^{{{1}}}, \\ "
            r"\omega = e^{{2\pi i/{2}}}".format(n_minus_1, n_minus_1, n)
        )
        
        result = ComplexLatex((-1)**n_minus_1, 0)
        
        return ComplexResult(
            latex_equation=latex_eq,
            result=result
        )

    @staticmethod
    def geometric_progression_roots(n: int)->ComplexResult:
        """
        Generate LaTeX showing nth roots of unity geometric progression
        """
        if n <= 0:
            raise ValueError("n must be positive")
        
        latex_eq = (
            r"1, \omega, \omega^2, \ldots, \omega^{{{0}-1}}, \\ "
            r"\omega = e^{{2\pi i/{0}}}".format(n)
        )
        
        result = ComplexLatex(math.cos(2*math.pi/n), math.sin(2*math.pi/n))
        
        return ComplexResult(
            latex_equation=latex_eq,
            result=result
        )    

    
