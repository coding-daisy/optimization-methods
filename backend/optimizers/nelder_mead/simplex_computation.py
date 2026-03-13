import numpy as np
from optimizers.evaluation_with_penalty import evaluate_with_penalty

def simplex_computation(function, current_simplex, alpha, beta, gamma, penalty, penalty_strength, search_space):

    # function_wp is function with penalty

    point_value = [[v, evaluate_with_penalty(v, function, penalty, penalty_strength, search_space)] for v in current_simplex]
    # apparently tuples are immutable in python!

    point_value.sort(key = lambda x: x[1])


    centroid = np.mean([p[0] for p in point_value[:-1]], axis = 0) # axis = 0 means: collapsing vertically

    reflected_point = reflected(alpha, centroid, point_value[-1][0])
    reflected_value = evaluate_with_penalty(reflected_point, function, penalty, penalty_strength, search_space)

    if (reflected_value < point_value[0][1]):
        expanded_point = extended(beta, centroid, reflected_point)
        expanded_value = evaluate_with_penalty(expanded_point, function, penalty, penalty_strength, search_space)
        if (expanded_value < reflected_value):
            point_value[-1] = [expanded_point, expanded_value]
        else:
            point_value[-1] = [reflected_point, reflected_value]
        return [p[0] for p in point_value]

    # is reflection better than the second-worst?
    if (reflected_value < point_value[-2][1]):
        point_value[-1] = [reflected_point, reflected_value]
        return [p[0] for p in point_value]
    

    # is reflection better than worst?
    if (reflected_value < point_value[-1][1]):
        point_value[-1] = [reflected_point, reflected_value]
    
    contracted_point = contracted(gamma, centroid, point_value[-1][0])
    contracted_value = evaluate_with_penalty(contracted_point, function, penalty, penalty_strength, search_space)

    if (contracted_value < point_value[-1][1]):
        point_value[-1] = [contracted_point, contracted_value]
        return [p[0] for p in point_value]

    
    shrinkage(point_value)
    # post: values aren't correct
    return [p[0] for p in point_value]


def reflected(alpha, centroid, worst_point):
    return centroid + alpha * (centroid - worst_point)

def extended(beta, centroid, reflected_point):
    return centroid + beta * (reflected_point - centroid)

def contracted(gamma, centroid, worst_point):
    return centroid + gamma * (worst_point - centroid)

def shrinkage(point_value):
    best_point = point_value[0][0]
    for i in range(1, len(point_value)):
        point_value[i][0] = 0.5 * (point_value[i][0] + best_point)
        # no need to update value: won't be needing that anymore



