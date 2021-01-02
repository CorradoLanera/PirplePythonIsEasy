#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
main.py: Homework #9: Classes (Python Is Easy course by Pirple)

Details:

Create a class called "Vehicle" and methods that allow you to set the
"Make", "Model", "Year,", and "Weight".

The class should also contain a "NeedsMaintenance" boolean that defaults
to False, and and "TripsSinceMaintenance" Integer that defaults to 0.

Next an inheritance classes from Vehicle called "Cars".

The Cars class should contain a method called "Drive" that sets the state
of a boolean isDriving to True.  It should have another method called
"Stop" that sets the value of isDriving to false.

Switching isDriving from true to false should increment the
"TripsSinceMaintenance" counter. And when TripsSinceMaintenance exceeds
100, then the NeedsMaintenance boolean should be set to true.

Add a "Repair" method to either class that resets the
TripsSinceMaintenance to zero, and NeedsMaintenance to false.

Create 3 different cars, using your Cars class, and drive them all a
different number of times. Then print out their values for Make, Model,
Year, Weight, NeedsMaintenance, and TripsSinceMaintenance

Extra Credit:

Create a Planes class that is also an inheritance class from Vehicle.
Add methods to the Planes class for Flying and Landing (similar to
Driving and Stopping), but different in one respect: Once the
NeedsMaintenance boolean gets set to true, any attempt at flight should
be rejected (return false), and an error message should be printed
saying that the plane can't fly until it's repaired.



Turning it In:

Zip up your code files and attach them here to receive a grade and
continue with the course.

Submit your assignment
You may only submit one file with maximum 100 MB in size
"""

__author__ = "Corrado Lanera"
__credits__ = [
    "https://www.datacamp.com/community/tutorials/f-string-formatting-in-python"
]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Corrado Lanera"
__email__ = "corrado.lanera@gmail.com"


# --- MODULES ----------------------------------------------------------


# --- PROGRAM DEFINITIONS ----------------------------------------------
class Vehicle:
    def __init__(self):
        self.Make = None
        self.Model = None
        self.Year = None
        self.Weight = None
        self.NeedsMaintenance = False
        self.TripsSinceMaintenance = 0

    # setters
    def setMake(self, make):
        self.Make = make

    def setModel(self, model):
        self.Model = model

    def setYear(self, year):
        self.Year = year

    def setWeight(self, weight):
        self.Weight = weight

    # methods
    def Repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False

    # str
    def __str__(self):
        return f"""Vehicle:
    Make: {self.Make}
    Model: {self.Model}
    Year: {self.Year}
    Weight: {self.Weight}
    
    Trips since maintenance: {self.TripsSinceMaintenance}
    Needs maintenance: {self.NeedsMaintenance}
"""


class Cars(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.isDriving = False

    def Drive(self):
        self.isDriving = True

    def Stop(self):
        if self.isDriving is True:
            self.isDriving = False
            self.TripsSinceMaintenance += 1

        if self.TripsSinceMaintenance > 100:
            self.NeedsMaintenance = True


def ride(car):
    car.Drive()
    car.Stop()


def rideBy(car, times):
    for t in range(times):
        ride(car)
    print(f"Run {car.Make} {car.Model} for {times} rides.")

# --- PROGRAM INTERACTIONS ---------------------------------------------

if __name__ == '__main__':
    interact = True

    go_on = True
    while interact and go_on is True:
        # --- START OF THE CODE TO RUN ---

        # Fiat Punto
        punto = Cars()
        punto.setMake("Fiat")
        punto.setModel("Punto")
        punto.setYear("2000")
        punto.setWeight(1025)
        print(punto)
        rideBy(punto, 17)
        print(punto)

        # Opel Corsa
        corsa = Cars()
        corsa.setMake("Opel")
        corsa.setModel("Corsa")
        corsa.setYear("1997")
        corsa.setWeight(1055)
        print(corsa)
        rideBy(corsa, 35)
        print(corsa)

        # Citroen C3
        c3 = Cars()
        c3.setMake("Citroen")
        c3.setModel("C3")
        c3.setYear("2004")
        c3.setWeight(1055)
        print(c3)
        rideBy(c3, 135)
        print(c3)



        # --- END OF THE CODE TO RUN ---
        go = input(
            "Press Enter to continue the interactive simulation" +
            " (anything else will quit it). "
        )
        go_on = go == ""
