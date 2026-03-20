# DevOps Prompt 模板

这些模板只描述当前仓库能落地的最小方案，不默认带数据库、Redis、K8s 或完整 CI 体系。

## 1. Backend Dockerfile

~~~~markdown
# 角色
你是 PromptWizard 的 DevOps 工程师。

# 仓库上下文
- 后端目录：`/Users/mac/PromptWizard/backend`
- Python 版本：3.13+
- 依赖管理：`uv`
- Web 框架：FastAPI

# 任务
请为后端编写一个可用于生产或联调的 Dockerfile。

# 约束
- 构建上下文是 `backend/`
- 基于真实的 `pyproject.toml`
- 使用 `uv sync --frozen`
- 启动命令必须与当前应用入口一致
- 只有在应用已存在对应接口时才添加 `HEALTHCHECK`

# 输出
请提供：
1. `backend/Dockerfile`
2. 可选的 `.dockerignore`
3. 构建和运行命令
~~~~

## 2. Frontend Dockerfile

~~~~markdown
# 角色
你是 PromptWizard 的 DevOps 工程师。

# 仓库上下文
- 前端目录：`/Users/mac/PromptWizard/front`
- 运行时：Node.js 20
- 前端框架：Vue 3 + Vite
- UI：Ant Design Vue

# 任务
请为前端编写 Dockerfile。

# 约束
- 构建上下文是 `front/`
- 使用 `npm ci`
- 如果是静态部署，说明最终如何托管 `dist/`
- 如果需要 API 地址，使用 `VITE_API_URL`

# 输出
请提供：
1. `front/Dockerfile`
2. 运行说明
3. 环境变量说明
~~~~

## 3. docker-compose.yml

~~~~markdown
# 任务
请为 PromptWizard 编写最小可用的 `docker-compose.yml`。

# 服务范围
- 必选：`backend`
- 可选：`front`

# 约束
- 不要默认加入数据库或 Redis
- 前端如需访问后端，请使用 `VITE_API_URL`
- 端口映射请与应用实际启动端口一致
- 不要引用不存在的 `/health`

# 输出
请给出完整 `docker-compose.yml`，并补充启动命令。
~~~~

## 4. GitHub Actions 最小模板

~~~~markdown
# 任务
请为该仓库生成最小 GitHub Actions 工作流。

# 目标
- 构建前端
- 校验后端依赖可安装

# 约束
- 只使用仓库真实存在的命令
- 前端目录是 `front/`
- 后端目录是 `backend/`
- 不要假设已有 lint/test 脚本

# 输出
请提供 `.github/workflows/{{workflow_name}}.yml` 完整内容。
~~~~

## 5. 检查清单

- [ ] 构建上下文是否正确
- [ ] 环境变量名是否使用 `VITE_API_URL`
- [ ] 是否避免了不存在的依赖服务
- [ ] 是否避免了不存在的健康检查路径
- [ ] CI 是否只调用真实命令
