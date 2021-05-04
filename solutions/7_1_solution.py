ospf_template = '''
Prefix              {:15}
AD/Metric           {:15}
Next-Hop            {:15}
Last update         {:15}
Outbound interface  {:15}
'''

with open('ospf.txt') as f:
    for line in f:
        values = line.split()
        pref= values[0]
        ad = values[2]
        nh = values[4][0:len(values[4]) - 1]
        lu = values[5][0:len(values[5]) - 1]
        outif = values[6]
        print(ospf_template.format(pref, ad, nh, lu, outif))
