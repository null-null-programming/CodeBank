class Person:
    def __init__(self, family_name, first_name):
        self.family_name = family_name
        self.first_name = first_name
    
    def get_full_name(self):
        return "{} {}".format(self.family_name, self.first_name)

person = Person("Tanaka", "Ichirou")
print(person.get_full_name())

class WesternPerson(Person):
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.family_name)

western_person = WesternPerson("Tanaka", "Ichiro")
print(western_person.get_full_name())