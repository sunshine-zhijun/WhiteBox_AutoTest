

temp1 = """
# !/usr/bin/env python
# -*- coding:utf-8 -*-
'''
#-----------------------------------------------------------------------
用例名称: {fun_name}
用例描述: 
前置条件: 
测试步骤: 
预期结果: 
测试环境: 
作者：
日期：2021-00-00
#-----------------------------------------------------------------------
'''
from unittest import mock
import pytest
import os
import allure
from {path} import *

@allure.feature('{fun_name}')
@pytest.mark.parametrize("data", {data}, ids={ids})
@pytest.mark.{fun_name}
class Test_{fun_name}():
    @staticmethod
    def test_{fun_name}(data):
        parameter = data["parameter"]
        exp = data["exp"]["text"]
        mock_value = data.get("mock_value")
        class_instance = {class_name}()
        '''
        mock 虚拟数据
        '''
        if mock_value:
            {mock_data}
        # egroup.get_egroup_interfaces = mock.Mock(return_value=mock_value)
        # elag.get_elag_interfaces = mock.Mock(return_value=mock_value)
        
        find = class_instance.{fun_name}({parameter})
        
        assert find == exp
"""    