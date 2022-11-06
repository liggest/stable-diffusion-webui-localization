"""
    WebUI extension launch script
"""

import json
from pathlib import Path
import shutil

here=Path(__file__).parent
ext_base=here.parent
here_tags=here / "tags"
tags_config=here_tags / "config.json"

with tags_config.open(encoding="utf-8") as f:
    config=json.load(f)
tag_file=config["tagFile"]

autocomplete_tags=None

tags=ext_base.glob("*/tags/") # find autocomplete base
for d in tags:
    if any(f.name==tag_file for f in d.iterdir()):
        autocomplete_tags=d
        break

if autocomplete_tags: # 安装了 tag-autocomplete
    shutil.copytree(here_tags,autocomplete_tags,dirs_exist_ok=True)

# localizations=here / "localizations"
# if localizations.exists():
#     shutil.copytree(localizations,here / "localization",dirs_exist_ok=True) # as a localization extension
