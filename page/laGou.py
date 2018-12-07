# coding=utf-8
from utils.operationJson import *
from utils.operationExcel import *
import json

operationJson = OperationJson()
operationExcel = OperationExcel()


def setSo(kd=None):
    '''对搜索的数据重新赋值'''
    dici1 = json.loads(operationJson.getRequestsData(1))
    dici1['kd'] = kd
    return dici1


def writePositionId(content):
    '''把职位id写道文件中'''
    with open(data_dir(fileName='positionId'), 'a')as f:
        f.write(content)


def getPositionId():
    '''获取职位详情'''
    with open(data_dir(fileName='positionId'), 'r')as f:
        return json.loads(f.read())


def getUrl():
    listUrl = []
    for item in getPositionId():
        url='https://www.lagou.com/jobs/{0}.html'.format(item)
        listUrl.append(url)
    return listUrl



# print(getUrl(getPositionId()))
