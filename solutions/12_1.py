import ipaddress
import subprocess
 
ip_list = ['8.8.8.8', '10.10.10.10', '4.4.4.4' , '192.168.88.1']
aliveip = []
deadip = []
 
def ip_list_check(ipadd):
    for ip in ipadd:
        reply = subprocess.run(['ping', '-c', '2', '-n', ip], stdout=subprocess.DEVNULL)
        if reply.returncode == 0:
            print(f"ip {ip} is alive")
            aliveip.append(ip)
        else:
            print(f"ip {ip} is unreachable")
            deadip.append(ip)
            
    return aliveip, deadip

if __name__ == "__main__":
    ip_list_check(ip_list)
    print(aliveip)
    print(deadip)
    
