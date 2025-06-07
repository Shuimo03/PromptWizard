<template>
  <div class="prompt-generator">
    <a-card title="Prompt 生成器" :bordered="false" class="shadow-lg">
      <a-form layout="vertical" :model="formData" @finish="generatePrompt">
        
        <!-- 角色选择区域 -->
        <a-form-item label="选择角色" name="role" class="mb-4 sm:mb-6">
          <a-select
            v-model:value="formData.role"
            placeholder="请选择一个角色"
            class="w-full"
          >
            <a-select-opt-group label="编程开发类">
              <a-select-option value="software_engineer">👨‍💻 专业编程专家</a-select-option>
              <a-select-option value="fullstack_developer">🔧全栈开发工程师</a-select-option>
              <a-select-option value="ai_developer">🤖AI 开发工程师</a-select-option>
              <a-select-option value="devops_engineer">⚙️DevOps 工程师</a-select-option>
            </a-select-opt-group>
            <a-select-opt-group label="写作创作类">
              <a-select-option value="academic_writer">👌学术写作专家</a-select-option>
              <a-select-option value="content_writer">✏️内容创作者</a-select-option>
              <a-select-option value="copywriter">📝文案策划师</a-select-option>
            </a-select-opt-group>
            <a-select-opt-group label="产品设计类">
              <a-select-option value="product_manager">📱产品经理</a-select-option>
              <a-select-option value="ui_designer">🎨UI 设计师</a-select-option>
              <a-select-option value="ux_researcher">👥用户体验研究员</a-select-option>
            </a-select-opt-group>
            <a-select-opt-group label="数据分析类">
              <a-select-option value="data_scientist">📊数据科学家</a-select-option>
              <a-select-option value="data_analyst">📊数据分析师</a-select-option>
              <a-select-option value="business_analyst">💼业务分析师</a-select-option>
            </a-select-opt-group>
            <a-select-opt-group label="市场营销类">
              <a-select-option value="marketing_specialist">🎯市场营销专家</a-select-option>
              <a-select-option value="seo_expert">🔍SEO 专家</a-select-option>
              <a-select-option value="growth_hacker">📈增长黑客</a-select-option>
            </a-select-opt-group>
            <a-select-opt-group label="其他专业类">
              <a-select-option value="legal_advisor">⚖️法律顾问</a-select-option>
              <a-select-option value="financial_advisor">💰财务顾问</a-select-option>
              <a-select-option value="career_coach">🚀职业规划师</a-select-option>
            </a-select-opt-group>
            <a-select-option value="custom">🤖自定义角色</a-select-option>
          </a-select>
          
          <!-- 自定义角色输入 -->
          <a-input
            v-if="formData.role === 'custom'"
            v-model:value="formData.customRole"
            placeholder="请输入自定义角色，如：区块链法律顾问、量化投资分析师..."
            :size="isMobile ? 'middle' : 'large'"
            class="mt-3"
          />
        </a-form-item>

        <!-- 背景描述区域 - 改为可选的补充信息 -->
        <a-form-item label="补充信息（可选）" name="background" class="mb-4 sm:mb-6">
          <a-textarea
            v-model:value="formData.background"
            placeholder="如有特殊要求、约束条件或背景信息需要说明，可在此补充..."
            :rows="isMobile ? 2 : 3"
            :size="isMobile ? 'middle' : 'large'"
            show-count
            :maxlength="300"
          />
          <div class="text-xs text-gray-400 mt-1">
            💡 提示：大多数情况下，选择合适的角色并描述期望目标即可生成优质 Prompt
          </div>
        </a-form-item>

        <!-- 期望描述区域 -->
        <a-form-item label="期望目标" name="expectation" class="mb-4 sm:mb-6" :rules="[{ required: true, message: '请描述期望目标' }]">
          <a-textarea
            v-model:value="formData.expectation"
            placeholder="请详细描述你希望这个角色帮你完成什么任务，越具体越好..."
            :rows="isMobile ? 4 : 5"
            :size="isMobile ? 'middle' : 'large'"
            show-count
            :maxlength="600"
          />
          <div class="text-xs text-gray-400 mt-1">
            🎯 例如：帮我写一篇关于AI发展的技术博客文章，要求通俗易懂，包含实际应用案例
          </div>
        </a-form-item>

        <!-- 生成按钮 -->
        <a-form-item class="mb-4 sm:mb-6">
          <a-button
            type="primary"
            :size="isMobile ? 'middle' : 'large'"
            :loading="isGenerating"
            @click="generatePrompt"
            class="w-full font-medium"
            :class="isMobile ? 'h-10 text-base' : 'h-12 text-lg'"
          >
            <template #icon>
              <ThunderboltOutlined />
            </template>
            生成 Prompt
          </a-button>
        </a-form-item>

        <!-- 生成的Prompt输出区域 -->
        <a-form-item label="生成的 Prompt" v-if="generatedPrompt">
          <a-card class="bg-gray-50 border-2 border-dashed border-gray-300">
            <template #extra>
              <a-space :size="isMobile ? 'small' : 'middle'">
                <a-button :size="isMobile ? 'small' : 'middle'" @click="copyPrompt">
                  <template #icon>
                    <CopyOutlined />
                  </template>
                  <span v-if="!isMobile">复制</span>
                </a-button>
                <a-button :size="isMobile ? 'small' : 'middle'" @click="refinePrompt" :loading="isRefining">
                  <template #icon>
                    <EditOutlined />
                  </template>
                  <span v-if="!isMobile">润色</span>
                </a-button>
                <a-button :size="isMobile ? 'small' : 'middle'" @click="toggleView">
                  <template #icon>
                    <component :is="isMarkdownView ? 'CodeOutlined' : 'EyeOutlined'" />
                  </template>
                  <span v-if="!isMobile">{{ isMarkdownView ? '源码' : '预览' }}</span>
                </a-button>
              </a-space>
            </template>
            
            <div class="prompt-output">
              <!-- Markdown预览模式 -->
              <div v-if="isMarkdownView" class="markdown-body" v-html="renderedMarkdown"></div>
              <!-- 源码模式 -->
              <pre v-else class="whitespace-pre-wrap leading-relaxed code-view" 
                   :class="isMobile ? 'text-xs' : 'text-sm'">{{ generatedPrompt }}</pre>
            </div>
          </a-card>
        </a-form-item>

      </a-form>
    </a-card>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted, onUnmounted } from 'vue'
