
from unittest import mock
import pytest
import os
import allure
from code.forward_policies.forward_policy import *
# from code.forward_policies.get_forward_name import *
# from utils.YamlUtil import YamlReader
# from utils.RequestUtil import Requests
# from config import Conf
# test_file = os.path.join(Conf.get_data_path(), 'yaml_data/forward_policy/get_fb.yml')
# print(test_file)

# data_list = YamlReader(test_file).data_all()
# print(data_list)
# data_list = current_test_file.get_cases()
@allure.feature('get_egress_port_keys_of_policy_name_todict')
@pytest.mark.parametrize("data", [{'discription': {'title': '出接口为egroup'}, 'mock_value': {'elag.get_elag_interfaces': ['C2'], 'egroup.get_egroup_interfaces': ['C1']}, 'exp': {'exp_re': {'C2': ['policy1'], 'C3': ['policy1'], 'C1': ['policy1']}}, 'parameter': {'policy_name': 'policy1', 'self_dict': {'1': {'configuration': {'evif_name': 'egroup1'}}}}}, {'discription': {'title': '出接口为elag'}, 'mock_value': {'elag.get_elag_interfaces': ['C2', 'C1', 'C3']}, 'exp': {'exp_re': {'C2': ['policy1'], 'C3': ['policy1'], 'C1': ['policy1']}}, 'parameter': {'policy_name': 'policy1', 'self_dict': {'1': {'configuration': {'evif_name': 'elag1'}}}}}, {'discription': {'title': '出接口为单接口'}, 'exp': {'exp_re': {'C1': ['policy1']}}, 'parameter': {'policy_name': 'policy1', 'self_dict': {'1': {'configuration': {'evif_name': 'C1'}}}}}, {'discription': {'title': '无出接口'}, 'exp': {'exp_re': {}}, 'parameter': {'policy_name': 'policy1', 'self_dict': {'1': {'configuration': {'evif_name1': 'C1'}}}}}], ids=['出接口为egroup', '出接口为elag', '出接口为单接口', '无出接口'])
@pytest.mark.sss
class Test_get_egress_port_keys_of_policy_name_todict():
    @staticmethod
    def test_get_egress_port_keys_of_policy_name_todict(data):
        parameter = data["parameter"]
        print("=====",data)
        exp = data["exp"]["exp_re"]
        print("==---",exp)
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
        
        find = class_instance.get_egress_port_keys_of_policy_name_todict(policy_name=parameter['policy_name'],self_dict=parameter['self_dict'])
        
        assert find == exp
