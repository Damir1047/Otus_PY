from abc import ABC
from homework_02 import exceptions

class Vehicle(ABC):

    def __init__(self, weight, fuel, fuel_consumption, started=False):
        self.weight = 60
        self.started = False
        self.fuel = 200
        self.fuel_consumption = 8

    def start(self):
        if self.started == False:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance):
        rashod_topliva = distance*self.fuel_consumption
        if rashod_topliva > self.fuel:
            raise exceptions.NotEnoughFuel
        else:
            self.fuel = self.fuel - rashod_topliva

