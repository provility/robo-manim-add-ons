from graphing.helpers.formula_part_item import FormulaPartsItem
from graphing.helpers.latex_symbols import LatexSymbols

"""
All methods return equation parts arrays for mathematical identities and transformations
For simple expressions use LatexGenerator.
For combined expressions use LatexBuilder.
Make sure to call to_latex_string() on the returned FormulaPartsItem because 
FormulaPartFactory returns a FormulaPartsItem object.
We need string representations of the formula parts to build complete formulas. (When we call append() in LatexBuilder.)

"""
class FormulaPartsFactory:
    """Builds formula parts arrays for mathematical identities and transformations"""
    
    @staticmethod
    def exponent_product_rule(base="x", m="m", n="n", equal_index=7) -> FormulaPartsItem:
        """x^m * x^n = x^(m+n)"""
        exponent_product = f"{m}+{n}" if not (isinstance(m, int) and isinstance(n, int)) else str(m + n)
        formula_parts = [
            base, "^", str(m), "\\cdot", base, "^", str(n), "=", 
            base, "^", "{", exponent_product, "}"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def power_of_power_rule(base="x", m="m", n="n", equal_index=7) -> FormulaPartsItem:
        """(x^m)^n = x^(mn)"""
        power_product = f"{m} \\cdot {n}" if not (isinstance(m, int) and isinstance(n, int)) else str(m * n)
        formula_parts = [
            "(", base, "^", str(m), ")", "^", str(n), "=",
            base, "^", "{", power_product, "}"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod 
    def complex_addition_rule(z1="z_1", z2="z_2", r1="r_1", r2="r_2", 
                            theta1="\\theta_1", theta2="\\theta_2", equal_index=11) -> FormulaPartsItem:
        """(r₁e^(iθ₁) + r₂e^(iθ₂)) = r₁(cos θ₁ + i sin θ₁) + r₂(cos θ₂ + i sin θ₂)"""
        formula_parts = [
            "(", r1, "e^{i", theta1, "}", "+", r2, "e^{i", theta2, "}", ")", "=",
            r1, "(\\cos", theta1, "+i\\sin", theta1, ")", "+",
            r2, "(\\cos", theta2, "+i\\sin", theta2, ")"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def complex_multiplication_rule(z1="z_1", z2="z_2", r1="r_1", r2="r_2",
                                  theta1="\\theta_1", theta2="\\theta_2", equal_index=11) -> FormulaPartsItem:
        """z₁z₂ = r₁r₂e^(i(θ₁+θ₂)) = r₁r₂(cos(θ₁+θ₂) + i sin(θ₁+θ₂))"""
        formula_parts = [
            "(", r1, "e^{i", theta1, "}", "\\cdot", r2, "e^{i", theta2, "}", ")", "=",
            r1, r2, "e^{i(", theta1, "+", theta2, ")}", "=",
            r1, r2, "(\\cos(", theta1, "+", theta2, ")", "+i\\sin(", theta1, "+", theta2, "))"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def de_moivre_formula(z="z", n="n", r="r", theta="\\theta", equal_index=13) -> FormulaPartsItem:
        """(r(cos θ + i sin θ))^n = r^n(cos(nθ) + i sin(nθ))"""
        formula_parts = [
            "(", r, "(", "\\cos", theta, "+", "i\\sin", theta, ")", ")", "^{", n, "}", "=",
            r, "^{", n, "}", "(", "\\cos(", n, theta, ")", "+", "i\\sin(", n, theta, ")", ")"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def euler_formula(theta="\\theta", equal_index=5) -> FormulaPartsItem:
        """e^(iθ) = cos θ + i sin θ"""
        formula_parts = [
            "e", "^{", "i", theta, "}", "=", "\\cos", theta, "+", "i", "\\sin", theta
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def complex_roots_unity(n="n", k="k", equal_index=3) -> FormulaPartsItem:
        """z_k = e^(2πik/n) = cos(2πk/n) + i sin(2πk/n)"""
        formula_parts = [
            "z_{", k, "}", "=", "e^{", "2\\pi i", k, "/", n, "}", "=",
            "\\cos(", "\\frac{2\\pi", k, "}{", n, "})", "+",
            "i\\sin(", "\\frac{2\\pi", k, "}{", n, "})"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def triangle_inequality_complex(z1="z_1", z2="z_2", equal_index=5) -> FormulaPartsItem:
        """|z₁ + z₂| ≤ |z₁| + |z₂|"""
        formula_parts = [
            "|", z1, "+", z2, "|", "\\leq", "|", z1, "|", "+", "|", z2, "|"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def complex_conjugate_product(z1="z_1", z2="z_2", equal_index=6) -> FormulaPartsItem:
        """overline(z₁z₂) = overline(z₁)overline(z₂)"""
        formula_parts = [
            "\\overline{", "{", z1, "\\cdot", z2, "}", "=",
            "\\overline{", "{", z1, "}", "\\cdot", "\\overline{", "{", z2, "}"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def quotient_rule(x="x", m="m", n="n", equal_index=10) -> FormulaPartsItem:
        """x^m/x^n = x^(m-n)"""
        formula_parts = [
            "\\frac{", x, "^", m, "}", "{", x, "^", n, "}", "=",
            x, "^", "{", m, "-", n, "}"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def radical_product_rule(x="x", y="y", equal_index=4) -> FormulaPartsItem:
        """√(xy) = √x * √y"""
        formula_parts = [
            "\\sqrt{", x, y, "}", "=", "\\sqrt{", x, "}", "\\sqrt{", y, "}"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def complex_division_polar(z1="z_1", z2="z_2", r1="r_1", r2="r_2", 
                             theta1="\\theta_1", theta2="\\theta_2", equal_index=5) -> FormulaPartsItem:
        """z₁/z₂ = (r₁/r₂)e^(i(θ₁-θ₂))"""
        formula_parts = [
            "\\frac{", z1, "}{", z2, "}", "=", "\\frac{", r1, "}{", r2, "}",
            "e^{i(", theta1, "-", theta2, ")}"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def complex_division_rectangular(z1="z_1", z2="z_2", a="a", b="b", c="c", d="d", equal_index=9) -> FormulaPartsItem:
        """(a+bi)/(c+di) = ((ac+bd)/(c²+d²)) + ((bc-ad)/(c²+d²))i"""
        formula_parts = [
            "\\frac{", a, "+", b, "i}{", c, "+", d, "i}", "=",
            "\\frac{", a, c, "+", b, d, "}{", c, "^2+", d, "^2}",
            "+", "i\\frac{", b, c, "-", a, d, "}{", c, "^2+", d, "^2}"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def modulus_reciprocal(z="z", equal_index=3) -> FormulaPartsItem:
        """|1/z| = 1/|z|"""
        formula_parts = [
            "|\\frac{1}{", z, "}|", "=", "\\frac{1}{|", z, "|}"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def complex_absolute_value(z="z", x="x", y="y", equal_index=3) -> FormulaPartsItem:
        """|z| = |x + yi| = √(x² + y²)"""
        formula_parts = [
            "|", z, "|", "=", "|", x, "+", y, "i", "|", "=",
            "\\sqrt{", x, "^2+", y, "^2}"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def complex_polar_exponential(z="z", r="r", theta="\\theta", equal_index=1) -> FormulaPartsItem:
        """z = re^(iθ)"""
        formula_parts = [
            z, "=", r, "e^{i", theta, "}"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def complex_conjugate_properties(z="z", x="x", y="y", equal_index=3) -> FormulaPartsItem:
        """z̄ = x - yi"""
        formula_parts = [
            "\\overline{", z, "}", "=", x, "-", y, "i"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def complex_conjugate_reciprocal(z="z", equal_index=5) -> FormulaPartsItem:
        """z·z̄ = |z|²"""
        formula_parts = [
            z, "\\cdot", "\\overline{", z, "}", "=", "|", z, "|^2"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def complex_nth_roots(z="z", n="n", k="k", r="r", theta="\\theta", equal_index=4) -> FormulaPartsItem:
        """z^(1/n) = r^(1/n)(cos((θ + 2πk)/n) + i sin((θ + 2πk)/n))"""
        formula_parts = [
            z, "^{\\frac{1}{", n, "}}", "=", r, "^{\\frac{1}{", n, "}}",
            "(\\cos(", "\\frac{", theta, "+2\\pi", k, "}{", n, "}",
            ")+i\\sin(", "\\frac{", theta, "+2\\pi", k, "}{", n, "}", ")"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def complex_logarithm(z="z", r="r", theta="\\theta", equal_index=3) -> FormulaPartsItem:
        """ln(z) = ln(r) + iθ"""
        formula_parts = [
            "\\ln(", z, ")", "=", "\\ln(", r, ")", "+", "i", theta
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def complex_exponential_periodic(z="z", equal_index=3) -> FormulaPartsItem:
        """e^(2πi) = 1"""
        formula_parts = [
            "e^{", "2\\pi i", "}", "=", "1"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def complex_trig_exponential(theta="\\theta", equal_index=3) -> FormulaPartsItem:
        """cos(θ) = (e^(iθ) + e^(-iθ))/2, sin(θ) = (e^(iθ) - e^(-iθ))/2i"""
        formula_parts = [
            "\\cos(", theta, ")", "=", "\\frac{", "e^{i", theta, "}+",
            "e^{-i", theta, "}", "}{2}", ",\\quad", "\\sin(", theta, ")", "=",
            "\\frac{", "e^{i", theta, "}-", "e^{-i", theta, "}", "}{2i}"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def complex_powers_i(equal_index=1) -> FormulaPartsItem:
        """i^n pattern: i, -1, -i, 1"""
        formula_parts = [
            "i^1", "&=", "i", "\\\\", "i^2", "&=", "-1", "\\\\",
            "i^3", "&=", "-i", "\\\\", "i^4", "&=", "1"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def complex_inverse_trig(z="z", equal_index=3) -> FormulaPartsItem:
        """arctan(z) = (i/2)ln((1-iz)/(1+iz))"""
        formula_parts = [
            "\\arctan(", z, ")", "=", "\\frac{i}{2}", "\\ln(",
            "\\frac{1-i", z, "}{1+i", z, "}"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def hyperbolic_exponential(x="x", equal_index=3) -> FormulaPartsItem:
        """cosh(x) = (e^x + e^(-x))/2, sinh(x) = (e^x - e^(-x))/2"""
        formula_parts = [
            "\\cosh(", x, ")", "=", "\\frac{", "e^{", x, "}+", "e^{-", x, "}}{2}",
            ",\\quad", "\\sinh(", x, ")", "=", "\\frac{", "e^{", x, "}-",
            "e^{-", x, "}}{2}"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def power_of_product_rule(x="x", y="y", n="n", equal_index=6):
        """(xy)^n = x^n * y^n"""
        formula_parts = [
            "(", x, y, ")", "^", n, "=", x, "^", n, "\\cdot", y, "^", n
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def difference_of_squares_rule(x="x", y="y", equal_index=10) -> FormulaPartsItem:
        """(x + y)(x - y) = x^2 - y^2"""
        formula_parts = [
            "(", x, "+", y, ")", "(", x, "-", y, ")", "=",
            x, "^2", "-", y, "^2"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def perfect_square_trinomial_rule(x="x", y="y", plus=True, equal_index=6) -> FormulaPartsItem:
        """(x ± y)^2 = x^2 ± 2xy + y^2"""
        sign = "+" if plus else "-"
        formula_parts = [
            "(", x, sign, y, ")", "^2", "=", x, "^2", sign,
            "2", x, y, "+", y, "^2"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def cube_expansion(x="x", y="y", plus=True, equal_index=6):
        """(x ± y)^3 = x^3 ± 3x^2y + 3xy^2 ± y^3"""
        sign = "+" if plus else "-"
        formula_parts = [
            "(", x, sign, y, ")", "^3", "=", x, "^3", sign,
            "3", x, "^2", y, "+", "3", x, y, "^2", sign, y, "^3"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def nested_radical(x="x") -> FormulaPartsItem:
        """√(√x) = ∜x"""
        formula_parts = [
            "\\sqrt{",  # 0
            "\\sqrt{",  # 1
            x,          # 2
            "}",        # 3
            "}",        # 4
            "=",        # 5
            "\\sqrt[4]{", # 6
            x,          # 7
            "}"         # 8
        ]
        return FormulaPartsItem(formula_parts, equal_index=5)

    @staticmethod
    def mixed_radical_rule(x="x", m="m", n="n") -> FormulaPartsItem:
        """x^(m/n) = ⁿ√(x^m) = (ⁿ√x)^m"""
        formula_parts = [
            x,          # 0
            "^{",       # 1
            f"\\frac{{{m}}}{{{n}}}", # 2
            "}",        # 3
            "=",        # 4
            f"\\sqrt[{n}]{{", # 5
            x,          # 6
            "^",        # 7
            m,          # 8
            "}",        # 9
            "=",        # 10
            "(",        # 11
            f"\\sqrt[{n}]{{", # 12
            x,          # 13
            "}}",       # 14
            ")",        # 15
            "^",        # 16
            m          # 17
        ]
        return FormulaPartsItem(formula_parts, equal_index=4)

    @staticmethod
    def radical_division_rule(x="x", y="y", n="n"):
        """ⁿ√(x/y) = ⁿ√x/ⁿ√y"""
        formula_parts = [
            f"\\sqrt[{n}]{{", # 0
            f"\\frac{{{x}}}{{{y}}}", # 1
            "}",        # 2
            "=",        # 3
            "\\frac{",  # 4
            f"\\sqrt[{n}]{{{x}}}", # 5
            "}{",      # 6
            f"\\sqrt[{n}]{{{y}}}", # 7
            "}"         # 8
        ]
        return FormulaPartsItem(formula_parts, equal_index=3)

    @staticmethod
    def factor_sum_cubes_rule(x="x", y="y"):
        """x³ + y³ = (x + y)(x² - xy + y²)"""
        formula_parts = [
            x,          # 0
            "^3",       # 1
            "+",        # 2
            y,          # 3
            "^3",       # 4
            "=",        # 5
            "(",        # 6
            x,          # 7
            "+",        # 8
            y,          # 9
            ")",        # 10
            "(",        # 11
            x,          # 12
            "^2",       # 13
            "-",        # 14
            x,          # 15
            y,          # 16
            "+",        # 17
            y,          # 18
            "^2",       # 19
            ")"         # 20
        ]
        return FormulaPartsItem(formula_parts, equal_index=5)

    @staticmethod
    def factor_difference_cubes_rule(x="x", y="y"):
        """x³ - y³ = (x - y)(x² + xy + y²)"""
        formula_parts = [
            x,          # 0
            "^3",       # 1
            "-",        # 2
            y,          # 3
            "^3",       # 4
            "=",        # 5
            "(",        # 6
            x,          # 7
            "-",        # 8
            y,          # 9
            ")",        # 10
            "(",        # 11
            x,          # 12
            "^2",       # 13
            "+",        # 14
            x,          # 15
            y,          # 16
            "+",        # 17
            y,          # 18
            "^2",       # 19
            ")"         # 20
        ]
        return FormulaPartsItem(formula_parts, equal_index=5)
    
    @staticmethod
    def log_product_rule(x="x", y="y", b="b"):
        """log_b(xy) = log_b(x) + log_b(y)"""
        formula_parts = [
            "\\log_{",  # 0
            b,          # 1
            "}(",       # 2
            x,          # 3
            y,          # 4
            ")",        # 5
            "=",        # 6
            "\\log_{",  # 7
            b,          # 8
            "}(",       # 9
            x,          # 10
            ")",        # 11
            "+",        # 12
            "\\log_{",  # 13
            b,          # 14
            "}(",       # 15
            y,          # 16
            ")"         # 17
        ]
        return FormulaPartsItem(formula_parts, equal_index=6)

    @staticmethod
    def log_quotient_rule(x="x", y="y", b="b"):
        """log_b(x/y) = log_b(x) - log_b(y)"""
        formula_parts = [
            "\\log_{",  # 0
            b,          # 1
            "}(",       # 2
            "\\frac{",  # 3
            x,          # 4
            "}{",       # 5
            y,          # 6
            "}",        # 7
            ")",        # 8
            "=",        # 9
            "\\log_{",  # 10
            b,          # 11
            "}(",       # 12
            x,          # 13
            ")",        # 14
            "-",        # 15
            "\\log_{",  # 16
            b,          # 17
            "}(",       # 18
            y,          # 19
            ")"         # 20
        ]
        return FormulaPartsItem(formula_parts, equal_index=9)

    @staticmethod
    def log_power_rule(x="x", n="n", b="b"):
        """log_b(x^n) = n·log_b(x)"""
        formula_parts = [
            "\\log_{",  # 0
            b,          # 1
            "}(",       # 2
            x,          # 3
            "^{",       # 4
            n,          # 5
            "}",        # 6
            ")",        # 7
            "=",        # 8
            n,          # 9
            "\\cdot",   # 10
            "\\log_{",  # 11
            b,          # 12
            "}(",       # 13
            x,          # 14
            ")"         # 15
        ]
        return FormulaPartsItem(formula_parts, equal_index=8)

    @staticmethod
    def log_base_change_rule(x="x", a="a", b="b"):
        """log_b(x) = log_a(x)/log_a(b)"""
        formula_parts = [
            "\\log_{",  # 0
            b,          # 1
            "}(",       # 2
            x,          # 3
            ")",        # 4
            "=",        # 5
            "\\frac{",  # 6
            "\\log_{",  # 7
            a,          # 8
            "}(",       # 9
            x,          # 10
            ")}",       # 11
            "{\\log_{", # 12
            a,          # 13
            "}(",       # 14
            b,          # 15
            ")}"        # 16
        ]
        return FormulaPartsItem(formula_parts, equal_index=5)

    @staticmethod
    def natural_log_definition(x="x"):
        """ln(x) = log_e(x)"""
        formula_parts = [
            "\\ln(",    # 0
            x,          # 1
            ")",        # 2
            "=",        # 3
            "\\log_{e}(", # 4
            x,          # 5
            ")"         # 6
        ]
        return FormulaPartsItem(formula_parts, equal_index=3)

    @staticmethod
    def log_exponential_rule(x="x", b="b"):
        """log_b(b^x) = x"""
        formula_parts = [
            "\\log_{",  # 0
            b,          # 1
            "}(",       # 2
            b,          # 3
            "^{",       # 4
            x,          # 5
            "}",        # 6
            ")",        # 7
            "=",        # 8
            x           # 9
        ]
        return FormulaPartsItem(formula_parts, equal_index=8)

    @staticmethod
    def exponential_log_rule(x="x", b="b"):
        """b^(log_b(x)) = x"""
        formula_parts = [
            b,          # 0
            "^{",       # 1
            "\\log_{",  # 2
            b,          # 3
            "}(",       # 4
            x,          # 5
            ")}",       # 6
            "=",        # 7
            x           # 8
        ]
        return FormulaPartsItem(formula_parts, equal_index=7)

    @staticmethod
    def ln_exponential_rule(x="x"):
        """ln(e^x) = x"""
        formula_parts = [
            "\\ln(",    # 0
            "e^{",      # 1
            x,          # 2
            "}",        # 3
            ")",        # 4
            "=",        # 5
            x           # 6
        ]
        return FormulaPartsItem(formula_parts, equal_index=5)

    @staticmethod
    def exponential_ln_rule(x="x"):
        """e^(ln(x)) = x"""
        formula_parts = [
            "e^{",      # 0
            "\\ln(",    # 1
            x,          # 2
            ")",        # 3
            "}",        # 4
            "=",        # 5
            x           # 6
        ]
        return FormulaPartsItem(formula_parts, equal_index=5)

    @staticmethod
    def log_zero_rule(b="b"):
        """log_b(1) = 0"""
        formula_parts = [
            "\\log_{",  # 0
            b,          # 1
            "}(",       # 2
            "1",        # 3
            ")",        # 4
            "=",        # 5
            "0"         # 6
        ]
        return FormulaPartsItem(formula_parts, equal_index=5)

    @staticmethod
    def log_one_rule(b="b"):
        """log_b(b) = 1"""
        formula_parts = [
            "\\log_{",  # 0
            b,          # 1
            "}(",       # 2
            b,          # 3
            ")",        # 4
            "=",        # 5
            "1"         # 6
        ]
        return FormulaPartsItem(formula_parts, equal_index=5)

    @staticmethod
    def log_reciprocal_rule(x="x", b="b"):
        """log_b(1/x) = -log_b(x)"""
        formula_parts = [
            "\\log_{",  # 0
            b,          # 1
            "}(",       # 2
            "\\frac{1}{", # 3
            x,          # 4
            "}",        # 5
            ")",        # 6
            "=",        # 7
            "-",        # 8
            "\\log_{",  # 9
            b,          # 10
            "}(",       # 11
            x,          # 12
            ")"         # 13
        ]
        return FormulaPartsItem(formula_parts, equal_index=7)

    @staticmethod
    def log_power_of_base(n="n", b="b"):
        """log_b(b^n) = n"""
        formula_parts = [
            "\\log_{",  # 0
            b,          # 1
            "}(",       # 2
            b,          # 3
            "^{",       # 4
            n,          # 5
            "}",        # 6
            ")",        # 7
            "=",        # 8
            n           # 9
        ]
        return FormulaPartsItem(formula_parts, equal_index=8)

    @staticmethod
    def log_exponential_base_change(x="x", a="a", b="b"):
        """b^x = a^(x·log_a(b))"""
        formula_parts = [
            b,          # 0
            "^{",       # 1
            x,          # 2
            "}",        # 3
            "=",        # 4
            a,          # 5
            "^{",       # 6
            x,          # 7
            "\\cdot",   # 8
            "\\log_{",  # 9
            a,          # 10
            "}(",       # 11
            b,          # 12
            ")",        # 13
            "}"         # 14
        ]
        return FormulaPartsItem(formula_parts, equal_index=4)   
    
    
    @staticmethod
    def pythagorean_identity(x="x"):
        """sin²(x) + cos²(x) = 1"""
        formula_parts = [
            "\\sin^2(",  # 0
            x,           # 1
            ")",         # 2
            "+",         # 3
            "\\cos^2(",  # 4
            x,           # 5
            ")",         # 6
            "=",         # 7
            "1"          # 8
        ]
        return FormulaPartsItem(formula_parts, equal_index=7)

    @staticmethod
    def reciprocal_identities(x="x"):
        """Basic reciprocal identities"""
        formula_parts = [
            "\\sin(",     # 0
            x,            # 1
            ")",          # 2
            "=",          # 3
            "\\frac{1}{", # 4
            "\\csc(",     # 5
            x,            # 6
            ")}",         # 7
            ",\\quad",    # 8
            "\\cos(",     # 9
            x,            # 10
            ")",          # 11
            "=",          # 12
            "\\frac{1}{", # 13
            "\\sec(",     # 14
            x,            # 15
            ")}",         # 16
            ",\\quad",    # 17
            "\\tan(",     # 18
            x,            # 19
            ")",          # 20
            "=",          # 21
            "\\frac{1}{", # 22
            "\\cot(",     # 23
            x,            # 24
            ")}"          # 25
        ]
        return FormulaPartsItem(formula_parts, equal_index=3)

    @staticmethod
    def quotient_identities(x="x"):
        """Basic quotient identities"""
        formula_parts = [
            "\\tan(",     # 0
            x,            # 1
            ")",          # 2
            "=",          # 3
            "\\frac{",    # 4
            "\\sin(",     # 5
            x,            # 6
            ")}{",        # 7
            "\\cos(",     # 8
            x,            # 9
            ")}",         # 10
            ",\\quad",    # 11
            "\\cot(",     # 12
            x,            # 13
            ")",          # 14
            "=",          # 15
            "\\frac{",    # 16
            "\\cos(",     # 17
            x,            # 18
            ")}{",        # 19
            "\\sin(",     # 20
            x,            # 21
            ")}"          # 22
        ]
        return FormulaPartsItem(formula_parts, equal_index=3)

    # Sum and Difference Formulas
    @staticmethod
    def sine_sum(x="x", y="y"):
        """sin(x + y) = sin(x)cos(y) + cos(x)sin(y)"""
        formula_parts = [
            "\\sin(",     # 0
            x,            # 1
            "+",          # 2
            y,            # 3
            ")",          # 4
            "=",          # 5
            "\\sin(",     # 6
            x,            # 7
            ")",          # 8
            "\\cos(",     # 9
            y,            # 10
            ")",          # 11
            "+",          # 12
            "\\cos(",     # 13
            x,            # 14
            ")",          # 15
            "\\sin(",     # 16
            y,            # 17
            ")"           # 18
        ]
        return FormulaPartsItem(formula_parts, equal_index=5)

    @staticmethod
    def sine_difference(x="x", y="y"):
        """sin(x - y) = sin(x)cos(y) - cos(x)sin(y)"""
        formula_parts = [
            "\\sin(",     # 0
            x,            # 1
            "-",          # 2
            y,            # 3
            ")",          # 4
            "=",          # 5
            "\\sin(",     # 6
            x,            # 7
            ")",          # 8
            "\\cos(",     # 9
            y,            # 10
            ")",          # 11
            "-",          # 12
            "\\cos(",     # 13
            x,            # 14
            ")",          # 15
            "\\sin(",     # 16
            y,            # 17
            ")"           # 18
        ]
        return FormulaPartsItem(formula_parts, equal_index=5)

    @staticmethod
    def cosine_sum(x="x", y="y"):
        """cos(x + y) = cos(x)cos(y) - sin(x)sin(y)"""
        formula_parts = [
            "\\cos(",     # 0
            x,            # 1
            "+",          # 2
            y,            # 3
            ")",          # 4
            "=",          # 5
            "\\cos(",     # 6
            x,            # 7
            ")",          # 8
            "\\cos(",     # 9
            y,            # 10
            ")",          # 11
            "-",          # 12
            "\\sin(",     # 13
            x,            # 14
            ")",          # 15
            "\\sin(",     # 16
            y,            # 17
            ")"           # 18
        ]
        return FormulaPartsItem(formula_parts, equal_index=5)

    @staticmethod
    def cosine_difference(x="x", y="y"):
        """cos(x - y) = cos(x)cos(y) + sin(x)sin(y)"""
        formula_parts = [
            "\\cos(",     # 0
            x,            # 1
            "-",          # 2
            y,            # 3
            ")",          # 4
            "=",          # 5
            "\\cos(",     # 6
            x,            # 7
            ")",          # 8
            "\\cos(",     # 9
            y,            # 10
            ")",          # 11
            "+",          # 12
            "\\sin(",     # 13
            x,            # 14
            ")",          # 15
            "\\sin(",     # 16
            y,            # 17
            ")"           # 18
        ]
        return FormulaPartsItem(formula_parts, equal_index=5)

    @staticmethod
    def tangent_sum(x="x", y="y"):
        """tan(x + y) = (tan(x) + tan(y))/(1 - tan(x)tan(y))"""
        formula_parts = [
            "\\tan(",     # 0
            x,            # 1
            "+",          # 2
            y,            # 3
            ")",          # 4
            "=",          # 5
            "\\frac{",    # 6
            "\\tan(",     # 7
            x,            # 8
            ")",          # 9
            "+",          # 10
            "\\tan(",     # 11
            y,            # 12
            ")}{",        # 13
            "1",          # 14
            "-",          # 15
            "\\tan(",     # 16
            x,            # 17
            ")",          # 18
            "\\tan(",     # 19
            y,            # 20
            ")}"          # 21
        ]
        return FormulaPartsItem(formula_parts, equal_index=5)

    @staticmethod
    def tangent_difference(x="x", y="y"):
        """tan(x - y) = (tan(x) - tan(y))/(1 + tan(x)tan(y))"""
        formula_parts = [
            "\\tan(",     # 0
            x,            # 1
            "-",          # 2
            y,            # 3
            ")",          # 4
            "=",          # 5
            "\\frac{",    # 6
            "\\tan(",     # 7
            x,            # 8
            ")",          # 9
            "-",          # 10
            "\\tan(",     # 11
            y,            # 12
            ")}{",        # 13
            "1",          # 14
            "+",          # 15
            "\\tan(",     # 16
            x,            # 17
            ")",          # 18
            "\\tan(",     # 19
            y,            # 20
            ")}"          # 21
        ]
        return FormulaPartsItem(formula_parts, equal_index=5)

    # Double Angle Formulas
    @staticmethod
    def double_angle_sine(x="x"):
        """sin(2x) = 2sin(x)cos(x)"""
        formula_parts = [
            "\\sin(",     # 0
            "2",          # 1
            x,            # 2
            ")",          # 3
            "=",          # 4
            "2",          # 5
            "\\sin(",     # 6
            x,            # 7
            ")",          # 8
            "\\cos(",     # 9
            x,            # 10
            ")"           # 11
        ]
        return FormulaPartsItem(formula_parts, equal_index=4)

    @staticmethod
    def double_angle_cosine_1(x="x"):
        """cos(2x) = cos²(x) - sin²(x)"""
        formula_parts = [
            "\\cos(",     # 0
            "2",          # 1
            x,            # 2
            ")",          # 3
            "=",          # 4
            "\\cos^2(",   # 5
            x,            # 6
            ")",          # 7
            "-",          # 8
            "\\sin^2(",   # 9
            x,            # 10
            ")"           # 11
        ]
        return FormulaPartsItem(formula_parts, equal_index=4)

    @staticmethod
    def double_angle_cosine_2(x="x"):
        """cos(2x) = 2cos²(x) - 1"""
        formula_parts = [
            "\\cos(",     # 0
            "2",          # 1
            x,            # 2
            ")",          # 3
            "=",          # 4
            "2",          # 5
            "\\cos^2(",   # 6
            x,            # 7
            ")",          # 8
            "-1"          # 9
        ]
        return FormulaPartsItem(formula_parts, equal_index=4)

    @staticmethod
    def double_angle_cosine_3(x="x"):
        """cos(2x) = 1 - 2sin²(x)"""
        formula_parts = [
            "\\cos(",     # 0
            "2",          # 1
            x,            # 2
            ")",          # 3
            "=",          # 4
            "1-2",        # 5
            "\\sin^2(",   # 6
            x,            # 7
            ")"           # 8
        ]
        return FormulaPartsItem(formula_parts, equal_index=4)

    # Half Angle Formulas
    @staticmethod
    def half_angle_sine(x="x"):
        """sin²(x/2) = (1-cos(x))/2"""
        formula_parts = [
            "\\sin^2(",   # 0
            "\\frac{",    # 1
            x,            # 2
            "}{2}",       # 3
            ")",          # 4
            "=",          # 5
            "\\frac{",    # 6
            "1-\\cos(",   # 7
            x,            # 8
            ")}{2}"       # 9
        ]
        return FormulaPartsItem(formula_parts, equal_index=5)

    @staticmethod
    def half_angle_cosine(x="x"):
        """cos²(x/2) = (1+cos(x))/2"""
        formula_parts = [
            "\\cos^2(",   # 0
            "\\frac{",    # 1
            x,            # 2
            "}{2}",       # 3
            ")",          # 4
            "=",          # 5
            "\\frac{",    # 6
            "1+\\cos(",   # 7
            x,            # 8
            ")}{2}"       # 9
        ]
        return FormulaPartsItem(formula_parts, equal_index=5)

    # Power Reduction Formulas
    @staticmethod
    def power_reduction_sine(x="x"):
        """sin²(x) = (1 - cos(2x))/2"""
        formula_parts = [
            "\\sin^2(",   # 0
            x,            # 1
            ")",          # 2
            "=",          # 3
            "\\frac{",    # 4
            "1-\\cos(",   # 5
            "2",          # 6
            x,            # 7
            ")}{2}"       # 8
        ]
        return FormulaPartsItem(formula_parts, equal_index=3)

    @staticmethod
    def power_reduction_cosine(x="x"):
        """cos²(x) = (1 + cos(2x))/2"""
        formula_parts = [
            "\\cos^2(",   # 0
            x,            # 1
            ")",          # 2
            "=",          # 3
            "\\frac{",    # 4
            "1+\\cos(",   # 5
            "2",          # 6
            x,            # 7
            ")}{2}"       # 8
        ]
        return FormulaPartsItem(formula_parts, equal_index=3)

    # Product-to-Sum Formulas
    @staticmethod
    def product_to_sum_sine(x="x", y="y"):
        """sin(x)sin(y) = (cos(x-y) - cos(x+y))/2"""
        formula_parts = [
            "\\sin(",     # 0
            x,            # 1
            ")",          # 2
            "\\sin(",     # 3
            y,            # 4
            ")",          # 5
            "=",          # 6
            "\\frac{",    # 7
            "\\cos(",     # 8
            x,            # 9
            "-",          # 10
            y,            # 11
            ")",          # 12
            "-",          # 13
            "\\cos(",     # 14
            x,            # 15
            "+",          # 16
            y,            # 17
            ")}{2}"       # 18
        ]
        return FormulaPartsItem(formula_parts, equal_index=6)
    
    @staticmethod
    def nested_radical(x="x"):
        """√(√x) = ∜x"""
        formula_parts = [
            "\\sqrt{",  # 0
            "\\sqrt{",  # 1
            x,          # 2
            "}",        # 3
            "}",        # 4
            "=",        # 5
            "\\sqrt[4]{", # 6
            x,          # 7
            "}"         # 8
        ]
        return FormulaPartsItem(formula_parts, equal_index=5)

    @staticmethod
    def mixed_radical_rule(x="x", m="m", n="n"):
        """x^(m/n) = ⁿ√(x^m) = (ⁿ√x)^m"""
        formula_parts = [
            x,          # 0
            "^{",       # 1
            f"\\frac{{{m}}}{{{n}}}", # 2
            "}",        # 3
            "=",        # 4
            f"\\sqrt[{n}]{{", # 5
            x,          # 6
            "^",        # 7
            m,          # 8
            "}",        # 9
            "=",        # 10
            "(",        # 11
            f"\\sqrt[{n}]{{", # 12
            x,          # 13
            "}}",       # 14
            ")",        # 15
            "^",        # 16
            m          # 17
        ]
        return FormulaPartsItem(formula_parts, equal_index=4)

    @staticmethod
    def radical_division_rule(x="x", y="y", n="n"):
        """ⁿ√(x/y) = ⁿ√x/ⁿ√y"""
        formula_parts = [
            f"\\sqrt[{n}]{{", # 0
            f"\\frac{{{x}}}{{{y}}}", # 1
            "}",        # 2
            "=",        # 3
            "\\frac{",  # 4
            f"\\sqrt[{n}]{{{x}}}", # 5
            "}{",      # 6
            f"\\sqrt[{n}]{{{y}}}", # 7
            "}"         # 8
        ]
        return FormulaPartsItem(formula_parts, equal_index=3)

    @staticmethod
    def factor_sum_cubes_rule(x="x", y="y"):
        """x³ + y³ = (x + y)(x² - xy + y²)"""
        formula_parts = [
            x,          # 0
            "^3",       # 1
            "+",        # 2
            y,          # 3
            "^3",       # 4
            "=",        # 5
            "(",        # 6
            x,          # 7
            "+",        # 8
            y,          # 9
            ")",        # 10
            "(",        # 11
            x,          # 12
            "^2",       # 13
            "-",        # 14
            x,          # 15
            y,          # 16
            "+",        # 17
            y,          # 18
            "^2",       # 19
            ")"         # 20
        ]
        return FormulaPartsItem(formula_parts, equal_index=5)

    @staticmethod
    def factor_difference_cubes_rule(x="x", y="y"):
        """x³ - y³ = (x - y)(x² + xy + y²)"""
        formula_parts = [
            x,          # 0
            "^3",       # 1
            "-",        # 2
            y,          # 3
            "^3",       # 4
            "=",        # 5
            "(",        # 6
            x,          # 7
            "-",        # 8
            y,          # 9
            ")",        # 10
            "(",        # 11
            x,          # 12
            "^2",       # 13
            "+",        # 14
            x,          # 15
            y,          # 16
            "+",        # 17
            y,          # 18
            "^2",       # 19
            ")"         # 20
        ]
        return FormulaPartsItem(formula_parts, equal_index=5)

    @staticmethod
    def cube_expansion(x="x", y="y", plus=True):
        """(x ± y)^3 = x^3 ± 3x^2y + 3xy^2 ± y^3"""
        sign = "+" if plus else "-"
        formula_parts = [
            "(",        # 0
            x,          # 1
            sign,       # 2
            y,          # 3
            ")",        # 4
            "^3",       # 5
            "=",        # 6
            x,          # 7
            "^3",       # 8
            sign,       # 9
            "3",        # 10
            x,          # 11
            "^2",       # 12
            y,          # 13
            "+",        # 14
            "3",        # 15
            x,          # 16
            y,          # 17
            "^2",       # 18
            sign,       # 19
            y,          # 20
            "^3"        # 21
        ]
        return FormulaPartsItem(formula_parts, equal_index=6)

    @staticmethod
    def radical_product_rule(x="x", y="y"):
        """√(xy) = √x * √y"""
        formula_parts = [
            "\\sqrt{",  # 0
            x,          # 1
            y,          # 2
            "}",        # 3
            "=",        # 4
            "\\sqrt{",  # 5
            x,          # 6
            "}",        # 7
            "\\sqrt{",  # 8
            y,          # 9
            "}"         # 10
        ]
        return FormulaPartsItem(formula_parts, equal_index=4)

    @staticmethod
    def quotient_rule(x="x", m="m", n="n"):
        """x^m/x^n = x^(m-n)"""
        formula_parts = [
            "\\frac{",  # 0
            x,          # 1
            "^",        # 2
            m,          # 3
            "}",        # 4
            "{",        # 5
            x,          # 6
            "^",        # 7
            n,          # 8
            "}",        # 9
            "=",        # 10
            x,          # 11
            "^",        # 12
            "{",        # 13
            m,          # 14
            "-",        # 15
            n,          # 16
            "}"         # 17
        ]
        return FormulaPartsItem(formula_parts, equal_index=10)
    
    @staticmethod
    def trig_ratio(func: str, numerator: str, denominator: str, angle: str = "\\theta", equal_index=3):
        formula_parts = [
            func,
            "(",
            angle,
            ")",
            "=",
            "\\frac{"+numerator+"}{"+denominator+"}"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod 
    def trig_ratio_value(func: str, numerator: str, denominator: str, value: str, angle: str = "\\theta", equal_index=3):
        formula_parts = [
            func,
            "(",
            angle,
            ")",
            "=",
            "\\frac{" + numerator + "}{" + denominator + "}",
            "=",
            value
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def trig_ratio_reciprocal(func: str, reciprocal_func: str, angle: str = "\\theta", equal_index=3):
        formula_parts = [
            func,
            "(",
            angle,
            ")",
            "=",
            "\\frac{1}{" + reciprocal_func + "(" + angle + ")}"
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def inverse_trig_basic(inverse_func: str, numerator: str, denominator: str, angle: str = "\\theta", equal_index=4):
        formula_parts = [
            inverse_func,
            "(",
            "\\frac{" + numerator + "}{" + denominator + "}",
            ")",
            "=",
            angle
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def inverse_trig_ratio(inverse_func: str, numerator: str, denominator: str, angle: str = "\\theta", equal_index=4):
        formula_parts = [
            inverse_func,
            "(",
            "\\frac{" + numerator + "}{" + denominator + "}",
            ")",
            "=",
            angle
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def inverse_trig_composition(func: str, inverse_func: str, angle: str = "x", equal_index=7):
        formula_parts = [
            inverse_func,
            "(",
            func + "(" + angle + ")",
            ")",
            "=",
            angle
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def inverse_trig_range(inverse_func: str, expression: str, lower_bound: str, upper_bound: str, angle: str = "\\theta", equal_index=4):
        formula_parts = [
            inverse_func,
            "(",
            expression,
            ")",
            "=",
            angle,
            ",\\quad " + lower_bound + " \\leq " + expression + " \\leq " + upper_bound
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def inverse_trig_double_angle(inverse_func: str, angle: str = "\\theta", equal_index=4):
        formula_parts = [
            inverse_func,
            "(2\\sin(" + angle + ")\\cos(" + angle + "))",
            "=",
            "2" + angle
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)
    
    @staticmethod
    def matrix_addition(matrix1="A", matrix2="B", result="C"):
        """Generate formula for matrix addition: A + B = C"""
        formula_parts = [
            matrix1,           # 0
            "+",              # 1
            matrix2,          # 2
            "=",             # 3
            result           # 4
        ]
        return FormulaPartsItem(formula_parts, equal_index=3)

    @staticmethod
    def matrix_multiplication(matrix1="A", matrix2="B", result="C"):
        """Generate formula for matrix multiplication: AB = C"""
        formula_parts = [
            matrix1,           # 0
            matrix2,          # 1
            "=",             # 2
            result           # 3
        ]
        return FormulaPartsItem(formula_parts, equal_index=2)

    @staticmethod
    def matrix_inverse(matrix="A"):
        """Generate formula for matrix inverse: AA^(-1) = I"""
        formula_parts = [
            matrix,           # 0
            matrix,          # 1
            "^{-1}",        # 2
            "=",            # 3
            "I"             # 4
        ]
        return FormulaPartsItem(formula_parts, equal_index=3)

    @staticmethod
    def matrix_determinant_property(matrix="A", matrix2="B"):
        """Generate formula for determinant property: det(AB) = det(A)det(B)"""
        formula_parts = [
            "\\det(",        # 0
            matrix,          # 1
            matrix2,         # 2
            ")",            # 3
            "=",            # 4
            "\\det(",       # 5
            matrix,         # 6
            ")",           # 7
            "\\det(",      # 8
            matrix2,       # 9
            ")"            # 10
        ]
        return FormulaPartsItem(formula_parts, equal_index=4)

    @staticmethod
    def matrix_transpose_property(matrix="A", matrix2="B"):
        """Generate formula for transpose property: (AB)^T = B^T A^T"""
        formula_parts = [
            "(",             # 0
            matrix,          # 1
            matrix2,         # 2
            ")",            # 3
            "^\\text{T}",   # 4
            "=",            # 5
            matrix2,         # 6
            "^\\text{T}",   # 7
            matrix,         # 8
            "^\\text{T}"    # 9
        ]
        return FormulaPartsItem(formula_parts, equal_index=5)

    @staticmethod
    def matrix_rank_inequality(matrix="A", m="m", n="n"):
        """Generate formula for rank inequality: rank(A) ≤ min(m,n)"""
        formula_parts = [
            "\\text{rank}(",  # 0
            matrix,           # 1
            ")",             # 2
            "\\leq",         # 3
            "\\min(",        # 4
            m,               # 5
            ",",             # 6
            n,               # 7
            ")"              # 8
        ]
        return FormulaPartsItem(formula_parts, equal_index=3)

    @staticmethod
    def characteristic_equation(matrix="A", lambda_var="\\lambda"):
        """Generate formula for characteristic equation: det(A - λI) = 0"""
        formula_parts = [
            "\\det(",        # 0
            matrix,          # 1
            "-",            # 2
            lambda_var,      # 3
            "I",            # 4
            ")",            # 5
            "=",            # 6
            "0"             # 7
        ]
        return FormulaPartsItem(formula_parts, equal_index=6)

    @staticmethod
    def matrix_trace_property(matrix1="A", matrix2="B"):
        """Generate formula for trace property: tr(AB) = tr(BA)"""
        formula_parts = [
            "\\text{tr}(",   # 0
            matrix1,         # 1
            matrix2,         # 2
            ")",            # 3
            "=",            # 4
            "\\text{tr}(",   # 5
            matrix2,         # 6
            matrix1,         # 7
            ")"             # 8
        ]
        return FormulaPartsItem(formula_parts, equal_index=4)

    @staticmethod
    def matrix_similarity(matrix1="A", matrix2="B", matrix3="P"):
        """Generate formula for matrix similarity: B = P^(-1)AP"""
        formula_parts = [
            matrix2,         # 0
            "=",            # 1
            matrix3,         # 2
            "^{-1}",       # 3
            matrix1,        # 4
            matrix3         # 5
        ]
        return FormulaPartsItem(formula_parts, equal_index=1)
    
    @staticmethod
    def power_rule(var="x", n="n"):
        """Generate power rule formula: d/dx(x^n) = nx^(n-1)"""
        formula_parts = [
            "\\frac{d}{dx}",  # 0
            "(",              # 1
            var,              # 2
            "^{",            # 3
            n,               # 4
            "}",             # 5
            ")",             # 6
            "=",             # 7
            n,               # 8
            var,             # 9
            "^{",            # 10
            n,               # 11
            "-1",            # 12
            "}"              # 13
        ]
        return FormulaPartsItem(formula_parts, equal_index=7)

    @staticmethod
    def chain_rule(f="f", g="g", x="x"):
        """Generate chain rule formula: d/dx(f(g(x))) = f'(g(x))g'(x)"""
        formula_parts = [
            "\\frac{d}{dx}",  # 0
            f"({f}(",         # 1
            g,                # 2
            f"({x})))",       # 3
            "=",              # 4
            f"{f}'(",         # 5
            g,                # 6
            f"({x}))",        # 7
            "\\cdot",         # 8
            f"{g}'(",         # 9
            x,                # 10
            ")"               # 11
        ]
        return FormulaPartsItem(formula_parts, equal_index=4)



    @staticmethod
    def fundamental_theorem_calculus(f="f", a="a", b="b", x="x"):
        """Generate Fundamental Theorem of Calculus"""
        formula_parts = [
            "\\int_{",        # 0
            a,                # 1
            "}^{",           # 2
            b,                # 3
            "}",             # 4
            f"{f}'({x})",     # 5
            "\\,d{x}",       # 6
            "=",             # 7
            f"{f}({b})",      # 8
            "-",             # 9
            f"{f}({a})"      # 10
        ]
        return FormulaPartsItem(formula_parts, equal_index=7)

    @staticmethod
    def substitution_rule(u="u", x="x"):
        """Generate integration by substitution formula"""
        formula_parts = [
            "\\int",          # 0
            f"f({u})",        # 1
            "\\frac{d{u}}{d{x}}", # 2
            "\\,d{x}",       # 3
            "=",             # 4
            "\\int",         # 5
            f"f({u})",        # 6
            "\\,d{u}"        # 7
        ]
        return FormulaPartsItem(formula_parts, equal_index=4)

    @staticmethod
    def integration_by_parts(u="u", v="v", x="x"):
        """Generate integration by parts formula"""
        formula_parts = [
            "\\int",          # 0
            f"{u}",           # 1
            "\\,d",           # 2
            f"{v}",           # 3
            "=",              # 4
            f"{u}{v}",        # 5
            "-",              # 6
            "\\int",          # 7
            f"{v}",           # 8
            "\\,d",           # 9
            f"{u}"            # 10
        ]
        return FormulaPartsItem(formula_parts, equal_index=4)
    
    @staticmethod
    def linear_system_matrix_form(coefficients, variables, rhs):
        """
        Generate matrix form of a system of linear equations: Ax = b
        
        Args:
            coefficients: 2D list of coefficients
            variables: List of variable names
            rhs: List of right-hand side values
        """
        formula_parts = [
            "\\begin{pmatrix}",  # 0
            " \\\\ ".join([" & ".join(map(str, row)) for row in coefficients]), # 1
            "\\end{pmatrix}",    # 2
            "\\begin{pmatrix}",  # 3
            " \\\\ ".join(variables), # 4
            "\\end{pmatrix}",    # 5
            "=",                 # 6
            "\\begin{pmatrix}",  # 7
            " \\\\ ".join(map(str, rhs)), # 8
            "\\end{pmatrix}"     # 9
        ]
        return FormulaPartsItem(formula_parts, equal_index=6)

    @staticmethod
    def system_solution(variables, values):
        """Generate solution format for system of equations."""
        formula_parts = [
            "\\begin{cases}",    # 0
            " \\\\ ".join([f"{var} = {val}" for var, val in zip(variables, values)]), # 1
            "\\end{cases}"       # 2
        ]
        return FormulaPartsItem(formula_parts, equal_index=None)

    def chain_equals(self, parts):
        # Join the parts with equals signs
        return " = ".join(parts)
     
    # Add to FormulaPartsFactory class

    @staticmethod 
    def derivative_sum_rule(u="u", v="v", equal_index=5):
        """Generate derivative sum rule: d/dx(u + v) = d/dx(u) + d/dx(v)"""
        formula_parts = [
        "\\frac{d}{dx}",  # 0
        "(",              # 1
        u,                # 2
        "+",              # 3
        v,                # 4
        ")=",            # 5
        "\\frac{d}{dx}", # 6
        u,               # 7
        "+",             # 8
        "\\frac{d}{dx}", # 9
            v                # 10
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def derivative_product_rule(u="u", v="v", equal_index=5):
        """Generate product rule: d/dx(uv) = u(dv/dx) + v(du/dx)"""
        formula_parts = [
            "\\frac{d}{dx}",  # 0
            "(",              # 1
            u,                # 2
            v,                # 3
            ")",              # 4
            "=",              # 5
            u,                # 6
            "\\frac{d}{dx}", # 7
            v,                # 8
            "+",              # 9
            v,                # 10
            "\\frac{d}{dx}", # 11
            u                 # 12
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def derivative_quotient_rule(u="u", v="v", equal_index=7):
        """Generate quotient rule: d/dx(u/v) = (v(du/dx) - u(dv/dx))/v^2"""
        formula_parts = [
            "\\frac{d}{dx}",  # 0
            "\\frac{",        # 1
            u,                # 2
            "}{",             # 3
            v,                # 4
            "}",              # 5
            "=",              # 6
            "\\frac{",        # 7
            v,                # 8
            "\\frac{d}{dx}", # 9
            u,                # 10
            "-",              # 11
            u,                # 12
            "\\frac{d}{dx}", # 13
            v,                # 14
            "}{",             # 15
            v,                # 16
            "^2",             # 17
            "}"               # 18
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def derivative_chain_rule(f="f", g="g", x="x", equal_index=5):
        """Generate chain rule: d/dx(f(g(x))) = f'(g(x))g'(x)"""
        formula_parts = [
            "\\frac{d}{dx}",  # 0
            f"({f}(",         # 1
            g,                # 2
            f"({x})))",       # 3
            "=",              # 4
            f"{f}'(",         # 5
            g,                # 6
            f"({x}))",        # 7
            "\\cdot",         # 8
            f"{g}'(",         # 9
            x,                # 10
            ")"               # 11
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def derivative_exponential_rule(a="a", x="x", equal_index=5):
        """Generate exponential rule: d/dx(a^x) = a^x ln(a)"""
        formula_parts = [
        "\\frac{d}{dx}",  # 0
        "(",              # 1
        a,                # 2
        "^{",             # 3
        x,                # 4
        "})",             # 5
        "=",              # 6
        a,                # 7
        "^{",             # 8
        x,                # 9
        "}",              # 10
        "\\ln(",          # 11
        a,                # 12
        ")"               # 13
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def derivative_log_rule(x="x", base="b", equal_index=5):
        """Generate logarithm rule: d/dx(log_b(x)) = 1/(x ln(b))"""
        formula_parts = [
        "\\frac{d}{dx}",  # 0
        "\\log_{",        # 1
        base,             # 2
        "}(",             # 3
        x,                # 4
        ")",              # 5
        "=",              # 6
        "\\frac{1}{",     # 7
        x,                # 8
        "\\ln(",          # 9
        base,             # 10
            ")}"              # 11
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def implicit_differentiation(y="y", x="x", equal_index=5):
        """Generate implicit differentiation notation: dy/dx"""
        formula_parts = [
        "\\frac{d",       # 0
        y,                # 1
        "}{d",            # 2
        x,                # 3
            "}"               # 4
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)     
    
    
    #Separated sum angle formulas
    @staticmethod
    def sum_angle_sine(x="\\alpha", y="\\beta", equal_index=5):
        """Generate sum formula for sine: sin(A+B) = sin(A)cos(B) + cos(A)sin(B)"""
        formula_parts = [
        "\\sin(",     # 0
        x,            # 1
        "+",          # 2
        y,            # 3
        ")",          # 4
        "=",          # 5
        "\\sin(",     # 6
        x,            # 7
        ")",          # 8
        "\\cos(",     # 9
        y,            # 10
        ")",          # 11
        "+",          # 12
        "\\cos(",     # 13
        x,            # 14
        ")",          # 15
        "\\sin(",     # 16
        y,            # 17
        ")"           # 18
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def sum_angle_cosine(x="\\alpha", y="\\beta", equal_index=5):
        """Generate sum formula for cosine: cos(A+B) = cos(A)cos(B) - sin(A)sin(B)"""
        formula_parts = [
            "\\cos(",     # 0
        x,            # 1
        "+",          # 2
        y,            # 3
        ")",          # 4
        "=",          # 5
        "\\cos(",     # 6
        x,            # 7
        ")",          # 8
        "\\cos(",     # 9
        y,            # 10
        ")",          # 11
        "-",          # 12
        "\\sin(",     # 13
        x,            # 14
        ")",          # 15
        "\\sin(",     # 16
        y,            # 17
        ")"           # 18
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def difference_angle_sine(x="\\alpha", y="\\beta", equal_index=5):
        """Generate difference formula for sine: sin(A-B) = sin(A)cos(B) - cos(A)sin(B)"""
        formula_parts = [
        "\\sin(",     # 0
        x,            # 1
        "-",          # 2
        y,            # 3
        ")",          # 4
        "=",          # 5
        "\\sin(",     # 6
        x,            # 7
        ")",          # 8
        "\\cos(",     # 9
        y,            # 10
        ")",          # 11
        "-",          # 12
        "\\cos(",     # 13
        x,            # 14
        ")",          # 15
        "\\sin(",     # 16
        y,            # 17
        ")"           # 18
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)

    @staticmethod
    def difference_angle_cosine(x="\\alpha", y="\\beta", equal_index=5):
        """Generate difference formula for cosine: cos(A-B) = cos(A)cos(B) + sin(A)sin(B)"""
        formula_parts = [
            "\\cos(",     # 0
            x,            # 1
            "-",          # 2
            y,            # 3
            ")",          # 4
            "=",          # 5
            "\\cos(",     # 6
            x,            # 7
            ")",          # 8
            "\\cos(",     # 9
            y,            # 10
            ")",          # 11
            "+",          # 12
            "\\sin(",     # 13
            x,            # 14
            ")",          # 15
            "\\sin(",     # 16
            y,            # 17
            ")"           # 18
        ]
        return FormulaPartsItem(formula_parts, equal_index=equal_index)