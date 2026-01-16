class Animal:
    def move(self):
        print('двигается')

class Swimming(Animal):
    def move(self):
        super().move()
        print('плавает')

class Flying(Animal):
    def move(self):
        super().move()
        print('летает')

class Duck(Swimming,Flying):
    def move(self):
        super().move()
        print('летает и плавает')

# MRO = metod resolution order
print(Duck.__mro__)
duck = Duck()
duck.move()
print("================")
print(Swimming.__mro__)
animal = Swimming()
animal.move()


