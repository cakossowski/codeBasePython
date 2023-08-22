# standard libraries
import customtkinter
from PIL import Image  # needed module for image manipulation
from PIL import Image, ImageTk  # seems necessary to export file into exe
from customtkinter import CTkImage  # necessary to import images properly


# creates new window, at the moment only for test purposes. all functions will be externalized at some point
def open_ingredients():
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
