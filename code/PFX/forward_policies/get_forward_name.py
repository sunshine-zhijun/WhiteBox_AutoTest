#!/usr/bin/env python
# coding=utf-8
true = True
false = False
policy1 = {
    "104461": {
        "configuration": {
            "ace_type": "ip",
            "ip_version": "ipv4",
            "action": "forward",
            "evif_name": "egroup1",
            "en_count": true,
            "dscp": "55",
            "is_exact_match": false
        }
    }
}

global_egroups={
    "1": {
        "configuration": {
            "interfaces": [
                "C1",
                "C2",
                "C3"
            ],
            "comment": "aster@123"
        }
    }
}
global_elags={
    "1": {
        "configuration": {
            "interfaces": [
                "C1",
                "C2",
                "C3"
            ],
            "comment": "aster@123"
        }
    }
}

class egroup():
    @staticmethod
    def get_egroup_interfaces(egroup_id):
        if egroup_id  not in global_egroups:
            return None
        egroup = global_egroups[egroup_id]
        return egroup['configuration']['interfaces']
class elag():
    @staticmethod
    def get_elag_interfaces(elag_id):
        if elag_id not in global_elags:
            return None
        elag = global_egroups[elag_id]
        return elag['configuration']['interfaces']



class forward_policy():
    def get_egress_port_keys_of_policy_name_todict(self,self_dict:dict,policy_name)->dict:
        find_egress_port_dict={}
        for key in self_dict.keys():
            if 'evif_name' in self_dict[key]['configuration']:
                print(self_dict)
                evif_name=self_dict[key]['configuration']['evif_name']
                if evif_name.startswith('elag'):
                    port_type = 'elag'
                    port_id = evif_name[4:]
                    egress_ports = elag.get_elag_interfaces(port_id)
                elif evif_name.startswith('egroup'):
                    port_type = 'egroup'
                    port_id = evif_name[6:]
                    print(port_id)
                    egress_ports = egroup.get_egroup_interfaces(port_id)
                    print("egress_ports is %s"%egress_ports)
                else:
                    egress_ports =evif_name
                if type(egress_ports)==list:
                    for every_port in egress_ports:
                        find_egress_port_dict[every_port]=[policy_name]
                else:
                    find_egress_port_dict[egress_ports]=[policy_name]
        return find_egress_port_dict



if __name__ == '__main__':
    fb = forward_policy()
    dict1 = fb.get_egress_port_keys_of_policy_name_todict(policy1, "policy1")
    print(dict1)
