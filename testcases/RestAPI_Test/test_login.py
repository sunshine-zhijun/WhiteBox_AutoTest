#!/usr/bin/env python
# coding=utf-8
import allure
import pytest
import requests
import urllib3
import json
import os
import allure
from utils.YamlUtil import YamlReader
from utils.RequestUtil import Requests
# from utils.RequestsUtil import *
from config import Conf
test_file = os.path.join(Conf.get_data_path(), 'yaml_data/testlogin.yml')
print(test_file)

data_list = YamlReader(test_file).data_all()
# print(data_list)
@pytest.mark.login
@pytest.mark.parametrize("login", data_list)
def test_yaml(login):
    """
    执行测试用例
    """
    uri = login['url']
    print(uri)
    data = login['parameter']
    print(data)
    exp = login['exp_status_code']
    request = Requests()
    # request = Request(ConfigYaml().get_config_url())
    res = request.get_response(uri, "post", parameter=data)
    print(res.text)
    assert res.status_code == exp



@allure.feature('购物车')
class TestShoppingTrolley(object):
    @allure.story('加入购物车')
    def test_add_shopping_torlley(self):

        login('sun', '123456')
        with allure.step('浏览商品'):
            allure.attach('笔记本','商品1')
        with allure.step('检验结果'):                                                                                                                                                                       
            allure.attach('成功', '期望结果')
            allure.attach('失败', '实际结果')
        assert 'success' == 'failed'

    @allure.story('修改购物车')
    def test_edit_shopping(self):
        print("ok")


@allure.step('用户登录')
def login(user, pwd):
    print(user, pwd)



class Login():
    def __init__(self, name, pwd):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        requests.adapters.DEFAULT_RETRIES =10
        self.session = requests.session()
        self.session.headers = {'Authorization': 'Basic a2FyYWY6a2FyYWY=', 'connection': 'close'}
        self.name = name
        self.pwd = pwd
    def login(self):
        loginUrl = "https://192.168.0.57/login"
        # params = json.loads('{"username": "admin", "password": "Passok"}') 
        params = {
            "username" : self.name,
            "password" : self.pwd
        }
        res = requests.post(url=loginUrl, json=params, headers=self.session.headers, verify=False)
        print(res.status_code)
        return res
    def login_status(self):
        res = self.login()
        if res.status_code == 201:
            print("恭喜，成功登陆")
            print("ok----", res.text)
        elif res.status_code == 400:
            print("用户名或者密码错误")
            print("error", res.text)
        else:
            print("未知错误")
            print(res.status_code)
        return res.status_code


@allure.feature("设备登陆功能")
@allure.story("设备登录")
def test_login():
    # @allure.story("正常登录")
    device = Login(name='admin', pwd='Passok')
    res = device.login()
    assert res.status_code == 201

    # @allure.story("异常登录")
    device2 = Login(name='admin1', pwd='Passok')
    res = device2.login()
    assert res.status_code == 403


if __name__ == '__main__':
    device = Login(name = "admin", pwd = "Passok")
    res = device.login_status()
