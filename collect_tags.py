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
            if not line:
                continue
            key,*val=line.split(sep=splitter,maxsplit=1)
            if not val:
                continue
            key=key.lower().replace(" ","_")
            val=(splitter or " ").join(val)
            if key in tags and tags[key]!=val:
                print(f"重复的 tag {key}  翻译 {tags[key]} => {val}")
            tags[key]=val
            count+=1
    print(f"读取了 {count} 个 tag")

print("读取",dan)

with dan.open(encoding="utf-8") as f:
    with new_dan.open("a",encoding="utf-8") as nf:
        count=0
        for line in f:
            key,_=line.split(",",maxsplit=1)
            if key in tags:
                nf.write(f'{line.strip()},"{tags[key]}"\n')
                count+=1

print(f"写入 {count} 个 tag 至 {new_dan}")

