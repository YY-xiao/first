# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import xlrd
import xlwt
data1 =xlrd.open_workbook(r'F:\XXXYAN\pythonProject\milk\21.xls')
table1 = data1.sheet_by_name(sheet_name='12')
data2 =xlrd.open_workbook(r'F:\XXXYAN\pythonProject\milk\22.xls')
table2 = data2.sheet_by_name(sheet_name='Sheet3')
wbk = xlwt.Workbook(r'F:\XXXYAN\pythonProject\milk\11.xls')
#wbk.save('12.xls')
rows1=table1.nrows
rows2=table2.nrows
cols1=table1.ncols
cols2=table2.ncols

for row in range(2,rows1-1):
    cell1 = table1.cell(row, 2)
    cell2=table2.cell(row,1)
    vcell1 = cell1.value
    vcell2=cell2.value
    if(vcell1!=vcell2):
        print(row+1)

print(table1.name)
print(table1.nrows)
print(table1.ncols)
rows = table1.row_values(3)#输出第三行的全部值，赋值给rows，这是以数组的形式
cols = table1.col_values(2)#
# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
a=table1.row(1)[0].value.encode('utf-8')#获取指定某单元格内容
