from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
import json

app = FastAPI()

# 添加 CORS 中间件,实现浏览器中跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

date = 'phi_data.json'
# 将文件路径写在一个位置，方便更改

def informations(key_word):
    with open(date, 'r') as d:
        out_data = set()
        a = json.load(d)
        for i in a:
            out_sign = True
            if key_word == i:
                out_sign = False
                e = a.get(key_word)
                out_data.add(f"\n\n·歌曲名称{e.get('sname')}\n·歌曲别名{e.get('soname')}\n·歌曲长度{e.get('sslen')}\n·难度定数{e.get('sds')}\n·曲师{e.get('squshi')}\n·谱师{e.get('spushi')}\n")
                # print(f"\n\n·歌曲名称{e.get('sname')}\n·歌曲别名{e.get('soname')}\n·歌曲长度{e.get('sslen')}\n·难度定数{e.get('sds')}\n·曲师{e.get('squshi')}\n·谱师{e.get('spushi')}\n")
            elif out_sign:
                out_data.add("未找到相关歌曲")
    return out_data

@app.get("/name/{name}")
def read_root(name):
    data = informations(name)
    return {"message": str(data)}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# print(str(informations("Lost Civilization")))