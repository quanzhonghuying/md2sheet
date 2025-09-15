"""
converter.py
Markdown ファイルを Pandoc で HTML に変換するモジュール
"""

import subprocess


class Converter:
    @staticmethod
    def md_to_html(md_file: str, html_file: str) -> None:
        try:
            subprocess.run(["pandoc", md_file, "-o", html_file], check=True)

            # 2. 強制的に UTF-8 で再保存（ここでエンコーディング統一）
            with open(html_file, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
            with open(html_file, "w", encoding="utf-8") as f:
                f.write(content)

        except FileNotFoundError:
            raise RuntimeError("Pandoc が見つかりません。インストールしてください。")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Pandoc 実行エラー: {e}")
