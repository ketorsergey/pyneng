ip_address = input('Введите IP-адрес: ') 
dec_octets = ip_address.split('.') 

if int(dec_octets[0]) in range(1, 224): 
    print('unicast') 
elif int(dec_octets[0]) in range(224, 240): 
    print('multicast') 
elif ip_address == '255.255.255.255': 
    print('local broadcast') 
elif ip_address == '0.0.0.0': 
    print('unassigned') 
else: 
    print('unsused') 

