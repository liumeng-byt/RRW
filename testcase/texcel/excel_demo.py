
# coding=gbk
# coding=utf-8

import xlrd

# 创建workbook对象
book = xlrd.open_workbook("testdata.xls")

# 创建sheet对象
sheet = book.sheet_by_index(0)
# sheet = book.sheet_by_name("美多商城接口测试")

# 获取总的行数列数
rows = sheet.nrows  # 总的行数
cols = sheet.ncols  # 总的列数
# print(rows)

# 读取每行内容
for r in range(rows):
    r_rows = sheet.row_values(r)
    # print(r_rows)

# 读取每列的内容
for c in range(cols):
    c_cols = sheet.col_values(c)
    # print(c_cols)

# 读取固定行列的内容
# print(sheet.cell(3, 2))

# 读取固定行
# print(sheet.row_values(0))

# 读取固定列
# print(sheet.col_values(0))