mac_table = []

with open('CAM_table.txt') as f:
    for line in f:
        if '/' in line:
            line = line.split()
            vlan, mac, mactype, intf = line
            mac_table.append([int(vlan), mac, intf])
        else:
            continue
            
for vlan, mac, intf in sorted(mac_table):
    print('{:<10}{:20}{}'.format(vlan, mac, intf))
