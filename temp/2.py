#!/usr/bin/env python
# coding=utf-8
# !/usr/bin/env python
# -*- coding:utf-8 -*-
# !python3
__author__ = "xxx"
"""自动化脚本生成工具"""
import os
import xlrd
import time
######################
TestCaseName = ""
TestCaseDescription = ""
TestCasePreCondition = ""
TestCaseStep = ""
TestCaseExpectResult = ""
TestEnvironment = ""
TestScriptName = ""
cur_path = os.getcwd()


def scripts_template():
    testcases = os.path.join(cur_path, u"用例模板.xlsx")
    data = xlrd.open_workbook(r'%s' % testcases)
    table = data.sheet_by_index(0)
    n_rows = table.nrows
    n_cols = table.ncols
    for i in range(1, n_rows):
        TestCaseName = table.cell_value(i, 1)
        TestCaseDescription = table.cell_value(i, 2)
        TestCasePreCondition = table.cell_value(i, 3)
        TestCaseStep = table.cell_value(i, 4)
        TestCaseExpectResult = table.cell_value(i, 5)
        TestEnvironment = table.cell_value(i, 0)
        TestScriptName = "test_{0}".format(TestCaseName)  #符合unittest测试用例定义的识别条件， 以"test"开头
        filename = os.path.join(cur_path, "{0}.py".format(TestScriptName))
        with open(filename, 'w', encoding='utf-8') as out:
            out.write('''# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
#-----------------------------------------------------------------------
用例名称: {0}
用例描述: {1}
前置条件: 
{2}
测试步骤: 
{3}
预期结果: 
{4}
测试环境: {5}
作者：{6}
日期：{7}
#-----------------------------------------------------------------------
"""

import unittest


class {8}(unittest.TestCase):

    def setUp(self):
        #TODO 添加用例执行前置条件
        pass

    def testRun(self):
        #TODO 添加用例执行测试步骤
        pass

    def tearDown(self):
        #TODO 添加恢复测试环境操作
        pass

if __name__ == '__main__':
    unittest.main()'''.format(TestCaseName, TestCaseDescription, TestCasePreCondition,
                      TestCaseStep, TestCaseExpectResult, TestEnvironment, __author__,
                      time.strftime('%Y-%m-%d'), TestScriptName));
    print("generate scripts finished!")


if __name__ == "__main__":
    scripts_template()
