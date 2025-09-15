# 詳細設計書 v1.0 - md2sheet

## 1. ドキュメント情報
- 作成日: 2025-09-15
- 対象システム: md2sheet
- バージョン: v1.0
- 作成者: （記入）

---

## 2. モジュール別詳細設計

### 2.1 InputHandler
- **役割**  
  ユーザー入力を処理し、Markdown ファイルパス・出力パス・出力モードを取得する。  

- **関数設計**
```python
class InputHandler:
    @staticmethod
    def get_input() -> dict:
        """
        入力値を取得する
        戻り値例:
        {
            "md_file": "docs/table.md",
            "mode": "excel",
            "output": "output.xlsx"
        }
        """

