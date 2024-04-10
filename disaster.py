import pandas as pd
import plotly.graph_objects as go

def load_and_convert_date(file_path):
    df = pd.read_excel(file_path)
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
    return df

# "사건-언론" 파일을 로드하고 처리합니다.
event_media_file_path = 'src\chart-disaster\!사건-언론.xlsx'
event_media_df = load_and_convert_date(event_media_file_path)

# 그래프 생성
fig = go.Figure()

# "사건-언론" 파일의 각 이벤트에 대한 열
event_columns = event_media_df.columns[1:]  # Excluding the date column

# 각 이벤트에 대한 트레이스 추가
for col in event_columns:
    fig.add_trace(go.Scatter(x=event_media_df['date'], y=event_media_df[col], mode='lines', name=col))

# 그래프 레이아웃 설정
fig.update_layout(
    title="Event Media Coverage",
        xaxis=dict(title='date'),
        yaxis=dict(title='Value', autorange=True),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)

# Save the figure
html_file_path = 'out\html\event_media_graph.html'
fig.write_html(html_file_path)
