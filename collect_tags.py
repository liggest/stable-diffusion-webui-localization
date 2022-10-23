"""
    提供若干 tag-翻译 对照文件
    参考生成的 danbooru-untranslated.csv ，将读到的翻译填充至 danbooru-zh.csv
"""

from pathlib import Path
from tag_util import dan_untrans, dan_zh, SEP, key_val_file, key_val_filtered, choose_val

tags={}

while path:=input("tag-翻译 对照文件路径：\n"):
    path=Path(path)
    print(repr(path))
    sep=input(f"分隔符（默认为 {repr(SEP)}）：") or SEP
    for i,(key,val) in enumerate(key_val_filtered(path,sep)):
        if current:=tags.get(key) and current!=val:
            print(f"发现 {key} 的不同翻译")
            val=choose_val(current,val)
            if val is not current:
                print(f"{key} 的翻译现在是 {val}")
        tags[key]=val
    print(f"读取了 {i+1} 个 tag")


print("读取",dan_untrans)

count=0
with dan_zh.open("a",encoding="utf-8") as zhf:
    for key,ttype in key_val_file(dan_untrans):
        if val:=tags.get(key):  # 若 tag 有翻译，也在 dan_untrans 中
            zhf.write(f'{key},{ttype},"{val}"\n') # tag,类型序号,"翻译"
            count+=1

print(f"写入 {count} 个 tag 至 {dan_zh}")
