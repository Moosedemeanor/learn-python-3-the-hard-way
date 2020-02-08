# sets variable 'cars' to int 100
cars = 100
# sets variable 'space_in_a_car' to floating point 4.0
space_in_a_car = 4.0
# sets variable 'drivers' to int 30
drivers = 30
# sets variable 'passengers' to int 90
passengers = 90
# sets variable 'cars_not_driven' to cars (100) - drivers (30)
cars_not_driven = cars - drivers
# sets varialbe 'cars_driven' to the amount of 'drivers'
cars_driven = drivers
# sets variable "carpool_capacity" to the number of cars driven times spaces
# in a car
carpool_capacity = cars_driven * space_in_a_car
# sets variable "average_passengers_per_car" to the number of passengers
# divided by the number of spaces availavle in a car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
    "in each car.")
