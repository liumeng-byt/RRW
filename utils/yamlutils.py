import os

import yaml


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
        return self._data_single

    def yaml_read_more(self):
        if not self._data_more:
            with open(self.path,'r',encoding='utf-8') as f:
                self._data_more = list(yaml.safe_load_all(f))
        return self._data_more