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

def preprocess_input(equation_str):
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
        # For 3D mode, default to z = expression
        lhs = 'z'
        rhs = equation_str
    else:
        lhs, rhs = equation_str.split('=')
    print(f"4. Before sympify - lhs: {lhs}, rhs: {rhs}")
    
    equation = sp.Eq(sp.sympify(lhs), sp.sympify(rhs))
    print(f"5. After sympify - lhs: {equation.lhs}, rhs: {equation.rhs}")
    
    return equation
