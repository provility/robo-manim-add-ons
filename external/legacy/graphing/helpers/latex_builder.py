from graphing.helpers.latex_symbols import LatexSymbols

"""
When you are building long Latex expressions use LatexBuilder.
if you just need a simple equation, use LatexGenerator.
LatexBuilder is a fluent interface for chaining parts of a Latex expressions together.
"""
class LatexBuilder:
   
    def __init__(self):
        self.current_expression = []
        self._environment_stack = []

    # Basic Building Methods
    def append(self, text) -> 'LatexBuilder':
        """Add text to current expression."""
        self.current_expression.append(str(text))
        return self

    # Operators
    def equals(self) -> 'LatexBuilder':
        return self.append(LatexSymbols.EQUALS)
    
    def approx(self)-> 'LatexBuilder':
        return self.append(LatexSymbols.APPROXIMATELY_EQUAL_TO)
    
    def proportional_to(self)-> 'LatexBuilder':
        return self.append(LatexSymbols.PROPORTIONAL_TO)    
    
    def plus(self) -> 'LatexBuilder':
        return self.append(LatexSymbols.PLUS)
    
    def minus(self) -> 'LatexBuilder': 
        return self.append(LatexSymbols.MINUS)
    
    def multiply(self) -> 'LatexBuilder': 
        return self.append(LatexSymbols.MULTIPLICATION)
    

    def cdot(self) -> 'LatexBuilder': 
        return self.append(LatexSymbols.DOT_PRODUCT)
    
    def cross_product(self)->'LatexBuilder': 
        return self.append(LatexSymbols.CROSS_PRODUCT)
    
    def divide(self) -> 'LatexBuilder': 
        return self.append(LatexSymbols.DIVISION)
    
    
    # relational operators
    def less_than(self) -> 'LatexBuilder': 
        return self.append(LatexSymbols.LESS_THAN)
    def less_than_equal(self) -> 'LatexBuilder': 
        return self.append(LatexSymbols.LESS_THAN_OR_EQUAL_TO)
    def greater_than(self) -> 'LatexBuilder': 
        return self.append(LatexSymbols.GREATER_THAN)
    def greater_than_equal(self) -> 'LatexBuilder': 
        return self.append(LatexSymbols.GREATER_THAN_OR_EQUAL_TO)
    def not_equal(self) -> 'LatexBuilder': 
        return self.append(LatexSymbols.NOT_EQUALS)
    def implies(self) -> 'LatexBuilder': 
        return self.append(LatexSymbols.IMPLIES)
    def if_and_only_if(self) -> 'LatexBuilder':
        return self.append(LatexSymbols.IF_AND_ONLY_IF)
    
    # Arrow Operators
    def right_arrow(self) -> 'LatexBuilder':
        return self.append(LatexSymbols.RIGHT_ARROW)
    def left_arrow(self) -> 'LatexBuilder':
        return self.append(LatexSymbols.LEFT_ARROW)
    def up_arrow(self) -> 'LatexBuilder':
        return self.append(LatexSymbols.UP_ARROW)
    def down_arrow(self) -> 'LatexBuilder':
        return self.append(LatexSymbols.DOWN_ARROW)
    def double_arrow(self) -> 'LatexBuilder':
        return self.append(LatexSymbols.DOUBLE_ARROW)
    
    
     # Set Notation
    def subset(self) -> 'LatexBuilder':
        """Append the subset symbol to the current expression."""
        return self.append(LatexSymbols.SUBSET)

    def subset_or_equal(self) -> 'LatexBuilder':
        """Append the subset or equal symbol to the current expression."""
        return self.append(LatexSymbols.SUBSET_OR_EQUAL)

    def superset(self) -> 'LatexBuilder':
        """Append the superset symbol to the current expression."""
        return self.append(LatexSymbols.SUPERSET)

    def superset_or_equal(self) -> 'LatexBuilder':
        """Append the superset or equal symbol to the current expression."""
        return self.append(LatexSymbols.SUPERSET_OR_EQUAL)

    def union(self) -> 'LatexBuilder':
        """Append the union symbol to the current expression."""
        return self.append(LatexSymbols.UNION)

    def intersection(self) -> 'LatexBuilder':
        """Append the intersection symbol to the current expression."""
        return self.append(LatexSymbols.INTERSECTION)

    def element_of(self) -> 'LatexBuilder':
        """Append the element of symbol to the current expression."""
        return self.append(LatexSymbols.ELEMENT_OF)

    def not_element_of(self) -> 'LatexBuilder':
        """Append the not element of symbol to the current expression."""
        return self.append(LatexSymbols.NOT_ELEMENT_OF)
    
    def perpendicular(self)-> 'LatexBuilder':
        return self.append(LatexSymbols.PERPENDICULAR)
    
    def parallel(self)-> 'LatexBuilder':
        return self.append(LatexSymbols.PARALLEL)
        
        
    
    def and_symbol(self) -> 'LatexBuilder':
        """Append the logical 'and' symbol to the current expression."""
        return self.append(LatexSymbols.AND)

    def or_symbol(self) -> 'LatexBuilder':
        """Append the logical 'or' symbol to the current expression."""
        return self.append(LatexSymbols.OR)

    def logical_and(self) -> 'LatexBuilder':
        """Append the logical 'and' symbol to the current expression."""
        return self.append(LatexSymbols.LOGICAL_AND)

    def logical_or(self) -> 'LatexBuilder':
        """Append the logical 'or' symbol to the current expression."""
        return self.append(LatexSymbols.LOGICAL_OR)

    # Building and Clearing
    def build(self) -> str:
        """Build and return the complete LaTeX expression."""
        while self._environment_stack:
            self.end_environment()
        return " ".join(map(str, self.current_expression))

    def clear(self) -> 'LatexBuilder':
        """Clear the current expression."""
        self.current_expression = []
        self._environment_stack = []
        return self

   
     # Environment Methods
    def begin_environment(self, env_name) -> 'LatexBuilder':
        """Start a LaTeX environment."""
        self._environment_stack.append(env_name)
        return self.append(f"\\begin{{{env_name}}}")

    def end_environment(self) -> 'LatexBuilder':
        """End the most recent environment."""
        if self._environment_stack:
            env = self._environment_stack.pop()
            return self.append(f"\\end{{{env}}}")
        return self

    def in_equation(self, inline=False) -> 'LatexBuilder':
        """Context manager for equation environment."""
        if inline:
            return self.append("$")
        return self.begin_environment("equation*")

    # Complex Expression Builders
    def build_equation_system(self, equations) -> 'LatexBuilder':
        """Build a system of equations."""
        self.begin_environment("cases")
        for eq in equations:
            self.append(eq).new_line()
        return self.end_environment()

    def build_theorem(self, name, statement) -> 'LatexBuilder':
        """Build a theorem environment."""
        return (self
            .begin_environment("theorem")
            .append(f"[{name}]")
            .append(statement)
            .end_environment())
        
    
