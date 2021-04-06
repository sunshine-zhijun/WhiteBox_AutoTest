
from unittest import mock
import pytest
import os
import allure
from code.pay_test.PayApi import *
# from code.forward_policies.get_forward_name import *
# from utils.YamlUtil import YamlReader
# from utils.RequestUtil import Requests
# from config import Conf
# test_file = os.path.join(Conf.get_data_path(), 'yaml_data/forward_policy/get_fb.yml')
# print(test_file)

# data_list = YamlReader(test_file).data_all()
# print(data_list)
# data_list = current_test_file.get_cases()
@allure.feature('pay')
@pytest.mark.parametrize("data", [{'discription': {'title': '支付成功测试'}, 'mock_value': {'self.auth': {'status_code': '200'}}, 'exp': {'exp_re': '支付成功'}, 'parameter': {'user_id': '001', 'amount': '1000', 'card': '621785360000099'}}, {'discription': {'title': '支付失败测试'}, 'mock_value': {'self.auth': {'status_code': '400'}}, 'exp': {'exp_re': '支付失败'}, 'parameter': {'user_id': '001', 'amount': '1001', 'card': '621785360000099'}}, {'discription': {'title': '服务器错误测试'}, 'mock_value': {'self.auth': {'status_code': '500'}}, 'exp': {'exp_re': '服务器异常'}, 'parameter': {'user_id': '001', 'amount': '1002', 'card': '621785360000099'}}], ids=['支付成功测试', '支付失败测试', '服务器错误测试'])
@pytest.mark.sss
class Test_pay():
    @staticmethod
    def test_pay(data):
        parameter = data["parameter"]
        print("=====",data)
        exp = data["exp"]["exp_re"]
        print("==---",exp)
        mock_value = data.get("mock_value")
        class_instance = PayApi()
        '''
        mock 虚拟数据
        '''
        if mock_value:
            
            PayApi.auth = mock.Mock(return_value = mock_value.get('self.auth'))
        # egroup.get_egroup_interfaces = mock.Mock(return_value=mock_value)
        # elag.get_elag_interfaces = mock.Mock(return_value=mock_value)
        
        find = class_instance.pay(user_id=parameter['user_id'],amount=parameter['amount'],card=parameter['card'])
        
        assert find == exp
