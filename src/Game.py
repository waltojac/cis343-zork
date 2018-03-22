'''
Created on Mar 16, 2018

@author: jacobwalton
'''
from Objects import Neighborhood
from Player import Player
import time

class Game(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.height = 0
        self.width = 0
        
        #grab and set the width. Checks for valid input
        flag = True
        while(flag):
            self.width = raw_input("Please enter the WIDTH of the neighborhood: ")
            try:
                self.width = int(self.width)
                flag = False
            except ValueError:
                print("That's not an int!")
                
        #grab and set the height. Checks for valid input
        flag = True  
        while(flag):
            self.height = raw_input("Please enter the HEIGHT of the neighborhood: ")
            try:
                self.height = int(self.height)
                flag = False
            except ValueError:
                print("That's not an int!")
            
        #create a neighborhood and player
        self.neighborhood = Neighborhood(self.width, self.height)
        self.player = Player()
    
def main():
    ''' ''' 
    #initialize the game
    game = Game()
    n = game.neighborhood
    p = game.player
    
    #instructions
    print("--- Welcome to the world of Zork ---")
    print
    print("You woke up from being chocolate wasted on your Halloween candy last")
    print("night only to find your entire neighborhood has turned into monsters,")
    print("except for those that were immune. Your task is to use the candy in your")
    print("bag to turn those monsters back into your friendly neighbors.")
    print
    time.sleep(4)
    #show the inventory
    print("Inventory: ")
    for wep in p.weapons:
        print("Name: " + str(wep.name) + "   \tUses: " + str(wep.uses))
    print
    time.sleep(2)
    #show the stats
    print("Your Attack Strength: " + str(p.attack))
    print("Your Health Points: " + str(p.hp))
    print("Number of Monsters in the Neighborhood: " + str(n.numMonsters))
    print
    print("Go to each house in the neighborhood, and turn all the monsters back")
    print("into humans! Good luck!")
    time.sleep(2)
    
    
    #main game loop
    while(True):
        print
        nStr = ""
        count = 1
        
        #print the neighborhood
        for i in n.grid:
            for h in i:
                nStr += "House " + str(count) +" (" + str(h.numMonsters) + " mon)\t |   "
                count += 1
            nStr += "\n"
            for j in range(len(i)):
                nStr += "----------------------"
            nStr += "\n"
        print (nStr)
        
        
        #grab the valid house number. Rejects non-ints
        flag = True
        while(flag):
            #choose house and decode number
            print
            choice = raw_input("Please enter the house number: ")
            try:
                choice = int(choice)
            except ValueError:
                print("That's not an int!")
                choice = 0
            if(choice <= 0 or choice >  game.height*game.width):
                print("Invalid house number. Enter an integer between 1-9.")
            else:
                flag = False
        
        
        #decode the house number into coordinates
        r = (choice - 1) / 3
        c = (choice - 1) % 3
        h = n.grid[r][c]
        
        #Show occupant info of the selected house
        mStr = "Occupants: "
        for monster in h.occupants:
            mStr += monster.name + ", "
        print (mStr)
        
        #attack all the monsters
        p.attackNPC(h)
        #defend from all the monsters
        p.defend(h)
        
        #show stats
        print("Your Health Points: " + str(p.hp))
        print("Number of Monsters left: " + str(n.numMonsters))
    
    
#call the main function
main()