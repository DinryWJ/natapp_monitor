

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from app.utils.cmd import simple_exec_cmd
from app.utils.thread import run_async

LOG_PATH = "logs/"


app = FastAPI(
    title="natapp monitor",
    version="1.0.0"
)



@app.on_event('startup')
def init():
    """
    初始化
    """
    # 配置允许域名列表、允许方法、请求头、cookie等
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    logger.add(LOG_PATH + "server.log", rotation="1 day", retention="30 days", compression="tar.gz")
    # 启动docker event监听
    run_async("startNatapp", simple_exec_cmd, (f"sh listenDispatcher.sh", ))
    logger.info("docker-maintain-server开机启动完成")


@app.get("/")
def root():
    return {"message": "hello world", "data": None}
