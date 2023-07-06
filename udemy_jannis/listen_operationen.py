students = ['Max', 'Monika', 'Erik', 'Franziska']

# pop entfernt das letzte Element einer Liste
last_student = students.pop()

print(last_student)
print(students)

# Listen "addieren"

students = ['Max', 'Monika', 'Erik', 'Franziska'] + ['Horst']

print(students)

# del entfernt indixierten Eintrag, aber der Index muss bekannt sein

del students[3]
print(students)

# .remove entfernt einen Eintrag, aber Eintrag muss bekannt sein, Index ist in dem Fall unwichtig
students.remove('Horst')
print(students)

# immer letztes Element einer Liste ausgeben
print(students[-1])

# List slicing

students = ['Max', 'Monika', 'Erik', 'Franziska'] + ['Horst']
# erschafft eine Kopie der Liste
print(students[:])

# Elemente auswählen, erstes Element inklusive, letztes Element exklusive
print(students[2:4])
print(students[1:4])
print(students[1:-1])

# Vollständige Liste bis zum letzten Element, 0 kann weggelassen werden // da geht auch [1:]
print(students[:-1])
