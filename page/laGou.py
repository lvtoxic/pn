# coding=utf-8
from utils.operationJson import *
from utils.operationExcel import *
import json

operationJson = OperationJson()


def setSo(kd=None):
    '''对搜索的数据重新赋值'''
    dici1=json.loads(operationJson.getRequestsData(1))
    dici1['kd'] = kd
    return dici1


# print(setSo('qwe'))
