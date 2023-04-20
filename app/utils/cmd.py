import subprocess

from loguru import logger


def exec_cmd(cmd_string):
    """
    执行cmd命令，并得到执行后的返回值,python调试界面不输出返回值
    :param cmd_string: cmd命令，如：'adb devices"'
    :return:
    """
    logger.info('运行cmd指令：{}'.format(cmd_string))
    p = subprocess.Popen(cmd_string, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.stdout.readlines()


def simple_exec_cmd(cmd_string):
    """
    执行cmd命令，返回执行的结果 0成功
    :param cmd_string: cmd命令，如：'adb devices"'
    :return:
    """
    logger.info('运行cmd指令：{}'.format(cmd_string))
    return subprocess.check_call(cmd_string, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)


def exec_cmd_wait(cmd_string):
    logger.info('运行cmd指令：{}'.format(cmd_string))
    p = subprocess.Popen(cmd_string, shell=True)
    return p.wait()


if __name__ == "__main__":
    import sys

    print(sys.argv)
    res = exec_cmd(sys.argv[1])
    print(res)
    print(len(res))
