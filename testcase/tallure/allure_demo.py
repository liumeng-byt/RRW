# encoding=utf-8
import allure
import pytest


@allure.feature("一级模块（首页）")
class TestAllure():
    @allure.story("二级模块（用户列表）")
    @allure.title("用例1标题")
    @allure.description("用例1的描述")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_1(self):
        print("用例1的结果")

    @allure.story("二级模块（用户列表）")
    @allure.title("用例2标题")
    @allure.description("用例1的描述")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_2(self):
        print("用例2的结果")

    @allure.story("二级模块（角色列表）")
    @allure.title("用例3标题")
    @allure.description("用例1的描述")
    def test_3(self):
        print("用例3的结果")

    @pytest.mark.parametrize("case",["用例4","用例5"])
    def test_4(self,case):
        print("%s的结果"%case)
        allure.dynamic.title("%s的标题"%case)
        allure.dynamic.story("%s的目录"%case)
        allure.dynamic.description("%s的描述"%case)



if __name__ == '__main__':
    pytest.main(["allure_demo.py"])
