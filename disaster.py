
import pandas as pd
import plotly.graph_objects as go

def load_and_convert_date(file_path):
    df = pd.read_excel(file_path)
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
    return df

# Load and process the "사건-언론" file
event_media_file_path = 'src\chart-disaster\!사건-언론.xlsx'
event_media_df = load_and_convert_date(event_media_file_path)

# Creating the figure
fig = go.Figure()

# Columns in "사건-언론" corresponding to different events
event_columns = event_media_df.columns[1:]  # Excluding the date column

# Adding traces for each event
for col in event_columns:
    fig.add_trace(go.Scatter(x=event_media_df['date'], y=event_media_df[col], mode='lines', name=col))

# Setting up the figure layout
fig.update_layout(
    title="Event Media Coverage",
    xaxis=dict(autorange=True),
    yaxis=dict(autorange=True)
)

# Save the figure
html_file_path = 'out\event_media_graph.html'
fig.write_html(html_file_path)
