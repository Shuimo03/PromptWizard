from fastapi import Request
from app.service.dify import DifyService
from typing import AsyncGenerator


async def get_dify_service(request: Request) -> AsyncGenerator[DifyService, None]:
    """获取 DifyService 实例"""
    service = request.app.state.dify_service
    yield service