"""
S.H.I.E.L.D.: "Sicherheits-Hochleistungs-Interface zur Erzeugung von Logins und Daten"
"""

import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("S.H.I.E.L.D. - Interface")
        self.geometry("500x500")