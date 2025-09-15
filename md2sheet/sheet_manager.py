"""
sheet_manager.py
DataFrame をシートに振り分けるモジュール
対応モード:
1. デフォルトモード - 全てを1シートにまとめる
2. コメントモード   - <!-- sheet:名前 --> コメントで分割
3. 見出しモード     - Markdown 見出し (# タイトル) で分割
"""

import pandas as pd
import re

class SheetManager:
    @staticmethod
    def assign_sheets(md_file: str, tables: list[pd.DataFrame]) -> dict[str, list[pd.DataFrame]]:
        if not tables:
            return {"Sheet1": []}

        with open(md_file, "r", encoding="utf-8") as f:
            md_text = f.read()

        # コメントモード
        comment_sheets = re.findall(r"<!--\s*sheet:(.+?)\s*-->", md_text)
        if comment_sheets and len(comment_sheets) == len(tables):
            return {name.strip(): [df] for name, df in zip(comment_sheets, tables)}

        # 見出しモード
        headings = re.findall(r"^#\s+(.+)$", md_text, flags=re.MULTILINE)
        if headings and len(headings) == len(tables):
            return {name[:31]: [df] for name, df in zip(headings, tables)}

        # デフォルトモード
        return {"Sheet1": tables}

