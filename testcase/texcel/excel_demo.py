
# coding=gbk
# coding=utf-8

import xlrd

# ����workbook����
book = xlrd.open_workbook("testdata.xls")

# ����sheet����
sheet = book.sheet_by_index(0)
# sheet = book.sheet_by_name("�����̳ǽӿڲ���")

# ��ȡ�ܵ���������
rows = sheet.nrows  # �ܵ�����
cols = sheet.ncols  # �ܵ�����
# print(rows)

# ��ȡÿ������
for r in range(rows):
    r_rows = sheet.row_values(r)
    # print(r_rows)

# ��ȡÿ�е�����
for c in range(cols):
    c_cols = sheet.col_values(c)
    # print(c_cols)

# ��ȡ�̶����е�����
# print(sheet.cell(3, 2))

# ��ȡ�̶���
# print(sheet.row_values(0))

# ��ȡ�̶���
# print(sheet.col_values(0))