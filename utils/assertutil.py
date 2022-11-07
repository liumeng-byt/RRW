import json

from utils.logutil import Logger


# from utils.logutil import logs


class AssertUtil:
    def __init__(self):
        self.log = Logger.logs(__file__)

    def code_assert(self, response_code, expected_code):
        """
        响应码相等
        :param response_code:
        :param expected_code:
        :return:
        """
        try:
            assert int(response_code) == int(expected_code)
            return True
        except:
            self.log.error("失败，响应码：%s,期望响应码：%s" % (response_code, expected_code))
            raise

    def errorcode_assert(self, response_errorcode, expected_errorcode):
        """
        errorcode相等
        :param response_errorcode:
        :param expected_errorcode:
        :return:
        """
        try:
            assert int(response_errorcode) == int(expected_errorcode)
            return True
        except:
            self.log.error("失败，返回errorcode:%s，期望errorcode:%s" % (response_errorcode, expected_errorcode))
            raise

    def body_equal(self, response_body, expected_body):
        """
        响应体相等
        :param response_body:
        :param expected_body:
        :return:
        """
        try:
            body = json.dumps(response_body)
            assert body == expected_body
            return True
        except:
            self.log.error("失败，响应body：%s,期望body：%s" % (body, expected_body))
            raise

    def body_include(self, response_body, expected_body):
        """
        响应体包含
        :param response_body:
        :param expected_body:
        :return:
        """
        try:
            # body = json.dumps(response_body) # 转换为json后，返回html中不会显示中文，所以需要对中文断言的，不用转换
            # assert expected_body in body
            assert expected_body in response_body
            return True
        except:
            self.log.error("失败，期望body%s不在返回body%s中" % (expected_body, response_body))
            raise
