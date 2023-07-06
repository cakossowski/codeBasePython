"""

Schreibe eine Funktion in Python, die prüft, ob eine Zahl gerade oder ungerade ist.
Die Funktion soll "gerade" zurückgeben, wenn die Zahl gerade ist, andernfalls "ungerade".

"""


def even_check(number):
    if number % 2 == 0:
        print(f'Die Zahl {number} ist gerade!')
    else:
        print(f'Die Zahl {number} ist ungerade!')


number = int(input('Bitte gib eine ganze Zahl ein um zu überprüfen, ob sie gerade oder ungerade ist: \n'))

even_check(number)
