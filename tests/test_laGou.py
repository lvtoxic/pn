# coding=utf-8

import unittest
from base.method import *
from page.laGou import *
from utils.public import *
import json
from utils.operationExcel import *
from utils.operationJson import *


class LaGou(unittest.TestCase):
    def setUp(self):
        self.obj = Method()
        self.p = IsAssert()
        self.excel = OperationExcel()
        self.operationJson = OperationJson()

    def tearDown(self):
        pass

    def statusCode(self, r):
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 0)

    def isContent(self, r, row):
        self.statusCode(r=r)
        self.assertTrue(self.p.isContent(row=row, str2=r.text))

    def test_lagou_001(self):
        '''拉钩翻页'''
        r = self.obj.post(row=1, data=operationJson.getRequestsData(1))
        self.statusCode(r=r)
        self.isContent(r=r, row=1)
        self.excel.writeResult(1, 'pass')

    def test_lagou_002(self):
        '''拉钩翻页'''
        r = self.obj.post(row=1, data=setSo('python'))
        list1 = []
        for i in range(0, 15):
            positionId = r.json()['content']['positionResult']['result'][1]['positionId']
            list1.append(positionId)
        writePositionId(json.dumps(list1))

    # def test_lagou_003(self):
    #     '''访问搜到到的每个职位的详情页面'''
    #     for i in range(1, 15):
    #         r = self.obj.get(url=getUrl()[i])
    #         self.assertTrue(self.p.isContent(2, r.text))


if __name__ == '__main__':
    unittest.main(verbosity=2)
