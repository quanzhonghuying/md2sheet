"""
input_handler.py
コマンドライン引数を処理するモジュール
"""

import argparse
import os

class InputHandler:
    @staticmethod
    def parse_args():
        parser = argparse.ArgumentParser(description="Markdown → Excel/CSV 変換ツール")
        parser.add_argument("input", help="入力 Markdown ファイル")
        parser.add_argument("--output", default="output.xlsx", help="出力ファイル (デフォルト: output.xlsx)")
        parser.add_argument("--mode", choices=["excel", "csv"], default="excel", help="出力モード (excel / csv)")
        args = parser.parse_args()

        if not os.path.exists(args.input):
            raise FileNotFoundError(f"入力ファイルが存在しません: {args.input}")

        return {
            "input": args.input,
            "output": args.output,
            "mode": args.mode
        }