import { message } from 'ant-design-vue'
import { 
  PlusOutlined, 
  CopyOutlined, 
  EditOutlined,
  ThunderboltOutlined,
  EyeOutlined,
  CodeOutlined
} from '@ant-design/icons-vue'
import { promptService } from '../api/prompt'
import MarkdownIt from 'markdown-it'
import hljs from 'highlight.js'
import 'highlight.js/styles/github.css'
import 'github-markdown-css/github-markdown.css'

// 初始化markdown-it
const md = new MarkdownIt({
  html: true,
  linkify: true,
  typographer: true,
  highlight: function (str, lang) {
    if (lang && hljs.getLanguage(lang)) {
      try {
        const highlighted = hljs.highlight(str, { language: lang }).value
        // 添加行号和改进的代码块样式
        return `<div class="code-block-wrapper">
                  <div class="code-block-header">
                    <span class="code-lang">${lang}</span>
                  </div>
                  <pre class="hljs"><code>${highlighted}</code></pre>
                </div>`
      } catch (__) {}
    }
    // 如果没有指定语言或者高亮失败，仍然提供基本的代码块样式
    return `<pre class="hljs"><code>${md.utils.escapeHtml(str)}</code></pre>`
  }
})

// 预定义的角色模板
const roleTemplates = {
  // 编程开发类
  software_engineer: {
    title: '专业编程专家',
    requirements: [
      '使用最佳实践和行业标准',
      '提供清晰的代码示例和注释',
      '考虑性能、安全性和可维护性',
      '解释技术选择的原因'
    ]
  },
  fullstack_developer: {
    title: '全栈开发工程师',
    requirements: [
      '前后端技术栈的最佳实践',
      '系统架构和数据流设计',
      '安全性和性能优化',
      '开发工具和部署流程'
    ]
  },
  ai_developer: {
    title: 'AI 开发工程师',
    requirements: [
      '机器学习模型的选择和应用',
      '数据预处理和特征工程',
      '模型训练和优化策略',
      '模型部署和监控方案'
    ]
  },
  devops_engineer: {
    title: 'DevOps 工程师',
    requirements: [
      '自动化部署和持续集成',
      '监控和日志管理',
      '性能优化和故障排查',
      '安全性和可扩展性'
    ]
  },

  // 写作创作类
  academic_writer: {
    title: '学术写作专家',
    requirements: [
      '严谨的学术写作规范',
      '清晰的论证结构',
      '准确的文献引用',
      '专业术语的准确使用'
    ]
  },
  content_writer: {
    title: '内容创作者',
    requirements: [
      '吸引人的内容结构',
      'SEO 优化和关键词策略',
      '目标受众分析',
      '内容营销策略'
    ]
  },
  copywriter: {
    title: '文案策划师',
    requirements: [
      '品牌调性把握',
      '吸引力文案创作',
      '用户心理洞察',
      '转化率优化'
    ]
  },

  // 产品设计类
  product_manager: {
    title: '产品经理',
    requirements: [
      '用户需求分析',
      '产品规划和路线图',
      '功能设计和优先级',
      '数据驱动决策'
    ]
  },
  ui_designer: {
    title: 'UI 设计师',
    requirements: [
      '视觉设计原则',
      '用户界面交互设计',
      '设计系统和规范',
      '原型设计和测试'
    ]
  },
  ux_researcher: {
    title: '用户体验研究员',
    requirements: [
      '用户研究方法',
      '用户行为分析',
      '可用性测试',
      '研究报告和建议'
    ]
  },

  // 数据分析类
  data_scientist: {
    title: '数据科学家',
    requirements: [
      '数据分析方法论',
      '统计模型和算法',
      '数据可视化',
      '业务洞察和建议'
    ]
  },
  data_analyst: {
    title: '数据分析师',
    requirements: [
      '数据收集和清洗',
      '数据分析和挖掘',
      '报告撰写和展示',
      '数据驱动决策建议'
    ]
  },
  business_analyst: {
    title: '业务分析师',
    requirements: [
      '业务流程分析',
      '需求收集和管理',
      '解决方案设计',
      'ROI 分析和评估'
    ]
  },

  // 市场营销类
  marketing_specialist: {
    title: '市场营销专家',
    requirements: [
      '市场策略制定',
      '营销活动策划',
      '效果分析和优化',
      '竞品分析和市场洞察'
    ]
  },
  seo_expert: {
    title: 'SEO 专家',
    requirements: [
      '搜索引擎优化策略',
      '关键词研究和分析',
      '内容优化建议',
      '技术 SEO 优化'
    ]
  },
  growth_hacker: {
    title: '增长黑客',
    requirements: [
      '用户增长策略',
      '转化率优化',
      '数据分析和实验',
      '渠道策略'
    ]
  },

  // 其他专业类
  legal_advisor: {
    title: '法律顾问',
    requirements: [
      '法律风险分析',
      '合规性建议',
      '文件审查和修改',
      '法律解决方案'
    ]
  },
  financial_advisor: {
    title: '财务顾问',
    requirements: [
      '财务分析和规划',
      '风险评估和管理',
      '投资策略建议',
      '财务报告解读'
    ]
  },
  career_coach: {
    title: '职业规划师',
    requirements: [
      '职业发展规划',
      '能力评估和建议',
      '简历和面试指导',
      '职业转型建议'
    ]
  },

  // 自定义角色模板
  custom: {
    title: '专业顾问',
    requirements: [
      '专业知识应用',
      '问题分析和解决',
      '清晰的沟通表达',
      '实用的建议和方案'
    ]
  }
}

