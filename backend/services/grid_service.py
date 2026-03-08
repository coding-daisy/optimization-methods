import numpy as np
from objective_functions import FUNCTIONS

def function_scaled(X, Y, function, plot_scaling):
    Z = function((X, Y))
    if not plot_scaling:
        return Z
    if (plot_scaling == "log"):
        return np.log(Z - Z.min() + 1)
    return Z

def compute_grid(req):

    function = FUNCTIONS[req.function_name]

    search_space = (
        (req.min_x, req.max_x),
        (req.min_y, req.max_y)
    )

    margin = max(abs(a - b) for a, b in search_space) * req.margin_ratio

    x = np.linspace(req.min_x - margin, req.max_x + margin, 100)
    y = np.linspace(req.min_y - margin, req.max_y + margin, 100)

    X, Y = np.meshgrid(x, y)

    Z = function_scaled(X, Y, function, req.plot_scaling)

    return {
        "x": x.tolist(),
        "y": y.tolist(),
        "z": Z.tolist()
    }




