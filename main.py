# coding: utf-8
from washing_machine import WashingMachine

__author__ = 'Eric-Nicolas'


def main() -> None:
    print("Opening the machine")

    laundry_quantity = 0
    while laundry_quantity == 0:
        laundry_quantity = input("Enter the quantity of laundry you want to wash: ")
        try:
            laundry_quantity = int(laundry_quantity)
            if laundry_quantity < 0:
                raise ValueError
        except ValueError:
            print("Please enter a positive number!")
            laundry_quantity = 0

    machine = WashingMachine()
    number_of_machines = 0
    machine_capacity = 0
    while machine_capacity < laundry_quantity:
        machine_capacity += machine.capacity
        number_of_machines += 1

    print("You will need " + str(number_of_machines) + " washing machines to wash your laundry!")
    print("About " + str(number_of_machines * machine.water_consumption) + " L of water will be consumed.")


if __name__ == '__main__':
    main()
