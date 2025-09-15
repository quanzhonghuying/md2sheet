import pandas as pd


class ExcelWriter:
    @staticmethod
    def write(excel_file: str, sheets: dict[str, list[pd.DataFrame]]) -> None:
        """
        DataFrame を Excel ファイルに出力する
        """
        with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
            if not sheets:
                # ✅ 兜底処理: テーブルが存在しない場合
                empty_df = pd.DataFrame({"メッセージ": ["表は存在しません"]})
                empty_df.to_excel(writer, sheet_name="Empty", index=False)
            else:
                for name, df_list in sheets.items():
                    for idx, df in enumerate(df_list):
                        # 同じシート名が複数ある場合は番号を付加
                        sheet_name = name if idx == 0 else f"{name}_{idx+1}"
                        df.to_excel(writer, sheet_name=sheet_name, index=False)
