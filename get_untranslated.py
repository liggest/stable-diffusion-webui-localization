from pathlib import Path

dan=Path("./tags/danbooru.csv")
new_dan=Path("./tags/danbooru-zh.csv")
untrans_dan=Path("./tags/danbooru-untranslated.csv")

tags=set()

with new_dan.open(encoding="utf-8") as f:
    tags=set( line.split(",",maxsplit=1)[0] for line in f )

total=0
with dan.open(encoding="utf-8") as f:
    with untrans_dan.open("w",encoding="utf-8") as uf:
        count=0
        for i,line in enumerate(f):
            key,_=line.split(",",maxsplit=1)
            if key not in tags:
                uf.write(line)
                count+=1
        total=i+1

print(f"{total}条中，{len(tags)}条已有翻译，{count}条尚无翻译")
