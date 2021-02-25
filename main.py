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
    number_of_machines = laundry_quantity // machine.capacity

    if number_of_machines * machine.capacity < laundry_quantity:
        number_of_machines += 1

    print("You will need " + str(number_of_machines) + " washing machines to wash your laundry!")
    print("About " + str(number_of_machines * machine.water_consumption) + " L of water will be consumed.")


if __name__ == '__main__':
    main()
