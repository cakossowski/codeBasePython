"""

Listen ineinander verschachteln und mit dict kombinieren

"""

# WICHTIG! Trenne die Listen auch mit einem Komma ab
liste = [
    ["Max", "Ulli", "Detlef"],
    ["Monika", "Beate", "Leonora"]
]

# Ausgabe des 1. Elements, der 1. Liste
print(liste[0][0])


# Listen in Dict

student = {
    "Informatik": ["Max", "Bill", "Joachim"],
    "BWL": ["Madlene", "Jan", "Paul"]
}

print(student["Informatik"])
