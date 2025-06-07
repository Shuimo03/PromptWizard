from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.routers import prompt
from app.service.dify import DifyService
import yaml

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 加载配置
    with open("app/config/dev.yaml", "r") as f:
        config = yaml.safe_load(f)

    # 初始化服务
    app.state.dify_service = DifyService(
        api_key=config["dify"]["APIKEY"],
        base_url=config["dify"]["APIServer"]
    )
    
    yield  # 应用运行期间
    
    # 清理资源
    await app.state.dify_service.close()

def create_app() -> FastAPI:
    app = FastAPI(
        title="PromptWizard API",
        description="API for optimizing prompts using Dify",
        version="0.1.0",
        lifespan=lifespan
    )

    # CORS 中间件
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 注册路由
    app.include_router(prompt.router)

    return app

app = create_app()

@app.get("/")
async def root():
    return {"message": "Welcome to PromptWizard API"}
