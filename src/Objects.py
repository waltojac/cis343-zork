'''
Created on Mar 16, 2018

@author: jacobwalton
'''
from observable_pattern import Observable
from observable_pattern import Observer
from numpy.oldnumeric.random_array import uniform
from random import randint, choice
from NPC import Person, Zombie, Vampire, Ghoul, Werewolve

class Neighborhood(Observer):
    ''' classdocs '''

    ''' Constructor '''
    def __init__(self, width, height):
        self.numMonsters = 0
        Observer.__init__(self)
        self.grid = [[House() for x in range(width)] for y in range(height)]
        for l in self.grid:
            for h in l:
                h.add_observer(self)
                self.numMonsters += h.numMonsters
                
    def updateObserver(self, object):
        self.numMonsters -= 1
            
        
class House(Observable, Observer):

    def __init__(self):
        #make observable and observer
        Observable.__init__(self)
        Observer.__init__(self)
        
        self.occupants = []
        self.numMonsters = 0
        
        #list of NPCS for randomization
        options = [Person, Zombie, Vampire, Ghoul, Werewolve]
        
        #add NPCS to house
        for i in range(randint(0,10)):
            op = choice(options)
            if (op != Person):
                self.numMonsters += 1
            tmp = op()
            Observable.add_observer(tmp, self)
            self.occupants.append(tmp)
            
    def updateObserver(self, object):
        self.occupants.remove(object)
        self.occupants.append(Person())
        self.numMonsters -= 1
        Observable.update(self)
        
    

class Weapon(object):

    def __init__(self, wName, fAttack, nUses):
        self.name = wName
        self.attack = fAttack
        self.uses = nUses
        
class HersheyKiss(Weapon):
    def __init__(self):
        Weapon.__init__(self, "hersheyKiss", 1, float('inf'))
        
class SourStraw(Weapon):
    def __init__(self):
        Weapon.__init__(self, "sourStraw", uniform(1.0, 1.75) , 2)
        
class ChocolateBar(Weapon):
    def __init__(self):
        Weapon.__init__(self, "chocolateBar", uniform(2, 2.4), 4)
        
class NerdBomb(Weapon):
    def __init__(self):
        Weapon.__init__(self, "nerdBomb", uniform(3.5, 5), 1)

        