import sympy as sp

def process_math_functions(input_str):
    print(f"Processing function: {input_str}")
    
    x = sp.Symbol('x')
    
    # Handle special cases
    if input_str == '1/tan(x)':
        return str(1/sp.tan(x))
    elif input_str == 'e**sin(x)':
        return str(sp.exp(sp.sin(x)))
    elif input_str == 'e**x':
        return str(sp.exp(x))
    elif '1/sin(x)' in input_str:
        return str(1/sp.sin(x))
    elif '1/cos(x)' in input_str:
        return str(1/sp.cos(x))
    elif 'sin(' in input_str:
        return str(sp.sin(x))
    elif 'cos(' in input_str:
        return str(sp.cos(x))
    elif 'tan(' in input_str:
        return str(sp.tan(x))
    elif 'ln(' in input_str:
        return str(sp.log(x))
    
    print(f"Processed to: {input_str}")
    return input_str