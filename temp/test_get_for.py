
                from unittest import mock
import pytest
import os
import allure
from code.forward_policies.get_forward_name import *
from utils.YamlUtil import YamlReader
from utils.RequestUtil import Requests
from config import Conf
@allure.feature('转发策略获取出接口')
@pytest.mark.parametrize("policy1", data_list, ids=["出接口为egroup", "出接口为elag", "出接口为单接口", "多个规则"])
@pytest.mark.get
class Test_get_forward():
    @staticmethod
    def test_get_egress_port_keys(policy1):
        print(policy1)
        data = policy1["parameter"]
        print("=====",data)
        exp = policy1["exp_status_code"]
        print("==---",exp)
        mock_value = policy1["mock_value"]
        get_fb = forward_policy()
        egroup.get_egroup_interfaces = mock.Mock(return_value=mock_value)
        elag.get_elag_interfaces = mock.Mock(return_value=mock_value)

        find = get_fb.get_egress_port_keys_of_policy_name_todict(self_dict=data, policy_name="policy1")

        assert find == exp

                