import re
import sympy as sp
from utils.math_functions import process_math_functions

def is_explicit_form(lhs_expr, rhs_expr):
    """Check if equation is in form y = f(x)"""
    y = sp.Symbol('y')
    
    # Only explicit if y is by itself on one side
    if lhs_expr == y and not rhs_expr.has(y):
        return True
    if rhs_expr == y and not lhs_expr.has(y):
        return True
    return False

def preprocess_input(equation_str, dimension='2d'):
    print(f"1. Input received: {equation_str}")
    
    equation_str = equation_str.replace(' ', '')
    print(f"2. After basic preprocessing: {equation_str}")
    
    if ',' in equation_str:  # Parametric form
        x_eq, y_eq = equation_str.split(',')
        x_expr = sp.sympify(process_math_functions(x_eq))
        y_expr = sp.sympify(process_math_functions(y_eq))
        return (x_expr, y_expr), None, "parametric"
    
    equation_str = process_math_functions(equation_str)
    print(f"3. After function processing: {equation_str}")
    
    if '=' not in equation_str:
        # Choose default variable based on dimension
        lhs = 'z' if dimension == '3d' else 'y'
        rhs = equation_str
    else:
        lhs, rhs = equation_str.split('=')
    print(f"4. Before sympify - lhs: {lhs}, rhs: {rhs}")
    
    equation = sp.Eq(sp.sympify(lhs), sp.sympify(rhs))
    print(f"5. After sympify - lhs: {equation.lhs}, rhs: {equation.rhs}")
    
    return equation

def process_math_functions(expr_str):
    # Handle coefficient multiplication for variables and functions
    expr_str = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr_str)  # 2x -> 2*x
    expr_str = re.sub(r'(\d)(sin|cos|tan|log|exp|sqrt)', r'\1*\2', expr_str)  # 2sin -> 2*sin
    
    expr_str = expr_str.replace('^', '**')
    
    return expr_str
