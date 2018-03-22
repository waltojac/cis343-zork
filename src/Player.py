'''
Created on Mar 16, 2018

@author: jacobwalton
'''
from random import randint, choice
from Objects import HersheyKiss, SourStraw, ChocolateBar, NerdBomb

class Player(object):

    """ Constructor """
    def __init__(self):
        self.attack = randint(10,20)
        self.hp = randint(100,125)
        self.hp = 1000
        
        #add weapons to inventory randomly
        self.weapons = [HersheyKiss()]
        weaponChoices = [SourStraw, ChocolateBar, NerdBomb]
        for i in range(9):
            self.weapons.append(choice(weaponChoices)())
        
    #attack function to attack all monsters in home  
    def attackNPC(self, home):
        
        flag = True
        options = []
        names = []
        
        #make a unique weapons list for viewing
        for each in self.weapons:
            if each.name not in names:
                names.append(each.name)
                options.append(each)
                
        options.sort()
        
        z = 0
        
        #grab a valid weapon
        while (flag):
            for j in range(len(options)):
                print(str(j) + " - " + str(options[j].name))
        
            z = raw_input("Pick a weapon:")
            try:
                z = int(z)
            except ValueError:
                print("That's not an int!")
                z = 10
            if (z < (len(options)) and z >= 0 and isinstance(z, int)):
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
            #TODO Iterator
            for x in home.occupants:
                x.defend(self.weapons[i], self)
                
            #decrease uses
            self.weapons[i].uses -= 1
            if self.weapons[i].uses == 0:
                print (str(self.weapons[i].name) + " is out of uses!")
                self.weapons.pop(i)
    
    #defend from all monsters in home
    def defend(self, home):
        totalLoss = 0
        for monster in home.occupants:
            totalLoss += monster.attack
        
        self.hp -= totalLoss
        if (self.hp < 0):
            print
            print("You were overcome by the monsters. Better luck next time!")
            print("Game over.")
            exit(0)
            
        