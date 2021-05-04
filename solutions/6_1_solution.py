mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
result = mac
i = 0

for macs in mac:
        smac = macs.split(':')
        result[i] = smac[0] + '.' + smac[1] + '.' + smac[2]
        i = i + 1

print(result)
