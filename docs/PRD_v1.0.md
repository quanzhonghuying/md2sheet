# PRD_v1.0 - Markdown → Excel / Google Sheet 変換ツール

## 1. 背景
- 開発チームでは、軽量でバージョン管理が容易な **Markdown** を用いて技術文書を作成するケースが増えている。  
- 一方で、顧客や業務部門は **Excel** や **Google Sheet** を標準フォーマットとして利用しており、直接 Markdown を参照できないことが多い。  
- このギャップを解消するために、Markdown 文書を **自動的に Excel / Google Sheet に変換するツール** を開発する。  

---

## 2. 目的
- **入力**: Markdown ファイル（`.md`）  
- **出力**:  
  - Excel (`.xlsx`)  
  - CSV（シートごとに分割ファイル）  
  - Google Sheet（将来的に API 経由でアップロード）  

本ツールにより、エンジニアは Markdown を維持しつつ、顧客や業務部門に適したフォーマットで資料を提供できる。  

---

## 3. 機能要件

### 3.1 入出力
- **入力**: コマンド実行時にユーザーが以下を指定  
  1. ソース Markdown ファイルパス  
  2. 出力ファイルパス（例: `output.xlsx`）  
- **出力**: Excel / CSV / Google Sheet  

### 3.2 テーブル解析
- Pandoc を利用して Markdown を HTML に変換  
- Pandas により `<table>` を抽出  
- Excel / CSV に変換して保存  

### 3.3 シート分割ルール
1. **デフォルトモード**  
   - 全テーブルを 1 枚のシート（`Sheet1`）にまとめる  

2. **コメントモード（推奨 ✅）**  
   - Markdown 内に以下のコメントを挿入し、シートを分割  
     - `<!-- sheet:シート名 -->`  
     - `[//]: # (sheet:シート名)`  
   - Markdown プレビューでは非表示のため、文書の見栄えを損なわない  

3. **見出しモード**  
   - `# 見出し` をシート分割トリガーとして使用  
   - 見出しテキストをシート名に利用  

4. **命名ルール**  
   - 指定がある場合 → その名称を利用（Excel 制限により 31 文字以内）  
   - 指定がない場合 → `Sheet1, Sheet2...` を自動付与  

### 3.4 出力モード
- Excel モード：`.xlsx` 出力（デフォルト）  
- CSV モード：シートごとにファイル分割  
- Google Sheet モード：API 経由でクラウドにアップロード（将来拡張）  

### 3.5 エラーハンドリング
- Markdown にテーブルが存在しない場合 → 空 Excel を生成し警告表示  
- テーブル数が見出しやコメントより多い場合 → 残りのテーブルは `SheetX` として出力  
- 1 つのシートに複数テーブルを連続配置可能  

---

## 4. 技術選定
- **言語**: Python 3  
- **ライブラリ**: pandas, openpyxl, lxml  
- **外部ツール**: pandoc（Markdown → HTML 変換用）  

---

## 5. プロジェクト構成
```plaintext
md2sheet/
├── md2sheet.py          # メインスクリプト
├── requirements.txt     # 依存ライブラリ
├── README.md            # プロジェクト概要
└── docs/
    └── PRD_v1.0.md      # 本仕様書
```
---
## 6. 利用方法

```bash
python md2sheet.py
```
**実行後のプロンプト例:**
```plaintext
Markdown ファイルのパスを入力してください: docs/table.md
出力モードを選択してください:
1. Excel
2. CSV
3. Google Sheet
出力ファイルパスを入力してください: output.xlsx
```

**出力メッセージ:**
```plaintext
✅ Excel ファイルを生成しました: output.xlsx
```
## 7. 拡張計画
### 7.1 Google Sheets API 対応
+ Excel 出力後、自動的に Google Drive にアップロードし、Google Sheet として公開できるようにする。

+ 実行完了時に共有用 URL を出力する。

### 7.2 カスタムルール定義
+ 設定ファイル（例: config.yaml）でシート分割ルールを自由に定義可能にする。

### 7.1 Google Sheets API 対応

+ Excel 出力後、自動的に Google Drive にアップロードし、Google Sheet として公開できるようにする。

+ 実行完了時に共有用 URL を出力する。

### 7.2 カスタムルール定義

+ 設定ファイル（例: config.yaml）でシート分割ルールを自由に定義可能にする。

+ \## 二級見出し でも分割できるように拡張する。

### 7.3 CI/CD パイプライン連携

+ GitHub Actions や GitLab CI で自動的に Markdown → Excel/Google Sheet を生成する仕組みを整備する。

+ ドキュメント変更時に最新の Excel/Google Sheet が自動的に作成・配布されるようにする。 