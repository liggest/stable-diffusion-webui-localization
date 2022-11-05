"""
    提供一个 tag-翻译 对照文件
    对于 danbooru-zh.csv 中存在但和提供文件翻译不同的 tag
    逐个选择更好的翻译，以此合并两个文件，重新写入 danbooru-zh.csv
    （在提供文件中存在但不在 danbooru-zh.csv 中存在的 tag 请用 collect_tags.py 添加）
"""

from pathlib import Path
from tag_util import dan_zh, get_sep, key_val_filtered, not_same, choose_val, write_csv

merge_file=Path(input("tag-翻译 对照文件路径：\n"))
print(repr(merge_file))
sep=get_sep(merge_file)

tags=dict(key_val_filtered(dan_zh))

count=0

try:
    for key,val in key_val_filtered(merge_file,sep): # tag、翻译 已经过滤过
        if not (current:=tags.get(key)): # 跳过 dan_zh 中不存在的项
            continue
        if not_same(current,val):
            print(f"发现 {key} 的不同翻译")
            new_val=choose_val(current,val)
            if new_val is not current:
                tags[key]=new_val
                print(f"{key} 的翻译现在是 {new_val}")
                count+=1
finally: # 保证中途 Ctrl+C 也能写入当时的 tags
    write_csv(tags.items(),dan_zh)

    print(f"重新写入了 {len(tags)} 个 tag，更新了其中的 {count} 个")
