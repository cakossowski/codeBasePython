# standard libraries
import customtkinter
from PIL import Image, ImageTk  # seems necessary to export file into exe
from customtkinter import CTkImage  # necessary to import images properly

# my modules
import help
import current_plan
import manage_dishes
import manage_ingredients
import generate_plan


customtkinter.set_appearance_mode("dark")  # sets the overall appearance to dark mode
customtkinter.set_default_color_theme("blue")  # sets the overall color theme for buttons, etc.


app = customtkinter.CTk()
app.title("F.O.O.D.Y.")
app.geometry("360x400")
app.grid_columnconfigure(0, weight=1)

# sets logo image and places it into grid
image = CTkImage(Image.open("logo.png"), size=(125, 60))
title_image = customtkinter.CTkLabel(app, image=image, text="")
title_image.grid(row=0, column=0, padx=20, pady=5)

title_label = customtkinter.CTkLabel(app, text="Willkommen bei F.O.O.D.Y.",
                                     font=customtkinter.CTkFont(size=20, weight="bold"))
title_label.grid(row=1, column=0, padx=30, pady=(15, 20))

# creates "Aktueller Plan" / "Current Plan" - Button
aktueller_plan = customtkinter.CTkButton(app, text="Aktueller Plan", command=current_plan.open_pdf)
aktueller_plan.grid(row=2, column=0, padx=20, pady=5)

# creates "Plan generieren" / "Generate Plan" - Button
plan_generieren = customtkinter.CTkButton(app, text="Plan generieren", command=generate_plan.open_generate_plan)
plan_generieren.grid(row=3, column=0, padx=20, pady=5)

# creates "Gerichte verwalten" / "Manage Dishes" - Button
gerichte_verwalten = customtkinter.CTkButton(app, text="Gerichte verwalten", command=manage_dishes.open_dishes)
gerichte_verwalten.grid(row=4, column=0, padx=20, pady=5)

# creates "Zutaten verwalten" / "Manage Ingredients" - Button
zutaten_verwalten = customtkinter.CTkButton(app, text="Zutaten verwalten", command=manage_ingredients.open_ingredients)
zutaten_verwalten.grid(row=5, column=0, padx=20, pady=5)

# creates "Hilfe" / "Help" - Button
hilfe = customtkinter.CTkButton(app, text="Hilfe", command=help.open_help_window)
hilfe.grid(row=6, column=0, padx=20, pady=5)

# creates "Beenden" / "Quit" - Button
beenden = customtkinter.CTkButton(app, text="Beenden", command=app.quit)
beenden.grid(row=8, column=0, padx=20, pady=30)

app.mainloop()
