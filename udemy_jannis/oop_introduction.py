class Student():

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.term = 1

    def increase_term(self):
        if self.term >= 9:
            print("Höchststudiendauer bereits erreicht!")
            return
        self.term = self.term + 1

    def name(self):
        print(self.firstname + " " + self.lastname + " (Semester: " + str(self.term) + ")")


"""
# _variablenname - ein Unterstrich ist Konvention, das auf Variable nicht von außen zugegriffen werden soll
# keine "harte" Konvention, technisch trotzdem möglich, aber besser zu vermeiden!

bei 2 __variablenname allerdings wird auf "privat" geschalten und es passiert nichts
"""

erik = Student("Erik", "Mustermann")
erik.increase_term()
erik.name()
