from task_11_1 import parse_cdp_neighbors
from task_11_2 import create_network_map
from draw_network_graph import draw_topology
from pprint import pprint

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
    ]

def true_topology(topology_dict):
    true_topology = {}
    for key, value in topology_dict.items():
        key, value = sorted([key, value])
        true_topology[key] = value
        
    return true_topology
        
   
if __name__ == "__main__":
    topology_dict = create_network_map(infiles)
    draw_topology(true_topology(topology_dict), output_filename="topology")
   
