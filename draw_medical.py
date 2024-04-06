import pandas as pd
import os
import plotly.graph_objects as go

def load_and_convert_date(file_path):
    df = pd.read_excel(file_path)
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
    return df

def add_trace_to_fig(fig, df, col_name):
    fig.add_trace(go.Scatter(x=df['date'], y=df[col_name], mode='lines', name=col_name))

def setup_figure_layout(fig, title):
    fig.update_layout(
        title=title,
        xaxis=dict(title='date', tickformat='%y%m%d', autorange=True),
        yaxis=dict(title='Value', autorange=True),
        autosize=False,
        width=1800,  # 그래프의 너비 설정
        height=900  # 그래프의 높이 설정
    )

##############################################################################################################
## 엑셀의 5번째, 6번째 열을 데이터 프레임에 제외하는 옵션 함수를 추가하고, 이를 이용해 데이터를 로드
##############################################################################################################
def load_and_convert_date(file_path, exclude_cols):
    # 모든 열의 인덱스를 가져온다
    all_cols = pd.read_excel(file_path, nrows=0).columns.tolist()

    # 제외할 열을 제거한다
    for col in exclude_cols:
        if col in all_cols:
            all_cols.remove(col)

    # 제외할 열을 제외하고 데이터를 로드한다
    df = pd.read_excel(file_path, usecols=all_cols)
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
    return df

### 제외할 열의 인덱스 ###
# 의료 AND("필수") NOT (수가)
# 의료 AND("수가") NOT (필수)
exclude_cols = [5, 6]  # Python은 0부터 인덱싱을 시작하므로, 5번째, 6번째 열을 제외한다
##############################################################################################################

# 파일 경로
file_path = 'election\src\의료-집계-통합.xlsx'

# 데이터 로드 및 날짜 변환
df = load_and_convert_date(file_path, exclude_cols)
# df = load_and_convert_date(file_path)

# 그래프 객체 생성 및 트레이스 추가
fig = go.Figure()

for column in df.columns[1:]:
    if df.columns.get_loc(column) not in exclude_cols:
        add_trace_to_fig(fig, df, column)

# 그래프 설정
setup_figure_layout(fig, "Medical Data")

# HTML 파일로 저장
output_path = 'election\out\medical_data.html'
fig.write_html(output_path)