// 生成本地模板
const generateTemplate = (role, background, expectation, customRole = '') => {
  const template = roleTemplates[role]
  if (!template) return ''

  // 如果是自定义角色，使用用户输入的角色名称
  const roleTitle = role === 'custom' ? customRole : template.title

  let prompt = `# 角色设定
你是一位${roleTitle}，在相关领域有深厚的专业知识和实践经验。

# 任务目标
${expectation}`

  if (background) {
    prompt += `\n\n# 补充信息
${background}`
  }

  prompt += `\n\n# 专业要求
${template.requirements.map((req, index) => `${index + 1}. ${req}`).join('\n')}

# 输出格式
请按照以下结构组织你的专业回答：

## 📋 任务理解
- 对需求的分析和理解
- 关键要点和注意事项

## 🎯 解决方案
- 详细的实施步骤或内容
- 具体的方法和技巧

## 💡 专业建议
- 最佳实践和优化建议
- 潜在风险和应对措施

## 📚 相关资源（如适用）
- 推荐的工具、方法或参考资料

请开始你的专业回答：`

  return prompt
}

// 响应式数据
const formData = reactive({
  role: '',
  customRole: '',  // 添加自定义角色字段
  background: '',
  expectation: ''
})

const generatedPrompt = ref('')
const isGenerating = ref(false)
const isRefining = ref(false)
const windowWidth = ref(window.innerWidth)

