# encoding=utf-8
import json
import os, pytest

import allure
from comman.excelconfig import ExcelConfig
from comman.exceldata import ExcelData
from config.conf import ConfigYaml, get_data_path, get_report_path, get_report_json_path, get_report_index_path

# 初始化用例文件、sheet名称、日志
from utils.assertutil import AssertUtil
from utils.colorutil import out_color
from utils.logutil import Logger
# from utils.logutil import logs
from utils.requestutil import Requests

excel_name = ConfigYaml().get_excel_name()  # excel文件名称
excel_path = os.path.join(get_data_path(), excel_name)  # excel文件路径
excel_sheet = ConfigYaml().get_excel_sheet_by()  # sheet名称
run_init = ExcelData(excel_path, excel_sheet)
run_list = run_init.get_run_case()  # 运行的用例列表
excel_config = ExcelConfig()  # 属性
log = Logger.logs(__file__)


class TestExcel(object):
    @pytest.mark.parametrize("data", run_list)
    def test_login(self, data):
        # print(data)
        path = data[excel_config.path]
        url_other = ConfigYaml().get_config_url()
        url_home = ConfigYaml().get_config_person_url()
        prepose_condition = data[excel_config.prepose_condition]
        case_model = data[excel_config.case_model]
        expect_result = data[excel_config.expect_result]
        case_id = data[excel_config.case_id]
        case_name = data[excel_config.case_name]
        method = data[excel_config.method]
        error_code = data[excel_config.errorcode]
        if data[excel_config.case_model] == "主页":
            url = url_home + path
        else:
            url = url_other + path

        if len(str(data[excel_config.params])) > 0:
            try:
                params = json.loads(data[excel_config.params].strip())  # 列表中嵌套字典，字典中又是str，所以请求参数需要转换为dict类型
            except:
                try:
                    params = eval(data[excel_config.params])
                except Exception as e:
                    Logger.logs(__file__).error(e)
                    print("str转换为dict出错")
                    return
        else:
            params = {}  # 默认是str，必须重新定义为dict Type
        if len(str(data[excel_config.headers])) > 0:
            try:
                headers = json.loads(data[excel_config.headers].strip())
            except:
                try:
                    headers = eval(data[excel_config.headers])
                except Exception as e:
                    Logger.logs(__file__).error(e)
                    # print("headers--str转换为dict出错")
                    return
        else:
            headers = {}  # 默认是str，必须重新定义为dict Type
        response = Requests().requests_api(url=url, json=params, method=method, headers=headers)
        data = "\n->%s--%s--%s:" % (data[excel_config.case_id], data[excel_config.case_name], response)
        print(out_color(data, color=34))
        allure.dynamic.feature(excel_sheet)  # 一级标签-sheet名称
        allure.dynamic.story(case_model)  # 二级标签-模块名称
        allure.dynamic.title(case_id + case_name)
        desc = "请求URL:{}" \
               "请求类型:{}" \
               "期望结果:{}" \
               "实际结果:{}".format(url + "\n\n", method + "\n\n", expect_result + "\n\n", response)
        allure.dynamic.description(desc)
        err_assert = AssertUtil()
        # if case_id in ("message_01", "like_01"):
        if error_code is not None:
            err_assert.errorcode_assert(response['body']['errorCode'], 0)
        else:
            log.error("AssertError,error_code之外的断言方法暂未设置")

# if __name__ == '__main__':
#     pytest.main(["-s", "test_login_excel.py"])
#     # os.system("allure generate ../report/result -o ../report/html --clean")
#     # subprocess.call("allure generate ../report/result -o ../report/html --clean", shell=True)
#     base.allure_report(get_report_json_path(),get_report_index_path())  # 通过json生成html
