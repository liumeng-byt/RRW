# encoding=utf-8
import os
import xlrd

from comman.excelconfig import ExcelConfig
from utils.excelutil import ExcelReader
from utils.logutil import Logger


class SheetError:
    pass


class ExcelData:
    def __init__(self, file_name, sheet_by):
        self.log = Logger.logs(__file__)
        self.data = ExcelReader(file_name, sheet_by).excel_read()

    def get_run_case(self):
        """
        返回需要执行的测试用例
        :return:
        """
        run_list = list()
        # for i in range(self.data):
        for i in self.data:
            # print(i)
            # 需要运行的
            try:
                if i[ExcelConfig.is_run].lower() == "y":
                    run_list.append(i)
            except Exception as e:
                self.log.error("参数填入错误:".format(e))
                return "参数填入错误"
        return run_list  # 返回列表中嵌套字典，字典中又是str，所以请求参数需要转换为dict类型

    def get_all_case(self):
        """
        返回所有excel用例
        :return:
        """
        # all_list = list()
        # for i in self.data:
        #     all_list.append(i)
        all_list = [i for i in self.data]

        return all_list

    def get_case_pre(self, pre):
        """
        根据前置条件，从全部测试用例中返回符合条件的测试用例
        :param pre:
        :return:
        """
        run_list = self.get_all_case()
        for i in run_list:
            if pre in dict(i).values():
                return i
            else:
                return None


if __name__ == '__main__':
    print(ExcelData("../data/testdat.xls", 0).get_all_case())
    # ExcelData("testdat.xls", 0).excel_data()
