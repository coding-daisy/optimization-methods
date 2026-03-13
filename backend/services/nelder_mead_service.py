from objective_functions import FUNCTIONS
from optimizers.nelder_mead.simplexes_computation import get_nelder_mead_simplexes
from services.grid_service import compute_grid
from objective_functions.function_factory import create_function

def run_nelder_mead(req):

    error_messages = []


    # GETTING THE FUNCTION

    if req.function_name != "custom":
        function = FUNCTIONS[req.function_name]
    else:
        # getting the custom function ! :D
        custom_tuple = create_function(req.custom_function)
        function = custom_tuple[0]
        error_messages = error_messages + ([] if (custom_tuple[1] == None) else [custom_tuple[1]])
        
    

    # FINISHED GETTING THE FUNCTION - THERE MIGHT BE ERRORS


    if error_messages:
        return {
            "error_messages": error_messages
        }
        

    search_space = (
        (req.min_x, req.max_x),
        (req.min_y, req.max_y)
    )

    simplexes = get_nelder_mead_simplexes(
        function,
        search_space,
        req.alpha,
        req.beta,
        req.gamma,
        req.max_iter,
        req.delta,
        req.penalty_function, 
        req.penalty_strength
    )

    frames = []

    for simplex in simplexes:
        frames.append({
            "x": [p[0] for p in simplex] + [simplex[0][0]],
            "y": [p[1] for p in simplex] + [simplex[0][1]]
        })

    
    # compute visualization surface
    grid = compute_grid(req, function)
    # passing in function separetely, since we might have custom one

    search_rectangle = [
        (req.min_x, req.min_y),
        (req.max_x, req.min_y),
        (req.max_x, req.max_y),
        (req.min_x, req.max_y),
        (req.min_x, req.min_y)
    ]
    
    plot_range = {
        "x": (min(grid["x"]), max(grid["x"])),
        "y": (min(grid["y"]), max(grid["y"]))
    }
    

    return {
        "optimizer": "nelder_mead",
        "frames": frames,
        "grid": grid,
        "search_rectangle": search_rectangle,
        "plot_range": plot_range
    }
    # frontend apparently can't read numpy arrays !

    # don't forget to add search rectangle !!!

    