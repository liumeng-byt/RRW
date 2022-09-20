import pytest

class TestApi:
    # 基础用法：传入单个参数
    @pytest.mark.parametrize('args',['name','age'])
    def test_api(self,args):
        print(args)

    # 拆包用法：传入多个参数
    @pytest.mark.parametrize('name,age',[['lisi','21'],['zhangsan','39']])
    def test_api(self,name,age):
        print(name,age)

if __name__ == '__main__':
    pytest.main()