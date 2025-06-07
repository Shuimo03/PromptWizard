from pydantic import BaseModel
from typing import Dict, Optional, Any

class PromptRequest(BaseModel):
    background: str
    role: str
    expectation: str

class DifyData(BaseModel):
    id: str
    workflow_id: str
    status: str
    outputs: Dict[str, Any]  # 改为 Dict 因为输出格式可能变化
    error: Optional[str] = None
    elapsed_time: Optional[float] = None
    total_tokens: Optional[int] = None
    total_steps: int = 0
    created_at: int
    finished_at: int

class DifyResponse(BaseModel):
    workflow_run_id: str
    task_id: str
    data: DifyData

class PromptResponse(BaseModel):
    optimized_prompt: str
    suggestions: Optional[str] = None

    @classmethod
    def from_dify_response(cls, dify_response: DifyResponse) -> "PromptResponse":
        """从 Dify 响应创建 PromptResponse"""
        # 从 outputs 中获取响应文本
        response_text = dify_response.data.outputs.get("response", "")
        
        return cls(
            optimized_prompt=response_text,
            suggestions=None
        )