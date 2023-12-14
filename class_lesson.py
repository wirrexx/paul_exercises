class personalData:
    def __init__(self, fname, lname, country):
        self.firstname = fname
        self.lastname = lname
        self.country = country

    def printPersonalData(self):
        print(
            f"Personal data: {self.firstname} {self.lastname} from {self.country}")


class sensitiveData(personalData):
    def __init__(self, fname, lname, country, geneticCode):
        super().__init__(fname, lname, country)
        self.dna = geneticCode

    def printPersonalDataNew(self):
        print(
            f"Personal data: {self.firstname} {self.lastname} from {self.country} and my DNA: {self.dna}")


person1 = personalData('Wisam', 'Odish', 'Sweden')
person1 = sensitiveData('Wisam', 'Odish', 'Sweden', 'XCUSs')
person1.printPersonalData()
person1.printPersonalDataNew()


class GrandParent:
    def print(self):
        print('I am a Grandparent')


class ParentA(GrandParent):
    def print(self):
        print('I am parent A')


class ParentB(GrandParent):
    def print(self):
        print('I am parent B')


class childA(ParentA, ParentB):
    pass


child = childA()
child.print()
