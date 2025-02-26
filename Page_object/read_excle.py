# coding:utf-8
'''
Created on 2018-12-1
@author: Lee
Project:读取excle作为DDT使用操作
'''
import xlrd


class ExcelTest():
    def __init__(self, excel_path, sheet_name):
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheet_by_name(sheet_name)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            # print(self.keys)
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r


if __name__ == "__main__":
    filePath = "../Parm_data/test.xlsx"
    sheetName = "Sheet1"
    data = ExcelTest(filePath, sheetName)
    ss=data.dict_data()[1]
    ll=ss["username"]
    ls=ss.values()
    print(ll)
    print(ls)
    print(ss)
