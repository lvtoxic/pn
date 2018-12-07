# coding=utf-8

import requests
from utils.excelData import *
from utils.operationExcel import *
from utils.operationJson import *

operationExcel = OperationExcel()


# def checkHeader(row, f1=None, f2=None):
#     '''检测请求头'''
#     url = operationExcel.get_url(row=row)
#     url = url.split('/')
#     if url[4] == 'positionAjax.json?needAddtionalResult=false':
#         return f1
#     elif url[5] == 'byPositionjson':
#         return f2


class Method:
    def __init__(self):
        self.operationJson = OperationJson()
        self.excel = OperationExcel()
    #
    # def post(self, row):
    #     try:
    #         r = requests.post(url=self.excel.get_url(row=row), data=self.operationJson.getRequestsData(row=row), headers=getHeadersValue(), timeout=6)
    #         return r
    #     except Exception as e:
    #         raise RuntimeError('请求接口发送异常')

    def post(self, row, data):
        try:
            r = requests.post(url=self.excel.get_url(row=row), data=data, headers=getHeadersValue(), timeout=6)
            return r
        except Exception as e:
            raise RuntimeError('请求接口发送异常')

    # def post(self, row, data):
    #     try:
    #         r = requests.post(url=self.excel.get_url(row=row), data=data, headers=checkHeader(row=row, f1=getHeadersValue(), f2=getHeadersInfo()), timeout=6)
    #         return r
    #     except Exception as e:
    #         raise RuntimeError('请求接口发送异常')

    def get(self, url, params=None):
        r = requests.get(url=url, params=params, headers=getHeadersValue(), timeout=6)
        return r


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
