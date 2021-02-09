# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import xlrd
import xlwt
data =xlrd.open_workbook(r'F:\XXXYAN\pythonProject\milk\12.xls')
table = data.sheet_by_name(sheet_name='12')
wbk = xlwt.Workbook(r'F:\XXXYAN\pythonProject\milk\12.xls')
#wbk.save('12.xls')

print(table.name)
print(table.nrows)
print(table.ncols)
rows = table.row_values(3)#输出第三行的全部值，赋值给rows，这是以数组的形式
cols = table.col_values(2)#
# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
a=table.row(1)[0].value.encode('utf-8')#获取指定某单元格内容
