"""

Liste mit [] - mutable
Dict mit {} -
Tupel mit () - immutable / Einmal gesetzt ist gesetzt

"""

t = (1, 2, 3)

# Elemente werden aber wie bei Listen indexiert
print(t)
print(t[0])



"""
Tupel "entpacken"
Anzahl der Variablen muss Anzahl der Elemente im Tupel übereinstimmen, dann können alle drei Variablen
in einem Rutsch erstellt werden
"""
#name, age, subject = student

def get_student():
    return "Max Müller", 22, "Informatik"


# hier ist Student eine Liste mit Tupeln gefüllt!
student = [
    ("Max Müller", 22, "Informatik"),
    ("Horst Seehofer", 24, "Jura")
    ]

# ohne Zwischenvariable direkt 3 Variablen zum entpacken
for name2, age2, subject2 in student:
    print(name2)
    print(age2)
    print(subject2)


