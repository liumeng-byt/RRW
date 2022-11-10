import os
import yaml

from utils.logutil import Logger


class YamlRead(object):
    def __init__(self, path):
        # self.logs = Logger.logs(__file__)
        if os.path.exists(path):
            self.path = path
        else:
            Logger.logs(__file__).error("文件不存在")
            raise FileNotFoundError('文件不存在')
        self._data_single = None
        self._data_more = None

    # 读取单段内容方法
    def yaml_read_single(self):
        if not self._data_single:
            try:
                with open(self.path, 'r', encoding='utf-8') as f:
                    self._data_single = yaml.safe_load(f)
                    # Logger.logs(__file__).debug("获取%s文件内容(单段)", self.path)  # TODO 报错
            except Exception as e:
                # Logger.logs(__file__).error("e")
                print("读取单段文件失败".format(e))
                return

        return self._data_single

    # 读取多段内容方法
    def yaml_read_more(self):
        if not self._data_more:
            try:
                with open(self.path, 'r', encoding='utf-8') as f:
                    self._data_more = list(yaml.safe_load_all(f))
                    # Logger.logs(__file__).debug("获取%s文件内的多段内容", self.path)
            except Exception as e:
                Logger.logs(__file__).error("多段文件读取失败")
        return self._data_more
