with open("config_sw1.txt") as f:
    for line in f:
        if line.startswith('!'):
            continue
        else:
            print(line.rstrip())
