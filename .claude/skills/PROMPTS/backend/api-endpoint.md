# 后端 API 开发 Prompt 模板

面向当前 `PromptWizard/backend` 仓库，默认目录是 `app/models/`、`app/service/`、`app/routers/`。

## 1. 新增或修改接口

~~~~markdown
# 角色
你是 PromptWizard 的后端工程师，需要遵循当前仓库现状。

# 仓库上下文
- 项目路径：`/Users/mac/PromptWizard/backend`
- 路由目录：`app/routers/`
- 模型目录：`app/models/`
- 服务目录：`app/service/`
- 当前依赖：FastAPI、httpx、uvicorn

# 任务
请帮我实现以下接口：{{task}}

# 接口信息
- 路由文件：`app/routers/{{router_file}}.py`
- 模型文件：`app/models/{{model_file}}.py`
- 服务文件：`app/service/{{service_file}}.py`
- HTTP 方法：`{{http_method}}`
- 路径：`{{route_path}}`

# 要求
- 先检查是否可复用现有 `PromptRequest` / `PromptResponse` 或现有 `DifyService`
- 保持现有绝对导入风格
- 不要擅自改成 `schemas/` 或 `services/`
- 如果需要新增路由，说明是否需要在 `app/main.py` 注册

# 输出
请按以下结构返回：
1. 需要修改的文件
2. 每个文件的完整代码或关键改动
3. 验证方式
~~~~

## 2. 可复用代码骨架

```python
from fastapi import APIRouter, Depends
from app.dependencies import get_dify_service
from app.models.dify import PromptRequest, PromptResponse
from app.service.dify import DifyService

router = APIRouter(prefix='/prompt', tags=['prompt'])


@router.post('/optimize', response_model=PromptResponse)
async def optimize_prompt(
    request: PromptRequest,
    service: DifyService = Depends(get_dify_service),
) -> PromptResponse:
    return await service.optimize_prompt(request)
```

## 3. Service 扩展示例

```python
import httpx


class ExampleService:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self._client = None

    @property
    async def client(self) -> httpx.AsyncClient:
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient()
        return self._client

    async def call_remote(self, payload: dict) -> dict:
        client = await self.client
        response = await client.post(
            f'{self.base_url}/endpoint',
            json=payload,
            timeout=30.0,
        )
        response.raise_for_status()
        return response.json()

    async def close(self) -> None:
        if self._client is not None and not self._client.is_closed:
            await self._client.aclose()
            self._client = None
```

## 4. 检查清单

- [ ] 路径是否使用 `app/models`、`app/service`、`app/routers`
- [ ] 导入风格是否与当前仓库一致
- [ ] `response_model` 是否和返回值一致
- [ ] 是否明确说明需要不要在 `main.py` 注册路由
- [ ] 是否给出可执行验证步骤
