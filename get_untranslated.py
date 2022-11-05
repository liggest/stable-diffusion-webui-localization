"""
    对比 danbooru.csv 和 danbooru-zh.csv
    找出目前尚未翻译的 tag
    生成 danbooru-untranslated.csv
"""

from tag_util import dan, dan_zh, dan_untrans, key_file, write_csv

tags=set(key_file(dan_zh)) # 读取已翻译的 tag

total=0
count=0

def diff_gen():
    global total,count
    for i,*key in enumerate(key_file(dan)):
        if key[0] not in tags:
            yield key # 未翻译的 tag 写入 dan_untrans
            count+=1
    total=i+1 # 只是计数

write_csv(diff_gen(),dan_untrans)

print(f"{total} 条中，{len(tags)} 条已有翻译，{count} 条尚无翻译")
