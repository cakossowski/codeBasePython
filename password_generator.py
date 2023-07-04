import secrets
import string

# setting up the whole alphabet to use as a base for the password
letters = string.ascii_letters
digits = string.digits
special_char = string.punctuation
alphabet = letters + digits + special_char

# getting user input to create password according to needs
pwd_length = (int(input('How many characters should the password have? Specify in a whole number: \n')))
required_letters = (int(input(f'How many letters should the {pwd_length} character password at least have? Specify in a whole number: \n')))
required_numbers = (int(input(f'How many numbers should the password have? {pwd_length-required_letters} characters are left to use. Specify in a whole number: \n')))


# in case user didn't specify amount of special characters it will be set to 0 and create the password without them
if (required_letters + required_numbers) >= pwd_length:
    required_special = 0
else:
    required_special = (int(input(f'How many special characters should the password have? {pwd_length - required_letters - required_numbers} characters are left to use. Specify in a whole number: \n')))

sum_chars = required_letters + required_numbers + required_special
success = 0
while True:
    # check if the overall of characters fit the pwd_length
    if (required_letters + required_numbers + required_special) < pwd_length or (required_letters + required_numbers + required_special) > pwd_length:
        print(f'The specified password length doesnt match the amount of previously set characters. Password length: {pwd_length} and sum of entered chars: {sum_chars}')
        break
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    # check if all characters are included and overall sums add up
    if sum(char in letters for char in pwd) >= required_letters and sum(char in digits for char in pwd) >= required_numbers and sum(char in special_char for char in pwd) >= required_special:
        success += 1
        break

if success == 1:
    print(pwd)

