f = open("sh_cdp_n_sw1.txt") 
command_output = f.read().split('\n')
cdp = {}

for line in command_output:
    if '>' in line:
        hostname = line.split('>')[0]
        print(hostname)
        
    elif len(line.split()) > 0 and line.split()[0] != "Capability" and line.split()[0] != "S" and line.split()[0] != "Device":
        remote_hostname = line.split()[0]
        local_intf = line.split()[1] + line.split()[2]
        remote_intf = line.split()[-2] + line.split()[-1]
        print(remote_hostname)
        print(local_intf)
        print(remote_intf)
        cdp[(hostname, local_intf)] = (remote_hostname, remote_intf)
        
        
        
print(cdp)
f.close()
