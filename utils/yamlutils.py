import os
import yaml


# TODO 为什么导入下面这个日志方法会报错，而在RequestUtil.py中导入又不报错
# from utils.logutil import logs


class YamlRead(object):
    def __init__(self, path):
        if os.path.exists(path):
            self.path = path
        else:
            raise FileNotFoundError('文件不存在')
        self._data_single = None
        self._data_more = None

    # 读取单段内容方法
    def yaml_read_single(self):
        if not self._data_single:
            with open(self.path, 'r', encoding='utf-8') as f:
                self._data_single = yaml.safe_load(f)
                # logs("yamlutils").debug("读取了%s文件内的单段内容",self.path)
        return self._data_single

    def yaml_read_more(self):
        if not self._data_more:
            with open(self.path,'r',encoding='utf-8') as f:
                self._data_more = list(yaml.safe_load_all(f))
                # logs("yamlutils").debug("读取了%s文件内的多段内容", self.path)
        return self._data_more