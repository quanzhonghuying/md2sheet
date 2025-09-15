"""
main.py
Markdown → Excel/CSV 変換ツール
"""

from md2sheet.input_handler import InputHandler
from md2sheet.converter import Converter
from md2sheet.extractor import TableExtractor
from md2sheet.sheet_manager import SheetManager
from md2sheet.excel_writer import ExcelWriter
from md2sheet.csv_writer import CSVWriter

def main():
    params = InputHandler.parse_args()
    md_file = params["input"]
    output_file = params["output"]
    mode = params["mode"]

    html_file = "temp.html"
    Converter.md_to_html(md_file, html_file)

    tables = TableExtractor.extract_tables(html_file)
    sheets = SheetManager.assign_sheets(md_file, tables)

    if mode == "excel":
        ExcelWriter.write(output_file, sheets)
        print(f"✅ Excel 出力完了: {output_file}")
    elif mode == "csv":
        CSVWriter.write(output_file, sheets)
        print(f"✅ CSV 出力完了: {output_file}")
    else:
        print(f"❌ 未知モード: {mode}")

if __name__ == "__main__":
    main()

