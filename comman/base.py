import subprocess

from config.conf import ConfigYaml
from utils.logutil import Logger
# from utils.logutil import logs
from utils.mysqlutil import MysqlUtile


def init_db(db_alias):
    # 初始化数据化信息，获取数据
    db_info = ConfigYaml().get_db_config_yml(db_alias)
    hsot = db_info["db_host"]
    user = db_info["db_user"]
    password = db_info["db_password"]
    db_name = db_info["db_name"]
    charset = db_info["db_charset"]
    port = int(db_info["db_port"])
    # 初始化mysql对象
    conn = MysqlUtile(host=hsot, user=user, password=password, database=db_name, port=port)
    return conn


def allure_report(allure_json, allure_index):
    """
    根据生成的json文件自动生成报告
    :param allure_json: json文件路径
    :param allure_index: 报告路径
    :return:
    """
    # allure_cmd = "allure generate ../report/result -o ../report/html --clean"
    allure_cmd = "allure generate %s -o %s --clean" % (allure_json, allure_index)
    print("：\nallure_json_path：%s\nallure_index_path：%s" % (allure_json, allure_index))
    try:
        subprocess.call(allure_cmd, shell=True)
    except:
        Logger.logs(__file__).error("生成报告失败")
        raise
