import os
import pandas as pd
from tkinter import filedialog
from tkinter import Tk

# 팝업창을 띄워서 폴더를 선택합니다.
root = Tk()
root.withdraw()  # GUI 창이 나타나지 않도록 합니다.
folder_selected = filedialog.askdirectory()  # 폴더 선택 창을 띄웁니다.

# 선택한 폴더 아래의 모든 엑셀 파일을 찾습니다.
for file_name in os.listdir(folder_selected):
    if file_name.endswith('.xlsx'):
        file_path = os.path.join(folder_selected, file_name)

        # 엑셀 파일을 읽어옵니다.
        df = pd.read_excel(file_path)

        # 마지막 행을 삭제합니다.
        df = df.iloc[:-1]

        # 변경된 데이터프레임을 다시 엑셀 파일로 저장합니다.
        df.to_excel(file_path, index=False)