class Person:
    family_name = "Yamada"
    first_name = "Tarou"
    
    def get_full_name(self):
        return "{} {}".format(self.family_name, self.first_name)

person = Person()
print(person.get_full_name())