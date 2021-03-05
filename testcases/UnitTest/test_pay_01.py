#!/usr/bin/env python
# coding=utf-8
from unittest import mock
from code.pay import PayApi
import pytest
import allure

@allure.feature("支付功能")
@allure.description("测试使用第三方支付接口的函数支付功能，成功返回200，失败返回400")
class TestPayAPI():
    @allure.story("支付成功")
    @allure.title("支付成功")
    @allure.description("支付成功，返回200")
    @allure.severity("critical")
    def test_success(self):
        pay = PayApi()
        with allure.step("进行支付"):
            pay.auth = mock.Mock(return_value={'status_code':'200'})
        with allure.step("支付状态"):
            status = pay.pay('aster', '888888', '10000')
            assert status ==  '支付成功'
    @allure.story("支付失败")
    @allure.title("支付失败")
    def test_fail(self):
        pay = PayApi()
        pay.auth = mock.Mock(return_value={'status_code':'400'})
        status = pay.pay('aster', '888888', '10000')
        assert status == '支付失败'
    @allure.story("服务器错误")
    def test_error(self):
        pay = PayApi()
        with allure.step("进行支付"):
            pay.auth = mock.Mock(return_value={'status_code':'500'})
        with allure.step("支付状态"):
            status = pay.pay('aster', '888888', '10000')
            assert status == '服务器错误'