// 移动端判断
const isMobile = computed(() => windowWidth.value < 768)

// 监听窗口大小变化
const handleResize = () => {
  windowWidth.value = window.innerWidth
}

onMounted(() => {
  window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
})

// 预定义角色选项 - 参考 awesome-prompts 优秀角色设定
const predefinedRoles = ref([
  // 编程开发类
  { value: 'professional-coder', label: '💻专业编程专家', tag: '编程', color: 'blue' },
  { value: 'fullstack-developer', label: '🔧全栈开发工程师', tag: '开发', color: 'cyan' },
  { value: 'ai-developer', label: '🤖AI/ML开发专家', tag: 'AI', color: 'purple' },
  { value: 'devops-engineer', label: '⚙️DevOps工程师', tag: '运维', color: 'orange' },
  
  // 写作创作类
  { value: 'academic-writer', label: '👌学术写作助手', tag: '学术', color: 'green' },
  { value: 'all-around-writer', label: '✏️全能写作专家', tag: '写作', color: 'blue' },
  { value: 'creative-writer', label: '🎨创意写作大师', tag: '创意', color: 'magenta' },
  { value: 'copywriter', label: '📝营销文案专家', tag: '文案', color: 'gold' },
  
  // 分析咨询类
  { value: 'data-analyst', label: '📊数据分析师', tag: '分析', color: 'green' },
  { value: 'business-analyst', label: '💼商业分析顾问', tag: '商业', color: 'blue' },
  { value: 'financial-advisor', label: '💰金融投资顾问', tag: '金融', color: 'gold' },
  { value: 'market-researcher', label: '📈市场研究专家', tag: '市场', color: 'lime' },
  
  // 教育培训类
  { value: 'tutor', label: '🎓个人导师', tag: '教育', color: 'orange' },
  { value: 'language-teacher', label: '🌍语言学习导师', tag: '语言', color: 'purple' },
  { value: 'skill-trainer', label: '💪技能培训师', tag: '培训', color: 'cyan' },
  
  // 设计创意类
  { value: 'ui-designer', label: '🎨UI/UX设计师', tag: '设计', color: 'magenta' },
  { value: 'graphic-designer', label: '🖼️平面设计师', tag: '平面', color: 'pink' },
  { value: 'brand-strategist', label: '🏷️品牌策略师', tag: '品牌', color: 'purple' },
  
  // 专业服务类
  { value: 'translator', label: '🌐专业翻译家', tag: '翻译', color: 'blue' },
  { value: 'legal-advisor', label: '⚖️法律顾问', tag: '法律', color: 'red' },
  { value: 'career-coach', label: '🚀职业规划师', tag: '职场', color: 'green' },
  { value: 'health-consultant', label: '🏥健康咨询师', tag: '健康', color: 'lime' },
  
  // 技术专家类
  { value: 'seo-expert', label: '🔍SEO优化专家', tag: 'SEO', color: 'green' },
  { value: 'security-expert', label: '🔒网络安全专家', tag: '安全', color: 'red' },
  { value: 'blockchain-expert', label: '⛓️区块链专家', tag: '区块链', color: 'gold' },
  
  // 研究学术类
  { value: 'researcher', label: '🔬科学研究员', tag: '研究', color: 'blue' },
  { value: 'academic-reviewer', label: '📚学术评审专家', tag: '评审', color: 'purple' },
  { value: 'patent-analyst', label: '📋专利分析师', tag: '专利', color: 'cyan' },
  
  // 创业商业类
  { value: 'startup-mentor', label: '🚀创业导师', tag: '创业', color: 'orange' },
  { value: 'product-manager', label: '📱产品经理', tag: '产品', color: 'blue' },
  { value: 'growth-hacker', label: '📈增长黑客', tag: '增长', color: 'green' },
  
  // 生活助手类
  { value: 'life-coach', label: '🌟生活教练', tag: '生活', color: 'yellow' },
  { value: 'travel-planner', label: '✈️旅行规划师', tag: '旅行', color: 'cyan' },
  { value: 'cooking-expert', label: '👨‍🍳烹饪专家', tag: '美食', color: 'orange' }
])

