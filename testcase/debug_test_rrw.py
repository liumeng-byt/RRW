import json

import requests

from config.conf import ConfigYaml, get_config_yaml
from utils.colorutil import out_color
from utils.requestutil import requests_get, requests_post, Requests
from utils.assertutil import AssertUtil


def test_login():
    """
    登录成功
    :return:
    """
    conf_read = ConfigYaml()
    base_url = conf_read.get_config_url()
    url = "{}/account/v1/loginByPassword".format(base_url)
    data = {
        "user": "15565280933",
        "password": "dc483e80a7a0bd9ef71d8cf973673924",  # a123456
        "appKey": "bcceb522717c2c49f895b561fa913d10",
    }
    response = requests.request(url=url, json=data, headers=None, method="post")
    json_data = json.loads(response.text)
    print(out_color("->login:{}".format(json.dumps(json_data, indent=2,ensure_ascii=False)),color=31))


def test_like():
    """
    点赞
    :return:
    """
    conf_read = ConfigYaml()
    base_url = conf_read.get_config_url()
    url = "{}/like/v1/send".format(base_url)
    data = {
        "uid": 965194180,
        "like_status": "false",
        "ugc_id": 90000652597,
        "ugc_uid": 965194180,
        "like_id": 90000652597,
        "like_type": 1,
        "pack": "eyJjMSI6OTAwMDA2NTI1OTcsInAzIjozfQ==",
        "liked_status": 1,
        "appKey": "bcceb522717c2c49f895b561fa913d10",
        "sessionKey": "betIJALLo2hDnkW0",
        "callId": "1662875732849",
        "sig": "7a480be5d64ad7e8b856c08bbc00fb70"
    }
    # headers = {
    #     "Cookie": "Hm_lvt_ad6b0fd84f08dc70750c5ee6ba650172=1662869652; LOCAL_STORAGE_KEY_RENREN_USER_BASIC_INFO=%7B%22userName%22%3A%22%u674E%u5FB7%u5C71%22%2C%22userId%22%3A965194180%2C%22headUrl%22%3A%22http%3A//img.xiaonei.com/photos/0/0/men_head.gif%22%2C%22secretKey%22%3A%22abd9f37587aee6dd2cb45e2d04201891%22%2C%22sessionKey%22%3A%22betIJALLo2hDnkW0%22%7D; Hm_lpvt_ad6b0fd84f08dc70750c5ee6ba650172=1662876037",
    # }

    response = Requests().requests_api(url=url, json=data, headers=None, method="post")
    print(out_color("->like:%s" % response, color=31))
    err_assert = AssertUtil()
    err_assert.errorcode_assert(response['body']['errorCode'], 0)


def test_message_list():
    """
    我的留言
    :return:
    """
    conf_read = ConfigYaml()
    base_url = conf_read.get_config_url()
    url = base_url + "/messageboard/v1/getMessageList"
    data = {"ownerId": 965194180, "limit": 10, "offset": 0, "appKey": "bcceb522717c2c49f895b561fa913d10",
            "sessionKey": "betIJALLo2hDnkW0", "callId": "1665308617806", "sig": "6631c13a8188bab18ba268615b76cdb2"}

    response = Requests().requests_api(url=url, json=data, headers=None, method="post")
    print(out_color("->message：%s" % response, color=31))
    err_assert = AssertUtil()
    err_assert.errorcode_assert(response['body']['errorCode'], 0)


if __name__ == '__main__':
    test_login()
    # test_like()
    # test_message_list()
