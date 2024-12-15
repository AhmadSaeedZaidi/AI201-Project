from d2.explicit import plot_explicit_2d
from d2.implicit import plot_implicit_2d
from d2.parametric import plot_parametric_2d
from d3.explicit.planes import plot_plane
from d3.implicit.implicit_plot import plot_implicit_surface
from d3.parametric.curves import plot_parametric_curve_3d
from d3.parametric.surfaces import plot_parametric_surface
import sympy as sp


def is_explicit_or_implicit(equation):
    if equation.is_Equality:
        free_symbols = equation.free_symbols
        x, y = sp.Symbol('x'), sp.Symbol('y')

        if equation.lhs == y or equation.rhs == y:
            return 'explicit'
        
        if x in free_symbols and y in free_symbols:
            solutions = sp.solve(equation, y, dict=False)
            if all(sol.has(x) for sol in solutions):
                if len(solutions) == 1:
                    return 'explicit'  
                else:
                    return 'implicit'  
    return 'unsupported'


def handle_graph(equation, range_value, color, is_3d):
    if is_3d:
        if isinstance(equation, tuple):
            return plot_parametric_curve_3d(equation, range_value, color)
        return plot_implicit_surface(equation, range_value, color)
    
    if isinstance(equation, tuple):
        return plot_parametric_2d(equation, range_value, color)
    
    eq_type = is_explicit_or_implicit(equation)
    print(f"Equation type: {eq_type}")
    
    if eq_type == 'explicit':
        return plot_explicit_2d(equation, range_value, color)
    elif eq_type == 'implicit':
        return plot_implicit_2d(equation, range_value, color)
    
    raise ValueError("Unsupported equation type.")

