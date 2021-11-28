import ipaddress

"""
Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']
"""
 
ip_list = ['8.8.4.4-10', '1.1.1.1', '172.21.41.128-172.21.41.132']
 
def convert_ranges_to_ip_list(ipadd):
    
    newiplist = []    
    
    for ip in ip_list:
        if len(ip.split("-")) > 1 and len(ip.split('-')[1].split('.')) == 1:
            startipv4 = ip.split("-")[0]
            startoctet = int(ip.split('-')[0].split('.')[3])
            endoctet = int(ip.split('-')[1])
            for i in range(startoctet, endoctet + 1):
                newiplist.append("{}.{}.{}.{}".format(startipv4.split('.')[0], startipv4.split('.')[1], startipv4.split('.')[2], i ))
        elif len(ip.split("-")) > 1 and len(ip.split('-')[1].split('.')) > 1:
            startipv4 = ip.split("-")[0]
            startoctet = int(ip.split('-')[0].split('.')[3])
            endoctet = int(ip.split('-')[1].split('.')[3])
            for i in range(startoctet, endoctet + 1):
                newiplist.append("{}.{}.{}.{}".format(startipv4.split('.')[0], startipv4.split('.')[1], startipv4.split('.')[2], i ))
        else:
            newiplist.append(ip)
            
    print(newiplist)        
    return newiplist
    

if __name__ == "__main__":
    convert_ranges_to_ip_list(ip_list)
    