// 角色过滤函数 - 支持多维度搜索
const filterOption = (input, option) => {
  const searchText = input.toLowerCase()
  const roleData = predefinedRoles.value.find(role => role.value === option.value)
  
  if (!roleData) return false
  
  // 支持按标签、名称、value搜索
  return (
    roleData.label.toLowerCase().includes(searchText) ||
    roleData.tag.toLowerCase().includes(searchText) ||
    roleData.value.toLowerCase().includes(searchText)
  )
}

// 生成Prompt
const generatePrompt = () => {
  if (!formData.role) {
    message.error('请选择角色')
    return
  }
  if (formData.role === 'custom' && !formData.customRole) {
    message.error('请输入自定义角色名称')
    return
  }
  if (!formData.expectation) {
    message.error('请输入期望目标')
    return
  }

  console.log('Generating template for role:', formData.role)

  // 先生成本地模板
  const template = generateTemplate(
    formData.role,
    formData.background,
    formData.expectation,
    formData.customRole
  )

  if (!template) {
    console.error('Template generation failed. Role:', formData.role)
    message.error('生成模板失败，请重试')
    return
  }

  generatedPrompt.value = template
  message.success('Prompt 模板生成成功！')
}

// 复制Prompt
const copyPrompt = async () => {
  try {
    await navigator.clipboard.writeText(generatedPrompt.value)
    message.success('已复制到剪贴板')
  } catch (error) {
    message.error('复制失败')
  }
}

