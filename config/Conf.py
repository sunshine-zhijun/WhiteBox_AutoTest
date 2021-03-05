#!/usr/bin/env python
# coding=utf-8
# coding=utf-8
import os
from utils.YamlUtil import YamlReader
# 1. 获取项目基本目录
# 1.2 获取当前项目的绝对路径
current = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(current))
print(current, BASE_DIR)
# 1.3 定义config目录的路径
_config_path = BASE_DIR + os.sep + "config"
_data_path = BASE_DIR + os.sep + "data"

def get_config_path():
    return _config_path
# 1.4 定义conf.yml的文件路径
_config_file = _config_path + os.sep + 'conf.yml'
def get_config_file():
    return _config_file
def get_data_path():
    return _data_path

# 2. 读取配置文件
class ConfigYaml():
    def __init__(self):
        self.config = YamlReader(get_config_file()).data()

        # 获取需要的信息
        def get_config_url(self):
            return self.config['BASE']['test']['url']

if __name__ == "__main__":
    conf_read = ConfigYaml()
    print(conf_read)

