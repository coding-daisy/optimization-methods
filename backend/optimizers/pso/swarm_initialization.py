import random
from optimizers.pso.point_class import PSO_Point
from optimizers.evaluation_with_penalty import evaluate_with_penalty

def initialize_swarm(swarm_size, search_space, function, penalty, penalty_strength, speed_range):


    swarm = {
        "best_fitness": float("inf"),
        "best_location": None,
        "points": []
    }

    (min_x, max_x), (min_y, max_y) = search_space

    for _ in range(swarm_size):
        # create individual points here !

        
        # points!
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)

        location = [x, y]

        # speed
        speed = [
            random.uniform(speed_range[0], speed_range[1]),
            random.uniform(speed_range[0], speed_range[1])
        ]

        fitness = evaluate_with_penalty(
            location, function, penalty, penalty_strength, search_space
        )

        point = PSO_Point(
            location = location,
            speed = speed,
            best_fitness = fitness,
            best_fitness_location = location
        )

        swarm["points"].append(point)

        # global values update
        if fitness <= swarm["best_fitness"]:
            swarm["best_fitness"] = fitness
            swarm["best_location"] = location
    
    return swarm
