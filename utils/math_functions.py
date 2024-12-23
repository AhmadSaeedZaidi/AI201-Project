import re
import sympy as sp

def process_math_functions(expr_str):
    # Handle coefficient multiplication for variables and functions
    expr_str = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr_str)  # 2x -> 2*x
    expr_str = re.sub(r'(\d)(sin|cos|tan|log|exp|sqrt)', r'\1*\2', expr_str)  # 2sin -> 2*sin
    
    # Handle e^x
    expr_str = re.sub(r'e\^(.*)', r'exp(\1)', expr_str)
    
    # Handle sqrt
    expr_str = re.sub(r'sqrt\((.*?)\)', r'sqrt(\1)', expr_str)
    
    return expr_str

def is_explicit_form(lhs_expr, rhs_expr):
    """Check if equation is in form y = f(x)"""
    y = sp.Symbol('y')
    
    # Only explicit if y is by itself on one side
    if lhs_expr == y and not rhs_expr.has(y):
        return True
    if rhs_expr == y and not lhs_expr.has(y):
        return True
    return False