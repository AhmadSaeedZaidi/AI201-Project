import re
import sympy as sp

def preprocess_input(input_str):
    input_str = input_str.replace('^', '**')
    input_str = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', input_str)

    try:
        if '=' in input_str:
            lhs, rhs = input_str.split('=')
        else:
            lhs, rhs = input_str, '0'

        lhs_expr = sp.sympify(lhs.strip())
        rhs_expr = sp.sympify(rhs.strip())

        return sp.Eq(lhs_expr, rhs_expr)

    except Exception as e:
        raise ValueError(f"Error processing input equation: {e}")
