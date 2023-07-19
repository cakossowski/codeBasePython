class Car:

    def __init__(self, brand, model, manufacturing_year, color, travel_distance_max):
        self.brand = brand
        self.model = model
        self.manufacturing_year = manufacturing_year
        self.color = color
        self.travel_distance_max = travel_distance_max
        self.original_travel_distance = travel_distance_max

    def drive_around(self, distance):
        self.travel_distance_max -= distance
        print(f'The car travelled for {distance} miles and can go on for {self.travel_distance_max} miles more.')

    def fill_gas(self):
        self.travel_distance_max = self.original_travel_distance
        print(f'The car has been refueled and can go on for {self.travel_distance_max} miles, once more!')


test = Car("audi", "a4", 1992, "blue", 1000)

test.drive_around(500)
test.fill_gas()
print(test.travel_distance_max)

