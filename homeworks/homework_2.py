class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f'Привет, меня зовут {self.name}, я друг Байэля, я родился {self.birth_date}, по профессии {self.occupation}, высшее образование {self.higher_education}.')

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name
    def introduce(self):
        super().introduce()
        print(f'Наша группа имела название {self.group_name}')

classmate_Алмаз = Classmate("Алмаз", "25 февраля 1997 года", "учитель", "имеется", "62-1")
classmate_Ильяз = Classmate("Ильяз", "3 марта 1999 года", "экспедитор", "имеется", "62-1")

class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
    def introduce(self):
        super().introduce()
        print(f'Мое хобби это {self.hobby}')

Friend_Адилет = Friend("Адилет", "1 июля 1999 года", "предприниматель", "нет", "бильярд")
Friend_Мирбек = Friend("Мирбек", "20 августа 2000 года", "военный", "имеется", "стрельба из лука")

class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, shared_memory):
        super().__init__(name, birth_date, occupation, higher_education, hobby)
        self.shared_memory = shared_memory
    def introduce(self):
        super().introduce()
        print(f'У нас есть общее воспоминание о {self.shared_memory}')

bestFriend_Ринат = BestFriend("Ринат", "13 сентября 1999 года", "предприниматель", "имеется", "бильярд", "школьных днях")



people = [classmate_Алмаз, classmate_Ильяз, Friend_Адилет, Friend_Мирбек, bestFriend_Ринат]

for person in people:
    person.introduce()

