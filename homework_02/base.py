from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    pass
    default_weight = 1500
    default_fuel = 200
    default_fuel_consumption = 25

    def __init__(self, weight, fuel, fuel_consumption, started=False):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started == False:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance):
        rashod_topliva = distance * self.fuel_consumption
        if rashod_topliva > self.fuel:
            raise exceptions.NotEnoughFuel
        else:
            self.fuel = self.fuel - rashod_topliva
