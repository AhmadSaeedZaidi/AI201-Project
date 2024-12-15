import sympy as sp
from d2.explicit import plot_explicit_2d
from d2.implicit import plot_implicit_2d

def determine_equation_type(equation):
    x, y = sp.symbols('x y')
    lhs, rhs = equation.lhs, equation.rhs
    
    # Check for explicit forms
    if lhs == y and not rhs.has(y):  # y = f(x)
        return "explicit"
    if rhs == y and not lhs.has(y):  # f(x) = y
        return "explicit"
    if lhs == x and not rhs.has(x):  # x = f(y)
        return "explicit"
    if rhs == x and not lhs.has(x):  # f(y) = x
        return "explicit"
        
    # If equation can be rearranged to y = f(x)
    try:
        solved = sp.solve(equation, y)
        if len(solved) == 1 and not solved[0].has(y):
            return "explicit"
    except:
        pass
        
    # If equation can be rearranged to x = f(y)
    try:
        solved = sp.solve(equation, x)
        if len(solved) == 1 and not solved[0].has(x):
            return "explicit"
    except:
        pass
    
    return "implicit"

def handle_graph(equation, range_values, color='blue', is_3d=False):
    if is_3d:
        raise NotImplementedError("3D plotting not yet implemented")
    
    eq_type = determine_equation_type(equation)
    print(f"Equation type: {eq_type}")
    
    
    if eq_type == "explicit":
        # Try to solve for y if possible
        try:
            solved = sp.solve(equation, sp.Symbol('y'))
            if len(solved) == 1:
                equation = sp.Eq(sp.Symbol('y'), solved[0])
        except:
            pass
        return plot_explicit_2d(equation, range_values, color)
    else:
        return plot_implicit_2d(equation, range_values, color)

