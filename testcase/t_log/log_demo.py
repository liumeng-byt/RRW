import logging

# 参数配置
logging.basicConfig(level=logging.WARNING,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')

# 配置日志文件
logging.getLogger("log_demo")

# 测试
logging.info("info")
logging.debug("debug")
logging.warning("warning")