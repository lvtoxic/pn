# coding=utf-8
import xlrd
from xlutils.copy import copy
from utils.public import *
from utils.excelData import *


class OperationExcel():
    def getExcel(self):
        '''打开文件'''
        db = xlrd.open_workbook(data_dir('data', 'data.xls'))
        sheet = db.sheet_by_index(0)
        return sheet

    def get_rows(self):
        '''获取excel行数'''
        return self.getExcel().nrows

    def get_row_cel(self, row, col):
        '''获取单元格内容'''
        return self.getExcel().cell_value(row, col)

    def get_url(self, row):
        '''获取请求地址'''
        return self.get_row_cel(row, getUrl())

    def get_request_data(self,row):
        '''获取请求参数'''
        return self.get_row_cel(row, get_Request_data())

    def get_Expect(self, row):
        '''获取期望结果'''
        return self.get_row_cel(row, getExpect())

    def get_Result(self, row):
        '''获取实际结果'''
        return self.get_row_cel(row, getResult())

    def get_CaseID(self, row):
        '''获取测试ID'''
        return self.get_row_cel(row, getCaseID())

# opera = OperationExcel()
# print(opera.get_Expect(1))
