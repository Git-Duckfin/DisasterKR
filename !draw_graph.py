import pandas as pd
from create_event_media_coverage_chart import create_event_media_coverage_chart
from tkinter import filedialog, Tk

def select_file(title, initialdir, filetypes):
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title=title, initialdir=initialdir, filetypes=filetypes)
    root.destroy()
    return file_path

def save_file(title, initialdir, filetypes):
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.asksaveasfilename(title=title, initialdir=initialdir, defaultextension='.html', filetypes=filetypes)
    root.destroy()
    return file_path

def main():
    # Select the Excel file
    excel_file = select_file('Select Excel File', 'src/', [('Excel Files', '*.xlsx')])
    if not excel_file:
        return

    df = pd.read_excel(excel_file)

    # Convert the date
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')

    # Select HTML file path
    html_file_path = save_file('Save HTML File', 'out/', [('HTML Files', '*.html')])
    if not html_file_path:
        return

    # Create and save the chart
    fig = create_event_media_coverage_chart(df, title='Medical Data Chart')
    fig.write_html(html_file_path, include_plotlyjs='cdn', full_html=False)

if __name__ == '__main__':
    main()
