
import random
from optimizers.pso.point_class import PSO_Point
from optimizers.evaluation_with_penalty import evaluate_with_penalty
import numpy as np
    # for working with positions as lists !

def get_points_and_movement(function, current_swarm, w, c_ind, c_grp, penalty, penalty_strength, search_space, max_speed):
    
    # per swarm: store best fitness & point

    # per point: store best fitness & point

    swarm_fitness = current_swarm["best_fitness"]
    swarm_location_np = np.array(current_swarm["best_location"])


    new_swarm = {}

    new_swarm["best_fitness"] = swarm_fitness
    new_swarm["best_location"] = swarm_location_np.tolist()
    new_swarm["points"] = []

    for point in current_swarm["points"]:

        best_fitness = point.best_fitness
        best_location = point.best_fitness_location
        best_location_np = np.array(point.best_fitness_location)

        speed = np.array(point.speed)
        location = np.array(point.location)

        R1 = np.array([random.random(), random.random()])
        R2 = np.array([random.random(), random.random()])

        new_speed_np = w * speed + c_ind * R1 * (best_location_np - location) + c_grp * R2 * (swarm_location_np - location)
        # clamp velocity
        new_speed_np = np.clip(new_speed_np, -max_speed, max_speed)
        new_speed = new_speed_np.tolist()
        new_location = (location + new_speed_np).tolist()
        new_fitness = evaluate_with_penalty(new_location, function, penalty, penalty_strength, search_space);

        if new_fitness <= best_fitness:
            best_fitness = new_fitness
            best_location = new_location
            # we aren't updating best_location_np -> not used anymore
        
        if new_fitness <= new_swarm["best_fitness"]:
            new_swarm["best_fitness"] = new_fitness
            new_swarm["best_location"] = new_location

        new_point = PSO_Point(
            location = new_location,
            speed = new_speed,
            best_fitness = best_fitness,
            best_fitness_location = best_location
        )
        
        new_swarm["points"].append(new_point)
            
    return new_swarm