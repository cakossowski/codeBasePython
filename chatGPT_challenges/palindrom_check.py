"""

Schreibe ein Python-Programm, das prüft, ob ein gegebener String ein Palindrom ist. Ein Palindrom ist ein Wort,
das vorwärts und rückwärts gelesen dasselbe ergibt. Beispiel: "radar".

"""


def palindrom_check(palindrom):
    return palindrom == palindrom[::-1]


palindrom = input('Bitte gib ein Wort ein um zu prüfen ob es ein Palindrom ist: \n')
result = palindrom_check(palindrom.lower())

if result:
    print(f'Das Wort "{palindrom}" ist ein Palindrom!')
else:
    print(f'Das Wort "{palindrom}" ist leider kein Palindrom!')

