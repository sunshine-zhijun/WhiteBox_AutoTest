
# !/usr/bin/env python
# -*- coding:utf-8 -*-
'''
#-----------------------------------------------------------------------
用例名称: get_egress_port_keys_of_policy_name_todict
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

@allure.feature('get_egress_port_keys_of_policy_name_todict')
@pytest.mark.parametrize("data", [{'discription': {'title': '出接口为egroup'}, 'parameter': {'self_dict': {'1': {'configuration': {'evif_name': 'egroup1'}}}, 'policy_name': 'policy1'}, 'mock_value': {'elag.get_elag_interfaces': ['C2'], 'egroup.get_egroup_interfaces': ['C1']}, 'exp': {'text': {'C3': ['policy1'], 'C1': ['policy1'], 'C2': ['policy1']}}}, {'discription': {'title': '出接口为elag'}, 'parameter': {'self_dict': {'1': {'configuration': {'evif_name': 'elag1'}}}, 'policy_name': 'policy1'}, 'mock_value': {'elag.get_elag_interfaces': ['C2', 'C1', 'C3']}, 'exp': {'text': {'C3': ['policy1'], 'C1': ['policy1'], 'C2': ['policy1']}}}, {'discription': {'title': '出接口为单接口'}, 'parameter': {'self_dict': {'1': {'configuration': {'evif_name': 'C1'}}}, 'policy_name': 'policy1'}, 'exp': {'text': {'C1': ['policy1']}}}, {'discription': {'title': '无出接口'}, 'parameter': {'self_dict': {'1': {'configuration': {'evif_name1': 'C1'}}}, 'policy_name': 'policy1'}, 'exp': {'text': {}}}], ids=['出接口为egroup', '出接口为elag', '出接口为单接口', '无出接口'])
@pytest.mark.get_egress_port_keys_of_policy_name_todict
class Test_get_egress_port_keys_of_policy_name_todict():
    @staticmethod
    def test_get_egress_port_keys_of_policy_name_todict(data):
        parameter = data["parameter"]
        exp = data["exp"]["text"]
        mock_value = data.get("mock_value")
        class_instance = forward_policy()
        '''
        mock 虚拟数据
        '''
        if mock_value:
            
            elag.get_elag_interfaces = mock.Mock(return_value = mock_value.get('elag.get_elag_interfaces'))
            egroup.get_egroup_interfaces = mock.Mock(return_value = mock_value.get('egroup.get_egroup_interfaces'))
        # egroup.get_egroup_interfaces = mock.Mock(return_value=mock_value)
        # elag.get_elag_interfaces = mock.Mock(return_value=mock_value)
        
        find = class_instance.get_egress_port_keys_of_policy_name_todict(self_dict=parameter['self_dict'],policy_name=parameter['policy_name'])
        
        assert find == exp
