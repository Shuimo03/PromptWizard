<template>
  <div class="prompt-generator">
    <a-card title="Prompt 生成器" :bordered="false" class="shadow-lg">
      <a-form layout="vertical" :model="formData" @finish="generatePrompt">
        
        <!-- 角色选择区域 -->
        <a-form-item label="选择角色" name="role" class="mb-4 sm:mb-6">
          <a-select
            v-model:value="formData.role"
            placeholder="🔍 搜索角色类型、专业领域或关键词..."
            :size="isMobile ? 'middle' : 'large'"
            show-search
            allow-clear
            :filter-option="filterOption"
            :dropdown-style="{ maxHeight: '400px', overflow: 'auto' }"
          >
            <!-- 编程开发类 -->
            <a-select-opt-group label="💻 编程开发类">
              <a-select-option
                v-for="role in predefinedRoles.filter(r => ['professional-coder', 'fullstack-developer', 'ai-developer', 'devops-engineer'].includes(r.value))"
                :key="role.value"
                :value="role.value"
              >
                <div class="flex items-center">
                  <a-tag :color="role.color" class="mr-2 text-xs">{{ role.tag }}</a-tag>
                  <span class="text-sm sm:text-base">{{ role.label }}</span>
                </div>
              </a-select-option>
            </a-select-opt-group>
            
            <!-- 写作创作类 -->
            <a-select-opt-group label="✏️ 写作创作类">
              <a-select-option
                v-for="role in predefinedRoles.filter(r => ['academic-writer', 'all-around-writer', 'creative-writer', 'copywriter'].includes(r.value))"
                :key="role.value"
                :value="role.value"
              >
                <div class="flex items-center">
                  <a-tag :color="role.color" class="mr-2 text-xs">{{ role.tag }}</a-tag>
                  <span class="text-sm sm:text-base">{{ role.label }}</span>
                </div>
              </a-select-option>
            </a-select-opt-group>
            
            <!-- 分析咨询类 -->
            <a-select-opt-group label="📊 分析咨询类">
              <a-select-option
                v-for="role in predefinedRoles.filter(r => ['data-analyst', 'business-analyst', 'financial-advisor', 'market-researcher'].includes(r.value))"
                :key="role.value"
                :value="role.value"
              >
                <div class="flex items-center">
                  <a-tag :color="role.color" class="mr-2 text-xs">{{ role.tag }}</a-tag>
                  <span class="text-sm sm:text-base">{{ role.label }}</span>
                </div>
              </a-select-option>
            </a-select-opt-group>
            
            <!-- 教育培训类 -->
            <a-select-opt-group label="🎓 教育培训类">
              <a-select-option
                v-for="role in predefinedRoles.filter(r => ['tutor', 'language-teacher', 'skill-trainer'].includes(r.value))"
                :key="role.value"
                :value="role.value"
              >
                <div class="flex items-center">
                  <a-tag :color="role.color" class="mr-2 text-xs">{{ role.tag }}</a-tag>
                  <span class="text-sm sm:text-base">{{ role.label }}</span>
                </div>
              </a-select-option>
            </a-select-opt-group>
            
            <!-- 设计创意类 -->
            <a-select-opt-group label="🎨 设计创意类">
              <a-select-option
                v-for="role in predefinedRoles.filter(r => ['ui-designer', 'graphic-designer', 'brand-strategist'].includes(r.value))"
                :key="role.value"
                :value="role.value"
              >
                <div class="flex items-center">
                  <a-tag :color="role.color" class="mr-2 text-xs">{{ role.tag }}</a-tag>
                  <span class="text-sm sm:text-base">{{ role.label }}</span>
                </div>
              </a-select-option>
            </a-select-opt-group>
            
            <!-- 专业服务类 -->
            <a-select-opt-group label="🌐 专业服务类">
              <a-select-option
                v-for="role in predefinedRoles.filter(r => ['translator', 'legal-advisor', 'career-coach', 'health-consultant'].includes(r.value))"
                :key="role.value"
                :value="role.value"
              >
                <div class="flex items-center">
                  <a-tag :color="role.color" class="mr-2 text-xs">{{ role.tag }}</a-tag>
                  <span class="text-sm sm:text-base">{{ role.label }}</span>
                </div>
              </a-select-option>
            </a-select-opt-group>
            
            <!-- 技术专家类 -->
            <a-select-opt-group label="🔧 技术专家类">
              <a-select-option
                v-for="role in predefinedRoles.filter(r => ['seo-expert', 'security-expert', 'blockchain-expert'].includes(r.value))"
                :key="role.value"
                :value="role.value"
              >
                <div class="flex items-center">
                  <a-tag :color="role.color" class="mr-2 text-xs">{{ role.tag }}</a-tag>
                  <span class="text-sm sm:text-base">{{ role.label }}</span>
                </div>
              </a-select-option>
            </a-select-opt-group>
            
            <!-- 研究学术类 -->
            <a-select-opt-group label="🔬 研究学术类">
              <a-select-option
                v-for="role in predefinedRoles.filter(r => ['researcher', 'academic-reviewer', 'patent-analyst'].includes(r.value))"
                :key="role.value"
                :value="role.value"
              >
                <div class="flex items-center">
                  <a-tag :color="role.color" class="mr-2 text-xs">{{ role.tag }}</a-tag>
                  <span class="text-sm sm:text-base">{{ role.label }}</span>
                </div>
              </a-select-option>
            </a-select-opt-group>
            
            <!-- 创业商业类 -->
            <a-select-opt-group label="🚀 创业商业类">
              <a-select-option
                v-for="role in predefinedRoles.filter(r => ['startup-mentor', 'product-manager', 'growth-hacker'].includes(r.value))"
                :key="role.value"
                :value="role.value"
              >
                <div class="flex items-center">
                  <a-tag :color="role.color" class="mr-2 text-xs">{{ role.tag }}</a-tag>
                  <span class="text-sm sm:text-base">{{ role.label }}</span>
                </div>
              </a-select-option>
            </a-select-opt-group>
            
            <!-- 生活助手类 -->
            <a-select-opt-group label="🌟 生活助手类">
              <a-select-option
                v-for="role in predefinedRoles.filter(r => ['life-coach', 'travel-planner', 'cooking-expert'].includes(r.value))"
                :key="role.value"
                :value="role.value"
              >
                <div class="flex items-center">
                  <a-tag :color="role.color" class="mr-2 text-xs">{{ role.tag }}</a-tag>
                  <span class="text-sm sm:text-base">{{ role.label }}</span>
                </div>
              </a-select-option>
            </a-select-opt-group>
            
            <!-- 自定义选项 -->
            <a-select-option value="custom" class="custom-role-option">
              <div class="flex items-center text-blue-600 font-medium">
                <PlusOutlined class="mr-2" />
                <span class="text-sm sm:text-base">🎯 自定义专业角色</span>
              </div>
            </a-select-option>
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
              </a-space>
            </template>
            
            <div class="prompt-output">
              <pre class="whitespace-pre-wrap leading-relaxed" 
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
  ThunderboltOutlined 
} from '@ant-design/icons-vue'
import MagicWandOutlined from './icons/MagicWandOutlined.vue'

