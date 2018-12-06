# coding=utf-8

import json
from utils.public import *
from utils.operationExcel import OperationExcel

class OperationJson:
    def __init__(self):
        self.excel=OperationExcel()


    def getReadJson(self):
        '''获取json文件内容'''
        with open(data_dir(fileName='requestData.json'), 'r',encoding='utf-8') as f:
            return json.load(f)

    def getRequestsData(self,row):
        '''获取请求参数'''
        return json.dumps(self.getReadJson()[self.excel.get_request_data(row=row)])



# opera = OperationJson()
# print(opera.getRequestsData(1))
