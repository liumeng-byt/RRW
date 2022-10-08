import os

from utils.yamlutil import YamlRead

# 获取当前文件的绝对路径
current_file_absolute = os.path.abspath(__file__)
# print(current_file_absolute)

# 获取项目的绝对路径
PROJECT_PATH_ABSOLUTE = os.path.dirname(os.path.dirname(current_file_absolute))
# print(PROJECT_PATH_ABSOLUTE)

# config文件夹路径
_config_dir_path = PROJECT_PATH_ABSOLUTE + os.sep + "config"

# data文件夹路径
_data_dir_path = PROJECT_PATH_ABSOLUTE + os.sep + "data"

# conf.yml文件路径
_config_yaml_path = _config_dir_path + os.sep + "conf.yml"

# lodin_data文件路径
_login_data_yml_path = _data_dir_path + os.sep + "login_data.yml"

# logs日志文件夹路径
_config_logs_path = PROJECT_PATH_ABSOLUTE + os.sep + "logs"

# db_conf.yml文件路径
_db_config_yaml_path = _config_dir_path + os.sep + "db_conf.yml"

# 返回data文件夹路径
def get_data_path():
    return _data_dir_path


# 返回login_data_yml路径
def get_login_data_path():
    return _login_data_yml_path

# 为私有变量返回给外部
def get_config_path():
    return _config_dir_path


# 为私有变量返回给外部
def get_config_yaml():
    return _config_yaml_path


def get_db_config_yaml():
    return _db_config_yaml_path


def get_logs_path():
    return _config_logs_path


class ConfigYaml:
    def __init__(self):
        self.config = YamlRead(get_config_yaml()).yaml_read_single()  # 读取conf.yml
        self.db_config = YamlRead(get_db_config_yaml()).yaml_read_single()   # 读取db_conf.yml

    def get_excel_name(self):
        """
        返回测试用例文件名
        :return:
        """
        self.excel_name =self.config['BASE']['excel']['excel_name']
        return self.excel_name

    def get_excel_sheet_by(self):
        """
        返回测试用例文件的sheet名称
        :return:
        """
        self.sheet_by =self.config['BASE']['excel']['sheet_by']
        return self.sheet_by

    def get_config_url(self):
        """
        获取url
        :return:
        """
        self.url = self.config['BASE']['test']['url']
        # print(self.url)
        return self.url

    def get_config_person_url(self):
        """
        获取个人中心url
        :return:
        """
        self.url = self.config['BASE']['test']['url_person']
        return self.url

    def get_config_loglevel(self):
        """
        获取日志级别
        :return:
        """
        self.log_level = self.config['BASE']['test']['log_level']
        return self.log_level

    def get_config_extension(self):
        """
        获取日志扩展名
        :return:
        """
        self.log_extension = self.config['BASE']['test']['log_extension']
        return self.log_extension

    def get_db_config_yml(self, db):
        """
        获取db_conf.yml文件内容,根据db_alias获取该名称下的数据信息
        :return:
        """
        return self.db_config[db]

# if __name__ == '__main__':
#     ConfigYaml().get_excel_sheet_by()