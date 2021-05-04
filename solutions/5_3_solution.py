i_port_type = input('Введите режим работы интерфейса (access/trunk):')
i_interface_num = input('Введите тип и номер интерфейса: ')
i_vlans = input('Введите номер влан(ов): ')

interface = {
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

print('\n' + "interface " + i_interface_num)
print('\n'.join(interface[i_port_type]).format(i_vlans))
