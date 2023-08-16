"""
F.O.O.D.Y. - [F]antastic [O]rganized [O]ptions for [D]elightful [Y]umminess

FOODY is a simple tool, that lets you create a pool of dishes you usually cook / want to cook and
organizes them in the background.

You can set your starting day of the week and for how many weekdays you need to plan in advance.
The app will randomly choose dishes from the pool and assign them to a weekday, once done
it will write everything (means Weekday and dish at the moment) into a file (simple textfile for now).

"""
import customtkinter
from PIL import Image
import subprocess
import os

from customtkinter import CTkImage

customtkinter.set_appearance_mode("dark")

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
def button_callback():
    print("button pressed")


def open_pdf():
    # Pfad zur lokalen PDF-Datei
    pdf_path = r"D:\PSD Mockups\FOODY\wochenplan.pdf"
    if os.name == 'nt':  # Windows
        os.startfile(pdf_path)
    elif os.name == 'posix':  # macOS und Linux
        subprocess.run(['open', pdf_path])
    else:
        print("Plattform nicht unterstützt")


def open_new_window():
    new_window = customtkinter.CTkToplevel()  # Erstellt ein neues Fenster
    new_window.focus_set()  # Setzt den Fokus auf das sekundäre Fenster
    new_window.attributes('-topmost', True)
    new_window.title("Neues Fenster")
    new_window.geometry("200x150")
    print("button pressed")

    label = customtkinter.CTkLabel(new_window, text="Dies ist ein neues Fenster!")
    label.pack(pady=20)

    close_button = customtkinter.CTkButton(new_window, text="Zurück", command=new_window.destroy)
    close_button.pack(pady=20)


def open_help_window():
    help_window = customtkinter.CTkToplevel()  # Erstellt ein neues Fenster
    help_window.focus_set()  # Setzt den Fokus auf das sekundäre Fenster
    help_window.attributes('-topmost', True)
    help_window.title("F.O.O.D.Y. - Hilfe")
    help_window.geometry("650x650")
    print("button pressed")

    help_label = customtkinter.CTkLabel(help_window, text=help_text,
                                         font=customtkinter.CTkFont(size=15, weight="bold"))
    help_label.pack(pady=10)

    close_button = customtkinter.CTkButton(help_window, text="Zurück", command=help_window.destroy)
    close_button.pack(pady=20)


app = customtkinter.CTk()
app.title("F.O.O.D.Y.")
app.geometry("360x400")
app.grid_columnconfigure(0, weight=1)


image = CTkImage(Image.open("D:\PSD Mockups\FOODY\logo.png"), size=(125, 60))
title_image = customtkinter.CTkLabel(app, image=image,text="")
title_image.grid(row=0, column=0, padx=20, pady=5)

title_label = customtkinter.CTkLabel(app, text="Willkommen bei F.O.O.D.Y.",
                                    font=customtkinter.CTkFont(size=20, weight="bold"))
title_label.grid(row=1, column=0, padx=30, pady=(15, 20))

aktueller_plan = customtkinter.CTkButton(app, text="Aktueller Plan", command=open_pdf)
aktueller_plan.grid(row=2, column=0, padx=20, pady=5)

plan_generieren = customtkinter.CTkButton(app, text="Plan generieren", command=open_new_window)
plan_generieren.grid(row=3, column=0, padx=20, pady=5)

gerichte_verwalten = customtkinter.CTkButton(app, text="Gerichte verwalten", command=open_new_window)
gerichte_verwalten.grid(row=4, column=0, padx=20, pady=5)

zutaten_verwalten = customtkinter.CTkButton(app, text="Zutaten verwalten", command=open_new_window)
zutaten_verwalten.grid(row=5, column=0, padx=20, pady=5)

hilfe = customtkinter.CTkButton(app, text="Hilfe", command=open_help_window)
hilfe.grid(row=6, column=0, padx=20, pady=5)

beenden = customtkinter.CTkButton(app, text="Beenden", command=app.quit)
beenden.grid(row=8, column=0, padx=20, pady=30)

app.mainloop()