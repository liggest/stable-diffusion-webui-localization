"""
    WebUI extension launch script
"""

import json
from pathlib import Path
import shutil

here=Path(__file__).parent
ext_base=here.parent
here_tags=here / "tags"
tag_file="danbooru.csv"

autocomplete_tags=None

tags=ext_base.glob("*/tags/") # find autocomplete base
for d in tags:
    if any(f.name==tag_file for f in d.iterdir()):
        autocomplete_tags=d
        break

if autocomplete_tags: # 安装了 tag-autocomplete
    shutil.copytree(here_tags,autocomplete_tags,dirs_exist_ok=True)

mix_localization=False
if mix_localization:
    here_locs=here / "localizations"
    zh_file="zh_CN.json"
    zh_localization=None

    for d in ext_base.glob("*/localizations/zh_CN.json"):
        if any(f.name==zh_file for f in d.iterdir()):
            zh_localization=d
            break

    if zh_localization:
        zh_json=zh_localization / zh_file
        with zh_json.open(encoding="utf-8") as f:
            zh_dict:dict[str,str]=json.load(f)
        here_json=here_locs / "localization-zh.json"
        with here_json.open(encoding="utf-8") as f:
            here_dict:dict=json.load(f)
        zh_dict.update(here_dict)
        rename_item={
            "图像":"图片",
            "提示词":"咒文",
            "通配符":"通配咒文",
            "重绘幅度":"去噪强度",
            "(":"（",
            ")":"）"
        }
        rename_dict={ 
            k:renamed 
            for k,v in zh_dict.items() 
            if (renamed:=v) and any( 
                (renamed:=renamed.replace(i,rename_item[i])) 
                for i in rename_item 
                if i in renamed 
            )
        }
        zh_dict.update(rename_dict)
        mix_json=here_locs / zh_file
        mix_json=mix_json.with_stem(f"{mix_json.stem}_mixed")
        with mix_json.open("w",encoding="utf-8") as f:
            json.dump(zh_dict,f,ensure_ascii=False,indent=4)

