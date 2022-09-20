import logging
"""-----------------------------------输出到控制台---------------------------------------------------------------------------"""
# 1、设置log名称(设置日志文件)
logger = logging.getLogger('log_file_demo')

# 2、设置log级别
logger.setLevel(logging.INFO)

# 3、创建handler对象
handler = logging.StreamHandler()

# 4、设置日志级别
handler.setLevel(logging.INFO)

# 5、定义输出格式
formater = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
handler.setFormatter(formater)

# 6、添加到handler对象
logger.addHandler(handler)
# 7、运行输出


"""-----------------------------------输出到文件---------------------------------------------------------------------------"""
# 1、设置log名称(设置日志文件)
logger = logging.getLogger('log_file_demo')

# 2、设置log级别
logger.setLevel(logging.INFO)

# 3、创建handler对象
handler = logging.FileHandler("./test.log")

# 4、设置日志级别
handler.setLevel(logging.INFO)

# 5、定义输出格式
formater = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
handler.setFormatter(formater)

# 6、添加到handler对象
logger.addHandler(handler)
# 7、运行输出

logger.info("我是-info")
logger.debug("我是-debug")