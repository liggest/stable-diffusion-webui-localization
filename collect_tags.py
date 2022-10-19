"""
    提供若干 tag-翻译 对照文件、分隔符，读取 tag 和翻译
    参考生成的 danbooru-untranslated.csv ，将读到的翻译填充至 danbooru-zh.csv
"""

from pathlib import Path

# dan=Path("./tags/danbooru.csv")
dan=Path("./tags/danbooru-untranslated.csv")
new_dan=Path("./tags/danbooru-zh.csv")

tags={}

while path:=input("tag-翻译 对照文件路径：\n"):
    path=Path(path)
    print(repr(path))
    splitter=input("分隔符（默认空白）：") or None
    count=0
    with path.open(encoding="utf-8") as f:
        for line in f:
            line=line.strip()
            if not line: # 忽略空行
                continue
            key,*val=line.split(sep=splitter)
            if not val: # 忽略没有分隔符的行
                continue
            key=key.strip().lower().replace(" ","_") # A key => a_key

            # # 如果要读取 danbooru-untranslated.csv 里面有翻译的项
            # # 可以交换注释和未注释部分
            # if len(val)<2: 
            #     continue
            # val=val[-1].strip('"') # 有多个分隔符的行，取最后一项
            val=(splitter or " ").join(val).strip('"')

            if key in tags and tags[key]!=val:
                print(f"重复的 tag {key}  翻译 {tags[key]} => {val}")
                # 多次读到相同的 tag，后读到的翻译会覆盖先读到的
            tags[key]=val
            count+=1
    print(f"读取了 {count} 个 tag")

print("读取",dan)

with dan.open(encoding="utf-8") as f:
    with new_dan.open("a",encoding="utf-8") as nf:
        count=0
        for line in f:
            # 同上
            # key,*vals=line.split(",") # 读 dan 里面的 tag
            key,_=line.split(",",maxsplit=1) # 读 dan 里面的 tag

            if key in tags:
                # 若 tag 有翻译，也在 dan 中
                # 同上
                # nf.write(f'{key},{val[0]},"{tags[key]}"\n') # tag,类型序号,"翻译"
                nf.write(f'{line.strip()},"{tags[key]}"\n') # tag,类型序号,"翻译"
                count+=1

print(f"写入 {count} 个 tag 至 {new_dan}")

