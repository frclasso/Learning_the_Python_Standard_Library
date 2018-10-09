#!/usr/bin/env python3


class Car:
    pass


class Truck(Car):  # Truck herda de Car
    pass


# instanciando objetos
c = Car()
t = Truck()
print(type(c))
print(type(t))
print(type(c) == type(t)) # retorna False, objetos diferentes

convert = Car()
print(type(c) == type(convert)) # retorna verdadeiro

# isinstance
print(isinstance(c, Car))  # isinstance(objeto, classe)
print(isinstance(t, Truck))
print(isinstance(t, Car)) # retorna True pois Truck herda de Car


r = range(0, 30)
if isinstance(r, range):
    print(list(r))