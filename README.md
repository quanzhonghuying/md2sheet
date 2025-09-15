# md2sheet

Markdown ファイルの `<table>` を Excel/CSV/Google Sheet に変換するツール。

---

## 特徴 (Features)

- Markdown のテーブルを Pandoc + pandas で解析
- Excel (xlsx) 出力（openpyxl 使用）
- CSV 出力
- Google Sheets アップロード（将来対応）
- シート分割ルール
  - デフォルト: 全テーブルを1シートにまとめる
  - コメントモード: `<!-- sheet:名前 -->`
  - 見出しモード: `# 見出し`

---

## インストール方法 (Installation)
### リポジトリを clone
```bash
git clone https://github.com/quanzhonghuying/md2sheet.git
cd md2sheet
```
### 仮想環境を作成
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 依存関係をインストール
```bash
pip install -r requirements.txt
```
## 使い方 (Usage)

### Excel 出力
```bash
python3 -m md2sheet.main tests/test_default.md --mode excel --output out.xlsx
```
### CSV 出力
```bash
python3 -m md2sheet.main tests/test_default.md --mode csv --output outputs/
```
### コメントモードテスト
```bash
python3 -m md2sheet.main tests/test_comment.md --mode excel --output out_comment.xlsx
```
### 見出しモードテスト
```bash
python3 -m md2sheet.main tests/test_heading.md --mode excel --output out_heading.xlsx
```
### 空ファイルテスト（テーブルなし）
```bash
python3 -m md2sheet.main tests/test_empty.md --mode excel --output out_empty.xlsx
```
## テストファイル (Test files)

- `tests/test_default.md` → 普通の Markdown テーブル  
- `tests/test_comment.md` → コメントでシート名指定  
- `tests/test_heading.md` → 見出しでシート分割  
- `tests/test_empty.md` → テーブルなし（空の Excel 生成）  

---

## 注意事項 (Notes)

- Pandoc が必要です。未インストールの場合は [Pandoc公式](https://pandoc.org/installing.html) からインストールしてください。  
- Excel 出力は `openpyxl` に依存します。  
- Google Sheets 出力は将来的に対応予定です。  
