import requests

from utils.logutil import logs

def requests_get(url, json=None, headers=None):
    """
    get请求封装
    :param url:
    :param json:
    :param headers:
    :return:
    """
    response = requests.get(url=url, json=json, headers=headers)
    code = response.status_code
    try:
        body = response.json()
    except Exception as e:
        body = response.text
    # res = dict()
    # response_dict = {}
    response_dict =dict()
    response_dict["code"] = code
    response_dict["body"] = body
    return response_dict


def requests_post(url, json=None, headers=None):
    """
    post请求封装
    :param url:
    :param json:
    :param headers:
    :return:
    """
    response = requests.post(url=url, json=json, headers=headers)
    code = response.status_code
    try:
        body = response.json()
    except Exception as e:
        body = response.text
    # response_dict = {}
    response_dict =dict()
    response_dict["code"] = code
    response_dict["body"] = body
    return response_dict



class Requests():
    """
    进一步封装get请求和post请求
    """
    def __init__(self):
        self.log = logs("RequestUtil")

    def requests_api(self,url,method,headers=None,json=None,data=None):
        if method == "get":
            self.log.debug("发送get请求")
            response = requests.get(url=url,headers=headers,json=json,data=data)
        elif method == "post":
            self.log.debug("发送post请求")
            response = requests.post(url=url,headers=headers,json=json,data=data)
        code = response.status_code
        try:
            body = response.json()
        except Exception as e:
            body = response.text

        response_dict = dict()
        response_dict["code"]=code
        response_dict["body"]=body
        return response_dict

    def get_api(self,url,**kwargs):
        response = self.requests_api(url,method="get",**kwargs)
        return response

    def post_api(self,url,**kwargs):
        response = self.requests_api(url,method="post",**kwargs)
        return response
