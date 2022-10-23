"""
    对比 danbooru.csv 和 danbooru-zh.csv
    找出目前尚未翻译的 tag
    生成 danbooru-untranslated.csv
"""

from tag_util import dan, dan_zh, dan_untrans, key_file, key_val_file

tags=set(key_file(dan_zh)) # 读取已翻译的 tag

total=0
count=0
with dan_untrans.open("w",encoding="utf-8") as uf:
    for i,(key,ttype) in enumerate(key_val_file(dan)):
        if key not in tags:
            uf.write(f"{key},{ttype}\n") # 未翻译的 tag 写入 dan_untrans
            count+=1
    total=i+1 # 只是计数

print(f"{total}条中，{len(tags)}条已有翻译，{count}条尚无翻译")
