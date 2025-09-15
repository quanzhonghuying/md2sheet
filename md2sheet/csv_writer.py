import os
import pandas as pd


class CSVWriter:
    @staticmethod
    def write(output_dir: str, sheets: dict[str, list[pd.DataFrame]]) -> None:
        """
        シートごとに CSV ファイルを出力する
        """
        os.makedirs(output_dir, exist_ok=True)

        if not sheets:
            # ✅ 兜底処理: テーブルが存在しない場合
            empty_df = pd.DataFrame({"メッセージ": ["表は存在しません"]})
            empty_file = os.path.join(output_dir, "Empty.csv")
            empty_df.to_csv(empty_file, index=False, encoding="utf-8")
        else:
            for name, df_list in sheets.items():
                for idx, df in enumerate(df_list):
                    file_name = f"{name}.csv" if idx == 0 else f"{name}_{idx+1}.csv"
                    file_path = os.path.join(output_dir, file_name)
                    df.to_csv(file_path, index=False, encoding="utf-8")
