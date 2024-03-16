import json
def shuru():
    date = 'phi_shuju.json'
    m1 = "1"
    m2 = "2"
    print(m1,m2)
    while True:
        name = input("1:")
        oname = input("2:")
        ds = input("3:")
        slen = input("4:")
        pushi = input("5:")
        qushi = input("6:")
        song ={'sname':name,'sds':ds,'soname':oname,'sslen':slen,'spushi':pushi,'squshi':qushi}
        with open(date,'a+')as d:
            json.dump(song,d,sort_keys=True,indent=4)
            
        huifu = input("是否继续（end/c):")
        if huifu == 'end':
            break
        