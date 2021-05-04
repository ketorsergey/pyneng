netmask = input('Введите сеть/маску в формате X.X.X.X/YY ')
ip = netmask.split("/")[0]
mask = netmask.split("/")[1]
mask_int = int(mask)
ip_oct = ip.split(".")

ip_template = '''
Network:
{:<8} {:<8} {:<8} {:<8}
{:08b} {:08b} {:08b} {:08b}
'''

ip_oct1_int = int(ip_oct[0])
ip_oct2_int = int(ip_oct[1])
ip_oct3_int = int(ip_oct[2])
ip_oct4_int = int(ip_oct[3])

ip_oct1_bin = "0" * (8 - len(bin(ip_oct1_int)[2:])) + bin(ip_oct1_int)[2:]
ip_oct2_bin = "0" * (8 - len(bin(ip_oct2_int)[2:])) + bin(ip_oct2_int)[2:]
ip_oct3_bin = "0" * (8 - len(bin(ip_oct3_int)[2:])) + bin(ip_oct3_int)[2:]
ip_oct4_bin = "0" * (8 - len(bin(ip_oct4_int)[2:])) + bin(ip_oct4_int)[2:]

ipadd_bin = ip_oct1_bin + ip_oct2_bin + ip_oct3_bin + ip_oct4_bin
network_bin = ipadd_bin[0:mask_int] + (32-mask_int) * "0"

network_bin_oct1 = network_bin[0:8]
network_bin_oct2 = network_bin[8:16]
network_bin_oct3 = network_bin[16:24]
network_bin_oct4 = network_bin[24:32]

network_oct1 = int(network_bin_oct1, 2)
network_oct2 = int(network_bin_oct2, 2)
network_oct3 = int(network_bin_oct3, 2)
network_oct4 = int(network_bin_oct4, 2)

print(ip_template.format(network_oct1, network_oct2, network_oct3, network_oct4, network_oct1, network_oct2, network_oct3, network_oct4))

bmask = "1" * mask_int + (32-mask_int) * "0"

mask_template = '''
Mask:
{}
{:<8} {:<8} {:<8} {:<8}
{:08b} {:08b} {:08b} {:08b}
'''

bmask_oct1 = bmask[0:8]
bmask_oct2 = bmask[8:16]
bmask_oct3 = bmask[16:24]
bmask_oct4 = bmask[24:32]

bmask_1 = int(bmask_oct1, 2)
bmask_2 = int(bmask_oct2, 2)
bmask_3 = int(bmask_oct3, 2)
bmask_4 = int(bmask_oct4, 2)

print(mask_template.format("/" + mask, bmask_1, bmask_2, bmask_3, bmask_4, bmask_1, bmask_2, bmask_3, bmask_4))
