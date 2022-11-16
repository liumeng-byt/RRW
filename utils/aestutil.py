# encoding=utf-8
import base64
import json

from Crypto.Cipher import AES


class AesUtil(object):
    def __init__(self):
        # 加密和解密必须使用同样的key、mode、iv
        self.key = b"sadjunb8_s2/s;s2"
        self.mode = AES.MODE_EAX
        self.iv = b"0" * 16

    def encrypt(self, data:dict) -> str:
        """
        AES 数据加密
        1、接收字典
        2、字典转字符串
        3、字符串转字节
        4、字节加密
        5、对加密的结果进行base64
        6、编码结果转字符串
        """
        encoder = AES.new(self.key, mode=self.mode, nonce=self.iv)
        content_str = json.dumps(data)
        content_byte = content_str.encode("utf-8")
        content_enc, _ = encoder.encrypt_and_digest(content_byte)
        result = base64.b64encode(content_enc).decode("utf-8")
        return result

    def decrypt(self, data: str) -> dict:
        """
        AES 数据解密
        1、接收字符串
        2、字符串转字节
        3、base64解码
        4、AES解密
        5、解密结果转字符串
        6、字符串转字典
        :param data:
        :return:
        """
        encoder = AES.new(self.key, mode=self.mode, nonce=self.iv)
        content_byte = base64.b64decode(data)
        content_dec = encoder.decrypt(content_byte)
        content_str = content_dec.decode("utf-8")
        result = json.loads(content_str)
        return result


# if __name__ == '__main__':
#     aes = AesUtil()
#     print("",aes.encrypt({"姓名":"谢敏","身份证号":"522323199405068544","银行卡号":"666666666666666","密码":"123456"}))
#     print(aes.decrypt("IwVtLgesfz01MAnVKg4CCCo3TOV5yxKn3TAjYHwrii+o42cls5HPR+UfgzXyrI6Aa7qoO3s4ebdmNk6FJnM44u05JTaIm0HxblYN8FQEyusVNBvasB2dUVtxXyM+aGf19hUmrlI/PEjUxsrNd4z29OOj6x9wdmAqiqJFBeA7vaTaHQkhqpnQlSOL/nfxx6e6nsbCCBp8hiHRB+0="))
