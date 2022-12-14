# stable-diffusion-webui-localization

尝试为 [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) 提供本地化支持

与[官方翻译](https://github.com/dtlnor/stable-diffusion-webui-localization-zh_CN)稍有区别

### 用法

> 伪装成一个 WebUI 扩展（

将本仓库克隆至 WebUI 的 `extensions` 目录

（名称任意，以 `localization-zh` 为例）

```
git clone "https://github.com/liggest/stable-diffusion-webui-localization.git" extensions/localization-zh
```

### 额外内容

在 [a1111-sd-webui-tagcomplete](https://github.com/DominikDoom/a1111-sd-webui-tagcomplete) 的加持下，WebUI 可以有 prompt 补全功能

它提供了一个 tag 众多的 `danbooru.csv` 文件，也可以为这个文件增加翻译

这里试着用网络上搜集来的 tag 翻译填补了极少一部分，还有大量 tag 是处于未翻译状态

要启用翻译，以扩展的形式安装好 tagcomplete 即可

可能有用的脚本：

- `get_untranslated.py` 
  
  找出目前尚未翻译的 tag，生成 `danbooru-untranslated.csv`
- `collect_tags.py` 
  
  通过提供 tag-翻译 对照文件，填充 `danbooru-zh.csv`
  
  （tag-翻译 对照文件即每行为 `tag分隔符翻译` 的文本文件）
- `merge_tags.py`
  
  合并提供的 tag-翻译 对照文件与 `danbooru-zh.csv` 中翻译不同的 tag，手动决定哪个翻译更好

- `merge_collect_tags.py`
  
  类似于同时做 `merge_tags.py` 和 `collect_tags.py`

> 汉化不完全，也不保证更新 \_(:з」∠)\_
> 
> 搜集 tag 的地方
> - [TagTable](https://github.com/zcyzcy88/TagTable)
> - [魔咒百科词典](https://aitag.top/)
> - [阿巧的 tag 翻译贴](https://ngabbs.com/read.php?tid=33869519)
