# 基本設計書 v1.0 - Markdown → Excel / Google Sheet 変換ツール

## 1. システム概要
本システムは、Markdown ファイル（.md）に含まれる表を解析し、  
Excel（.xlsx）、CSV、または Google Sheet 形式に変換するツールである。  

- 入力: Markdown ファイルパス  
- 出力: Excel / CSV / Google Sheet  
- 主な処理フロー:  
  1. Markdown → HTML 変換（Pandoc）  
  2. HTML テーブル解析（Pandas）  
  3. シート分割ルール適用  
  4. Excel / CSV / Google Sheet への出力  

---

## 2. システム構成図

```plaintext
md2sheet
├── InputHandler       # 入力パス処理
├── Converter          # Markdown → HTML 変換 (Pandoc)
├── TableExtractor     # HTML テーブル解析 (pandas)
├── SheetManager       # シート分割ルール適用
├── ExcelWriter        # Excel 出力 (openpyxl)
├── CSVWriter          # CSV 出力
└── GoogleSheetWriter  # Google Sheets API 出力（将来対応）
```
## 3. モジュール設計

### 3.1 InputHandler
- **役割**: ユーザー入力を処理し、Markdown ファイルパス・出力ファイルパス・出力モードを取得する  
- **機能**:
  - 入力値のバリデーション（ファイル存在確認、拡張子チェックなど）  
  - デフォルト値の設定（出力パスが未指定の場合は `output.xlsx`）  
- **インターフェース**:
  ```python
  class InputHandler:
      def get_input() -> dict:
          """
          戻り値例:
          {
              "md_file": "docs/table.md",
              "mode": "excel",
              "output": "output.xlsx"
          }
          """
### 3.2 Converter
- **役割**: Pandoc を利用して Markdown → HTML に変換する  
- **機能**:  
  - Pandoc コマンドを実行して HTML ファイルを生成  
  - コマンド失敗時はエラーメッセージを返却  

---

### 3.3 TableExtractor
- **役割**: HTML 内の `<table>` を DataFrame として抽出する  
- **機能**:  
  - `pandas.read_html()` を使用してテーブルを抽出  
  - テーブルが存在しない場合は空リストを返却  

---

### 3.4 SheetManager
- **役割**: シート分割ルールを適用する  
- **モード**:  
  - デフォルトモード: 全テーブルを 1 シートにまとめる  
  - コメントモード: `<!-- sheet:名前 -->` や `[//]: # (sheet:名前)` を検出して分割  
  - 見出しモード: `# 見出し` をシート名として分割  
- **補足**: シート名は 31 文字制限に合わせて調整  

---

### 3.5 ExcelWriter
- **役割**: Excel ファイルを生成する  
- **機能**:  
  - `openpyxl` を利用  
  - 複数シートに DataFrame を書き込み  

---

### 3.6 CSVWriter
- **役割**: シートごとに個別の CSV ファイルを出力する  

---

### 3.7 GoogleSheetWriter（将来対応）
- **役割**: Google Sheets API を利用してアップロードする  
- **機能**:  
  - アップロード後、共有リンクを返却  

---

## 4. データ設計

### 4.1 入力データ
- Markdown ファイル（UTF-8）  
- 内部フォーマット: HTML に変換した後、pandas DataFrame として扱う  

### 4.2 出力データ
- Excel ファイル（`.xlsx`, openpyxl）  
- CSV ファイル（UTF-8, カンマ区切り）  
- Google Sheet（クラウドリソース, ID 管理）  

---

## 5. エラーハンドリング
- ファイルが存在しない場合 → エラーメッセージを表示し処理終了  
- Markdown にテーブルが存在しない場合 → 空の Excel を生成  
- Pandoc 実行エラー → ユーザーにインストール確認を促す  
- 出力パスが無効 → デフォルト名（`output.xlsx`）を利用  

---

## 6. 今後の拡張
- Google Sheets API による自動アップロード機能  
- 設定ファイル（`config.yaml`）によるルールカスタマイズ  
- CI/CD（GitHub Actions など）との連携による自動生成  
