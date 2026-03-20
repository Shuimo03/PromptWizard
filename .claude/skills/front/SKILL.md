---
name: front
description: PromptWizard 前端开发 Skill。适用于 Vue 3 + Vite + Ant Design Vue + axios 场景下的组件开发、页面调整、API 接入和展示层修复。默认遵循当前仓库的 JavaScript 写法，而不是假设 TypeScript、Pinia 或 HeroUI 已经存在。
---

# Front Skill

## 适用范围

当任务涉及以下内容时使用本 Skill：

- 修改 `front/src/components/`
- 修改 `front/src/api/`
- 修改 `front/src/App.vue`
- 修改前端样式与交互
- 对接后端 `/prompt/optimize`
- 修复 Vue 页面渲染、表单提交流程、Markdown 展示问题

## 当前仓库事实

### 技术栈

- `Vue 3`
- `Vite`
- `JavaScript` 为主，不是 TypeScript
- `Ant Design Vue`
- `axios`
- `tailwindcss`
- `markdown-it`
- `highlight.js`

来源见 [`front/package.json`](/Users/mac/PromptWizard/front/package.json)。

### 已有关键文件

```text
front/
├── src/
│   ├── App.vue
│   ├── main.js
│   ├── api/
│   │   └── prompt.js
│   ├── assets/
│   └── components/
│       └── PromptGenerator.vue
```

### 当前前端约定

- UI 组件使用 `Ant Design Vue`
- API 客户端在 [`front/src/api/prompt.js`](/Users/mac/PromptWizard/front/src/api/prompt.js)
- 环境变量使用 `VITE_API_URL`
- 组件多使用 `<script setup>`，但目前是 JavaScript 写法

不要默认以下技术已经接入：

- TypeScript
- Pinia
- HeroUI
- Heroicons
- VueUse
- 单元测试框架

## 工作规则

1. 默认写 Vue SFC + `<script setup>` + JavaScript。
2. 除非用户明确要迁移，否则不要把单个文件突然改成 TypeScript 体系。
3. 新组件优先复用 Ant Design Vue 生态，而不是引入新 UI 库。
4. 调接口时优先复用现有 `axios` 客户端模式。
5. 页面和组件的目录命名先遵循当前仓库现状，不强推新分层。

## 组件开发规范

### 推荐模式

```vue
<script setup>
import { computed, ref } from 'vue'
import { message } from 'ant-design-vue'

const loading = ref(false)
const hasResult = computed(() => false)

const handleSubmit = async () => {
  loading.value = true
  try {
    message.success('提交成功')
  } finally {
    loading.value = false
  }
}
</script>
```

### 表单和交互

- 表单优先使用 `a-form`、`a-form-item`、`a-input`、`a-textarea`
- 操作反馈优先使用 `message`
- 卡片和布局优先使用 `a-card`、`a-layout`、`a-space`

## API 集成规范

当前已有模式：

```javascript
import axios from 'axios'

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
  timeout: 60000,
})
```

新增 API 时：

- 保持 `src/api/*.js` 风格一致
- 不要凭空改成 `request.ts`
- 不要引入 `Promise.reject` 包装式样板，除非确有统一拦截器

## 样式规范

- 优先保持现有 Ant Design Vue + 工具类样式混用方式
- 移动端适配优先考虑 `sm:` 断点
- 只在必要时写 `<style scoped>`
- 如果 Tailwind 工具类足够表达，不必再写额外样式块

## 路由注意事项

[`front/src/main.js`](/Users/mac/PromptWizard/front/src/main.js) 当前引用了 `./router`，但仓库里未发现对应文件。处理涉及路由的任务时：

1. 先确认用户是否遗漏了文件
2. 或者在同一任务里一并补齐路由实现
3. 不要在 skill 里假设 `src/router/index.ts` 已存在

## 不要这样做

- 不要使用 `@heroui/react`
- 不要写 Pinia Store 模板，除非任务明确要求引入 Pinia
- 不要使用不存在的 `@/types/*`、`src/api/request.ts`、`src/stores/*`
- 不要在 Vue 模板里引用未定义的变量
- 不要把当前 JS 项目直接描述成完整 TS 项目

## 完成前检查

- [ ] 引用的组件库是否是 Ant Design Vue
- [ ] 环境变量是否使用 `VITE_API_URL`
- [ ] 新文件类型是否和当前仓库一致
- [ ] 模板里使用的变量和方法是否都已定义
- [ ] 如果涉及路由，是否核对过实际路由文件存在性
