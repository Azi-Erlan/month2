#родительский, суперкласс
class Car:
    # инициализатор(конструктор)
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.speed = 0

    def drive_to(self, destination):
        print(f'Car {self.model} driving to', {destination})

#дочерний, подкласс
class Bus(Car):
    def __init__(self, model, color, number):
        super().__init__(model, color)
        self.number = number
    def drive_to(self, destination):
       super()
       print(f'Bus {self.model} driving to', destination)

bus_42 = Bus('Ikarus', 'green')
print(bus_42.number)
print(bus_42.speed)
bus_42.drive_to('Bishkek')