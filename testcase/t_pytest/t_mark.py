import os

import pytest

import config
from config.conf import ConfigYaml


class TestApi:
    # 基础用法：传入单个参数
    @pytest.mark.parametrize('args',['name','age'])
    def test_api1(self,args):
        print(args)

    # 拆包用法：传入多个参数
    @pytest.mark.parametrize('name,age',[['shcg','21'],['demn','39']])
    def test_api2(self,name,age):
        print(name,age)

    person_url = ConfigYaml().get_config_person_url()
    home_url = ConfigYaml().get_config_url()

    @pytest.mark.parametrize("args",[(person_url,home_url)])
    def test_api3(self,args):
        print(args)

if __name__ == '__main__':
    pytest.main()
