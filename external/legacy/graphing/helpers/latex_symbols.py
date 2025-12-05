
class LatexSymbols:
    # Relational Operators
    LESS_THAN = "<"
    GREATER_THAN = ">"
    LESS_THAN_OR_EQUAL_TO = "\\leq"
    GREATER_THAN_OR_EQUAL_TO = "\\geq"
    EQUALS = "="
    NOT_EQUALS = "\\neq"

    # Arrows
    RIGHT_ARROW = "\\rightarrow"
    LEFT_ARROW = "\\leftarrow"
    UP_ARROW = "\\uparrow"
    DOWN_ARROW = "\\downarrow"
    DOUBLE_ARROW = "\\leftrightarrow"
    IMPLIES = "\\implies"
    IF_AND_ONLY_IF = "\\iff"

    # Mathematical Symbols
    PLUS = "+"
    MINUS = "-"
    MULTIPLICATION = "\\times"
    DIVISION = "\\div"
    FRACTION = "\\frac"
    SQUARE_ROOT = "\\sqrt"
    ABSOLUTE_VALUE = ("\\left|", "\\right|")  # Tuple for opening and closing delimiters
    INFINITY = "\\infty"
    PI = "\\pi"
    I = "i"
    APPROXIMATELY_EQUAL_TO = "\\approx"
    PROPORTIONAL_TO = "\\propto"
    DEGREES = "\\degree"    

    # Logic Symbols
    FOR_ALL = "\\forall"
    EXISTS = "\\exists"
    NOT = "\\neg"
    AND = "\\wedge"
    OR = "\\vee"

    # Set Notation
    SUBSET = "\\subset"
    SUBSET_OR_EQUAL = "\\subseteq"
    SUPERSET = "\\supset"
    SUPERSET_OR_EQUAL = "\\supseteq"
    UNION = "\\cup"
    INTERSECTION = "\\cap"
    ELEMENT_OF = "\\in"
    NOT_ELEMENT_OF = "\\notin"

    # Miscellaneous
    DOTS = "\\dots"
    THEREFORE = "\\therefore"
    BECAUSE = "\\because"
    QUAD = "\\quad"
    CURLY_BRACES = ("\\left\\{", "\\right\\}")  # Auto-sizing curly braces

    # Additional Mathematical Notation
    OVERLINE = "\\overline"
    OVERBRACE = "\\overbrace"   
    UNDERBRACE = "\\underbrace" 
    TRIANGLE = "\\triangle"
    DOT_PRODUCT = "\\cdot"
    THETA = "\\theta"
    OMEGA = "\\omega"
    COS = "\\cos"
    SIN = "\\sin"
    ANGLE = "\\angle"
    PARALLEL = "\\parallel"
    PERPENDICULAR = "\\perp"
    
    VECTOR = "\\vec"
    UNIT_VECTOR = "\\hat"
    CROSS_PRODUCT = "\\times"
    PERP_VECTOR = "\\perp"  
    
    # Add inverse trig symbols to existing LatexSymbols
    ARCSIN = "\\arcsin"
    ARCCOS = "\\arccos"
    ARCTAN = "\\arctan"
    ARCSEC = "\\text{arcsec}"  # Not standard LaTeX commands
    ARCCSC = "\\text{arccsc}"
    ARCCOT = "\\text{arccot}"
    
    # Additional Mathematical Notation
    CUBE_ROOT = "\\sqrt[3]{"
    NTH_ROOT = "\\sqrt[n]{"
    
    # Greek Letters
    ALPHA = "\\alpha"
    BETA = "\\beta"
    GAMMA = "\\gamma"
    DELTA = "\\delta"
    THETA = "\\theta"
    LAMBDA = "\\lambda"
    PI = "\\pi"
    SIGMA = "\\sigma"
    PHI = "\\phi"
    RHO = "\\rho"
    
    
    # Complex Numbers
    IMAGINARY_UNIT = "i"
    REAL_PART = "\\text{Re}"
    IMAGINARY_PART = "\\text{Im}"
    COMPLEX_CONJUGATE = "\\overline"
    EULERS_CONSTANT = "e"
    
    
     # Matrix-related symbols
    MATRIX_LEFT_BRACKET = "\\left["
    MATRIX_RIGHT_BRACKET = "\\right]"
    MATRIX_LEFT_PAREN = "\\left("
    MATRIX_RIGHT_PAREN = "\\right)"
    MATRIX_LEFT_BRACE = "\\left\\{"
    MATRIX_RIGHT_BRACE = "\\right\\}"
    MATRIX_LEFT_VERT = "\\left|"
    MATRIX_RIGHT_VERT = "\\right|"
    MATRIX_DOUBLE_VERT = "\\|"
    MATRIX_COLUMN_SEPARATOR = "&"
    MATRIX_ROW_SEPARATOR = "\\\\"
    DETERMINANT = "\\det"
    TRANSPOSE = "^\\text{T}"
    INVERSE = "^{-1}"
    TRACE = "\\text{tr}"
    RANK = "\\text{rank}"
    
    # Calculus symbols
    DERIVATIVE = "\\frac{d}{dx}"
    PARTIAL_DERIVATIVE = "\\frac{\\partial}{\\partial #1}"
    INTEGRAL = "\\int"
    DOUBLE_INTEGRAL = "\\iint"
    TRIPLE_INTEGRAL = "\\iiint"
    LINE_INTEGRAL = "\\oint"
    SURFACE_INTEGRAL = "\\oiint"
    VOLUME_INTEGRAL = "\\oiiint"
    INFINITY = "\\infty"
    LIMIT = "\\lim"
    SUMMATION = "\\sum"
    PRODUCT = "\\prod"
    DIFFERENTIAL = "\\,dx"
    PARTIAL = "\\partial"
    DELTA = "\\Delta"
    NABLA = "\\nabla"
    
    
    # Trigonometric Functions
    SEC = "\\sec"
    CSC = "\\csc"
    COT = "\\cot"
    
    # Mathematical Sets
    REAL_NUMBERS = "\\mathbb{R}"
    COMPLEX_NUMBERS = "\\mathbb{C}"
    INTEGERS = "\\mathbb{Z}"
    NATURAL_NUMBERS = "\\mathbb{N}"
    RATIONAL_NUMBERS = "\\mathbb{Q}"
    
    # Common Mathematical Structures
    MATRIX_CELL_SEPARATOR = "&"
    MATRIX_ROW_SEPARATOR = "\\\\"
    MATRIX_ALIGNMENT = "\\begin{align*}"
    END_ALIGNMENT = "\\end{align*}"
    
    # Common Operations
    COMPOSITION = "\\circ"
    TENSOR_PRODUCT = "\\otimes"
    DIRECT_SUM = "\\oplus"
    DIRECT_PRODUCT = "\\times"
    
    # Integration Symbols
    CLOSED_INTEGRAL = "\\oint"
    SURFACE_INTEGRAL = "\\iint"
    VOLUME_INTEGRAL = "\\iiint"
    
    # Differential Operators
    PARTIAL_DIFFERENTIAL = "\\partial"
    NABLA = "\\nabla"
    DEL = "\\nabla"
    LAPLACIAN = "\\Delta"
    
    # Function Spaces
    MAPSTO = "\\mapsto"
    FUNCTION_ARROW = "\\to"
    SURJECTION = "\\twoheadrightarrow"
    INJECTION = "\\hookrightarrow"
    BIJECTION = "\\leftrightarrow"
    
    
