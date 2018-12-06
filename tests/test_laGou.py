# coding=utf-8

import unittest
from base.method import *
from page.laGou import *


class LaGou(unittest.TestCase):
    def setUp(self):
        self.obj = Method()
        self.p = IsAssert()

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
        r = self.obj.post(1)
        self.statusCode(r=r)
        self.isContent(r=r, row=1)

    def test_lagou_002(self):
        '''拉钩翻页'''
        r = self.obj.post(row=1, data=setSo('python'))
        print(r.text)


if __name__ == '__main__':
    unittest.main(verbosity=2)
