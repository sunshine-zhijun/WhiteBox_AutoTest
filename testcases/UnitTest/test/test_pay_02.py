#!/usr/bin/env python
# coding=utf-8
from unittest import mock
from code.pay import *
import pytest
import allure


feature1 = "支付功能"
step = ["进行支付", "支付状态返回"]
description = "测试使用第三方支付接口的函数支付功能，成功返回200，失败返回400"
datalist={
    "fun": "pay",
    "mock_fun":["auth"]
}
auth = "pay.auth = mock.Mock(return_value={'status_code':'200'})"
# print(exec(auth))
@pytest.mark.pas
@allure.feature(feature1)
@allure.description(description)


# eval("%s_send(self.pkt_type, pkt_macro)"%self.device_type)



class TestPayAPI():
    @allure.story("支付成功")
    @allure.title("支付成功")
    @allure.description("支付成功，返回200")
    @allure.severity("critical")
    def test_success(self):
        pay = PayApi()
        for step1 in step: 
            with allure.step(step1):
                exec(auth)
                status = pay.pay('aster', '888888', '10000')
        assert status ==  '支付成功'

