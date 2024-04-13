import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import os

root_dir = os.getcwd()
output_dir = os.path.join(root_dir, 'src', 'election-result', 
        '역대선거_데이터_20240412')

# 데이터 로드
def load_data():
    excel_path = output_dir+'\선거투표율-행렬전환.xlsx'
    data = pd.read_excel(excel_path, header=None)
    data = data.replace('-', float('nan'))
    return data

# 성별 투표율 그래프
def plot_gender_voting(data):
    years = data.iloc[4:22, 0].tolist()
    male_voting = data.iloc[4:22, 3].astype(float)
    female_voting = data.iloc[4:22, 4].astype(float)
    comments = data.iloc[23:25, 1].dropna().tolist()
    fig = px.line(x=years, y=[male_voting, female_voting],
                    labels={'x': 'Year', 'value': 'Voting Rate (%)', 'variable': 'Gender'},
                    title=data.iloc[0, 1])
    fig.update_traces(mode='lines+markers')
    fig.update_layout(title='Graph of Voting Rate by Gender Group',
                      legend_title='Gender', xaxis_title='Year', yaxis_title='Voting Rate (%)',
                      showlegend=True, xaxis=dict(fixedrange=True), yaxis=dict(fixedrange=True))
    # 주석 추가, 제목 우측에 위치
    fig.add_annotation(text=comments[0], xref="paper", yref="paper", x=1, y=1.10, showarrow=False, align="left", font=dict(size=14))
    fig.add_annotation(text=comments[1], xref="paper", yref="paper", x=1, y=1.05, showarrow=False, align="left", font=dict(size=14))
    return fig

# 연령별 투표율 그래프
def plot_age_group_voting(data):
    years = data.iloc[4:22, 0].tolist()
    age_groups = data.iloc[3, 5:16].tolist()
    age_group_voting = data.iloc[4:22, 5:16].astype(float)
    comments = data.iloc[23:25, 1].dropna().tolist()
    fig = go.Figure()
    for i, age_group in enumerate(age_groups):
        fig.add_trace(go.Scatter(x=years, y=age_group_voting.iloc[:, i], mode='lines+markers', name=age_group))
    fig.update_layout(title='Graph of Voting Rate by Age Group',
                      xaxis_title='Year', yaxis_title='Voting Rate (%)',
                      legend_title='Age Groups', xaxis=dict(fixedrange=True), yaxis=dict(fixedrange=True))
    # 주석 추가, 제목 우측에 위치
    fig.add_annotation(text=comments[0], xref="paper", yref="paper", x=1, y=1.10, showarrow=False, align="left", font=dict(size=14))
    fig.add_annotation(text=comments[1], xref="paper", yref="paper", x=1, y=1.05, showarrow=False, align="left", font=dict(size=14))
    return fig

# 히트맵 생성
def create_heatmap(data):
    years = data.iloc[4:22, 0].tolist()
    age_groups = data.iloc[3, 5:16].tolist()
    age_group_voting = data.iloc[4:22, 5:16].astype(float)
    comments = data.iloc[23:25, 1].dropna().tolist()
    # single_comment = ' | '.join(comments)  # 주석을 하나로 결합

    fig = px.imshow(age_group_voting.T, labels=dict(x="Year", y="Age Group", color="Voting Rate"),
                    x=years, y=age_groups, aspect="auto", title="Heatmap of Voting Rate by Age Group")
    fig.update_xaxes(side="bottom")
    # 주석 추가, 제목 우측에 위치
    fig.add_annotation(text=comments[0], xref="paper", yref="paper", x=1, y=1.10, showarrow=False, align="left", font=dict(size=14))
    fig.add_annotation(text=comments[1], xref="paper", yref="paper", x=1, y=1.05, showarrow=False, align="left", font=dict(size=14))
    # fig.add_annotation(text=single_comment, xref="paper", yref="paper", x=1.1, y=1.05, showarrow=False, align="left", font=dict(size=10))
    return fig

# 메인 코드
data = load_data()
fig_age = plot_age_group_voting(data)
fig_gender = plot_gender_voting(data)
heatmap_fig = create_heatmap(data)

root_dir = os.getcwd()
output_dir = os.path.join(root_dir, 'out', 'election-result')
os.makedirs(output_dir, exist_ok=True)

os.chdir(output_dir)
# HTML 파일로 저장
fig_age.write_html('voting_rate_by_age.html', auto_open=False)
fig_gender.write_html('voting_rate_by_gender.html')
heatmap_fig.write_html('voting_rate_heatmap.html')
