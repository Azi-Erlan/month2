class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print('возраст не может быть отрицательным')

    def make_sound(self):
        print('Животное издает звук')

class Dog(Animal):
    def make_sound(self):
        print('Собака лает: Гав гав!')

class Cat(Animal):
    def make_sound(self):
        print('Кошка издает звук:Мяяяяяу')

dog = Dog('Рекс', 5)
cat = Cat('Пушок', 6)

print(dog.name, dog.age)
print(cat.name, cat.age)

dog.name = 'Мухтар'
dog.age = 4

cat.name = 'Снежок'
cat.age = 3

print(dog.name, dog.age)
print(cat.name, cat.age)
