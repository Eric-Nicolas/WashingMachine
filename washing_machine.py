# coding: utf-8

__author__ = 'Eric-Nicolas'


class WashingMachine:
    def __init__(self) -> None:
        self._capacity = 8  # in kg.
        self._spinning_speed = 1400  # in laps/min.
        self._full_wash_time = 35  # in min.
        self._WATER_CONSUMPTION = 60  # in L

    @property
    def capacity(self):
        return self._capacity
    
    @property
    def spinning_speed(self):
        return self._spinning_speed

    @property
    def full_wash_time(self):
        return self._full_wash_time
    
    @property
    def water_consumption(self):
        return self._WATER_CONSUMPTION
