"""
    提供一个 tag-翻译 对照文件
    对于 danbooru-zh.csv 中存在但和提供文件翻译不同的 tag
    逐个选择更好的翻译，以此合并两个文件，重新写入 danbooru-zh.csv
    （在提供文件中存在但不在 danbooru-zh.csv 中存在的 tag 请用 collect_tags.py 添加）
"""

from pathlib import Path

from tag_util import dan_zh, SEP, split_gen, to_key, to_val, key_val_filtered, choose_val

merge_file=Path(input("tag-翻译 对照文件路径：\n"))
print(repr(merge_file))
sep=input(f"分隔符（默认为 {repr(SEP)}）：") or SEP

tags={}
with dan_zh.open(encoding="utf-8") as f:
    for key,ttype,val in split_gen(f):
        key=to_key(key)
        tags[key]=(ttype,to_val(val))

count=0

try:
    for key,val in key_val_filtered(merge_file,sep): # tag、翻译 已经过滤过
        if not (current:=tags.get(key)):
            continue
        ttype,old_val=current
        if old_val!=val:
            print(f"发现 {key} 的不同翻译")
            new_val=choose_val(old_val,val)
            if new_val is not old_val:
                tags[key]=(ttype,new_val)
                print(f"{key} 的翻译现在是 {new_val}")
                count+=1
finally: # 保证中途 Ctrl+C 也能写入当时的 tags
    with dan_zh.open("w",encoding="utf-8") as f:
        for key,(ttype,val) in tags.items():
            f.write(f'{key},{ttype},"{val}"\n')

    print(f"重新写入了 {len(tags)} 个 tag，更新了其中的 {count} 个")
