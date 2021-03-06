'''
Created on Mar 16, 2018
Title: NPC.py
Description: Class of a monsters used in Zork.
@author: jacobwalton
'''
from observable_pattern import Observable
from random import randint
from abc import abstractmethod

class NPC(Observable): 
    
    ''' Constructor '''
    def __init__(self, healthPoint, attackStrength):
        Observable.__init__(self)
        self.hp = healthPoint
        self.attack = attackStrength
        
    @abstractmethod
    def defend(self, weapon, player):
        pass
        
      
''' Person class.'''
class Person(NPC):
    name = "Person"
    def __init__(self):
        NPC.__init__(self, 100, -1)
    def defend(self, weapon, player):
        pass


''' Zombie class.'''
class Zombie(NPC):
    name = "Zombie"
    def __init__(self):
        healthPoint = randint(50,100)
        attackStrength = randint(0,10)
        NPC.__init__(self, healthPoint, attackStrength)
    
    #defense function. 2x for sourStraws
    def defend(self, weapon, player):
        if (weapon.name == "sourStraw"):
            self.hp = self.hp - (2 * weapon.attack * player.attack)
        else:
            self.hp = self.hp - (weapon.attack * player.attack)
        if (self.hp <= 0):
            print("Zombie defeated!")
            Observable.update(self)

''' Vampire class.'''
class Vampire(NPC):
    name = "Vampire"
    def __init__(self):
        healthPoint = randint(100,200)
        attackStrength = randint(10,20)
        NPC.__init__(self, healthPoint, attackStrength)
    
    #defense function
    def defend(self, weapon, player):
        if (weapon.name != "chocolateBar"):
            self.hp = self.hp - (weapon.attack * player.attack)
        if (self.hp <= 0):
            print("Vampire defeated!")
            Observable.update(self)
            
''' Ghoul class.'''
class Ghoul(NPC):
    name = "Ghoul"
    def __init__(self):
        healthPoint = randint(40,80)
        attackStrength = randint(15,30)
        NPC.__init__(self, healthPoint, attackStrength)
    
    #defense function
    def defend(self, weapon, player):
        if (weapon.name == "nerdBomb"):
            self.hp = self.hp - (5 * weapon.attack * player.attack)
        else:
            self.hp = self.hp - (weapon.attack * player.attack)
        if (self.hp <= 0):
            print("Ghoul defeated!")
            Observable.update(self)
            
''' Werewolve class.'''        
class Werewolve(NPC):
    name = "Werewolve"
    def __init__(self):
        healthPoint = 200
        attackStrength = randint(0,40)
        NPC.__init__(self, healthPoint, attackStrength)
        
    #defense function
    def defend(self, weapon, player):
        if ((weapon.name != "chocolateBar") and (weapon.name != "sourStraw")):
            self.hp = self.hp - (weapon.attack * player.attack)
            
        #if they are defeated and ready to be a human
        if (self.hp <= 0):
            print("Werewolve defeated!")
            Observable.update(self)




