ignore = ["duplex", "alias", "configuration"]

res = open('res_config.txt', 'w')

with open("config_sw1.txt") as f:
    for line in f:
        if line.startswith('!'):
            continue
        elif ignore[0] in line or ignore[1] in line or ignore[2] in line:
            continue
        else:
            res.write(line.rstrip() + '\n')
res.close()
