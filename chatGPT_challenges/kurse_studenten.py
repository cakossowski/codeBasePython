class Studenten:

    def __init__(self, name, alter, matrikel):
        self.name = name
        self.alter = alter
        self.matrikel = matrikel

    def information_student(self):
        return f'Name: {self.name}, Matrikel: {self.matrikel}'


class Kurs:

    def __init__(self, kursname, kursnummer):
        self.kursname = kursname
        self.kursnummer = kursnummer
        self.studentenliste = []

    def hinzufuegen_student(self, student):
        self.studentenliste.append(student)

    def entfernen_student(self, gesuchte_matrikel):
        for student in self.studentenliste:
            if student.matrikel == gesuchte_matrikel:
                self.studentenliste.remove(student)
                return
        print('Student nicht gefunden')

    def ausgeben_studentenliste(self):
        for student in self.studentenliste:
            print(student.information_student())


student1 = Studenten("Max Horstmann", 20, "12345")
kurs1 = Kurs("Python", "PY101")

kurs1.hinzufuegen_student(student1)
kurs1.ausgeben_studentenliste()
