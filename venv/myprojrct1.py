import os
from tkinter import Tk, Button
from tkinter.filedialog import askopenfilename
from PyPDF2 import PdfReader
from reportlab.pdfgen import canvas

def reduce_pdf_pages(input_path, output_path, max_lines_per_page, font_size, line_spacing):
    with open(input_path, 'rb') as file:
        reader = PdfReader(file)
        total_pages = len(reader.pages)

        c = canvas.Canvas(output_path)
        current_page = 0
        current_line = 0

        while current_page < total_pages:
            page = reader.pages[current_page]
            content = page.extract_text()

            lines = content.split('\n')
            for line in lines:
                if current_line >= max_lines_per_page:
                    c.showPage()
                    current_line = 0

                c.setFont("Helvetica", font_size)
                c.drawString(100, 800 - (current_line * line_spacing), line.strip())
                current_line += 1

            current_page += 1

        c.save()

def choose_file():
    # Prompt the user to select a PDF file
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    input_file = askopenfilename(title="اختر ملف PDF")

    # Generate the output file path
    output_file = os.path.splitext(input_file)[0] + '_reduced.pdf'

    # Specify the desired maximum lines per page
    max_lines_per_page = 40

    # Specify the desired font size
    font_size = 8

    # Specify the desired line spacing
    line_spacing = 12

    # Call the function to reduce the pages and get the output file path
    reduce_pdf_pages(input_file, output_file, max_lines_per_page, font_size, line_spacing)

    print("تم تقليل صفحات PDF بنجاح.")
    print("مسار الملف المقلص:", output_file)

    # Open the reduced PDF file using the default PDF viewer
    os.startfile(output_file)

# Create a Tkinter window
window = Tk()
# Create a button for file selection
button = Button(window, text="اختر", command=choose_file)
button.pack()

# Run the Tkinter event loop
window.mainloop()










