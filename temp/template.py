#!/usr/bin/env python
# coding=utf-8
__author__ = "xxx"
"""自动化脚本生成工具"""
import os
import xlrd
import time

import os
import time
import os
import xlrd
import time
import pandas as pd
import json
import ast
test_case_name = ""
test_case_id = ""
test_case_description = ""
mock_value = {}
parameter = {}
cur_path = os.getcwd()
dicat1 = {}
list1 = []




temp = """
from unittest import mock
import pytest
import os
import allure
from {path} import *
# from code.forward_policies.get_forward_name import *
# from utils.YamlUtil import YamlReader
# from utils.RequestUtil import Requests
# from config import Conf
# test_file = os.path.join(Conf.get_data_path(), 'yaml_data/forward_policy/get_fb.yml')
# print(test_file)

# data_list = YamlReader(test_file).data_all()
# print(data_list)
# data_list = current_test_file.get_cases()
@allure.feature('{fun_name}')
@pytest.mark.parametrize("data", {data}, ids={ids})
@pytest.mark.sss
class Test_{fun_name}():
    @staticmethod
    def test_{fun_name}(data):
        parameter = data["parameter"]
        print("=====",data)
        exp = data["exp"]["exp_re"]
        print("==---",exp)
        mock_value = data.get("mock_value")
        class_instance = {class_name}()
        '''
        mock 虚拟数据
        '''
        if mock_value:
            {mock_data}
        # egroup.get_egroup_interfaces = mock.Mock(return_value=mock_value)
        # elag.get_elag_interfaces = mock.Mock(return_value=mock_value)
        
        find = class_instance.{fun_name}({parameter})
        
        assert find == exp
"""
class CSV_Parser:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.df = pd.read_excel(csv_file, keep_default_na=False)

    def get_test_cases_groups(self):
        """
        group test cases by case['TestCase']
        """
        tmp = []
        # self.select_cases_match_level(level)
        for id_index in self.df['用例编号']:
            tmp.append(int(id_index.split('_')[0]))
    
        self.df['id_index'] = tmp 
        grouped_cases = self.df.groupby(by=['id_index'])
        return grouped_cases

    def get_cases(self):
        test_cases = []
        cases_group = self.get_test_cases_groups()
        for i in cases_group.groups:
            tmp_var = cases_group.get_group(i)
            test_cases.append(tmp_var.to_dict(orient='records'))
        test_cases = sorted(test_cases, key=lambda e:e[0]['id_index'], reverse=False)

        return test_cases

    def get_case_count(self):
        """
        get the case count.
        """
        return self.get_test_cases_groups().ngroups

if __name__ == "__main__":

    # scripts_template()
    level = [1,2,3,4]
    current_test_file = CSV_Parser(csv_file="用例模板.xlsx")
    valid_cases = current_test_file.get_cases()
    print("111111111111", valid_cases)
    case_count  = current_test_file.get_case_count()
    print(case_count)
    
    for case in valid_cases:
        list1 = []
        list2 = []
        item = case[0].get("项目名")
        class_name = case[0].get("类")
        if case[0].get("类") != '':
            print(case[0].get("项目名"))
            print(case[0].get("类"))
            code_path = "code." + case[0].get("项目名")+"."+case[0].get("类")
        else:
            code_path = "code." + case[0].get("项目名")+"."+case[0].get("用例名")
        test_case_name = case[0]["用例名"]

        test_name = "test_{0}".format(test_case_name)
        filename = os.path.join(cur_path, "{0}.py".format(test_name))
        st = ""
        parameter_st = ""
        for i in case:
            dict1 = {}
            dict1["exp"] = ast.literal_eval(i["exp"])
            print(i.get("mock_value"))
            print(type(i.get("mock_value")))
            if i.get("mock_value"):
                print(i.get("mock_value"))
                dict1["mock_value"] = ast.literal_eval(i["mock_value"])
                # 将mock_value 数据转化为字符串,格式化模板
                for key in dict1["mock_value"].keys():
                    print("000000",key)
                    if "self" in key:
                        print(key)
                        new = key.replace('self', class_name)
                        print(new)
                        key1 = new
                        st1 = "    "*3 + "%s = %s"%(key1, "mock.Mock(return_value = mock_value.get('"+key+"'))")
                    else:
                        st1 = "    "*3 + "%s = %s"%(key, "mock.Mock(return_value = mock_value.get('"+key+"'))")
                    if st1 not in st:
                        st = st + '\n' + st1
            dict1["parameter"] = ast.literal_eval(i["parameter"])
            dict1["discription"] = {}
            list2.append(i["测试描述"])
            dict1["discription"]["title"] = i["测试描述"]
            
            list1.append(dict1)
           
            # 将mock_value 数据转化为字符串,格式化模板
            # for key in dict1["mock_value"].keys():
            #     print("000000",key)
            #     st1 = "        %s = %s"%(key, "mock.Mock(return_value = mock_value.get('"+key+"'))")
            #     if st1 not in st:
            #         st = st + '\n' + st1
            # 将 parameter 数据转化为字符串,格式化模板
            for key in dict1["parameter"].keys():
                print("`````",key)
                st2 = "%s=%s"%(key, "parameter['"+key+"']")
                if st2 not in parameter_st and parameter_st != '':
                    parameter_st = parameter_st + "," + st2
                elif st2 not in parameter_st:
                    parameter_st = parameter_st + st2
        testfile_path = '../testcases/UnitTest/' + item 
        print(testfile_path)
        if not os.path.exists(testfile_path):
            os.mkdir(testfile_path)
        with open(testfile_path + "/test_" + test_case_name+".py", "w", encoding='utf-8') as out:
            out.write(temp.format(data=list1, fun_name=test_case_name, mock_data=st, parameter=parameter_st, path=code_path, class_name=class_name, ids=list2))
    print(list1)
