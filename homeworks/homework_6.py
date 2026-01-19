class Distance:
    conversion_dict = {"cm": 0.01,"m": 1,"km": 1000}

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"Distance = {self.value} {self.unit}"

    def convert(self):
        return self.value * Distance.conversion_dict.get(self.unit, 1)

    def __add__(self, other):
        total_meters = self.convert() + other.convert()
        return Distance(
            total_meters / Distance.conversion_dict[self.unit],
            self.unit
        )

    def __sub__(self, other):
        result_meters = self.convert() - other.convert()
        if result_meters < 0:
            raise ValueError("The range result cannot be negative")
        return Distance(
            result_meters / Distance.conversion_dict[self.unit],
            self.unit
        )
    def __eq__(self, other):
        return self.convert() == other.convert()

    def __lt__(self, other):
        return self.convert() < other.convert()

    def __gt__(self, other):
        return self.convert() > other.convert()


distanse_1 = Distance(10, "m")
distanse_2 = Distance(2, "km")
distanse_3 = Distance(500, "cm")
distanse_4 = Distance(1000, "cm")

print(distanse_1.value, distanse_1.unit)
print(distanse_2.value, distanse_2.unit)
print(Distance(10, "m"))
print(distanse_1 + distanse_2)
print(distanse_2 + distanse_1)
print(distanse_1 - distanse_3)
# print(distanse_3 - distanse_1)    # вариант с ValueError (работает)
print(distanse_1 == distanse_4)
print(distanse_2 > distanse_1)
print(distanse_1 < distanse_3)