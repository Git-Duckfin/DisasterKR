import os, sys
import plotly.graph_objects as go
import pandas as pd

def create_event_media_coverage_chart(event_media_df, file_path):
    """
    Given a DataFrame and a file path, creates a Plotly chart.

    Args:
        event_media_df (pd.DataFrame): DataFrame containing the data for the chart.
        file_path (str): The file path of the input file, used to extract the title for the chart.

    Returns:
        plotly.graph_objs._figure.Figure: The Plotly figure object for the chart.
    """

    # Extract title from file path
    title = os.path.basename(file_path).split('.')[0]

    # Create the Plotly chart
    fig = go.Figure()
    
    # Assuming your DataFrame has a 'date' column and other columns for data
    for col in event_media_df.columns[1:]:  # Skipping the 'date' column
        fig.add_trace(go.Scatter(x=event_media_df['date'], y=event_media_df[col], mode='lines', name=col))

    # Update layout
    fig.update_layout(
        title=title,
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
    return fig

# if len(sys.argv) > 1:
#     title_name = sys.argv[1]
# else:
#     # breakpoint()
#     title_name = "Select File"  # Default title

# initialdir='src/!integrated'
# event_media_file_path = os.path.join(initialdir, title_name+'.xlsx')

# event_media_df = load_and_convert_date(event_media_file_path)  # Move this line above the next line
# fig = create_event_media_coverage_chart(event_media_df, sys.argv[1])