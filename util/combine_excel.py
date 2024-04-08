import pandas as pd
import os
from tkinter import Tk, filedialog

def select_files():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_paths = filedialog.askopenfilenames(title='Select Excel Files', filetypes=[('Excel Files', '*.xlsx')])
    root.destroy()
    return file_paths

def combine_excel_files(file_paths):
    combined_df = pd.DataFrame()
    for i, file_path in enumerate(file_paths):
        df = pd.read_excel(file_path, engine='openpyxl', dtype={0: str})
        if i == 0:
            combined_df = df
        else:
            common_dates = combined_df.iloc[:, 0].isin(df.iloc[:, 0])
            df_common = df[df.iloc[:, 0].isin(combined_df.iloc[:, 0][common_dates])]
            combined_df_common = combined_df[combined_df.iloc[:, 0].isin(df.iloc[:, 0][common_dates])]
            combined_df = pd.concat([combined_df_common, df_common.iloc[:, 1:]], axis=1)
    return combined_df

def main():
    root = Tk()
    root.withdraw()  # Hide the main window for file dialog

    file_paths = select_files()
    if file_paths:
        combined_data = combine_excel_files(file_paths)

        # Specify the default directory for saving the file
        default_dir = os.path.join(os.getcwd(), 'src')
        if not os.path.exists(default_dir):
            os.makedirs(default_dir)

        output_file = filedialog.asksaveasfilename(
            initialdir=default_dir,
            title="Save Combined Excel File",
            defaultextension='.xlsx',
            filetypes=[('Excel Files', '*.xlsx')]
        )

        if output_file:
            combined_data.to_excel(output_file, index=False)
            print(f"Combined file saved to {output_file}")

    root.destroy()

if __name__ == "__main__":
    main()
