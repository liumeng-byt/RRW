# coding=utf-8
import os

import xlrd

from utils.logutil import Logger


class SheetTypeError:
    pass


class ExcelReader(object):
    def __init__(self, file_path, sheet_by):
        self._data = list()
        self.log = Logger.logs(__file__)
        if os.path.exists(file_path):
            self.file_path = file_path
            self.sheet_by = sheet_by
        else:
            self.log.error("文件不存在")
            raise FileNotFoundError("文件不存在")

    def excel_read(self):
        if not self._data:
            work_book = xlrd.open_workbook(self.file_path)

            if type(self.sheet_by) not in (int, str):
                # raise SheetTypeError("输入的sheet类型不符合规则")
                self.log.error("输入的类型不符合规则")
                raise ("输入的类型不符合规则")

            # 名称或索引读取sheet
            elif type(self.sheet_by) == int:
                sheet = work_book.sheet_by_index(self.sheet_by)
            elif type(self.sheet_by) == str:
                sheet = work_book.sheet_by_name(self.sheet_by)
            # 读取sheet内容
            rows = sheet.nrows  # 总行数
            title = sheet.row_values(0)  # 首行即标题
            # s = dict(zip(sheet.row_values(0),sheet.row_values(1)))  # 标题和第一行绑定
            for row in range(1, rows):
                per_row = sheet.row_values(row)
                self._data.append(dict(zip(title, per_row)))
        return self._data

# if __name__ == '__main__':
#     print(ExcelReader("testdat.xls", 0).excel_read())
