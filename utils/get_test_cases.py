#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""

@File    :   separate_cases
@Time    :   2020/10/2020/10/20 19:14:08
@Author  :   Jia Zezhi
@Version :   1.0
@Contact :   jiazezhi@asterfusion.com
@License :   (C)Copyright 2017-2020, Asterfusion
@Desc    :   None

"""
import pandas as pd
import pathlib
# import util.globalVar as gl


class CSV_Parser:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.df = pd.read_csv(csv_file)

    def get_test_cases_groups(self, level):
        """
        group test cases by case['TestCase']
        """
        tmp = []
        self.select_cases_match_level(level)
        for id_index in self.df['ID']:
            tmp.append(int(id_index.split('_')[0]))
        
        self.df['id_index'] = tmp
        grouped_cases = self.df.groupby(by=['TestCase', 'id_index'])

        return grouped_cases

    def replace_parameter(self, inlet, outlet1, outlet2, outlet3, target_ip):
        """
        change ingress/egress to adapt different product.
        """

        self.df = self.df.replace(r'\$<inlet>', inlet, regex=True)
        self.df = self.df.replace(r'\$<outlet1>', outlet1, regex=True)
        self.df = self.df.replace(r'\$<outlet2>', outlet2, regex=True)
        self.df = self.df.replace(r'\$<outlet3>', outlet3, regex=True)
        self.df = self.df.replace(r'\$<target_ip>', target_ip, regex=True)

        return self.df

    def select_cases_match_level(self, level):
        """
        select the cases that match test level.
        """
        self.df = self.df[self.df['Level'].isin(level)]

    def get_cases(self, level, inlet, outlet1, outlet2, outlet3, target_ip):
        test_cases = []
        self.replace_parameter(inlet, outlet1, outlet2, outlet3, target_ip)
        cases_group = self.get_test_cases_groups(level)
        for i in cases_group.groups:
            tmp_var = cases_group.get_group(i)
            test_cases.append(tmp_var.to_dict(orient='records'))
        test_cases = sorted(test_cases, key=lambda e:e[0]['id_index'], reverse=False)
        # print(len(test_cases))

        return test_cases

    def get_case_count(self, level):
        """
        get the case count.
        """
        return self.get_test_cases_groups(level).ngroups

if __name__ == '__main__':

    level = [1,2,3,4]
    current_test_file = CSV_Parser(csv_file="testcases\X564P\Interface\Interface.csv")
    valid_cases = current_test_file.get_cases(level, 'CN', 'NB1', 'NB2', 'NB3', '192.168.0.1')
    case_count  = current_test_file.get_case_count(level)
    # print(case_count)
    for i in valid_cases:
        print(type(i[2]))
        print("\n")
        print("\n")

