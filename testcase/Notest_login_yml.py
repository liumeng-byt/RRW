import pytest

from config.conf import get_login_data_path, ConfigYaml
from utils.assertutil import AssertUtil
from utils.requestutil import Requests
from utils.yamlutil import YamlRead

ip = ConfigYaml().get_config_url()
res_data = YamlRead(get_login_data_path()).yaml_read_more()


@pytest.mark.parametrize("data", res_data)
def test_login(data):
    print(data)
    url = ip + data['path']
    data = data['data']
    res = Requests().post_api(url=url, json=data)
    AssertUtil().errorcode_assert(res['body']['errorCode'], data['expect_errorCode'])

# if __name__ == '__main__':
#     pytest.main(["-s","Notest_login_yml.py","--html=./report/repot.html"])
