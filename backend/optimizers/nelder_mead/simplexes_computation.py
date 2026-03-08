from optimizers.nelder_mead.simplex_computation import simplex_computation
import numpy as np


def random_simplex(search_space):
    # n-dimensional -> n+1 points
    
    simplex = []

    for _ in range(len(search_space) + 1):

        # duplicates are very unlikely !

        point = np.array([
            np.random.uniform(low, high)
            for (low, high) in search_space
        ])

        simplex.append(point)

    return simplex
    



def get_nelder_mead_simplexes(function, search_space, alpha=1, beta=2, gamma=0.5,
                max_iter=10, goal_delta=1e-6):

    initial_simplex = random_simplex(search_space)

    current_simplex = initial_simplex

    simplexes = []
    simplexes.append(current_simplex)

    for i in range(max_iter):

        current_simplex = simplex_computation(function, current_simplex, alpha, beta, gamma, penalty =  "squared distance", penalty_strength = 10, search_space = search_space)

        simplexes.append(current_simplex)

        # the simplex itself should never be changed - we keep the same reference

        values = [function(p) for p in current_simplex]

        # we stop when best - worst < delta
        
        current_delta = max(values) - min(values)
        if current_delta <= goal_delta:
            break

    
    return simplexes