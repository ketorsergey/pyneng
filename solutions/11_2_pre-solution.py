from pprint import pprint

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
    ]

def parse_cdp_neighbors(infiles):
    
    cdp = {}
    
    for files in infiles:
        
        command_output = open("{}".format(files)).read()
            
        for line in command_output.split('\n'):
            if '>' in line:
                hostname = line.split('>')[0]
        
            elif len(line.split()) > 0 and line.split()[0] != "Capability" and line.split()[0] != "S" and line.split()[0] != "Device":
                remote_hostname = line.split()[0]
                local_intf = line.split()[1] + line.split()[2]
                remote_intf = line.split()[-2] + line.split()[-1]
                cdp[(hostname, local_intf)] = (remote_hostname, remote_intf)
        
    return cdp
        


if __name__ == "__main__":
    
    pprint(parse_cdp_neighbors(infiles))