// 润色Prompt
const refinePrompt = async () => {
  if (!generatedPrompt.value) return
  
  isRefining.value = true
  try {
    // 获取当前角色标题
    const template = roleTemplates[formData.role]
    const roleTitle = formData.role === 'custom' ? formData.customRole : template.title

    // 调用后端 API 进行润色
    const response = await promptService.optimizePrompt({
      background: formData.background || '',
      role: roleTitle,
      expectation: formData.expectation
    })

    if (response.optimized_prompt) {
      generatedPrompt.value = response.optimized_prompt
      message.success('✨ Prompt 润色完成！')
    } else {
      throw new Error('润色结果为空')
    }
  } catch (error) {
    console.error('Refine error:', error)
    message.error('润色失败，请重试')
  } finally {
    isRefining.value = false
  }
}

// 添加视图切换状态
const isMarkdownView = ref(true)

// 计算属性：渲染后的Markdown
const renderedMarkdown = computed(() => {
  if (!generatedPrompt.value) return ''
  return md.render(generatedPrompt.value)
})

// 切换视图模式
const toggleView = () => {
  isMarkdownView.value = !isMarkdownView.value
}
</script>

<style scoped>
.prompt-generator {
  width: 100%;
  margin: 0 auto;
  padding: 0;
}

.prompt-output {
  max-height: 600px;
  overflow-y: auto;
  background-color: #fff;
  border-radius: 4px;
  padding: 12px;
}

.code-view {
  font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
}

/* Markdown样式优化 */
.markdown-body {
  padding: 16px;
  font-size: 14px;
  line-height: 1.6;
}

:deep(.markdown-body pre) {
  background-color: #f6f8fa;
  border-radius: 6px;
  padding: 16px;
  overflow: auto;
}

:deep(.markdown-body code) {
  background-color: rgba(175, 184, 193, 0.2);
  border-radius: 6px;
  padding: 0.2em 0.4em;
  font-size: 85%;
}

:deep(.markdown-body pre code) {
  background-color: transparent;
  padding: 0;
}

:deep(.markdown-body h1) {
  padding-bottom: 0.3em;
  font-size: 2em;
  border-bottom: 1px solid #d0d7de;
}

:deep(.markdown-body h2) {
  padding-bottom: 0.3em;
  font-size: 1.5em;
  border-bottom: 1px solid #d0d7de;
}

:deep(.markdown-body blockquote) {
  padding: 0 1em;
  color: #656d76;
  border-left: 0.25em solid #d0d7de;
}

:deep(.markdown-body ul),
:deep(.markdown-body ol) {
  padding-left: 2em;
}

:deep(.markdown-body table) {
  border-spacing: 0;
  border-collapse: collapse;
  margin: 16px 0;
}

:deep(.markdown-body table th),
:deep(.markdown-body table td) {
  padding: 6px 13px;
  border: 1px solid #d0d7de;
}

:deep(.markdown-body table tr:nth-child(2n)) {
  background-color: #f6f8fa;
}

/* 移动端优化 */
@media (max-width: 768px) {
  .prompt-output {
    max-height: 400px;
    padding: 8px;
  }

  .markdown-body {
    padding: 8px;
    font-size: 12px;
  }

  :deep(.markdown-body pre) {
    padding: 8px;
  }
}

.ant-select-selection-item {
  display: flex;
  align-items: center;
}

:deep(.ant-card-head-title) {
  font-size: 1.25rem;
  font-weight: 600;
}

:deep(.ant-form-item-label) {
  font-weight: 500;
}

