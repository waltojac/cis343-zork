'''
Created on Mar 16, 2018

@author: jacobwalton
'''
from Objects import Neighborhood, House
from Player import Player
from numpy import integer

class Game(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        n = Neighborhood(3,3)
        
        #print("Grid: " + str(n.grid))
        #print("Occupants[1][1]" + str(n.grid[1][1].occupants))
    
    
def main():
    ''' ''' 
    #g = Game()
    #display the neighborhood
    n = Neighborhood(3,3)
    p = Player()
    
    #instructions
    print("--- Welcome to the world of Zork ---")
    print
    print("You woke up from being chocolate wasted on your Halloween candy last")
    print("night only to find your entire neighborhood has turned into monsters,")
    print("except for those that were immune. Your task is to use the candy in your")
    print("bag to turn those monsters back into your friendly neighbors.")
    print
    print("Inventory: ")
    for wep in p.weapons:
        print("Name: " + str(wep.name) + "   \tUses: " + str(wep.uses))
    print
    print("Your Attack Strength: " + str(p.attack))
    print("Your Health Points: " + str(p.hp))
    print("Number of Monsters in the Neighborhood: " + str(n.numMonsters))
    print
    print("Go to each house in the neighborhood, and turn all the monsters back")
    print("into humans! Good luck!")
    
    
    while(True):
        print
        nStr = ""
        count = 1
        for i in n.grid:
            for h in i:
                nStr += "House " + str(count) +" (" + str(h.numMonsters) + " mon)\t |   "
                count += 1
            nStr += "\n------------------------------------------------------------------\n"
        print (nStr)
        
        flag = True
        while(flag):
            #choose house and decode number
            choice = raw_input("Please enter the house number: ")
            try:
                choice = int(choice)
            except ValueError:
                print("That's not an int!")
                choice = 0
            if(choice <= 0 or choice > 9 ):
                print("Invalid house number. Enter an integer between 1-9.")
            else:
                flag = False
        
        r = (choice - 1) / 3
        c = (choice - 1) % 3
        h = n.grid[r][c]
        
        #Show occupant info
        mStr = "Occupants: "
        for monster in h.occupants:
            mStr += monster.name + ", "
        print (mStr)
        
        p.attackNPC(h)
        p.defend(h)
        #print(str(p.weapons))
        print("Your Health Points: " + str(p.hp))
        print("Number of Monsters left: " + str(n.numMonsters))



    

main()