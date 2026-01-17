class Car:
    # инициализатор(конструктор)
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self._fined = False
        self.__max_speed = 0

    def drive_to(self, destination):
        self._test()
        print(self._fined)
        print(self.__max_speed)
        print(f'Car {self.model} driving to', destination)

    def _test(self):
        print(f'Car {self.color}')

    # геттер
    def get_max_speed(self):
        return self.__max_speed

    #сеттер
    def set_max_speed(self, value):
        if value <= 0:
            raise ValueError("max_speed must be positive")
        self.__max_speed = value

    @property   # это геттер
    def max_speed(self):
        return self.get_max_speed()
    @max_speed.setter   # это сеттер
    def max_speed(self, value):
        if value <= 0:
            raise ValueError("max_speed must be positive")
        self.__max_speed = value


car_subaru = Car("Subaru", "red")
print(car_subaru.color)
car_subaru.drive_to("Karakol")
print(car_subaru._fined)
# print(car_subaru.__max_speed) # error
print(car_subaru._Car__max_speed) # только для тестов
print(car_subaru.get_max_speed())
car_subaru.set_max_speed(100)
print(car_subaru.get_max_speed())

print(car_subaru.max_speed)
car_subaru.max_speed = 120
print(car_subaru.max_speed)