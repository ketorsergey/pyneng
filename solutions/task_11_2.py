
from task_11_1 import parse_cdp_neighbors
from pprint import pprint

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
    ]

def create_network_map(filenames):
    
    network_map = {}
    
    for filename in filenames:
        with open(filename) as command_output:
            parsed = parse_cdp_neighbors(command_output.read())
            network_map.update(parsed)
    return network_map
   
   
if __name__ == "__main__":
    topology = create_network_map(infiles)
    pprint(topology)
