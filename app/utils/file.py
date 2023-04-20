import time




def follow_file(file, end_str):
    """
    持续获取新增的日志
    :param file: 日志文件
    """
    # 持续没产生新日志的秒数
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(1)
            continue
        if line.endswith(end_str):
            # 发送消息
            break
        yield line
    yield line

