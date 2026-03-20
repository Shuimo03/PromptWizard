---
name: devops
description: PromptWizard DevOps Skill。适用于为当前前后端仓库补充 Dockerfile、docker-compose、基础 CI 配置和部署草稿。强调与现有仓库结构一致，不默认假设已经有完整容器化或云原生体系。
---

# DevOps Skill

## 适用范围

当任务涉及以下内容时使用本 Skill：

- 为 `backend/` 或 `front/` 编写 Dockerfile
- 编写 `docker-compose.yml`
- 为 GitHub Actions 草拟构建流程
- 补充本地运行、打包、部署文档

## 当前仓库事实

```text
PromptWizard/
├── backend/
│   ├── pyproject.toml
│   └── app/
└── front/
    ├── package.json
    └── src/
```

### 后端

- Python `3.13+`
- `FastAPI`
- `httpx`
- `uvicorn`
- 运行入口见 [`backend/pyproject.toml`](/Users/mac/PromptWizard/backend/pyproject.toml)

### 前端

- `Vue 3`
- `Vite`
- `Ant Design Vue`
- `axios`
- `tailwindcss`
- 运行脚本见 [`front/package.json`](/Users/mac/PromptWizard/front/package.json)

### 当前缺失项

以下内容当前仓库里并没有成型实现，不能在模板里假装已经存在：

- Dockerfile
- docker-compose.yml
- `.github/workflows/*`
- Kubernetes 清单
- Helm Chart
- Terraform
- 统一健康检查接口
- 统一 lint/test 脚本

## 工作规则

1. 容器化配置必须基于真实依赖和真实启动命令。
2. 如果要加 `HEALTHCHECK`，先确认应用里确实有对应接口。
3. 不要默认使用数据库、Redis 或消息队列，除非任务明确要求。
4. CI 配置里不要直接调用仓库里不存在的脚本。
5. 如果引入新环境变量，名称必须和应用读取逻辑一致。

## 环境变量约定

### 前端

当前 API 地址变量是：

```text
VITE_API_URL
```

来源见 [`front/src/api/prompt.js`](/Users/mac/PromptWizard/front/src/api/prompt.js)。

### 后端

当前 Dify 配置主要来自 YAML 文件，而不是环境变量强制注入。若为了容器化改为环境变量，需要同时修改应用读取逻辑。

## 推荐交付物

### 1. Backend Dockerfile

要求：

- 基于 `python:3.13-slim`
- 以 `backend/` 为构建上下文
- 安装 `uv`
- 使用 `uv sync --frozen`
- 启动命令与 `uvicorn`/项目入口保持一致

### 2. Frontend Dockerfile

要求：

- 基于 `node:20-alpine`
- 构建 `front/`
- 如果是纯静态部署，可使用 `nginx`
- 如果只是开发镜像，可直接 `npm run dev -- --host 0.0.0.0`

### 3. docker-compose.yml

仅在任务需要时再加入这些服务：

- `backend`
- `front`

不要默认添加：

- `db`
- `redis`
- `worker`

## CI 编写原则

如果新增 GitHub Actions，优先从“最小可执行”开始：

1. 前端 `npm ci`
2. 前端 `npm run build`
3. 后端 `uv sync --frozen`
4. 后端基础导入检查或启动检查

只有仓库里已经补齐对应脚本时，才加入：

- `npm run lint`
- `pytest`
- `ruff`
- `mypy`

## 示例思路

### Compose 中的前后端联调

```yaml
services:
  backend:
    build:
      context: ./backend
    ports:
      - "8000:8000"

  front:
    build:
      context: ./front
    ports:
      - "5173:5173"
    environment:
      VITE_API_URL: http://backend:8000
```

### GitHub Actions 最小构建

```yaml
jobs:
  frontend-build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
        working-directory: front
      - run: npm run build
        working-directory: front

  backend-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.13'
      - uses: astral-sh/setup-uv@v4
      - run: uv sync --frozen
        working-directory: backend
```

## 不要这样做

- 不要写 `DIF Y_API_KEY` 这类拼写错误的环境变量
- 不要默认引用 `/health`，除非接口已存在
- 不要假设仓库已经有 PostgreSQL、Redis、K8s、Terraform
- 不要在 CI 中调用不存在的 `lint` 或 `test` 命令

## 完成前检查

- [ ] 启动命令是否来自真实仓库
- [ ] 构建上下文是否正确
- [ ] 环境变量名是否和应用读取逻辑一致
- [ ] 健康检查路径是否真实存在
- [ ] CI 步骤是否都能在当前仓库落地
