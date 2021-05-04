access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}

for intf, vlans in trunk.items():
    print("interface FastEthernet" + intf)
    for command in trunk_template:
        if command.endswith("allowed vlan"):
            if vlans[0].endswith('add'):
                print(f" {command} " + vlans[0] +' '+ vlans[1] +','+ vlans[2])
            elif vlans[0].endswith('only'):
                print(f" {command} " + vlans[1] +','+ vlans[2])
            elif vlans[0].endswith('del'):
                print(f" {command} " + 'remove' + ' ' + vlans[1])
            else:
                pass
        else:
            print(f" {command}")
