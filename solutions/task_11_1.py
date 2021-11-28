def parse_cdp_neighbors(command_output):
    """
    Тут мы передаем вывод команды одной строкой потому что именно в таком виде
    будет получен вывод команды с оборудования. Принимая как аргумент вывод
    команды, вместо имени файла, мы делаем функцию более универсальной: она может
    работать и с файлами и с выводом с оборудования.
    Плюс учимся работать с таким выводом.
    """
   
    cdp = {}

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
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))
