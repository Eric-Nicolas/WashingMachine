# coding: utf-8
import time
import os

__author__ = 'Eric-Nicolas'


class WashingMachine:
    def __init__(self) -> None:
        self._capacity = 8  # in kg.
        self._spinning_speed = 1400  # in laps/min.
        self._full_wash_time = 35  # in min.
        self._WATER_CONSUMPTION = 60  # in L

    @property
    def capacity(self) -> int:
        return self._capacity
    
    @property
    def spinning_speed(self) -> int:
        return self._spinning_speed

    @property
    def full_wash_time(self) -> int:
        return self._full_wash_time
    
    @property
    def water_consumption(self) -> int:
        return self._WATER_CONSUMPTION

    def start(self, weight) -> None:
        pass
