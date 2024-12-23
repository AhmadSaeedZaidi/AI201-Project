from utils.math_functions import is_explicit_form
from d2.explicit import plot_explicit_2d
from d2.implicit import plot_implicit_2d
from d2.parametric import plot_parametric_2d
from d3.cartesian import plot_explicit_3d

def handle_graph(equation, range_values, color='blue', plot_type='2d'):
    print(f"Equation type: {plot_type}")
    
    if plot_type == '2d':
        lhs_expr, rhs_expr = equation.lhs, equation.rhs
        if is_explicit_form(lhs_expr, rhs_expr):
            return plot_explicit_2d(equation, range_values, color)
        else:
            return plot_implicit_2d(equation, range_values, color)
    elif plot_type == 'parametric':
        return plot_parametric_2d(equation, range_values, color)
    elif plot_type == '3d':
        return plot_explicit_3d(equation, range_values, color)
    else:
        raise ValueError(f"Invalid plot type: {plot_type}")

