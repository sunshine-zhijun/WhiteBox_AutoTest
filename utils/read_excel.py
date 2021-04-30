import os
import time
import os
import time
import pandas as pd
import json
import ast

class ExcelParser:
    def __init__(self, excel_file):
        self.excel_file = excel_file
        self.df = pd.read_excel(excel_file, keep_default_na=False)

    def get_test_cases_groups(self):
        """
        group test cases by case['TestCase']
        """
        tmp = []
        # self.select_cases_match_level(level)
        for id_index in self.df['ID']:
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