from fastapi import APIRouter, Depends
from app.models.dify import PromptRequest, PromptResponse
from app.service.dify import DifyService
from app.dependencies import get_dify_service

router = APIRouter(prefix="/prompt", tags=["prompt"])


@router.post("/optimize", response_model=PromptResponse)
async def optimize_prompt(
    request: PromptRequest,
    service: DifyService = Depends(get_dify_service),
) -> PromptResponse:
    """优化给定的 Prompt"""
    return await service.optimize_prompt(request)
