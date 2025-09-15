"""
extractor.py
HTML 内の <table> を抽出し、DataFrame に変換するモジュール
"""

import pandas as pd


class TableExtractor:
    @staticmethod
    def extract_tables(html_file: str) -> list[pd.DataFrame]:
        try:
            return pd.read_html(html_file, encoding="utf-8", flavor="lxml")
        except ValueError:
            return []
        except Exception as e:
            raise RuntimeError(f"HTML 解析エラー: {e}")
