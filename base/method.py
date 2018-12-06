# coding=utf-8

import requests
from utils.excelData import *
from utils.operationExcel import *
from utils.operationJson import *


class Method:
    def __init__(self):
        self.operationJson = OperationJson()
        self.excel = OperationExcel()

    def post(self, row):
        try:
            r = requests.post(url=self.excel.get_url(row=row), data=self.operationJson.getRequestsData(row=row), headers=getHeadersValue(), timeout=6)
            return r
        except Exception as e:
            raise RuntimeError('请求接口发送异常')

    def post(self, row, data):
        try:
            r = requests.post(url=self.excel.get_url(row=row), data=data, headers=getHeadersValue(), timeout=6)
            return r
        except Exception as e:
            raise RuntimeError('请求接口发送异常')


class IsAssert():
    def __init__(self):
        self.excel = OperationExcel()

    def isContent(self, row, str2):
        flag = None
        if self.excel.get_Expect(row=row) in str2:
            flag = True
        else:
            flag = False
        return flag
