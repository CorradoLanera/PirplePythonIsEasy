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
__credits__ = []
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Corrado Lanera"
__email__ = "corrado.lanera@gmail.com"


# --- MODULES ----------------------------------------------------------


# --- PROGRAM DEFINITIONS ----------------------------------------------
class Veicle:
    def __init__(self):
        None


# --- PROGRAM INTERACTIONS ---------------------------------------------

if __name__ == '__main__':
    interact = True

    go_on = True
    while go_on is True:
        # --- START OF THE CODE TO RUN ---
        # --- END OF THE CODE TO RUN ---
        go = input(
            "Press Enter to continue the interactive simulation" +
            " (anything else will quit it). "
        )
        go_on = go == ""
