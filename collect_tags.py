"""
    提供若干 tag-翻译 对照文件
    参考生成的 danbooru-untranslated.csv ，将读到的翻译填充至 danbooru-zh.csv
"""

from pathlib import Path
from tag_util import dan_untrans, dan_zh, get_sep, key_file, key_val_filtered, not_same, choose_val, write_csv

tags={}

while path:=input("tag-翻译 对照文件路径（留空进入下一步）：\n"):
    path=Path(path)
    print(repr(path))
    sep=get_sep(path)
    for i,(key,val) in enumerate(key_val_filtered(path,sep)):
        if (current:=tags.get(key)) and not_same(current,val):
            print(f"发现 {key} 的不同翻译")
            val=choose_val(current,val)
            if val is not current:
                print(f"{key} 的翻译现在是 {val}")
        tags[key]=val
    print(f"读取了 {i+1} 个 tag")


print("读取",dan_untrans)

count=0

def diff_gen():
    global count
    for key in key_file(dan_untrans):
        if val:=tags.get(key): # 若 tag 有翻译，也在 dan_untrans 中
            yield key,val
            count+=1

write_csv(diff_gen(),dan_zh,"a")

print(f"写入 {count} 个 tag 至 {dan_zh}")
