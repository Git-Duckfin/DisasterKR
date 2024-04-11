from enum import auto
import html
from turtle import left
from colorama import init
from networkx import center
import pandas as pd
from sklearn.decomposition import non_negative_factorization
from torch import initial_seed
from create_event_media_coverage_chart import create_event_media_coverage_chart
from tkinter import dialog, filedialog, Tk
import os

def select_file(title, initialdir, filetypes):
    """
    Opens a file dialog to select a file.

    Args:
        title (str): The title of the file dialog window.
        initialdir (str): The initial directory to open the file dialog in.
        filetypes (list): A list of file types to filter the files in the dialog.

    Returns:
        str: The path of the selected file.
    """
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title=title, 
        initialdir=initialdir, filetypes=filetypes)
    root.destroy()
    return file_path

def save_file(title, initialdir, filetypes):
    """
    Opens a file dialog to save a file.

    Args:
        title (str): The title of the file dialog window.
        initialdir (str): The initial directory to open the file dialog in.
        filetypes (list): A list of file types to filter the files in the dialog.

    Returns:
        str: The path of the saved file.
    """
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.asksaveasfilename(title=title, 
        initialdir=initialdir, defaultextension='.html', filetypes=filetypes)
    root.destroy()
    return file_path

def main():
    """
    The main function of the script.
    """
    initial_dir = os.path.join(os.getcwd(), 'src/!integrated')
    # Select the Excel file
    excel_file = select_file('Select Excel File', 
                             initial_dir, [('Excel Files', '*.xlsx')])
    if not excel_file:
        return

    df = pd.read_excel(excel_file)
    # Convert the date
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
    
    fig = create_event_media_coverage_chart(df, excel_file)
    print("Saving the chart...")
    # Save the HTML file
    html_dir = os.path.join(os.getcwd(),'out','html')
    html_file_path = save_file('Save HTML File', html_dir, [('HTML Files', '*.html')])
    if not html_file_path:
        return
    
    fig.update_layout(
        autosize=True,  # set autosize to True
        margin=dict(t=200),  # adjust top margin to avoid overlap with title
        # *** arrange traces in a single line ***
        # grid=dict(rows=1, columns=len(fig.data)),
        # template=dict(layout=dict(polar=dict(barmode='stack'))),  # Change 'plotly' to 'polar'
        # *** set the width of each trace ***
        barmode='group',  # set the bar mode to group
        bargap=0.1,  # set the gap between bars
        bargroupgap=0.2  # set the gap between groups of bars
    )
    fig.write_html(html_file_path, include_plotlyjs='cdn', full_html=False)

main()