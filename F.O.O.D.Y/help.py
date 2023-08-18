import customtkinter

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


# specific function to create help window once button is pressed
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