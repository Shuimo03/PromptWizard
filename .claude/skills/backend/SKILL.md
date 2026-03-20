---
name: backend
description: PromptWizard 后端开发 Skill。适用于 FastAPI 路由、Pydantic 模型、Dify 服务集成、配置加载、依赖注入和后端调试。优先匹配当前仓库的真实结构，而不是套用通用 FastAPI 脚手架。
---

# Backend Skill

## 适用范围

当任务涉及以下内容时使用本 Skill：

- 修改 `backend/app/routers/`
- 修改 `backend/app/models/`
- 修改 `backend/app/service/`
- 修改 `backend/app/dependencies.py`
- 修改 `backend/app/main.py`
- 排查 Dify API 调用、配置读取或响应映射问题

## 当前仓库事实

以当前仓库为准，不要假设存在额外目录或工具。

```text
backend/
├── app/
│   ├── main.py
│   ├── dependencies.py
│   ├── config/
│   │   ├── dev.yaml
│   │   └── settings.py
│   ├── models/
│   │   └── dify.py
│   ├── routers/
│   │   └── prompt.py
│   ├── service/
│   │   └── dify.py
│   └── tests/
├── pyproject.toml
└── uv.lock
```

### 已有依赖

- Python `3.13+`
- `fastapi`
- `httpx`
- `uvicorn`
- `python-dotenv`

不要默认引入以下能力，除非任务明确要求并且你同步补齐依赖与接入：

- PostgreSQL
- SQLAlchemy
- Alembic
- Redis
- Celery
- Pydantic Settings

## 现有代码约定

### 目录约定

- 请求/响应模型目前放在 `app/models/`，不是 `app/schemas/`
- 服务层目录目前是 `app/service/`，不是 `app/services/`
- 路由通过 `app.include_router(...)` 在 [`backend/app/main.py`](/Users/mac/PromptWizard/backend/app/main.py) 注册

### 导入约定

当前代码大量使用绝对导入，例如：

```python
from app.models.dify import PromptRequest, PromptResponse
from app.service.dify import DifyService
```

除非做统一重构，否则保持这种风格。

### 配置约定

- 运行时配置在 [`backend/app/config/dev.yaml`](/Users/mac/PromptWizard/backend/app/config/dev.yaml)
- `main.py` 直接读取 `app/config/dev.yaml`
- [`backend/app/config/settings.py`](/Users/mac/PromptWizard/backend/app/config/settings.py) 存在，但当前不是主入口配置来源

新增配置时，不要只改 `settings.py` 而忘记同步 `main.py`。

## 工作规则

1. 修改接口前先查看相关 `router`、`model`、`service` 三层是否已经存在。
2. 如果只是扩展 Dify 能力，优先复用 [`backend/app/service/dify.py`](/Users/mac/PromptWizard/backend/app/service/dify.py)。
3. 如果新增接口，先判断是否需要新增模型，还是复用 [`backend/app/models/dify.py`](/Users/mac/PromptWizard/backend/app/models/dify.py)。
4. 不要无故把现有目录从 `service` 改成 `services`，也不要把 `models` 全量迁到 `schemas`。
5. 只有在用户明确要求重构时，才进行目录层级升级。

## 推荐工作流

### 1. 修改已有接口

- 查看路由定义和 response_model
- 查看对应 service 方法的输入输出
- 查看模型是否已经能表达新字段
- 修改后补最小测试或最小手工验证步骤

### 2. 新增接口

建议按以下顺序：

1. 在 `app/models/` 定义或补充请求/响应模型
2. 在 `app/service/` 实现业务逻辑
3. 在 `app/routers/` 暴露接口
4. 在 `app/main.py` 注册路由
5. 在 `app/tests/` 增加测试或至少给出验证命令

### 3. 调试外部服务

排查顺序：

1. 配置是否正确加载
2. 请求体字段名是否符合 Dify 接口要求
3. `httpx` 请求和超时设置是否合理
4. 响应 JSON 是否和 `Pydantic` 模型匹配
5. 路由层是否正确返回 `PromptResponse`

## 示例模式

### 路由扩展

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

### Service 扩展

```python
import httpx


class DifyService:
    async def optimize_prompt(self, request):
        client = await self.client
        response = await client.post(
            url=f'{self.base_url}/workflows/run',
            json={...},
            headers={...},
            timeout=30.0,
        )
        response.raise_for_status()
        return ...
```

## 不要这样做

- 不要写出 `app/schemas/`、`app/services/` 这类当前仓库里不存在的固定路径
- 不要默认项目已经接入数据库
- 不要要求不存在的 `health.py`、`ruff`、`mypy`、`pytest` 配置一定已经可用
- 不要为了“更标准”就强行重构现有绝对导入

## 完成前检查

- [ ] 路径是否真实存在
- [ ] 导入路径是否和当前仓库一致
- [ ] 新字段是否在 model、service、router 三层都对齐
- [ ] 如果新增配置，是否同步更新了实际加载入口
- [ ] 是否给出了验证方式
