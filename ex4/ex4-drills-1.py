# -*- coding: utf-8 -*-
# 
# Learn Python the Hard Way, 3rd Edition
# Exercise 4: Variables and Names
#
# Study Drills: Write comments above each of the variable assignments.

# Total number of available cars
cars = 100

# The capacity for passenger in a car (in person/car)
space_in_a_car = 4.0

# Total number of available drivers
drivers = 30

# Total number of available passengers
passengers = 90

# Total number of cars without driver
cars_not_driven = cars - drivers

# Total car with driver
cars_driven = drivers

# Total number of passengers can be carried in the carpool
carpool_capacity = cars_driven * space_in_a_car

# Average number of passenger need to be carried per car
average_passengers_per_car = passengers // cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
