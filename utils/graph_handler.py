import sympy as sp
from d2.explicit import plot_explicit_2d
from d2.implicit import plot_implicit_2d
from d2.parametric import plot_parametric_2d
from d3.cartesian import plot_explicit_3d

def determine_equation_type(equation):
    x, y, z = sp.symbols('x y z')
    lhs, rhs = equation.lhs, equation.rhs
    
    # Check for 3D equation
    if str(equation).find('z') != -1:
        return "3d_explicit"
    
    # Rest of the 2D checks
    if str(equation).find('y**') != -1:
        return "implicit"
    
    if lhs == y and not rhs.has(y):
        return "explicit"
    if rhs == y and not lhs.has(y):
        return "explicit"
    if lhs == x and not rhs.has(x):
        return "explicit"
    if rhs == x and not lhs.has(x):
        return "explicit"
    
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
        return plot_explicit_3d(equation, range_values, color)
    
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

