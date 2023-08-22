import subprocess  # needed for opening pdfs
import os

user_os = os.name


# opens pdf
def open_pdf():
    # Get the directory of the current script or executable
    base_path = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(base_path, "wochenplan.pdf")
    print(pdf_path)

    if user_os == 'nt':  # Windows
        os.startfile(pdf_path)
    elif user_os == 'posix':  # macOS und Linux
        subprocess.run(['open', pdf_path])
    else:
        print("Plattform nicht unterstützt")

