import os
import sys
from utils.read_excel import  ExcelParser
from utils.template import *
import os
import time
import os
import time
import pandas as pd
import ast
from common.intial import *
from common.log import *
# from run import *

# CODE_PATH = CODE_PATH + project
file_list = []

# 遍历数据目录(文件),返回excel文件路径
def traverse(f):
    if os.path.isfile(f):
        file_list.append(f)
        return file_list
    fs = os.listdir(f)
    for f1 in fs:
        tmp_path = os.path.join(f,f1)
        if not os.path.isdir(tmp_path):
            if '.xlsx' in tmp_path:
                file_list.append(tmp_path)
        else:
            traverse(tmp_path)
    return file_list


# 根据模板生成test脚本文件
class GenerateTest():
    def __init__(self, path_excel):
        self.path_excel = path_excel
        self.default_temp = 'temp1'
    
    def generate_case(self):
        try:
            current_test_file = ExcelParser(self.path_excel)
            mode_code = self.path_excel.strip('xlsx').split('/')[-1].strip('.')
            unittest_path = TEST_PATH
            valid_cases = current_test_file.get_cases()
            case_count  = current_test_file.get_case_count()
            # logger.success('The total number of newly generated test scripts is {}', case_count)
            # print("本次共新生成测试脚本数量为:%s"%(valid_cases, case_count))
            for case in valid_cases:
                list1 = []
                list2 = []
                st = ""
                parameter_st = ""
                test_path = ''
                for root, dirs, files in os.walk(CODE_PATH):
                    for file in files:
                        if file == mode_code + '.py':
                            item = os.path.dirname(os.path.join(root, file)).replace(CODE_PATH, '') + '/'
                class_name = case[0].get("ClassName")
                
                if item != None:
                    import_code_path = (CODE_PATH + item).replace('/', '.') + mode_code
                case_name = case[0]["FunctionName"]
                test_name = "test_{0}".format(case_name)
                test_path = unittest_path + item
                if not os.path.exists(test_path):
                    os.makedirs(test_path)
                test_file_path = os.path.join(test_path, "{0}.py".format(test_name))
                try:
                    for i in case:
                        dict1 = {}
                        # 期望数据转化为json格式
                        dict1["exp"] = ast.literal_eval(i["Expect"])
                        dict1["parameter"] = ast.literal_eval(i["Parameter"])
                        dict1["discription"] = {}
                        list2.append(i["Description"])
                        dict1["discription"]["title"] = i["Description"]
                        # mock value数据转化为json格式
                        if i.get("MockValue"):
                            dict1["mock_value"] = ast.literal_eval(i["MockValue"])
                            # 将mock_value 数据转化为字符串,格式化模板
                            for key in dict1["mock_value"].keys():
                                if "self" in key:
                                    new_key = key.replace('self', class_name)
                                    mock_string = "    "*3 + "%s = %s"%(new_key, "mock.Mock(return_value = mock_value.get('"+key+"'))")
                                else:
                                    mock_string = "    "*3 + "%s = %s"%(key, "mock.Mock(return_value = mock_value.get('"+key+"'))")
                                if mock_string not in st:
                                    st = st + '\n' + mock_string      
                        list1.append(dict1)
                        #取参格式化
                        for key in dict1["parameter"].keys():
                            st2 = "%s=%s"%(key, "parameter['"+key+"']")
                            if st2 not in parameter_st and parameter_st != '':
                                parameter_st = parameter_st + "," + st2
                            elif st2 not in parameter_st:
                                parameter_st = parameter_st + st2

                    with open(test_file_path, "w", encoding='utf-8') as out:
                        if self.default_temp == "temp1":
                            out.write(temp1.format(data=list1, fun_name=case_name, mock_data=st, parameter=parameter_st, path=import_code_path, 
                                    class_name=class_name, ids=list2))
                except Exception as e:
                    print(e)

        except Exception as e:
            logger.error("Failed to automatically generate test script. {}", e)


if __name__ == "__main__":
    path1 = os.path.abspath(os.path.dirname(__file__))
    print(path1)
    path = path1 + '/../data/excel_data/forward_policy.xlsx'
    file_list = traverse(path)
    print(file_list)
    for excel in file_list:
        testcase = GenerateTest(excel)
        testcase.generate_case()
