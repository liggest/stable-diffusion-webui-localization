# stable-diffusion-webui-localization

尝试为 [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) 提供本地化文件

### 用法

将仓库中的 `localizations` 目录复制到 WebUI 项目下

### 额外内容

在 [a1111-sd-webui-tagcomplete](https://github.com/DominikDoom/a1111-sd-webui-tagcomplete) 的加持下，WebUI 可以有 prompt 补全功能

它提供了一个 tag 众多的 `danbooru.csv` 文件，也可以为这个文件增加翻译

这里试着用网络上搜集来的 tag 翻译填补了极少一部分，还有大量 tag 是处于未翻译状态

安装好上述扩展，将仓库中的 `tags` 目录复制到 WebUI 项目下即可

可能有用的脚本：

- `get_untranslated.py` 
  找出目前尚未翻译的 tag，生成 `danbooru-untranslated.csv`
- `collect_tags.py` 
  通过提供 tag-翻译 对照文件，填充 `danbooru-zh.csv`
（tag-翻译 对照文件即每行为 `tag分隔符翻译` 的文本文件）
- `merge_tags.py`
  合并提供的 tag-翻译 对照文件与 `danbooru-zh.csv` 中翻译不同的 tag，手动决定哪个翻译更好


> 汉化不完全，也不保证更新 \_(:з」∠)\_
> 
> 搜集 tag 的地方
> - [TagTable](https://github.com/zcyzcy88/TagTable)
> - [魔咒百科词典](https://aitag.top/)
> - [阿巧的 tag 翻译贴](https://ngabbs.com/read.php?tid=33869519)
