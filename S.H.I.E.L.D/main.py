"""
S.H.I.E.L.D.: "Sicherheits-Hochleistungs-Interface zur Erzeugung von Logins und Daten"
"""

import customtkinter
import ui

customtkinter.set_appearance_mode("dark")  # sets the overall appearance to dark mode
customtkinter.set_default_color_theme("blue")  # sets the overall color theme for buttons, etc.


class App(customtkinter.CTk):

    _instance = None

    @classmethod
    def get_instance(cls):
        return cls._instance

    def __init__(self):
        App._instance = self
        super().__init__()

        self.title("S.H.I.E.L.D. - Interface")
        self.geometry("500x500")

        self.entrybox = ui.EntryboxElements(self)
        self.entrybox.grid(row=1, column=1, padx=10,
                           pady=10, sticky="nsw")

        self.textlabels = ui.LabelsEntryBoxes(self)
        self.textlabels.grid(row=1, column=0, padx=10,
                             pady=10, sticky="nsw")

        self.password_display = customtkinter.CTkEntry(self, state='readonly')
        self.password_display.grid(row=6, column=0, padx=20, pady=30)

        self.passwort = customtkinter.CTkButton(self, text="Password", command=self.display_password)
        self.passwort.grid(row=8, column=0, padx=20, pady=30)

        self.beenden = customtkinter.CTkButton(self, text="Beenden", command=self.quit)
        self.beenden.grid(row=8, column=1, padx=20, pady=30)

    def display_password(self):
        import pass_gen
        letter_value = self.entrybox.letter_value
        number_value = self.entrybox.number_value
        special_char_value = self.entrybox.special_char_value
        generated_password = pass_gen.create_password(letter_value, number_value, special_char_value)
        self.password_display.configure(state='normal')
        self.password_display.delete(0, 'end')
        self.password_display.insert(0, f"{generated_password}")
        self.password_display.configure(state='readonly')


if __name__ == "__main__":
    App().mainloop()