// 响应式数据
const formData = reactive({
  role: '',
  customRole: '',
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

// 生成Prompt函数
const generatePrompt = async () => {
  // 只验证期望目标是否填写，补充信息为可选
  if (!formData.expectation.trim()) {
    message.warning('请填写期望目标')
    return
  }

  // 验证角色选择
  if (!formData.role) {
    message.warning('请选择一个角色')
    return
  }

  let roleText = ''
  if (formData.role === 'custom') {
    if (!formData.customRole.trim()) {
      message.warning('请输入自定义角色')
      return
    }
    roleText = formData.customRole.trim()
  } else {
    const selectedRole = predefinedRoles.value.find(r => r.value === formData.role)
    if (selectedRole) {
      // 正确处理emoji和角色名称
      roleText = selectedRole.label.replace(/^[\u{1F000}-\u{1F6FF}]|^[\u{1F900}-\u{1F9FF}]|^[\u{2600}-\u{26FF}]|^[\u{2700}-\u{27BF}]|^[\u{1F680}-\u{1F6FF}]|^[\u{1F1E0}-\u{1F1FF}]/gu, '').trim()
    } else {
      roleText = '专业助手'
    }
  }

  isGenerating.value = true
  
  try {
    // 模拟API调用延迟
    await new Promise(resolve => setTimeout(resolve, 1500))
    
    // 根据角色类型智能生成更详细的Prompt
    const roleCategory = getRoleCategory(formData.role)
    const prompt = generateIntelligentPrompt(roleText, formData.expectation.trim(), formData.background.trim(), roleCategory)

    generatedPrompt.value = prompt
    message.success('🎉 Prompt 生成成功！')
  } catch (error) {
    message.error('生成失败，请重试')
  } finally {
    isGenerating.value = false
  }
}

// 获取角色类别
const getRoleCategory = (roleValue) => {
  const categories = {
    'programming': ['professional-coder', 'fullstack-developer', 'ai-developer', 'devops-engineer'],
    'writing': ['academic-writer', 'all-around-writer', 'creative-writer', 'copywriter'],
    'analysis': ['data-analyst', 'business-analyst', 'financial-advisor', 'market-researcher'],
    'education': ['tutor', 'language-teacher', 'skill-trainer'],
    'design': ['ui-designer', 'graphic-designer', 'brand-strategist'],
    'service': ['translator', 'legal-advisor', 'career-coach', 'health-consultant'],
    'tech': ['seo-expert', 'security-expert', 'blockchain-expert'],
    'research': ['researcher', 'academic-reviewer', 'patent-analyst'],
    'business': ['startup-mentor', 'product-manager', 'growth-hacker'],
    'lifestyle': ['life-coach', 'travel-planner', 'cooking-expert']
  }
  
  for (const [category, roles] of Object.entries(categories)) {
    if (roles.includes(roleValue)) return category
  }
  return 'general'
}

// 智能生成Prompt
const generateIntelligentPrompt = (roleText, expectation, background, category) => {
  // 根据角色类别定制专业要求
  const categoryRequirements = {
    'programming': [
      '使用最佳实践和行业标准',
      '提供清晰的代码示例和注释',
      '考虑性能、安全性和可维护性',
      '解释技术选择的原因'
    ],
    'writing': [
      '确保内容结构清晰、逻辑连贯',
      '使用适当的语言风格和语调',
      '注意目标受众和使用场景',
      '提供具体的写作技巧和建议'
    ],
    'analysis': [
      '基于数据和事实进行分析',
      '提供清晰的分析框架和方法',
      '使用图表或可视化说明（如适用）',
      '给出可执行的建议和结论'
    ],
    'design': [
      '遵循设计原则和用户体验最佳实践',
      '考虑目标用户和使用场景',
      '提供具体的设计建议和解决方案',
      '解释设计决策的依据'
    ],
    'general': [
      '提供专业、准确的信息',
      '使用清晰、易懂的表达方式',
      '给出实用的建议和指导',
      '确保内容的完整性和实用性'
    ]
  }

  const requirements = categoryRequirements[category] || categoryRequirements['general']

  let prompt = `# 角色设定
你是一位经验丰富的${roleText}，在相关领域有深厚的专业知识和实践经验。

# 任务目标
${expectation}`

  if (background) {
    prompt += `

# 补充信息
${background}`
  }

  prompt += `

# 专业要求
${requirements.map((req, index) => `${index + 1}. ${req}`).join('\n')}

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
    // 模拟润色API调用
    await new Promise(resolve => setTimeout(resolve, 2000))
    
    // 智能润色：添加更多实用的指导元素
    let refinedPrompt = generatedPrompt.value
    
    // 在专业要求后添加思维方法指导
    if (refinedPrompt.includes('# 专业要求')) {
      refinedPrompt = refinedPrompt.replace(
        '# 输出格式',
        `# 思维方法
请采用以下思维方式来处理任务：
1. **系统性思考**：全面考虑问题的各个方面和影响因素
2. **用户导向**：始终以用户需求和体验为中心
3. **实用性优先**：提供可操作、可执行的具体方案
4. **持续优化**：考虑长期发展和改进空间

# 输出格式`
      )
    }
    
    // 在输出格式最后添加质量控制
    if (refinedPrompt.includes('请开始你的专业回答：')) {
      refinedPrompt = refinedPrompt.replace(
        '请开始你的专业回答：',
        `## ✅ 质量检查
请在回答前确认：
- [ ] 内容是否专业准确
- [ ] 建议是否具体可行
- [ ] 格式是否清晰易读
- [ ] 是否满足所有要求

请开始你的专业回答：`
      )
    }
    
    // 如果是编程相关角色，添加代码规范提醒
    if (formData.role && ['professional-coder', 'fullstack-developer', 'ai-developer', 'devops-engineer'].includes(formData.role)) {
      refinedPrompt = refinedPrompt.replace(
        '请开始你的专业回答：',
        `## 💻 代码规范提醒
如需提供代码示例，请确保：
- 代码格式规范，有适当的注释
- 包含必要的错误处理
- 考虑安全性和性能
- 提供测试用例（如适用）

请开始你的专业回答：`
      )
    }
    
    // 如果是写作相关角色，添加写作质量提醒
    if (formData.role && ['academic-writer', 'all-around-writer', 'creative-writer', 'copywriter'].includes(formData.role)) {
      refinedPrompt = refinedPrompt.replace(
        '请开始你的专业回答：',
        `## ✍️ 写作质量提醒
请确保写作内容：
- 语言准确，表达清晰
- 逻辑严密，结构合理
- 符合目标读者的阅读水平
- 有吸引力和说服力

请开始你的专业回答：`
      )
    }
    
    generatedPrompt.value = refinedPrompt
    message.success('✨ Prompt 润色完成！已添加专业指导元素')
  } catch (error) {
    message.error('润色失败，请重试')
  } finally {
    isRefining.value = false
  }
}
</script>

<style scoped>
.prompt-generator {
  width: 100%;
  margin: 0 auto;
  padding: 0;
}

.prompt-output {
  max-height: 400px;
  overflow-y: auto;
  font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
  background-color: #fff;
  border-radius: 4px;
  padding: 12px;
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
</style> 