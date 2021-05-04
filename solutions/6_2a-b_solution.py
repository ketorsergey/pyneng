ip_address = input('Введите IP-адрес: ')

ip_correct = False

while not ip_correct:
	if ip_address.count(".") != 3: 
		pass
	dec_octets = ip_address.split('.')
	for octet in dec_octets: 
		if octet.isdigit() is False: 
			pass
			break
		elif int(octet) not in range(0, 256):
			pass
			break
	else: 
		print('Корректный ip')
		ip_correct = True
		break
	ip_address = input('Некорректный IP, введите IP-адрес еще раз: ')

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
