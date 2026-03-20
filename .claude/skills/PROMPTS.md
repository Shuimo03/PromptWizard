# Prompt 模板索引

本目录存放可直接复用的 Prompt 模板。目标不是覆盖所有场景，而是优先服务当前 `PromptWizard` 仓库。

## 当前可用文件

```text
.claude/skills/
├── PROMPTS.md
├── PROMPTS/
│   ├── README.md
│   ├── backend/
│   │   └── api-endpoint.md
│   ├── devops/
│   │   └── dockerfile.md
│   └── frontend/
│       └── component.md
└── front/
    └── PROMPTS/
        └── vue-component.md
```

## 使用原则

1. 先选最贴近当前任务和当前仓库的模板。
2. 把 `{{变量}}` 替换成真实路径、真实依赖、真实文件名。
3. 如果模板和仓库现状冲突，以仓库事实为准，不要硬套模板。
4. 输出代码前，先核对目录、包名、环境变量和现有导入方式。

## 模板说明

| 文件 | 用途 | 适用场景 |
|------|------|----------|
| `PROMPTS/README.md` | 通用模板集合 | 需求澄清、实现、修复、评审 |
| `PROMPTS/backend/api-endpoint.md` | FastAPI 接口与服务扩展 | 新增或修改后端接口 |
| `PROMPTS/devops/dockerfile.md` | 容器化与 CI 草稿 | Dockerfile、Compose、CI |
| `PROMPTS/frontend/component.md` | Vue 前端开发模板 | 组件、API 模块、路由 |
| `front/PROMPTS/vue-component.md` | 更轻量的 Vue 组件模板 | 快速生成单个组件 |

## 维护要求

- 索引里列出的文件必须真实存在。
- 模板中的技术栈必须和仓库一致，除非明确写明“迁移方案”。
- 模板示例必须能被复制，不允许出现会打断 Markdown 的错误嵌套代码块。
