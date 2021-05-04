i_port_type = input('Введите режим работы интерфейса (access/trunk):')
i_interface_num = input('Введите тип и номер интерфейса: ')
vlans_num = {
'access': "Введите номер VLAN: ",
'trunk': "Введите разрешенные VLANы: "
            }


interface_type = {
            'access': 
            [
                                "switchport mode access", "switchport access vlan {}",
                                "switchport nonegotiate", "spanning-tree portfast",
                                "spanning-tree bpduguard enable"
                                ],
            'trunk': 
            [
                                "switchport trunk encapsulation dot1q", "switchport mode trunk",
                                "switchport trunk allowed vlan {}"
                                ]
}
print(vlans_num[i_port_type])
i_vlans = input()
print('\n' + "interface " + i_interface_num)
print('\n'.join(interface_type[i_port_type]).format(i_vlans))
