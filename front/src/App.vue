<script setup>
import PromptGenerator from './components/PromptGenerator.vue'
</script>

<template>
  <div id="app">
    <a-layout class="min-h-screen bg-gray-50">
      <a-layout-header class="bg-white shadow-sm">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8">
          <h1 class="text-xl sm:text-2xl font-bold text-blue-600 m-0 leading-relaxed">
            PromptWizard
          </h1>
          <p class="text-gray-500 m-0 text-sm sm:text-base">智能化 Prompt 生成工具</p>
        </div>
      </a-layout-header>
      
      <a-layout-content class="p-4 sm:p-6 flex-1">
        <div class="container mx-auto max-w-4xl">
          <PromptGenerator />
        </div>
      </a-layout-content>
    </a-layout>
  </div>
</template>

<style scoped>
.ant-layout-header {
  height: auto;
  line-height: normal;
  padding: 12px 0;
}

/* 移动端适配 */
@media (max-width: 640px) {
  .ant-layout-header {
    padding: 8px 0;
  }
}

/* 确保容器在小屏幕上的适当边距 */
@media (max-width: 768px) {
  .container {
    padding-left: 0.5rem;
    padding-right: 0.5rem;
  }
}

/* 确保布局占满全屏 */
.ant-layout {
  min-height: 100vh;
}

.flex-1 {
  flex: 1;
}

.bg-gray-50 {
  background-color: #f9fafb;
}
</style>
