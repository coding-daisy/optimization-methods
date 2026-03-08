from pydantic import BaseModel
from typing import Literal


class OptimizationRequest(BaseModel):
    function_name: str = "himmelblau"
    custom_function: str = ""

    min_x: float = -5
    min_y: float = -5
    max_x: float = 5
    max_y: float = 5
    margin_ratio: float = 0.2

    max_iter: int = 20
    alpha: float = 1
    beta: float = 2
    gamma: float = 0.5
    delta: float = 1e-6
    
    plot_scaling: Literal["logarithmic", "linear"] = "linear"
        # Literal is something like Enum -> fixed values



