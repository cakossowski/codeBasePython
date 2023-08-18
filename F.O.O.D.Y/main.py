import customtkinter
from PIL import Image  # needed module for image manipulation
import subprocess  # needed for opening pdfs
import os
from customtkinter import CTkImage  # necessary to import images properly

customtkinter.set_appearance_mode("dark")  # sets the overall appearance to dark mode

# help text, probably will be changed in the future
help_text = """

Willkommen bei FOODY!

Das hier ist nur die erste provisorische Hilfe, diese wird nach und nach ausgebaut.

"Aktueller Plan": 
Zeigt den zuletzt generierten Plan an

"Plan generieren" : 
Führt dich zum Fenster wo du Pläne einstellen und anlegen kannst.

"Gerichte verwalten":
Du kannst bestehende Gerichte verwalten oder neue anlegen

"Zutaten verwalten":
Du kannst bestehende Zutaten verwalten oder neue anlegen

"Hilfe":
Diese Seite siehst du gerade, du hast intuitiv erraten, welche Funktion 'Hilfe' erfüllt!

"Beenden":
Schließt die App.

"""


# simple function to simulate button press
def button_callback():
    print("button pressed")


# opens pdf
def open_pdf():
    # relative path to pdf, definitely works on linux
    pdf_path = r"../F.O.O.D.Y/wochenplan.pdf"
    # abspath shows current path of file, just kept as a reference for future me
    # print(os.path.abspath(__file__))
    if os.name == 'nt':  # Windows
        os.startfile(pdf_path)
    elif os.name == 'posix':  # macOS und Linux
        subprocess.run(['open', pdf_path])
    else:
        print("Plattform nicht unterstützt")


# creates new window, at the moment only for test purposes. all functions will be externalized at some point
def open_new_window():
    new_window = customtkinter.CTkToplevel()  # creates new window
    new_window.focus_set()  # sets focus on this window
    new_window.attributes('-topmost', True)  # topmost ensures that window is displayed in foreground
    new_window.title("Neues Fenster")  # titles new window
    new_window.geometry("200x150")  # sets size of window

    # labels the window when opened, like a headline of the window
    label = customtkinter.CTkLabel(new_window, text="Dies ist ein neues Fenster!")
    label.pack(pady=20)

    # creates the close button, which destroys the current window on press
    close_button = customtkinter.CTkButton(new_window, text="Zurück", command=new_window.destroy)
    close_button.pack(pady=20)


# specific function to create help window once button is pressed, will be externalized in coming "patch"
def open_help_window():
    help_window = customtkinter.CTkToplevel()
    help_window.focus_set()
    help_window.attributes('-topmost', True)
    help_window.title("F.O.O.D.Y. - Hilfe")
    help_window.geometry("650x650")

    help_label = customtkinter.CTkLabel(help_window, text=help_text,
                                        font=customtkinter.CTkFont(size=15, weight="bold"))
    help_label.pack(pady=10)

    close_button = customtkinter.CTkButton(help_window, text="Zurück", command=help_window.destroy)
    close_button.pack(pady=20)


app = customtkinter.CTk()
app.title("F.O.O.D.Y.")
app.geometry("360x400")
app.grid_columnconfigure(0, weight=1)

# sets logo image and places it into grid
image = CTkImage(Image.open("../F.O.O.D.Y/logo.png"), size=(125, 60))
title_image = customtkinter.CTkLabel(app, image=image, text="")
title_image.grid(row=0, column=0, padx=20, pady=5)

title_label = customtkinter.CTkLabel(app, text="Willkommen bei F.O.O.D.Y.",
                                     font=customtkinter.CTkFont(size=20, weight="bold"))
title_label.grid(row=1, column=0, padx=30, pady=(15, 20))

# creates "Aktueller Plan" / "Current Plan" - Button
aktueller_plan = customtkinter.CTkButton(app, text="Aktueller Plan", command=open_pdf)
aktueller_plan.grid(row=2, column=0, padx=20, pady=5)

# creates "Plan generieren" / "Generate Plan" - Button
plan_generieren = customtkinter.CTkButton(app, text="Plan generieren", command=open_new_window)
plan_generieren.grid(row=3, column=0, padx=20, pady=5)

# creates "Gerichte verwalten" / "Manage Dishes" - Button
gerichte_verwalten = customtkinter.CTkButton(app, text="Gerichte verwalten", command=open_new_window)
gerichte_verwalten.grid(row=4, column=0, padx=20, pady=5)

# creates "Zutaten verwalten" / "Manage Ingredients" - Button
zutaten_verwalten = customtkinter.CTkButton(app, text="Zutaten verwalten", command=open_new_window)
zutaten_verwalten.grid(row=5, column=0, padx=20, pady=5)

# creates "Hilfe" / "Help" - Button
hilfe = customtkinter.CTkButton(app, text="Hilfe", command=open_help_window)
hilfe.grid(row=6, column=0, padx=20, pady=5)

# creates "Beenden" / "Quit" - Button
beenden = customtkinter.CTkButton(app, text="Beenden", command=app.quit)
beenden.grid(row=8, column=0, padx=20, pady=30)

app.mainloop()