/* 通用移动端优化 */
@media (max-width: 768px) {
  .prompt-generator {
    padding: 0;
  }
  
  :deep(.ant-card) {
    margin: 0;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }
  
  :deep(.ant-card-head) {
    padding: 16px 16px 0 16px;
    border-bottom: none;
  }
  
  :deep(.ant-card-body) {
    padding: 16px;
  }
  
  :deep(.ant-card-head-title) {
    font-size: 1.1rem;
  }
  
  :deep(.ant-form-item) {
    margin-bottom: 16px;
  }
  
  :deep(.ant-form-item-label) {
    font-size: 14px;
    margin-bottom: 6px;
    font-weight: 600;
  }
  
  :deep(.ant-select-selector) {
    border-radius: 8px;
    min-height: 44px;
    padding: 8px 12px;
  }
  
  :deep(.ant-input) {
    border-radius: 8px;
    min-height: 44px;
    padding: 12px;
    font-size: 16px;
  }
  
  :deep(.ant-btn) {
    border-radius: 8px;
    min-height: 44px;
    font-size: 16px;
  }
  
  :deep(.ant-btn-primary) {
    background: linear-gradient(135deg, #1890ff 0%, #096dd9 100%);
    border: none;
    font-weight: 600;
  }
  
  .prompt-output {
    max-height: 300px;
    font-size: 12px;
    line-height: 1.5;
    padding: 8px;
  }
  
  :deep(.ant-tag) {
    font-size: 10px;
    padding: 2px 6px;
    border-radius: 4px;
  }
}

/* 超小屏幕优化 (iPhone SE 等) */
@media (max-width: 480px) {
  .prompt-generator {
    padding: 0;
  }
  
  :deep(.ant-card-head) {
    padding: 12px 12px 0 12px;
  }
  
  :deep(.ant-card-body) {
    padding: 12px;
  }
  
  :deep(.ant-form-item) {
    margin-bottom: 12px;
  }
  
  :deep(.ant-space) {
    gap: 6px !important;
  }
  
  :deep(.ant-space-item) {
    margin-right: 0 !important;
  }
  
  .prompt-output {
    max-height: 250px;
    padding: 6px;
    font-size: 11px;
  }
  
  :deep(.ant-card-head-title) {
    font-size: 1rem;
  }
  
  :deep(.ant-card-extra) {
    margin-left: 6px;
  }
  
  :deep(.ant-btn-sm) {
    padding: 4px 8px;
    font-size: 12px;
    min-height: 32px;
  }
}

/* 平板优化 */
@media (min-width: 768px) and (max-width: 1024px) {
  .prompt-generator {
    max-width: 700px;
    margin: 0 auto;
    padding: 0 20px;
  }
  
  :deep(.ant-card-body) {
    padding: 20px;
  }
}

/* 桌面端优化 */
@media (min-width: 1025px) {
  .prompt-generator {
    max-width: 800px;
    margin: 0 auto;
    padding: 0 24px;
  }
  
  :deep(.ant-card-body) {
    padding: 24px;
  }
  
  .prompt-output {
    padding: 16px;
  }
}

/* 触摸设备优化 */
@media (hover: none) and (pointer: coarse) {
  :deep(.ant-btn) {
    min-height: 48px;
  }
  
  :deep(.ant-select-selector) {
    min-height: 48px;
  }
  
  :deep(.ant-input) {
    min-height: 48px;
  }
  
  :deep(.ant-textarea) {
    min-height: 48px;
  }
}

/* 防止 iOS Safari 缩放 */
:deep(.ant-input),
:deep(.ant-select-selection-search-input),
:deep(.ant-textarea) {
  font-size: 16px !important;
  -webkit-appearance: none;
}

/* 确保在所有设备上文本可读 */
@media (max-width: 768px) {
  :deep(.ant-input),
  :deep(.ant-select-selector),
  :deep(.ant-btn),
  :deep(.ant-textarea) {
    font-size: 16px !important;
  }
  
  :deep(.ant-input::placeholder),
  :deep(.ant-textarea::placeholder) {
    font-size: 14px;
    color: #bfbfbf;
  }
}

/* 优化滚动体验 */
.prompt-output {
  -webkit-overflow-scrolling: touch;
}

/* 确保卡片在小屏幕上的边距 */
@media (max-width: 640px) {
  :deep(.ant-card) {
    margin: 8px 4px;
    border-radius: 16px;
  }
}

/* 角色选择器优化 */
:deep(.ant-select-item-option-grouped) {
  padding-left: 24px;
}

:deep(.ant-select-item-group) {
  color: #666;
  font-weight: 600;
  font-size: 12px;
  padding: 8px 12px 4px 12px;
  background-color: #fafafa;
}

:deep(.custom-role-option) {
  border-top: 1px solid #f0f0f0;
  margin-top: 4px;
  padding-top: 8px !important;
}

:deep(.custom-role-option .ant-select-item-option-content) {
  font-weight: 500;
}

/* 搜索下拉框优化 */
:deep(.ant-select-dropdown) {
  border-radius: 8px;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.12);
}

