# -*- coding: utf-8 -*-

"""
main.py: Homework #1: Variables (Python Is Easy course by Pirple)

What's your favorite song?

Think of all the attributes that you could use to describe that song.
That is: all of it's details or "meta-data".
These are attributes like "Artist", "Year Released", "Genre",
"Duration", etc. Think of as many different characteristics as you can.

In your text editor, create an empty file and name it main.py

Now, within that file, list all of the attributes of the song, one after
another, by creating variables for each attribute, and giving each
variable a value.

Give each variable its own line. Then, after you have listed the
variables, print each one of them out.

For extra credit, add comments to your code, that explain the different
attributes. Also add a title to the top of your file explaining what the
file is, and what it's for.

Take your code file(s) and save them with the ".py" extension.
Then, place those file(s) in a folder, and create a .zip file out of the
entire folder. Attach the zip file here to receive a grade and continue
with the course.

Submit your assignment
You may only submit one file with maximum 100 MB in size
"""

__author__ = "Corrado Lanera"
__credits__ = "https://stackoverflow.com/questions/1523427/what-is-the-common-header-format-of-python-files"
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Corrado Lanera"
__email__ = "corrado.lanera@gmail.com"

# ----------------------------------------------------------------------

Title = "November Rain"
Year = 1992
Month = 2
Day = 18
Artist = "Guns N' Roses"
Text = "Axl Rose"
Album = "Use Your Illusion I"
Genre = "Hard Rock"
Awards = "MTV Video Music Award for Best Cinematography"
DurationInSecondsAlbum = 537
DurationInSecondsRadio = 283
Platinum = 5
Gold = 4
Wiki = "https://en.wikipedia.org/wiki/November_Rain"

print("Title:", Title)
print("Year:", Year)
print("Month:", Month)
print("Day:", Day)
print("Artist:", Artist)
print("Text:", Text)
print("Album:", Album)
print("Genre:", Genre)
print("Awards:", Awards)
print("Album version duration (s):", DurationInSecondsAlbum)
print("Radio version duration (s):", DurationInSecondsRadio)
print("Platinum discs:", Platinum)
print("Gold disc:", Gold)
print("Info source:", Wiki)
