# 前端开发 Prompt 模板

面向当前 `PromptWizard/front` 仓库，默认使用 Vue 3 + JavaScript + Ant Design Vue。

## 1. Vue 组件开发

~~~~markdown
# 角色
你是 PromptWizard 的前端工程师。

# 仓库上下文
- 项目路径：`/Users/mac/PromptWizard/front`
- 技术栈：Vue 3、Vite、JavaScript、Ant Design Vue、axios
- API 地址变量：`VITE_API_URL`

# 任务
请帮我实现这个组件：{{task}}

# 组件信息
- 文件路径：`src/components/{{component_name}}.vue`
- 是否复用现有接口：{{reuse_api}}
- 是否需要表单提交：{{has_form}}

# 要求
- 默认使用 `<script setup>` + JavaScript
- 优先复用 Ant Design Vue 组件
- 不要引入 HeroUI、Pinia、TypeScript 类型文件
- 如需调接口，优先复用 `src/api/prompt.js` 的风格
- 明确 loading、错误提示和成功反馈

# 输出
1. 组件完整代码
2. 如果需要，说明还要修改哪些文件
3. 给出验证方式
~~~~

## 2. API 模块开发

~~~~markdown
# 角色
你是 PromptWizard 的前端工程师。

# 仓库上下文
- API 目录：`src/api/`
- 当前文件示例：`src/api/prompt.js`
- axios 基础地址：`import.meta.env.VITE_API_URL || 'http://localhost:8000'`

# 任务
请新增或修改一个 API 模块：{{task}}

# 约束
- 使用 JavaScript
- 保持现有 `axios.create(...)` 风格
- 不要凭空改成 `request.ts`
- 导出方式保持简单明确

# 输出
请给出完整文件内容和调用示例。
~~~~

## 3. 路由调整

~~~~markdown
# 任务
请帮我处理前端路由相关改动。

# 重要说明
当前 `src/main.js` 引用了 `./router`，但仓库里未发现对应文件。

# 要求
- 先判断是补齐路由文件，还是改回单页入口
- 不要假设 `src/router/index.ts` 已存在
- 如果新增路由文件，请同时说明 `main.js` 的改动
~~~~

## 4. 组件参考骨架

```vue
<script setup>
import { computed, reactive, ref } from 'vue'
import { message } from 'ant-design-vue'

const loading = ref(false)
const formState = reactive({
  value: '',
})

const canSubmit = computed(() => formState.value.trim().length > 0)

const handleSubmit = async () => {
  if (!canSubmit.value) {
    message.warning('请输入内容')
    return
  }

  loading.value = true
  try {
    message.success('提交成功')
  } catch (error) {
    message.error('提交失败')
    throw error
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <a-card title="示例组件">
    <a-form layout="vertical">
      <a-form-item label="内容">
        <a-input v-model:value="formState.value" />
      </a-form-item>
      <a-button type="primary" :loading="loading" @click="handleSubmit">
        提交
      </a-button>
    </a-form>
  </a-card>
</template>
```

## 5. 检查清单

- [ ] 是否仍然基于 Vue 3 + JavaScript
- [ ] 是否使用 Ant Design Vue 而不是其他 UI 库
- [ ] 是否引用了真实存在的文件和环境变量
- [ ] 模板中的变量和方法是否都已定义
