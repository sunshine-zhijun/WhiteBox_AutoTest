#!/usr/bin/env python
# coding=utf-8
import pytest
import argparse
# import allure
import os
import time
from utils.generate_caces import traverse
from utils.generate_caces import GenerateTest
from common.log import *

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--project', type=str, default='PFX')
parser.add_argument('--file', type=str, default='')
parser.add_argument('--auto_write', type=str, default='true')
parser.add_argument('--pt', action='append', help='pytest command line argument. such as: --pt=-s --pt=-v')

try:
    args = parser.parse_args()
    project = args.project
    fun_file = args.file
    auto_write = args.auto_write
    pytest_parameter = args.pt

except Exception as e:
    logger.error('Invalid parameter.', e)


def generate(excel_path=None):
    path1 = os.path.abspath(os.path.dirname(__file__))
    excel_path = '/data/excel_data/' + project
    path = path1 + excel_path
    file_list = []
    file_list = traverse(path)
    if not fun_file and fun_file in file_list:
        logger.info(fun_file)

    logger.trace("进行待测试的excel文件列表:\n{}",file_list)
    for excel in file_list:
        if fun_file and fun_file in excel.split('/')[-1] or not fun_file:
            testcase = GenerateTest(excel)
            testcase.generate_case()

def pytest_run(pytest_parameter):
    list1 = ['--alluredir', 'report/allure-data', '--html', 'report/report.html',
            '--cov', 'code', '--cov-report', 'html:report/coverage-report']
    if pytest_parameter:
        list1.extend(pytest_parameter)
    logger.debug('pytest parameter: {}', list1)
    pytest.main(list1)


logoStr = """ 
 █████╗ ██╗   ██╗████████╗ ██████╗ ████████╗███████╗███████╗████████╗ 
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝ 
███████║██║   ██║   ██║   ██║   ██║   ██║   █████╗  ███████╗   ██║    
██╔══██║██║   ██║   ██║   ██║   ██║   ██║   ██╔══╝  ╚════██║   ██║    
██║  ██║╚██████╔╝   ██║   ╚██████╔╝   ██║   ███████╗███████║   ██║    
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝    ╚═╝   ╚══════╝╚══════╝   ╚═╝    
┌┐ ┬ ┬ ╔═╗┬ ┬┌─┐┌─┐┬─┐ ╔╦╗┌─┐┌─┐┌┬┐ ╔╦╗┌─┐┌─┐┌┬┐ | Welcome to AutoTest
├┴┐└┬┘ ╚═╗│ │├─┘├┤ ├┬┘  ║ ├┤ └─┐ │   ║ ├┤ ├─┤│││ | Version: v1.0.0    
└─┘ ┴  ╚═╝└─┘┴  └─┘┴└─  ╩ └─┘└─┘ ┴   ╩ └─┘┴ ┴┴ ┴ | Have fun!          
                         https://
"""


if __name__ == '__main__':
    logger.log(display, logoStr)
    logger.info('PROJECT:  {}', project)
    logger.log(display, "\n\n" + '*'*40+'Start Test'+'*'*40 + '\n')
    if auto_write == 'true':
        try:
            logger.info('Automatically generate test scripts')
            generate()
        except Exception as e:
            logger.warning('fail to generate test scripts. {}', e)
        finally:
            logger.info('Unit testing with pytest')
    pytest_run(pytest_parameter)

