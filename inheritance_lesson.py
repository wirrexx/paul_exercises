# Inheritance, vad är det exakt? Ett verktyg att skapa klasser.
# Hur använder man det? Idén bakom det, är friheten att designa klasser, genom att låna från andra klasser.
# När använder man det?

# Person:, namn, adress, ålder, sex
# Anställd:, vad kan jag låna från Person klassen till anställda klassen, t.ex. namn, adress, ålder, sex osv.
# Anställd:, kan ha t.ex. arbetsdagar och semester

class Person:  # Parent klassen
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def get_full_name(self):
        return f"Hello {self.f_name} {self.l_name}, Welcome to Valve"


class Employee(Person):  # Kallar på Parent klassen, det här är inheritance
    def get_full_name(self):
        return f"Hello {self.l_name} {self.f_name}, Welcome to Valve"


mike = Person('Mike', 'Doe')
print(mike.get_full_name())

wisam = Employee('Wisam', 'Odish')

print(wisam.f_name)
print(wisam.get_full_name())
