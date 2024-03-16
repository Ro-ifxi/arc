import json
import os

def chaxun():
    m2 = "1"
    m3 = "2"
    print(f'{m2}\n{m3}')
    date = 'phi_shuju.json'
    with open(date,'r')as d:
        a = json.load(d)
        sa = []
        while True:
            b = str(input("1:"))
            c = str(input("2:"))
            for i in a:
                i = dict(i)
                if b == 'name' or b == 'oname':
                    if c == i[b]:
                        for keys in i :
                            print(f'{keys}:{i[keys]}')
                elif b !='name' and b !='oname':
                    if c == i[b]:
                        sa.append(i['name'])
                else:
                    print(wzd)
                    break
            print(sa)
                    
