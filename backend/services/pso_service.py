from objective_functions import FUNCTIONS
from services.grid_service import compute_grid
from objective_functions.function_factory import create_function

from optimizers.pso.swarm_initialization import initialize_swarm
from optimizers.pso.points_movements import get_points_and_movement

def run_pso(req):

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

    # no special stopping conditions yet !

    initial_points = initialize_swarm(
        req.swarm_size, search_space, function, req.penalty_function, req.penalty_strength, [req.init_max_speed, req.init_max_speed]
    )

    current_swarm = initial_points

    all_swarms = []
    all_swarms.append(initial_points)

    for _ in range(req.max_iter):
        current_swarm = get_points_and_movement(function, current_swarm, req.w, req.c_ind, req.c_grp, req.penalty_function, req.penalty_strength, search_space, req.max_speed)
        all_swarms.append(current_swarm)


    frames = []

    for swarm in all_swarms:

        points_list = []

        for point in swarm["points"]:
            points_list.append({
                "x": point.location[0],
                "y": point.location[1],
                "speed_x": point.speed[0],
                "speed_y": point.speed[1]
            })
        frames.append(points_list)


    
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
        "optimizer": "pso",
        "frames": frames,
        "grid": grid,
        "search_rectangle": search_rectangle,
        "plot_range": plot_range
    }

    