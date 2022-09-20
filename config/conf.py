import os

# from utils.logutil import logs
from utils.yamlutils import YamlRead

# 获取当前文件的绝对路径
current_file_absolute = os.path.abspath(__file__)
# print(current_file_absolute)

# 获取项目的绝对路径
PROJECT_PATH_ABSOLUTE = os.path.dirname(os.path.dirname(current_file_absolute))
# print(PROJECT_PATH_ABSOLUTE)


# config文件夹路径
_config_dir_path = PROJECT_PATH_ABSOLUTE + os.sep + "config"
# conf.yml文件路径
_config_yaml_path = _config_dir_path + os.sep + "conf.yml"
# logs日志文件夹路径
_config_logs_path = PROJECT_PATH_ABSOLUTE + os.sep + "logs"



# 为私有变量返回给外部
def get_config_path():
    return _config_dir_path


# 为私有变量返回给外部
def get_config_yaml():
    return _config_yaml_path

def get_logs_path():
    return _config_logs_path


class ConfigYaml(object):
    def __init__(self):
        self.config = YamlRead(get_config_yaml()).yaml_read_single()

    def get_config_url(self):
        """
        获取url
        :return:
        """
        self.url = self.config['BASE']['test']['url']
        # logs("conf").debug("获取主页url：%s",self.url)
        return self.url

    def get_config_person_url(self):
        """
        获取个人中心url
        :return:
        """
        self.url = self.config['BASE']['test']['url_person']
        # logs("conf").debug("获取个人中心url：%s", self.url)
        return self.url

    def get_config_loglevel(self):
        """
        获取日志级别
        :return:
        """
        self.log_level = self.config['BASE']['test']['log_level']
        # logs("conf").debug("获取日志级别：%s", self.log_level)
        return self.log_level

    def get_config_extension(self):
        """
        获取日志扩展名
        :return:
        """
        self.log_extension = self.config['BASE']['test']['log_extension']
        # logs("conf").debug("获取日志扩展名：%s", self.log_extension)
        return self.log_extension


# if __name__ == '__main__':
#     conf_read = ConfigYaml()
#     # data = conf_read.get_config_url()
#     # print(data)
#     # print(conf_read.get_config_extension())
#     # print(conf_read.get_config_loglevel())
#     pass
