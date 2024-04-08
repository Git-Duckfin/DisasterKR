import pandas as pd
import os
import glob

import plotly.graph_objects as go

def load_and_convert_date(file_path):
    df = pd.read_excel(file_path)
    df['date'] = pd.to_datetime(df['date'], format='%Y%m')
    return df

def add_trace_to_fig(fig, df, col_name, trace_name, color):
    fig.add_trace(go.Scatter(x=df['date'], y=df[col_name], mode='lines', name=trace_name, line=dict(color=color)))

def setup_figure_layout(fig, title):
    fig.update_layout(
        title=title,
        xaxis=dict(autorange=True),
        yaxis=dict(autorange=True)
    )

# 파일 경로
file_paths = [
]

common_dir = 'src\common'
for file_name in os.listdir(common_dir):
    if file_name.startswith('선거일-') and file_name.endswith('.xlsx'):
        file_paths.append(os.path.join(common_dir, file_name))


# 데이터 로드 및 날짜 변환
dfs = [load_and_convert_date(fp) for fp in file_paths]

# 그래프 객체 생성 및 트레이스 추가
fig = go.Figure()
trace_names = ['대통령 선거', '자방 선거', '국회의원 선거', '북한 미사일 발사', '심판', '심판 (정부 키워드 포함)', '의료', '의료정책']
trace_colors = ['blue', 'blue', 'blue', 'purple', 'red', 'red', 'green', 'green']
for df, name, color in zip(dfs, trace_names, trace_colors):
    add_trace_to_fig(fig, df, df.columns[1], name, color)

# 그래프 설정
setup_figure_layout(fig, "All Data")

# HTML 파일로 저장
fig.write_html('out\integrated_graph.html')
