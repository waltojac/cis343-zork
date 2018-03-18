'''
Created on Mar 16, 2018

@author: jacobwalton
'''
from random import randint, choice
from Objects import HersheyKiss, SourStraw, ChocolateBar, NerdBomb
from scipy.stats.distributions import randint_gen
from observable_pattern import Observable

class Player(object):
    '''
    classdocs
    '''

    def __init__(self):
        self.attack = randint(10,20)
        self.hp = randint(100,125)
        self.weapons = [HersheyKiss()]
        weaponChoices = [SourStraw, ChocolateBar, NerdBomb]
        for i in range(9):
            self.weapons.append(choice(weaponChoices)())
            
    def attackNPC(self, home):
        
        flag = True
        #options = list(set(self.weapons))
        options = []
        names = []
        for each in self.weapons:
            if each.name not in names:
                names.append(each.name)
                options.append(each)
                
        options.sort()
        
        z = 0
        
        while (flag):
            for j in range(len(options)):
                print(str(j) + " - " + str(options[j].name))
        
            z = int(input("Pick a weapon:"))
            if (z < (len(options)) and z >= 0):
                flag = False
                break
            else:
                print("\nPlease enter a vaild weapon choice as an int.")
        
        i = 0
        for i in range(len(self.weapons)):
            if self.weapons[i].name == options[z].name:
                break
        #print("i = " + str(i))
                
        
        #print(str(self.weapons[i]))
        
        #attack each occupant
        if len(home.occupants) != 0:
            for x in range(len(home.occupants)):
                home.occupants[x].defend(self.weapons[i], self)
                
            #decrease uses
            self.weapons[i].uses -= 1
            if self.weapons[i].uses == 0:
                print (str(self.weapons[i].name) + " is out of uses!")
                self.weapons.pop(i)
        
        
            
        