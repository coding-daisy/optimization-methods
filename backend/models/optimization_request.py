from pydantic import BaseModel
from typing import Literal


class BaseOptimizationRequest(BaseModel):

    optimization_method: str = "nelder_mead"

    function_name: str = "himmelblau"
    custom_function: str = ""

    min_x: float = -5
    min_y: float = -5
    max_x: float = 5
    max_y: float = 5
    margin_ratio: float = 0.2

    penalty_function: Literal["none", "linear", "squared distance"] = "linear"
    penalty_strength: float = 1

    max_iter: int = 20
    
    plot_scaling: Literal["logarithmic", "linear"] = "linear"
        # Literal is something like Enum -> fixed values


class NelderMeadRequest(BaseOptimizationRequest):
    alpha: float = 1
    beta: float = 2
    gamma: float = 0.5
    delta: float = 1e-6


class PSORequest(BaseOptimizationRequest):

    w: float = 0.7
    c_ind: float = 1.5
    c_grp: float = 1.5
    swarm_size: int = 30
    init_max_speed: float = 1
    max_speed: float = 2

class SARequest(BaseOptimizationRequest):

    init_temperature: float = 10
    p_function: str = "Boltzmann"
    speed_range: float = 1
    temperature_decrease: float = 0.05