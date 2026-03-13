from objective_functions import FUNCTIONS
from services.grid_service import compute_grid
from objective_functions.function_factory import create_function
from optimizers.simulated_annealing.p_function import get_p_function
from optimizers.simulated_annealing.initialization import get_init_situation
from optimizers.simulated_annealing.next_situation_logic import get_next_situation


def run_sa(req):

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


    # GET THE PROBABILITY FUNCTION

    p_function = get_p_function(req.p_function)


    # no special stopping conditions yet !

    initial_sit = get_init_situation(
        function, search_space, req.init_temperature, req.penalty_function, req.penalty_strength
    )

    all_sit = []
    all_sit.append(initial_sit)

    current_sit = initial_sit

    while (current_sit.temperature - req.temperature_decrease >= 0):
        next_sit = get_next_situation(function, current_sit, req.temperature_decrease, p_function, req.speed_range, search_space, req.penalty_function, req.penalty_strength)
        all_sit.append(next_sit)
        current_sit = next_sit



    frames = []

    for situation in all_sit:

        frame = {
            "x": situation.position[0],
            "y": situation.position[1],
            "tmp": situation.temperature

        }

        frames.append(frame)


    
    # compute visualization surface
    grid = compute_grid(req, function)
    # passing in function separately, since we might have custom one

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
        "optimizer": "sa",
        "frames": frames,
        "grid": grid,
        "search_rectangle": search_rectangle,
        "plot_range": plot_range
    }
