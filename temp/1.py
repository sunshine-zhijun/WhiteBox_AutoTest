#!/usr/bin/env python
# coding=utf-8
global tab
tab = "    "
    

def write_py(parameter, mock_value, exp, fun_name, fun_sc, class_name):
    with open ('./test.py', 'w') as f:
        f.write('#!/usr/bin/env python \n# coding=utf-8\n')
        f.write("class Test%s():\n"%fun_name)
        f.write(tab + "def test_%s():\n"%fun_name)
if __name__ == '__main__':
    parameter = {'interface':{'config':'111'}}

    print(parameter)
    mock_value = {
    "egroup.get_egroup_interfaces": "[1,2,3]",
    "elag.get_elag_interfaces": "[11,12,13]"
    }
    print(mock_value)
    exp = "200"
    fun_name = "get_fb"
    fun_sc = "获取转发策略"
    class_name = "forw"
    write_py(parameter, mock_value, exp, fun_name, fun_sc, class_name)
