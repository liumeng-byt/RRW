import json
import os

import allure
import pytest
import requests

from config.conf import get_login_data_path, ConfigYaml
from utils.colorutil import out_color
from utils.yamlutil import YamlRead

ip = ConfigYaml().get_config_url()
res_data = YamlRead(get_login_data_path()).yaml_read_more()


class TestYaml(object):
    @pytest.mark.parametrize("datas", res_data)
    def test_login(self, datas):
        url = ip + datas['path']
        data = datas['data']
        case_id = datas["case_id"]
        case_name = datas["case_name"]
        res = requests.post(url=url, json=data)
        result = "\n->%s--%s--%s:" % (case_id,case_name,res.json())
        print(out_color(result,color=32))
        # TODO 以下两个插件设置后在报告中不起效
        # allure.dynamic.feature("login")  # 一级标签-sheet名称
        # allure.dynamic.story("login")  # 二级标签-模块名称
        allure.dynamic.title(datas["case_id"] + datas["case_name"])
        desc = "请求URL:{}" \
               "请求类型:{}" \
               "期望结果:{}" \
               "实际结果:{}".format(url + "\n\n", "post" + "\n\n", "{dynamic}" + "\n\n", res.json())

        allure.dynamic.description(desc)
        if data['password'] == "dc483e80a7a0bd9ef71d8cf973673924":
            assert res.json()['errorCode'] == 0
        else:
            assert res.json()['errorCode'] == 1129013

