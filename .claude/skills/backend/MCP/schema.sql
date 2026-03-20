-- PromptWizard Database Schema
-- 使用 postgres-mcp 执行: execute_sql

-- 创建用户表
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT true
);

-- 创建 Prompt 表
CREATE TABLE IF NOT EXISTS prompts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    background TEXT NOT NULL,
    role TEXT NOT NULL,
    expectation TEXT NOT NULL,
    generated_prompt TEXT,
    score INTEGER CHECK (score >= 0 AND score <= 100),
    source VARCHAR(50) DEFAULT 'manual',
    model VARCHAR(100),
    tokens INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 创建 Prompt 标签关联表
CREATE TABLE IF NOT EXISTS prompt_tags (
    prompt_id UUID NOT NULL REFERENCES prompts(id) ON DELETE CASCADE,
    tag VARCHAR(100) NOT NULL,
    PRIMARY KEY (prompt_id, tag)
);

-- 创建索引
CREATE INDEX IF NOT EXISTS idx_prompts_user_id ON prompts(user_id);
CREATE INDEX IF NOT EXISTS idx_prompts_created_at ON prompts(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_prompts_score ON prompts(score DESC);
CREATE INDEX IF NOT EXISTS idx_prompt_tags_tag ON prompt_tags(tag);

-- 启用 pg_stat_statements 用于慢查询分析（如需要）
-- CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
