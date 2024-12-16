import sympy as sp
from d2.explicit import plot_explicit_2d
from d2.implicit import plot_implicit_2d
from d2.parametric import plot_parametric_2d

def determine_equation_type(equation):
    x, y = sp.symbols('x y')
    lhs, rhs = equation.lhs, equation.rhs
    
    # First check if y appears with any power
    if isinstance(lhs, sp.Pow) and lhs.base == y:
        return "implicit"
    if isinstance(rhs, sp.Pow) and rhs.base == y:
        return "implicit"
    
    # Then check normal explicit cases
    if lhs == y and not rhs.has(y):
        return "explicit"
    if rhs == y and not lhs.has(y):
        return "explicit"
    if lhs == x and not rhs.has(x):
        return "explicit"
    if rhs == x and not lhs.has(x):
        return "explicit"
    
    # If y appears in any other way that's not just y by itself
    if (lhs.has(y) and lhs != y) or (rhs.has(y) and rhs != y):
        return "implicit"
    
    try:
        solved = sp.solve(equation, y)
        if len(solved) == 1 and not solved[0].has(y):
            return "explicit"
    except:
        pass
        
    try:
        solved = sp.solve(equation, x)
        if len(solved) == 1 and not solved[0].has(x):
            return "explicit"
    except:
        pass
    
    return "implicit"

def handle_graph(equation, range_values, color='blue', dimension='2d'):
    if dimension == '3d':
        raise NotImplementedError("3D plotting not yet implemented")
    
    if dimension == '2d_parametric':
        return plot_parametric_2d(equation, range_values, color)
    
    eq_type = determine_equation_type(equation)
    print(f"Equation type: {eq_type}")
    
    if eq_type == "explicit":
        try:
            solved = sp.solve(equation, sp.Symbol('y'))
            if len(solved) == 1:
                equation = sp.Eq(sp.Symbol('y'), solved[0])
        except:
            pass
        return plot_explicit_2d(equation, range_values, color)
    else:
        return plot_implicit_2d(equation, range_values, color)

