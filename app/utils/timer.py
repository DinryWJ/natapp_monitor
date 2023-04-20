import threading
from datetime import datetime, timedelta

from loguru import logger


def __daily_exec(func, args):
    func(args)
    timer = threading.Timer(interval=60, function=__daily_exec, args=(func, args))
    timer.start()


def daily_exec_job(func, args):
    #now = datetime.now()
    # 计算距离下一次执行还需要多少时间
    #seconds = (timedelta(hours=24) - (
            #now - now.replace(hour=hour, minute=0, second=0, microsecond=0))).total_seconds() % (24 * 3600)
    # logger.info(f"下次上报时间{seconds}秒")
    timer = threading.Timer(interval=60, function=__daily_exec, args=(func, args))
    timer.start()
