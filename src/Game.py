'''
Created on Mar 16, 2018

@author: jacobwalton
'''
from Objects import Neighborhood, House
from Player import Player

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
    p = Player()
    h = House()
    
    print(str(h.occupants))
    p.attackNPC(h)
    #print(str(p.weapons))

    

main()