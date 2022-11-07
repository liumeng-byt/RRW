import os
import yaml



# # TODO 为什么导入下面这个日志方法会报错，而在RequestUtil.py中导入又不报错
# from utils.logutil import Logger


class YamlRead(object):
    def __init__(self, path):
        # self.logs = logs()
        if os.path.exists(path):
            self.path = path
        else:
            raise FileNotFoundError('文件不存在')
        self._data_single = None
        self._data_more = None

    # 读取单段内容方法
    def yaml_read_single(self):
        if not self._data_single:
            try:
                with open(self.path, 'r', encoding='utf-8') as f:
                    self._data_single = yaml.safe_load(f)
                    # logs(__file__).debug("获取%s文件内容(单段)",self.path)
            except Exception as e:
                # self.logs.error("read error")
                # self.logs.error(e)
                print("read eroor")
                print(e)
        return self._data_single

    # 读取多段内容方法
    def yaml_read_more(self):
        if not self._data_more:
            with open(self.path, 'r', encoding='utf-8') as f:
                self._data_more = list(yaml.safe_load_all(f))
                # Logger.logs(__file__).debug("获取%s文件内的多段内容", self.path)
        return self._data_more
