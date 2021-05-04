with open('CAM_table.txt') as f:
    for line in f:
        if '/' in line:
            line = line.split()
            print('{:10}{:20}{}'.format(line[0],line[1],line[3]))
        else:
            continue
            
