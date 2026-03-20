# Vue 组件 Prompt 模板

用于当前 `PromptWizard/front` 仓库的快速组件生成，默认技术栈为 Vue 3 + JavaScript + Ant Design Vue。

~~~~markdown
# 角色
你是 PromptWizard 的前端工程师。

# 任务
请创建一个 Vue 组件。

# 组件信息
- 名称：`{{component_name}}`
- 路径：`src/components/{{component_name}}.vue`
- 用途：{{component_purpose}}

# 输入
- 需求描述：{{requirement_description}}
- 依赖接口：{{api_dependency}}
- 交互说明：{{interaction_notes}}

# 约束
- 使用 `<script setup>`
- 默认使用 JavaScript，不要切到 TypeScript
- 优先复用 Ant Design Vue
- 如果需要请求后端，沿用 `src/api/prompt.js` 的调用方式
- 显式处理 loading、空状态、错误反馈

# 输出要求
- 返回完整 `.vue` 文件
- 如需改动额外文件，单独列出
- 给出简短验证步骤
~~~~

## 参考骨架

```vue
<script setup>
import { reactive, ref } from 'vue'
import { message } from 'ant-design-vue'

const loading = ref(false)
const formState = reactive({
  input: '',
})

const handleSubmit = async () => {
  loading.value = true
  try {
    message.success('操作成功')
  } catch (error) {
    message.error('操作失败')
    throw error
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <a-card title="示例组件">
    <a-input v-model:value="formState.input" placeholder="请输入内容" />
    <a-button type="primary" :loading="loading" class="mt-4" @click="handleSubmit">
      提交
    </a-button>
  </a-card>
</template>
```

## 检查清单

- [ ] 未引入 HeroUI、Pinia、TypeScript 类型文件
- [ ] 模板变量均已在脚本中定义
- [ ] 组件可直接放入当前仓库使用
