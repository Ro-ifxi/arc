import json
# 导入python包

date = './zhutao/phi_data.json'
# 将文件路径写在一个位置，方便更改

def chaxun():
    print(f'\nhi~ 这里是查询姬，需要我为您做些什么?\n-----------------\n您可输入的查询类型有\n')
    print(f'·歌曲名称：name\n·歌曲别名:oname\n·歌曲长度：sslen\n·难度定数：sds\n·曲师：squshi\n·谱师：spushi\n\n-----------------\n')
    # date = 'phi_shuju.json'
    with open(date, 'r') as d:
        a = json.load(d)
        sa = set()
        while True:
            b = str(input("请选择查询类型:"))
            c = str(input("请输入关键字:"))
            for i in a:
                if b == 'name' or b == 'oname':
                    out_sign = True
                    if c == i:
                        out_sign = False
                        e = a.get(c)
                        print(f"\n\n·歌曲名称{e.get('sname')}\n·歌曲别名{e.get('soname')}\n·歌曲长度{e.get('sslen')}\n·难度定数{e.get('sds')}\n·曲师{e.get('squshi')}\n·谱师{e.get('spushi')}\n")
                    elif out_sign:
                        # 如果按照原来的方法，每比较一次将会产生一次输出，所以只有不存在才打印。
                        sa.add("未找到相关歌曲")
                elif b != 'name' and b != 'oname':
                    for f in a.keys():
                        if c in a.get(f).values():
                            sa.append(a.get(f).get('sname'))
                            print(f"为您找到以下相关歌曲哦~\n{sa}")
                else:
                    print('未找到相关歌曲')
            if b or c == 'e':
                break
        print(list(sa))

def shuru():
    # date = 'phi_shuju.json'
    print(f'\nhi~ 这里是输入姬，你可以按照提示输入歌曲信息~~')
    print(f'-----------------------------------------')
    allsongs = {}
    while True:
        name = input("·曲名:")
        oname = input("·别名:")
        ds = input("·定数:")
        slen = input("·长度:")
        pushi = input("·谱师:")
        qushi = input("·曲师:")
        song = {'sname': name, 'sds': ds, 'soname': oname, 'sslen': slen, 'spushi': pushi, 'squshi': qushi}
        allsongs = {name: song}
        with open(date, 'a+')as d:
            json.dump(allsongs, d, sort_keys=True, indent=4)
            
        huifu = input("-------------\n是否继续输入？（end/c):")
        if huifu == 'end':
            break
        

while True:
    a1 = input("--------------------\n\n请选择查询（c）/输入（s）\n（输入e以终止）\n\n--------------------\n:")
    if a1 == 's':
        shuru()
    if a1 == 'c':
        chaxun()
    else:
        break
