# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 15:02:25 2020

@author: Joana  Teye
"""

"""
Project: Character Input
Description: This project asks for the age and name of a user and returns the year they will
turn 100 years old
"""

name = input('please enter your name: ')
age = input('please enter your age: ')
while age.isdigit() == False:
    age = input('Please enter your age in numbers: ')
#year represents the year the user will turn 100 years old
age=int(age)
BirthYear = 2020-age
year = BirthYear+100
print(name + ', you will be 100 years old in the year, ' + str(year))


