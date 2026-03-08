from fastapi import APIRouter

from models.optimization_request import OptimizationRequest
from services.nelder_mead_service import run_nelder_mead

router = APIRouter()


@router.post("/nelder_mead")
def nelder_mead_endpoint(req: OptimizationRequest):
    return run_nelder_mead(req)