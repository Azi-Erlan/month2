class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f'Hy my name is {self.name}, I was born on {self.birth_date}. I work as a {self.occupation}, and higher education is {self.higher_education}')

person_anna = Person('Anna', '21 oktober', 'manager', True)
person_johan = Person('Johan', '5 December', 'woodcutter', False)
person_adam = Person('Adam', '10 May', 'taxi driver', False )
print(person_anna.name)
print(person_anna.birth_date)
print(person_anna.occupation)
print(person_anna.higher_education)
person_anna.introduce()

print(person_johan.name)
print(person_johan.birth_date)
print(person_johan.occupation)
print(person_johan.higher_education)
person_johan.introduce()

print(person_adam.name)
print(person_adam.birth_date)
print(person_adam.occupation)
print(person_adam.higher_education)
person_adam.introduce()
