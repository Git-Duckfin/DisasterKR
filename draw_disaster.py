import pandas as pd
from create_event_media_coverage_chart import create_event_media_coverage_chart

# 데이터 로드
df = pd.read_excel('src\chart-disaster\!사건-언론.xlsx')

# 날짜 변환
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')

# 그래프 생성
fig = create_event_media_coverage_chart(df)

# 파일 이름 설정
html_file_name='disaster_data'
# 파일 저장 경로 설정
html_file_path = '.\\'  # Declare and initialize the variable
html_file_path += 'out\\' + html_file_name + ".html"
# 그래프 표시
fig.write_html(html_file_path)