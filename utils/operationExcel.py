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

    def get_request_data(self, row):
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

    def writeResult(self, row, content):
        '''测试结果写道文件中'''
        col = getResult()
        work = xlrd.open_workbook(data_dir('data', 'data.xls'))
        old_content = copy(work)
        ws = old_content.get_sheet(0)
        ws.write(row, col, content)
        old_content.save(data_dir('data', 'api.xls'))

    def run_success_result(self):
        '''获取成功用例数'''
        pass_count = []
        fail_count = None
        for i in range(1, self.get_rows()):
            if self.get_Result(i) == 'pass':
                pass_count.append(i)
            return int(len(pass_count))

    def run_fail_result(self):
        '''获取失败用例数'''
        return int((self.get_rows() - 1) - self.run_success_result())

    def run_pass_rate(self):
        '''测试通过率'''
        if self.run_fail_result() == 0:
            return '100%'
        elif self.run_fail_result() != 0:
            rate = str(int(self.run_fail_result() / (self.run_success_result() - 1) * 100)) + '%'
        return rate


opera = OperationExcel()
print(opera.run_pass_rate())
