import json
# 导入python包


date = 'arcdate.json'
with open(date, 'r', encoding='utf-8') as d:
    a = json.load(d)
    sa = []
    # 总列表，没一个元素为一首歌
    for i in a:
        for e in a[i]:
            sa.append(e)


all_dates = {}
for i in sa:
    en = i.get("title_localized").get("en")  
    # 歌曲名称
    artist = i.get("artist")
    # 曲师
    bpm = i.get("bpm")
    # bpm
    infos = i.get("difficulties")
    uses = infos[2]
    chartDesigner = uses.get("chartDesigner")
    # 谱师
    rating = uses.get("rating")
    # 定数
    
    all_dates[en] = {"sds":rating, 
                        "sname":en, 
                        "soname":None, 
                        "spushi":chartDesigner, 
                        "squshi":artist,
                        "sslen":bpm
                        }


write_path = 'phi_data.json'
# 通过设置文件路径，就能够生成数据文件，将该文件路径在主模块中替换，就可以直接使用

with open(write_path, 'a+', encoding='utf-8') as f:
    json.dump(all_dates, f, indent=1)
        
    


    





    