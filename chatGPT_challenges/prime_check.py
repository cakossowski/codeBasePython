"""

Schreibe eine Funktion in Python, die prüft, ob eine Zahl eine Primzahl ist. Eine Primzahl ist eine Zahl,
die nur durch 1 und sich selbst ohne Rest teilbar ist.

"""


def prime_check():
    number = int(input('Bitte gib eine ganze Zahl ein um zu prüfen, ob es sich um eine Primzahl handelt oder nicht! \n'))
    if number % 1 == 0 and number % number == 0:
        print(f'Die Zahl {number} ist eine Primzahl!')
    else:
        print(f'Die Zahl {number} ist leider keine Primzahl!')


prime_check()
