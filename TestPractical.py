# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 14:24:18 2022

@author: Lata
"""

from Agent import Action, Agent
from datetime import datetime
from enum import Enum, IntEnum

print("Enter the number of the action you were doing 1 up to 9")
actionEnum= int(input("Enter: "))
testAgent= Agent(Action(actionEnum))

d1 = datetime(year = 2020, month = 2, day = 25, hour = 15, minute = 55, second = 59)
print(testAgent.sense_world(d1, False))

print("My shcedule for the day is exactly at : " + str(d1))

print(testAgent.perform_action())
