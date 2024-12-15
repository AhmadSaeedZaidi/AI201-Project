import re
import sympy as sp
from utils.math_functions import process_math_functions

def preprocess_input(input_str):
    print(f"1. Input received: {input_str}")
    input_str = input_str.strip()
    input_str = input_str.replace('^', '**')
    input_str = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', input_str)
    print(f"2. After basic preprocessing: {input_str}")
    
    if '=' not in input_str:
        input_str = process_math_functions(input_str)
        print(f"3. After function processing: {input_str}")
        lhs, rhs = 'y', input_str
    else:
        lhs, rhs = input_str.split('=')
        rhs = process_math_functions(rhs)
    
    print(f"4. Before sympify - lhs: {lhs}, rhs: {rhs}")
    lhs_expr = sp.sympify(lhs.strip())
    rhs_expr = sp.sympify(rhs.strip())
    print(f"5. After sympify - lhs: {lhs_expr}, rhs: {rhs_expr}")
    
    return sp.Eq(lhs_expr, rhs_expr)
