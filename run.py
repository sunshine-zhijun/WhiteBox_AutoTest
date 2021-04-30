#!/usr/bin/env python
# coding=utf-8
import pytest
import allure
import os
from utils.generate_caces import traverse
from utils.generate_caces import GenerateTest

def generate(excel_path=None):
    path1 = os.path.abspath(os.path.dirname(__file__))
    if excel_path == None:
        excel_path = '/data/excel_data/'
    path = path1 + excel_path
    file_list = traverse(path)
    print("进行待测试的excel文件列表:\n",file_list)
    for excel in file_list:
        testcase = GenerateTest(excel)
        testcase.generate_case()






if __name__ == '__main__':
    # pytest.main(['-s', '-q', '--alluredir', './report/xml'])
    generate()
    pytest.main()

