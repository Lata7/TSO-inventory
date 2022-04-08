from datetime import datetime
from enum import Enum, IntEnum

class Action(IntEnum):
    Breakfast = 1
    Lunch = 2
    Dinner = 3
    Sleep = 4
    Gym = 5
    Class = 6
    Church = 7
    Television = 8
    River = 9

class Agent: #agent class

  def __init__(self, initialstate):
       self.state = initialstate
       pass

  def sense_world(self, dt, sick):
    
        return self.state

  def perform_action(self): #actions performed by Lata
        if self.state == Action.Lunch:
    
            return "I am eating lunch"
        
        elif self.state == Action.Breakfast:
                                                
            return "I am eating breakfast"
        
        elif self.state == Action.Dinner:
            
            return "I am busy eating dinner"
        
        elif self.state == Action.Sleep:
            
            return "I am asleep don't wake me up"
        
        elif self.state == Action.Gym:
            
            return "I am busy in a workout"
        
        elif self.state == Action.Class:
            
            return "I am in AI class"
        
        elif self.state == Action.Church:
            
            return "I am at Church praying"
        
        elif self.state == Action.Television:
            
            return "I am appearing on the television come look"
        
        elif self.state == Action.River:
            
            return "I am at the River"
            
        