:deep(.ant-select-item-option:hover) {
  background-color: #f0f7ff;
}

:deep(.ant-select-item-option-selected) {
  background-color: #e6f7ff;
  font-weight: 500;
}

/* 标签样式优化 */
:deep(.ant-tag) {
  border-radius: 4px;
  font-size: 10px;
  line-height: 1.2;
  padding: 1px 6px;
  margin-right: 6px;
}

/* 提示文字样式 */
.text-gray-400 {
  color: #9ca3af;
  font-size: 12px;
  line-height: 1.4;
}

/* 表单验证样式优化 */
:deep(.ant-form-item-has-error .ant-input) {
  border-color: #ff4d4f;
}

:deep(.ant-form-item-has-error .ant-textarea) {
  border-color: #ff4d4f;
}

:deep(.ant-form-item-explain-error) {
  font-size: 12px;
  margin-top: 4px;
}

/* 字数统计样式 */
:deep(.ant-input-show-count-suffix) {
  color: #bfbfbf;
  font-size: 11px;
}

/* 移动端提示文字优化 */
@media (max-width: 768px) {
  .text-gray-400 {
    font-size: 11px;
    line-height: 1.3;
  }
}

/* 代码块样式优化 */
:deep(.code-block-wrapper) {
  margin: 1em 0;
  border-radius: 8px;
  overflow: hidden;
  background: #f6f8fa;
  border: 1px solid #e1e4e8;
}

:deep(.code-block-header) {
  display: flex;
  align-items: center;
  padding: 8px 16px;
  background: #f1f3f4;
  border-bottom: 1px solid #e1e4e8;
}

:deep(.code-lang) {
  font-size: 12px;
  font-weight: 600;
  color: #57606a;
  text-transform: uppercase;
}

:deep(.markdown-body pre) {
  margin: 0;
  padding: 16px;
  background-color: #f6f8fa;
  border-radius: 0 0 8px 8px;
  overflow-x: auto;
}

:deep(.markdown-body pre code) {
  padding: 0;
  font-size: 14px;
  line-height: 1.6;
  color: #24292e;
  background-color: transparent;
  border-radius: 0;
  white-space: pre;
  font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
}

:deep(.hljs) {
  background: #f6f8fa !important;
  padding: 0 !important;
}

/* 代码高亮颜色主题优化 */
:deep(.hljs-keyword),
:deep(.hljs-selector-tag),
:deep(.hljs-subst) {
  color: #d73a49;
}

:deep(.hljs-string),
:deep(.hljs-doctag) {
  color: #032f62;
}

:deep(.hljs-title),
:deep(.hljs-section),
:deep(.hljs-selector-id) {
  color: #6f42c1;
}

:deep(.hljs-comment),
:deep(.hljs-quote) {
  color: #6a737d;
}

:deep(.hljs-number),
:deep(.hljs-literal) {
  color: #005cc5;
}

:deep(.hljs-variable),
:deep(.hljs-template-variable),
:deep(.hljs-tag) {
  color: #22863a;
}

/* 移动端适配 */
@media (max-width: 768px) {
  :deep(.code-block-header) {
    padding: 6px 12px;
  }

  :deep(.markdown-body pre) {
    padding: 12px;
  }

  :deep(.markdown-body pre code) {
    font-size: 12px;
  }
}
</style> 