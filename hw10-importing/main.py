#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
main.py: Homework #10: Importing (Python Is Easy course by Pirple)

"""

__author__ = "Corrado Lanera"
__credits__ = []
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Corrado Lanera"
__email__ = "corrado.lanera@gmail.com"


# --- MODULES ----------------------------------------------------------


# --- PROGRAM DEFINITIONS ----------------------------------------------

class Foo:
    def __init__(self):
        None


# --- PROGRAM INTERACTIONS ---------------------------------------------

if __name__ == '__main__':
    interact = False

    go_on = True
    while interact and go_on is True:
        # --- START OF THE CODE TO RUN ---

        # --- END OF THE CODE TO RUN ---
        go = input(
            "Press Enter to continue the interactive simulation" +
            " (anything else will quit it). "
        )
        go_on = go == ""
