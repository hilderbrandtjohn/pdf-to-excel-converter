import PyPDF2
import openpyxl

# Open the PDF file in read-binary mode
with open('path/to/your.pdf', 'rb') as file:
    # Create a PDF object
    pdf = PyPDF2.PdfFileReader(file)

    # Create a new Excel file
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Iterate through the pages of the PDF
    for page in range(pdf.getNumPages()):
        # Extract the text from the current page
        text = pdf.getPage(page).extractText()

        # Split the text into rows
        rows = text.split('\n')

        # Iterate through the rows and write them to the Excel sheet
        for row in rows:
            sheet.append(row.split())

    # Save the Excel file
    workbook.save('excel_file.xlsx')