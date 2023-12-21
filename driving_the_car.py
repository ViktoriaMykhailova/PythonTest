import random


class Car:

    def __init__(self, model, color, economy, mileage: int = 0, fuel: int = 100):
        self.mileage = mileage
        self.fuel = fuel
        self.economy = economy
        self.color = color
        self.model = model

    def drive(self, distance):
        if distance * self.economy / 100 > self.fuel:
            print("Error: not enough fuel")
        else:
            self.mileage += distance
            self.fuel = self.fuel - (distance * self.economy / 100)
            return self.mileage

    def get_distance_left(self):
        expect_distance = self.fuel / (self.economy / 100)
        return round(expect_distance, 0)

    def fuel_up(self):
        self.fuel += 20
        return self.fuel


list_models = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
list_colors = ["black", "white", "red", "green", "blue"]
list_economy = list(range(9, 16))

list_drive = []
list_cars = []

for _ in range(1, 11):
    model_car = random.choice(list_models)
    list_cars.append(model_car)

for j in list_cars:
    car_color = random.choice(list_colors)
    car_economy = random.choice(list_economy)
    car_1 = Car(j, car_color, car_economy)
    car_1.drive(200)
    car_1.fuel_up()
    car_1.drive(100)
    list_drive.append(car_1)

max_fuel_car = None
max_distance_left = 0

for car in list_drive:
    distance_left = car.get_distance_left()
    if max_distance_left > distance_left:
        max_distance_left = distance_left
    max_fuel_car = car

print(max_fuel_car.model, max_fuel_car.color, max_fuel_car.economy, max_fuel_car.mileage, max_fuel_car.fuel)
