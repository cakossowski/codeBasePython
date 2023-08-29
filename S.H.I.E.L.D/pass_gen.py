import ui
import main
import customtkinter
import secrets
import string


def create_password(letter_value, number_value, special_char_value):
    pwd_length = letter_value + number_value + special_char_value

    # setting up the whole alphabet to use as a base for the password
    letters = string.ascii_letters
    digits = string.digits
    special_char = string.punctuation
    alphabet = letters + digits + special_char

    while True:
        pwd = ''
        for i in range(pwd_length):
            pwd += secrets.choice(alphabet)

        # check if all characters are included and overall sums add up
        if (sum(char in letters for char in pwd) >= letter_value and
                sum(char in digits for char in pwd) >= number_value and
                sum(char in special_char for char in pwd) >= special_char_value):
            return pwd




