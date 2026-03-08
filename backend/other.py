from fastapi import FastAPI
import numpy as np
from pydantic import BaseModel
from objective_functions import FUNCTIONS
from optimizers.nelder_mead.optimizer import nelder_mead


app = FastAPI()

def function_scaled(X, Y, function, plot_scaling):
    Z = function((X, Y))
    if (not plot_scaling):
        return Z
    if (plot_scaling == "log"):
        return np.log(Z - Z.min() + 1)

class OptimizationRequest(BaseModel):
    function_name: str = "himmelblau"

    min_x: float = -5
    min_y: float = -5
    max_x: float = 5
    max_y: float = 5
    margin_ratio: float = 0.2

    max_iter: int = 20
    alpha: float = 1
    beta: float =2
    gamma: float = 0.5
    goal_delta: float = 1e-6
    
    plot_scaling: str = "log"

@app.post("/nelder_mead")
def run_optimizer(req: OptimizationRequest):

    function = FUNCTIONS[req.function_name]

    search_space = (
        (req.min_x, req.max_x),
        (req.min_y, req.max_y)
    )

    simplexes = nelder_mead(
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
    
    margin = max(abs(a - b) for a, b in search_space) * req.margin_ratio

    x = np.linspace(req.min_x - margin, req.max_x + margin, 100)
    y = np.linspace(req.min_y - margin, req.max_y + margin, 100)

    X, Y = np.meshgrid(x, y)

    Z = function_scaled(X, Y, function, req.plot_scaling)

    return {
        "frames": frames, 
        "grid": {
            "x": x.tolist(),
            "y": y.tolist(),
            "z": Z.tolist()
        }
        }
    

