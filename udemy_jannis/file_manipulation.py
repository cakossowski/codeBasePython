
"""
Pfad einfach mit Rechtsklick in PyCharm kopieren lassen, falls Pfad nicht ganz bekannt ist
Parameter 'r' - read / 'w' - write / 'a' - append
w läuft von Anfang an durch und überschreibt alles
a hängt die Daten aber an, statt bisheriges zu überschreiben
"""
file = open("/home/alex/PycharmProjects/codeBasePython/data_manipulation/lesen.txt", "r")
for line in file:

    """ 
    .strip() sorgt dafür, dass der Zeilenumbruch \n in Dateien entfernt wird und 
    Python alle Zeilen ohne Zwischenzeile druckt
    """
    print(line.strip())
file.close()

file = open("/home/alex/PycharmProjects/codeBasePython/data_manipulation/schreiben.txt", "w")
file.write("Das ist ein TEST zum beschreiben \n")

studenten = ['Alex', 'Horst', 'Achim']

for student in studenten:
    file.write(student + '\n')

print('File has been written')
file.close()


"""
WICHTIG! Files am besten wie folgend aufgeführt öffnen, damit Dateien bei Fehlern im Codeblock automatisch
geschlossen werden!

Und Datei kann nur innerhalb des "with" Blocks beabreitet werden!
"""

with open('/home/alex/PycharmProjects/codeBasePython/data_manipulation/schreiben.txt', 'r') as file:
    # irgendwelche Anweisungen mit indent
    for line in file:
        print(line.strip())

