
london_co = {
        "r1": {
                    "location": "21 New Globe Walk",
                    "vendor": "Cisco",
                    "model": "4451",
                    "ios": "15.4",
                    "ip": "10.255.0.1"
                },
        "r2": {
                    "location": "21 New Globe Walk",
                    "vendor": "Cisco",
                    "model": "4451",
                    "ios": "15.4",
                    "ip": "10.255.0.2"
                },
        "sw1": {
                    "location": "21 New Globe Walk",
                    "vendor": "Cisco",
                    "model": "3850",
                    "ios": "3.6.XE",
                    "ip": "10.255.0.101",
                    "vlans": "10,20,30",
                    "routing": True
                }
}

hostname = input('Введите имя устройства: ')
list_keys = list(london_co['{}'.format(hostname)].keys())
str_list_keys = '(' + ', '.join(list_keys) + '):'
parameter = input('Введите имя параметра {}'.format(str_list_keys))

print('\n' + '-' * 30)
print(london_co['{}'.format(hostname)]['{}'.format(parameter)])
