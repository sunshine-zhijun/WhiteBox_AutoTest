
# !/usr/bin/env python
# -*- coding:utf-8 -*-
'''
#-----------------------------------------------------------------------
用例名称: get_elag_interfaces
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
from code.PFX.forward_policies.test1.forward_policy import *

@allure.feature('get_elag_interfaces')
@pytest.mark.parametrize("data", [{'discription': {'title': '可获取到elag子接口'}, 'parameter': {'elag': '1'}, 'mock_value': {'global_elags': {'1': {'configuration': {'comment': 'aster@123', 'interfaces': ['C1', 'C2', 'C3']}}}}, 'exp': {'text': ['C2', 'C1', 'C3']}}], ids=['可获取到elag子接口'])
@pytest.mark.get_elag_interfaces
class Test_get_elag_interfaces():
    @staticmethod
    def test_get_elag_interfaces(data):
        parameter = data["parameter"]
        exp = data["exp"]["text"]
        mock_value = data.get("mock_value")
        class_instance = elag()
        '''
        mock 虚拟数据
        '''
        if mock_value:
            
            global_elags = mock.Mock(return_value = mock_value.get('global_elags'))
        # egroup.get_egroup_interfaces = mock.Mock(return_value=mock_value)
        # elag.get_elag_interfaces = mock.Mock(return_value=mock_value)
        
        find = class_instance.get_elag_interfaces(elag=parameter['elag'])
        
        assert find == exp
