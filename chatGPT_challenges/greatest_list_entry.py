"""

Schreibe ein Python-Programm, das den größten Wert aus einer Liste von Zahlen findet und ausgibt.

"""

import random

numbers = []

endwert = random.randint(3,30)
if endwert < 3:
    endwert = 3

for _ in range(0, endwert):
    element = random.randint(0, 15)
    numbers.append(element)

check_value = numbers[0]
position = 0


for i, element in enumerate(numbers):
    if check_value < element:
        check_value = element
        position = i+1


print(numbers)
print(f'{check_value} ist der größte Wert der Zahlenkette und befindet sich an der {position}. Position')
