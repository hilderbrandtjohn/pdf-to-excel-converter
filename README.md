# Python pdf-to-excel-converter
This python file reads a PDF file, extracts the text from each page, splits the text into rows, and then writes the rows to the Excel file. The rows are split into cells based on the presence of a space character.
### Install Dependencies
1. Python  - install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)
2. **Libraries** - install PyPDF2 library for reading the PDF, and the openpyxl library for creating the Excel file. You can install these libraries using pip, the Python package manager, like so:
```bash
pip install pypdf2 openpyxl
```
To run the file replace the **'path/to/your.pdf'** in with **open('path/to/your.pdf', 'rb') as file:** with the file path to your pdf.
From the comand line on the same directory as your python file run:
```bash
python converter.py
```
