"""

[C]omma [S]eperated [V]alue
Datei muss dabei inhaltlich so aussehen:

sdfsdfsdf;sdfsdfsdf;123123123;1515155

Jede Zeile ist eine Zeile in der Tabelle, alles durch ; abgetrennt eine Spalte.
In diesem Format kann die Datei auch in Excel geöffnet werden und wird korrekt angezeigt!

"""

with open('/home/alex/PycharmProjects/codeBasePython/data_manipulation/csv.txt') as file:
    for line in file:
        # nach .strip ist es immer noch eine Zeichenkette, also funktioniert .split() auch!
        data = line.strip().split(';')
        # Filtern nach Spalte 3
        if data[2] == 'BER' or data[2] == 'BUD':
            print(data)

        """
        Filtern nach Zahl, das Continue in Kombination mit der Condition überspringt die Zeilen 
        einfach und führt erst zum Schluss den gewünschten Befehl aus
        """
        if int(data[1]) < 20:
            continue

        print(data)
