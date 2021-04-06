#!/usr/bin/env python
# coding=utf-8
import pytest
import allure
import os




def export_test():
    os.system("touch test_test.py")
    with open ("test_test.py") as f:
        f.write("********")





if __name__ == '__main__':
    # pytest.main(['-s', '-q', '--alluredir', './report/xml'])
    pytest.main()
    # export_test()
    # os.system('allure serve report/xml')
