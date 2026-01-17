class Car:
    # инициализатор(конструктор)
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def drive_to(self, destination):
        print(f'Car {self.model} driving to', {destination})

    def change_color(self, nev_color):
        self.color = nev_color
car_mercedes_bens = Car("mybach", "black")
car_subaru = Car("Subaru", "red")
print(car_subaru)
print(car_subaru.model)
print(car_subaru.color)
print(type(car_subaru))
print(car_mercedes_bens.model)
print(car_mercedes_bens.color)
car_mercedes_bens.drive_to('Karakol')
