"""
    提供若干 tag-翻译 对照文件
    合并 danbooru-zh.csv 和这些文件，按 danbooru.csv 的顺序重新写入 danbooru-zh.csv
    遇到相同 tag 不同翻译的情况，逐个选择更好的翻译
    （类似于同时做 merge_tags.py 和 collect_tags.py）
"""

from pathlib import Path
from tag_util import dan, dan_zh, get_sep, key_file, key_val_filtered, not_same, choose_val, write_csv

print("读取",dan_zh)
zh_tags=dict(key_val_filtered(dan_zh))
print(f"读取了已翻译的 {len(zh_tags)} 个 tag")

tags=zh_tags.copy() # 保留 zh_tags

count=0
new_count=0
update_count=0
def tag_gen(): # 保证dan_zh 的 tag 顺序和 dan 相同
    global count,new_count
    for key in key_file(dan):
        if val:=tags.get(key): # 若 key 有翻译
            yield key,val
            if key not in zh_tags:
                new_count+=1
            count+=1

try:
    while path:=input("tag-翻译 对照文件路径（留空进入下一步）：\n"):
        path=Path(path)
        print(repr(path))
        sep=get_sep(path)
        for i,(key,val) in enumerate(key_val_filtered(path,sep)): # tag、翻译 已经过滤过
            if (current:=tags.get(key)) and not_same(current,val):
                print(f"发现 {key} 的不同翻译")
                val=choose_val(current,val)
                if val is not current:
                    print(f"{key} 的翻译现在是 {val}")
                    if key in zh_tags:
                        update_count+=1
            tags[key]=val
        print(f"读取了 {i+1} 个 tag")
finally: # 保证中途 Ctrl+C 也能写入当时的 tags
    write_csv(tag_gen(),dan_zh)
    # with dan_zh.open("w",encoding="utf-8") as f:
    #     for key,(ttype,val) in tags.items():
    #         f.write(f'{key},{ttype},"{val}"\n')
    print(f"重新写入了 {count} 个 tag，相比原来更新了的 {update_count} 个，新增了 {new_count} 个")
