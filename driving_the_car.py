import random

import pandas as pd


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

    def distance_left(self):
        expect_distance = self.fuel / (self.economy / 100)
        return expect_distance

    def fuel_up(self):
        self.fuel += 20
        return self.fuel


list_models = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
list_colors = ["black", "white", "red", "green", "blue"]
list_economy = list(range(9, 16))

list_drive = []
list_cars = []

i = 1
for i in range(1, 11):
    model_car = random.choice(list_models)
    list_cars.append(model_car)
    i += 1

print(list_cars)

for j in list_cars:
    car_color = random.choice(list_colors)
    car_economy = random.choice(list_economy)
    car_2 = Car(j, car_color, car_economy)
    print(f"Car: {car_2.model}, color: {car_2.color}, economy: {car_2.economy} l/100km, mileage: {car_2.mileage} km, "
          f"fuel: {car_2.fuel} l")
    print(f"The car drove {car_2.drive(200)} km")
    print(f"Left distance", round(car_2.distance_left(), 0))
    print(f"The car was filled with 20 l. Liters in tank after refueling {car_2.fuel_up()} l")
    print(f"Distance after refuel", round(car_2.distance_left(), 0))
    print(f"The car drove another 100 km. Total distance - {car_2.drive(100)} km")
    print(f"Fuel left after drive - {car_2.fuel} l")
    list_drive.append([[car_2.model], [car_2.color], [car_2.economy], [car_2.mileage], [car_2.fuel]])

print(list_drive)

df = pd.DataFrame(list_drive)
print(df)
max_fuel = df[4].max()
# max_fuel = df[df['fuel'] == df['fuel'].max()]
print(f"Maximum amount of fuel remaining after drive: {max_fuel} l")
