import json

import pytest
import requests

from config.conf import ConfigYaml, get_config_yaml
from utils.RequestUtil import requests_get, requests_post, Requests


def test_login():
    conf_read = ConfigYaml()
    base_url = conf_read.get_config_url()
    # url = "https://rrwapi.renren.com/account/v1/loginByPassword"
    url = base_url + "/account/v1/loginByPassword"
    data = {
        "user": "15565280933",
        "password": "dc483e80a7a0bd9ef71d8cf973673924",
        "appKey": "bcceb522717c2c49f895b561fa913d10",
        "sessionKey": "betIJALLo2hDnkW0",
        "callId": "1662873700822",
        "sig": "1e8fd64c86805b25acf3be878a958bb2"
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }
    req_api = Requests()
    response = req_api.post_api(url, json=data, headers=headers)
    print("登录---",response)


def test_like():
    conf_read = ConfigYaml()
    base_url = conf_read.get_config_url()
    # url = "https://rrwapi.renren.com/like/v1/send"
    url = base_url + "/like/v1/send"
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
    headers = {
        "Cookie": "Hm_lvt_ad6b0fd84f08dc70750c5ee6ba650172=1662869652; LOCAL_STORAGE_KEY_RENREN_USER_BASIC_INFO=%7B%22userName%22%3A%22%u674E%u5FB7%u5C71%22%2C%22userId%22%3A965194180%2C%22headUrl%22%3A%22http%3A//img.xiaonei.com/photos/0/0/men_head.gif%22%2C%22secretKey%22%3A%22abd9f37587aee6dd2cb45e2d04201891%22%2C%22sessionKey%22%3A%22betIJALLo2hDnkW0%22%7D; Hm_lpvt_ad6b0fd84f08dc70750c5ee6ba650172=1662876037",
    }
    req_api = Requests()
    response = req_api.post_api(url=url, json=data, headers=headers)
    print("主页点赞---",response)


def test_personal():
    conf_read = ConfigYaml()
    base_url = conf_read.get_config_person_url()
    # url="http://www.renren.com/personal/965194180"
    url = base_url + "/personal/965194180"
    headers = {
        "Cookie": "Hm_lvt_ad6b0fd84f08dc70750c5ee6ba650172=1662869652; LOCAL_STORAGE_KEY_RENREN_USER_BASIC_INFO=%7B%22userName%22%3A%22%u674E%u5FB7%u5C71%22%2C%22userId%22%3A965194180%2C%22headUrl%22%3A%22http%3A//img.xiaonei.com/photos/0/0/men_head.gif%22%2C%22secretKey%22%3A%22abd9f37587aee6dd2cb45e2d04201891%22%2C%22sessionKey%22%3A%22betIJALLo2hDnkW0%22%7D; Hm_lpvt_ad6b0fd84f08dc70750c5ee6ba650172=1662876037",
    }
    req = Requests()
    response = req.get_api(url=url, headers=headers)
    print("个人主页---",response)

