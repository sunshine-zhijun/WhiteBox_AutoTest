
from unittest import mock
import pytest
import os
import allure
from code.forward_policies.get_forward_name import *
# from utils.YamlUtil import YamlReader
# from utils.RequestUtil import Requests
# from config import Conf
# test_file = os.path.join(Conf.get_data_path(), 'yaml_data/forward_policy/get_fb.yml')
# print(test_file)

# data_list = YamlReader(test_file).data_all()
# print(data_list)
# data_list = current_test_file.get_cases()
@allure.feature('转发策略获取出接口')
@pytest.mark.parametrize("data", [{'parameter': {'self_dict': {'1': {'configuration': {'evif_name': 'egroup1'}}}, 'policy_name': 'policy1'}, 'mock_value': {'elag.get_elag_interfaces': ['C2'], 'egroup.get_egroup_interfaces': ['C1']}, 'exp': {'exp_re': {'C3': ['policy1'], 'C1': ['policy1'], 'C2': ['policy1']}}}, {'parameter': {'self_dict': {'1': {'configuration': {'evif_name': 'elag1'}}}, 'policy_name': 'policy1'}, 'mock_value': {'elag.get_elag_interfaces': ['C2', 'C1', 'C3']}, 'exp': {'exp_re': {'C3': ['policy1'], 'C1': ['policy1'], 'C2': ['policy1']}}}])
@pytest.mark.sss
class Test_get_for_1():
    @staticmethod
    def test_get_for_1(data):
        print(policy1)
        parameter = data["parameter"]
        print("=====",data)
        exp = data["exp"]["exp_re"]
        print("==---",exp)
        mock_value = data["mock_value"]
        get_fb = forward_policy()
        '''
        mock 虚拟数据
        '''
        
        elag.get_elag_interfaces = mock.Mock(return_value = mock_value.get('elag.get_elag_interfaces'))
        egroup.get_egroup_interfaces = mock.Mock(return_value = mock_value.get('egroup.get_egroup_interfaces'))
        # egroup.get_egroup_interfaces = mock.Mock(return_value=mock_value)
        # elag.get_elag_interfaces = mock.Mock(return_value=mock_value)
        
        find = get_fb.get_egress_port_keys_of_policy_name_todict(self_dict=parameter['self_dict'],policy_name=parameter['policy_name'])
        
        assert find == exp
