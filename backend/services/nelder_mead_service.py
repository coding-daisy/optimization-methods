from objective_functions import FUNCTIONS
from optimizers.nelder_mead.simplexes_computation import get_nelder_mead_simplexes
from services.grid_service import compute_grid

def run_nelder_mead(req):
    function = FUNCTIONS[req.function_name]

    search_space = (
        (req.min_x, req.max_x),
        (req.min_y, req.max_y)
    )

    simplexes = get_nelder_mead_simplexes(
        function,
        search_space,
        alpha = req.alpha,
        beta = req.beta,
        gamma = req.gamma,
        max_iter = req.max_iter,
        goal_delta = req.goal_delta
    )

    frames = []

    for simplex in simplexes:
        frames.append({
            "x": [p[0] for p in simplex] + [simplex[0][0]],
            "y": [p[1] for p in simplex] + [simplex[0][1]]
        })

    
    # compute visualization surface
    grid = compute_grid(req)
    

    return {
        "optimizer": "nelder_mead",
        "frames": frames,
        "grid": grid
    }
    # frontend apparently can't read numpy arrays !

    # don't forget to add search rectangle !!!

    