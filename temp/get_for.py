
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
@pytest.mark.parametrize("data", [{'mock_value': {'egroup.get_egroup_interfaces': ['C2']}, 'exp': "{'C1': ['policy1'], 'C2': ['policy1'], 'C3': ['policy2']}", '参数': "{'1':{'configration':{'evif_name':'egroup2'}}}"}, {'mock_value': {'egroup.get_egroup_interfaces': ['C2']}, 'exp': "{'C1': ['policy1'], 'C2': ['policy1'], 'C3': ['policy2']}", '参数': "{'1':{'configration':{'evif_name':'egroup2'}}}"}, {'mock_value': {'egroup.get_egroup_interfaces': ['C3']}, 'exp': "{'C1': ['policy1'], 'C2': ['policy1'], 'C3': ['policy3']}", '参数': "{'1':{'configration':{'evif_name':'egroup3'}}}"}])
@pytest.mark.get
class Test_get_forward():
    @staticmethod
    def get_for(data):
        print(policy1)
        parameter = data["parameter"]
        print("=====",data)
        exp = data["exp_status_code"]
        print("==---",exp)
        mock_value = data["mock_value"]
        get_fb = forward_policy()
        '''
        mock 虚拟数据
        '''
        
        egroup.get_egroup_interfaces = mock.Mock(return_value(mock_value['egroup.get_egroup_interfaces']
        # egroup.get_egroup_interfaces = mock.Mock(return_value=mock_value)
        # elag.get_elag_interfaces = mock.Mock(return_value=mock_value)
        
        find = get_fb.get_egress_port_keys_of_policy_name_todict(self_dict=data, policy_name="policy1")
        
        assert find == exp
