# standard libraries
import customtkinter
from PIL import Image, ImageTk  # seems necessary to export file into exe
from customtkinter import CTkImage  # necessary to import images properly
from tkinter import PhotoImage  # needed to turn images into buttons

customtkinter.set_appearance_mode("dark")  # sets the overall appearance to dark mode
customtkinter.set_default_color_theme("blue")  # sets the overall color theme for buttons, etc.


# creates new window, at the moment only for test purposes. all functions will be externalized at some point
def open_generate_plan():
    generate_plan_window = customtkinter.CTkToplevel()  # creates new window
    generate_plan_window.focus_set()  # sets focus on this window
    generate_plan_window.attributes('-topmost', True)  # topmost ensures that window is displayed in foreground
    generate_plan_window.title("F.O.O.D.Y.  - Plan generieren")  # titles window
    generate_plan_window.geometry("460x690")  # sets size of window

    # for now the following functions are only placeholders for debugging and testing
    def button_press_reset():
        print("Button reset has been pressed")

    def button_press_generate():
        print("Button generate has been pressed")

    def button_press_add_dish():
        print("Dish has been added")

    def button_press_remove_dish():
        print("Dish has been removed")

    def button_press_edit_list():
        print("List has been changed")

    def checkbox_event(checkbox_var):
        print(f"checkbox {checkbox_var} toggled, current value:", checkbox_var.get())

    # heading for window
    label = customtkinter.CTkLabel(generate_plan_window, text="Stelle hier deinen Plan zusammen!")
    label.grid(row=0, padx=10, pady=5, sticky="w")

    # creates the upper frame, where dishes are displayed
    frame_dish_list = customtkinter.CTkScrollableFrame(generate_plan_window, width=350, height=350, corner_radius=5)
    frame_dish_list.grid(row=1, column=0, padx=5, pady=10, sticky="w")

    # creates the lower frame, where filters [checkboxes] are displayed
    frame_filter_list = customtkinter.CTkScrollableFrame(generate_plan_window, width=430, height=150, corner_radius=5)
    frame_filter_list.grid(row=2, column=0, padx=5, pady=5)

    # frame to align buttons on right, next to dish list
    frame_buttons_dish_list = customtkinter.CTkFrame(generate_plan_window)
    frame_buttons_dish_list.grid(row=1, column=0, pady=10, sticky="se")

    # frame to align buttons on bottom
    frame_buttons_bottom = customtkinter.CTkFrame(generate_plan_window, width=450, height=50)
    frame_buttons_bottom.grid(row=10, column=0, pady=5)

    # creates the add_dish button
    image_add_button = customtkinter.CTkImage(Image.open("../resources/add_button.png"), size=(60, 60))
    button_add_dish = customtkinter.CTkButton(frame_buttons_dish_list, image=image_add_button, text="",
                                              command=button_press_add_dish, height=60, width=60,
                                              fg_color="transparent")
    button_add_dish.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    # creates the remove_dish button
    image_trash_button = customtkinter.CTkImage(Image.open("../resources/trash_button.png"), size=(60, 60))
    button_remove_dish = customtkinter.CTkButton(frame_buttons_dish_list, image=image_trash_button, text="",
                                                 command=button_press_remove_dish,
                                                 height=60, width=60,
                                                 fg_color="transparent")
    button_remove_dish.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    # creates the edit_dish button
    image_edit_button = customtkinter.CTkImage(Image.open("../resources/edit_button.png"), size=(60, 60))
    button_edit_dish = customtkinter.CTkButton(frame_buttons_dish_list, image=image_edit_button, text="",
                                               command=button_press_edit_list, height=60, width=60,
                                               fg_color="transparent")
    button_edit_dish.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    # creates the reset button, which destroys the current window on press
    close_button = customtkinter.CTkButton(frame_buttons_bottom, text="Home", command=generate_plan_window.destroy)
    close_button.grid(row=10, column=0, padx=5, pady=5)

    # creates the reset button, which unchecks all filters and empties the dish list
    reset_button = customtkinter.CTkButton(frame_buttons_bottom, text="Zurücksetzen", command=button_press_reset)
    reset_button.grid(row=10, column=1, padx=5, pady=5)

    # creates the "generate plan" button, to generate the meal plan
    generate_button = customtkinter.CTkButton(frame_buttons_bottom, text="Plan generieren",
                                              command=button_press_generate)
    generate_button.grid(row=10, column=2, padx=5, pady=5)

    # variables for checkboxes
    check_keto = customtkinter.StringVar(value="off")
    check_vegan = customtkinter.StringVar(value="off")
    check_vegetarian = customtkinter.StringVar(value="off")

    # this is the beginning of the filter section, all filters have to be set manually

    # filter keto
    checkbox_keto = customtkinter.CTkCheckBox(master=frame_filter_list, text="Ketogen",
                                              command=lambda: checkbox_event(check_keto),
                                              variable=check_keto, onvalue="on", offvalue="off")
    checkbox_keto.grid(pady=5)

    # filter vegan
    checkbox_vegan = customtkinter.CTkCheckBox(master=frame_filter_list, text="Vegan",
                                               command=lambda: checkbox_event(check_vegan),
                                               variable=check_vegan, onvalue="on", offvalue="off")
    checkbox_vegan.grid(pady=5)

    # filter vegetarian
    checkbox_vegetarian = customtkinter.CTkCheckBox(master=frame_filter_list, text="Vegetarisch",
                                                    command=lambda: checkbox_event(check_vegetarian),
                                                    variable=check_vegetarian, onvalue="on", offvalue="off")
    checkbox_vegetarian.grid(pady=5)
