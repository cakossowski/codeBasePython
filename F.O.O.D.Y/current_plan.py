import subprocess  # needed for opening pdfs
import os

user_os = os.name


def get_pdf_path():
    if user_os == 'nt':
        # relative path to pdf, windows
        return r"..\F.O.O.D.Y\wochenplan.pdf"
    elif user_os == 'posix':
        # relative path to pdf, linux
        return r"../F.O.O.D.Y/wochenplan.pdf"
    else:
        print("Unknown OS")


# opens pdf
def open_pdf():
    pdf_path = get_pdf_path()
    # abspath shows current path of file, just kept as a reference for future me
    # print(os.path.abspath(__file__))
    if user_os == 'nt':  # Windows
        os.startfile(pdf_path)
    elif user_os == 'posix':  # macOS und Linux
        subprocess.run(['open', pdf_path])
    else:
        print("Plattform nicht unterstützt")

