from tkinter import StringVar
import customtkinter


class ValueFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.value_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.value_frame.grid(row=0, column=0, padx=5, pady=5)


class LabelsEntryBoxes(customtkinter.CTkLabel):
    def __init__(self, master):
        super().__init__(master)

        self.letter_text = customtkinter.CTkLabel(self, text="Amount of letters: ", fg_color="transparent")
        self.letter_text.grid(row=0, column=0, padx=5, pady=5)

        self.number_text = customtkinter.CTkLabel(self, text="Amount of numbers: ", fg_color="transparent")
        self.number_text.grid(row=1, column=0, padx=5, pady=5)

        self.special_char_text = customtkinter.CTkLabel(self, text="Amount of special chars: ", fg_color="transparent")
        self.special_char_text.grid(row=2, column=0, padx=5, pady=5)


class EntryboxElements(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.letter_value = 0
        self.number_value = 0
        self.special_char_value = 0

        self.letter_var = StringVar()
        self.letter_var.trace("w", lambda *args: self.update_value("letter_value", self.letter_var))

        self.number_var = StringVar()
        self.number_var.trace("w", lambda *args: self.update_value("number_value", self.number_var))

        self.special_char_var = StringVar()
        self.special_char_var.trace("w", lambda *args: self.update_value("special_char_value",
                                                                         self.special_char_var))

        validation = self.register(only_numbers)
        self.letter_box = customtkinter.CTkEntry(self, width=35, corner_radius=10, validate="key",
                                                 validatecommand=(validation, "%P"), textvariable=self.letter_var)
        self.letter_box.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")

        self.number_box = customtkinter.CTkEntry(self, width=35, corner_radius=10, validate="key",
                                                 validatecommand=(validation, "%P"), textvariable=self.number_var)
        self.number_box.grid(row=1, column=1, padx=5, pady=10, sticky="nsew")

        self.special_char_box = customtkinter.CTkEntry(self, width=35, corner_radius=10, validate="key",
                                                       validatecommand=(validation, "%P"),
                                                       textvariable=self.special_char_var)
        self.special_char_box.grid(row=2, column=1, padx=5, pady=10, sticky="nsew")

    def update_value(self, attr_name, var):
        value = var.get()
        setattr(self, attr_name, int(value) if value else 0)


def only_numbers(entry_by_user):
    if entry_by_user.isdigit() or entry_by_user == "":
        return True
    return False

