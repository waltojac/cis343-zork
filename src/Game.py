'''
Created on Mar 16, 2018

@author: jacobwalton
'''
from Objects import Neighborhood

class Game(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        n = Neighborhood(3,3)
        print("Grid: " + str(n.grid))
        print("Occupants[1][1]" + str(n.grid[1][1].occupants))
    
    
def main():
    ''' ''' 
    g = Game()

main()