#coding=utf-8

import os

def data_dir(data='data',fileName=None):
    '''查找文件的目录'''
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),data,fileName)




# print(data_dir('data','data.xls'))



