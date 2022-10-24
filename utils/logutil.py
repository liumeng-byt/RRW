import logging
import datetime
import os

from config import conf

level = {
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "warning": logging.WARNING,
    "error": logging.ERROR
}


class Logger:
    def __init__(self, log_save_file, log_read_name, log_level):
        self.log_save_file = log_save_file
        self.log_read_name = log_read_name
        self.log_level = log_level

        self.logger = logging.getLogger(self.log_read_name)  # 设置日志名称
        self.logger.setLevel(level[self.log_level])  # 设置日志级别

        if not self.logger.handlers:
            # 输出到控制台
            handler_console = logging.StreamHandler()  # 创建控制台handler
            handler_console.setLevel(level[self.log_level])  # 创建控制台日志级别
            formater = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
            handler_console.setFormatter(formater)  # 定义输出格式

            # 输出到文件
            handler_file = logging.FileHandler(self.log_save_file)
            handler_file.setLevel(level[self.log_level])
            handler_file.setFormatter(formater)

            # 添加到hander
            self.logger.addHandler(handler_console)
            self.logger.addHandler(handler_file)


# 在yamlutils.py中导入日志方法logs使用时会报错，但是在RequestUtil.py中导入使用又不报错，只能把写死
log_path = conf.get_logs_path()  # logs文件夹路径
log_extension = conf.ConfigYaml().get_config_extension()  # log扩展名
loglevel = conf.ConfigYaml().get_config_loglevel()  # 日志级别

# 在yamlutils.py中导入日志方法logs使用时会报错，但是在RequestUtil.py中导入使用又不报错，只能把写死
# log_path= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+os.sep + "logs" # logs文件夹路径
# log_extension = ".log"  # log扩展名
# loglevel = "debug"  # 日志级别

# current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 当前时间  时间中的冒号，会报错，可以换成-
# current_time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")  # 当前时间
current_time = datetime.datetime.now().strftime("%Y-%m-%d")  # 当前时间
log_save_file = os.path.join(log_path, current_time + log_extension)  # 日志文件名称


# 定义方法，返回外部使用
def logs(log_path=__file__):
    return Logger(log_save_file=log_save_file, log_read_name=log_path, log_level=loglevel).logger
