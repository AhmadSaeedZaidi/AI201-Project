from d2.explicit import plot_explicit_2d
from d2.implicit import plot_implicit_2d
from d2.parametric import plot_parametric_2d
from d3.explicit.planes import plot_plane
from d3.implicit.implicit_plot import plot_implicit_surface
from d3.parametric.curves import plot_parametric_curve_3d
from d3.parametric.surfaces import plot_parametric_surface
import sympy as sp


def is_explicit_or_implicit(equation):
    """
    Determines whether the given equation is explicit or implicit.

    Args:
        equation (sympy.Eq): The standardized equation object.

    Returns:
        str: 'explicit' if the equation is explicit, 'implicit' otherwise.
    """
    if equation.is_Equality:
        free_symbols = equation.free_symbols
        x, y = sp.Symbol('x'), sp.Symbol('y')

        if x in free_symbols and y in free_symbols:
            solutions = sp.solve(equation, y, dict=False)

            if all(sol.has(x) for sol in solutions):
                if len(solutions) == 1:
                    return 'explicit'  
                else:
                    return 'implicit'  

        z = sp.Symbol('z')
        if z in free_symbols and len(free_symbols) == 3:
            return 'implicit'  
    return 'unsupported'


def handle_graph(equation, range_value, color_clicks):
    color = 'blue' if (color_clicks or 0) % 2 == 0 else 'red'

    if equation.is_Equality:
        eq_type = is_explicit_or_implicit(equation)

        if eq_type == 'explicit':
            return plot_explicit_2d(equation, range_value, color)
        
        elif eq_type == 'implicit':
            if sp.Symbol('z') in equation.free_symbols:
                return plot_implicit_surface(equation, range_value, color)
            return plot_implicit_2d(equation, range_value, color)

    elif isinstance(equation, tuple):
        if len(equation) == 2:
            return plot_parametric_2d(equation, range_value, color)
        elif len(equation) == 3:
            return plot_parametric_curve_3d(equation, range_value, color)

    raise ValueError("Unsupported equation type.")

