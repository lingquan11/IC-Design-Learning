#!/usr/bin/env python3
"""检查仓库内 Markdown 相对链接是否指向存在的文件。

用法：在仓库根目录运行 `python3 scripts/check_links.py`。
外部链接（http/https/mailto）与纯锚点链接跳过；带锚点的链接只校验文件部分。
发现断链时逐条打印并以退出码 1 结束，全部可达时以退出码 0 结束。
仅使用 Python 标准库。
"""

import os
import re
import sys
import urllib.parse

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#")


def main() -> int:
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    total = 0
    missing = []
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d != ".git"]
        for name in sorted(files):
            if not name.endswith(".md"):
                continue
            path = os.path.join(dirpath, name)
            with open(path, encoding="utf-8") as f:
                text = f.read()
            for match in LINK_RE.finditer(text):
                url = match.group(1).strip().split()[0].strip("<>")
                if url.startswith(SKIP_PREFIXES):
                    continue
                target_part = urllib.parse.unquote(url.split("#")[0])
                if not target_part:
                    continue
                total += 1
                target = os.path.normpath(os.path.join(dirpath, target_part))
                if not os.path.exists(target):
                    missing.append((os.path.relpath(path, root), url))
    print(f"checked={total} missing={len(missing)}")
    for source, url in missing:
        print(f"MISSING {source} -> {url}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
