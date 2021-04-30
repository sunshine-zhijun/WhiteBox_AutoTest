
# !/usr/bin/env python
# -*- coding:utf-8 -*-
'''
#-----------------------------------------------------------------------
用例名称: pay
用例描述: 
前置条件: 
测试步骤: 
预期结果: 
测试环境: Phone
作者：
日期：2021-03-23
#-----------------------------------------------------------------------
'''
from unittest import mock
import pytest
import os
import allure
from code.pay_test.PayApi import *

@allure.feature('pay')
@pytest.mark.parametrize("data", [{'exp': {'text': '支付成功'}, 'mock_value': {'self.auth': {'status_code': '200'}}, 'discription': {'title': '支付成功测试'}, 'parameter': {'card': '621785360000099', 'amount': '1000', 'user_id': '001'}}, {'exp': {'text': '支付失败'}, 'mock_value': {'self.auth': {'status_code': '400'}}, 'discription': {'title': '支付失败测试'}, 'parameter': {'card': '621785360000099', 'amount': '1001', 'user_id': '001'}}, {'exp': {'text': '服务器异常'}, 'mock_value': {'self.auth': {'status_code': '500'}}, 'discription': {'title': '服务器错误测试'}, 'parameter': {'card': '621785360000099', 'amount': '1002', 'user_id': '001'}}], ids=['支付成功测试', '支付失败测试', '服务器错误测试'])
@pytest.mark.pay
class Test_pay():
    @staticmethod
    def test_pay(data):
        parameter = data["parameter"]
        exp = data["exp"]["text"]
        mock_value = data.get("mock_value")
        class_instance = PayApi()
        '''
        mock 虚拟数据
        '''
        if mock_value:
            
            PayApi.auth = mock.Mock(return_value = mock_value.get('self.auth'))
        # egroup.get_egroup_interfaces = mock.Mock(return_value=mock_value)
        # elag.get_elag_interfaces = mock.Mock(return_value=mock_value)
        
        find = class_instance.pay(card=parameter['card'],amount=parameter['amount'],user_id=parameter['user_id'])
        
        assert find == exp
