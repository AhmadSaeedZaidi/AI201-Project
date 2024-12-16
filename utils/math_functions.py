import sympy as sp

def process_math_functions(input_str):
    print(f"Processing function: {input_str}")
    
    x = sp.Symbol('x')
    
    if input_str == 'sin(x)':
        return str(sp.sin(x))
    elif input_str == 'cos(x)':
        return str(sp.cos(x))
    elif input_str == 'tan(x)':
        return str(sp.tan(x))
    elif input_str == 'e^x':
        return str(sp.exp(x))
    elif input_str == 'e^sin(x)':
        return str(sp.exp(sp.sin(x)))
    elif input_str == 'ln(x)':
        return str(sp.log(x))
    
    return input_str