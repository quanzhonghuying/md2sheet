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
```
+ **処理手順**

1. ユーザーに入力をプロンプト表示

1. 値を取得

1. ファイル存在チェック・拡張子確認

1. 結果を dict で返却

+ **エラーケース**

  + ファイルが存在しない場合 → エラー出力

  + モードが不正の場合 → デフォルト値適用

### 2.2 Converter

+ **役割**
Pandoc を利用して Markdown を HTML に変換する。

+ **関数設計**
```python
class Converter:
    @staticmethod
    def md_to_html(md_file: str, html_file: str) -> None:
        """
        Markdown を HTML に変換する
        """
```

+ **処理手順**

  1. subprocess で pandoc を実行

  1. 正常終了時 → HTML ファイル生成

  1. 失敗時 → RuntimeError を投げる

+ **エラーケース**

  + Pandoc 未インストール

  + 入力ファイルなし

  + 出力パスが不正

### 2.3 TableExtractor

+ 役割
HTML ファイルから <table> を抽出し、DataFrame 化する。

+ 関数設計

```python
class TableExtractor:
    @staticmethod
    def extract_tables(html_file: str) -> list[pd.DataFrame]:
        """
        HTML 内のテーブルを抽出し DataFrame リストとして返却
        """
```

+ **処理手順**

  1. pandas.read_html() で HTML を解析

  1. DataFrame のリストを返却

  1. テーブルが存在しない場合は空リスト

+ **エラーケース**

  + HTML が不正 → 例外発生

  + テーブルがない → 空リスト返却


### 2.4 SheetManager

+ 役割
シート分割ルールを適用し、DataFrame をシートごとに振り分ける。

+ **関数設計**
```python
class SheetManager:
    @staticmethod
    def assign_sheets(md_file: str, tables: list[pd.DataFrame]) -> dict[str, list[pd.DataFrame]]:
        """
        シート名をキー、DataFrame リストを値とする辞書を返却
        """
```

+ **処理手順**

  1. Markdown ファイルを読み取りルールを解析

  1. コメントモード / 見出しモード / デフォルトモードを判定

  1. DataFrame をシートに振り分ける

+ **エラーケース**

  + 見出し名が長すぎる場合 → 31 文字以内に切り詰め

  + 重複シート名 → 番号を付加して回避

### 2.5 ExcelWriter

+ **役割**
DataFrame を Excel ファイルに出力する。

+ **関数設計**
```python
class ExcelWriter:
    @staticmethod
    def write(excel_file: str, sheets: dict[str, list[pd.DataFrame]]) -> None:
        """
        Excel ファイルを生成
        """
```

+ **処理手順**

  1. openpyxl で新規 Excel を作成

  1. 各シートに DataFrame を書き込み

  1. 保存

+ **エラーケース**

  + 出力パスが不正

  + 書き込み中に I/O エラー

### 2.6 CSVWriter

+ **役割**
シートごとに個別 CSV ファイルを出力する。

+ **関数設計**
```python
class CSVWriter:
    @staticmethod
    def write(output_dir: str, sheets: dict[str, list[pd.DataFrame]]) -> None:
        """
        各シートを CSV ファイルとして保存
        """
```

+ **処理手順**

  1. 出力ディレクトリ作成

  1. 各シートごとに CSV を保存

### 2.7 GoogleSheetWriter（将来対応）

+ **役割**
Google Sheets API を利用してアップロードする。

+ **関数設計**
```python
class GoogleSheetWriter:
    @staticmethod
    def upload(sheets: dict[str, list[pd.DataFrame]]) -> str:
        """
        Google Sheet にアップロードし URL を返却
        """
```
## 3. 共通エラーハンドリング

+ ファイルが存在しない場合 → エラーメッセージ表示後終了

+ Pandoc 実行エラー → インストール確認を促す

+ テーブルが存在しない場合 → 空の Excel を出力

+ 出力パスが無効 → デフォルト値 (output.xlsx) を利用
