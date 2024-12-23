import re
import sympy as sp
from utils.math_functions import process_math_functions

def preprocess_input(equation_str, plot_type='2d'):
    print(f"1. Input received: {equation_str}")
    
    equation_str = equation_str.replace(' ', '')
    print(f"2. After basic preprocessing: {equation_str}")
    
    equation_str = process_math_functions(equation_str)
    print(f"3. After function processing: {equation_str}")
    
    if '=' in equation_str:
        lhs, rhs = equation_str.split('=')
    else:
        if plot_type == '3d':
            lhs = 'z'
        else:
            lhs = 'y'
        rhs = equation_str
    
    z = sp.Symbol('z')
    y = sp.Symbol('y')
    lhs_expr = z if lhs.strip() == 'z' else (y if lhs.strip() == 'y' else sp.sympify(lhs))
    rhs_expr = sp.sympify(rhs)
    print(f"5. After sympify - lhs: {lhs_expr}, rhs: {rhs_expr}")
    
    equation = sp.Eq(lhs_expr, rhs_expr)
    
    if plot_type == 'parametric':
        x_expr, y_expr = equation.lhs, equation.rhs
        return (x_expr, y_expr)
    else:
        return equation
