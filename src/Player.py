'''
Created on Mar 16, 2018

@author: jacobwalton
'''
from random import randint, choice
from Objects import HersheyKiss, SourStraw, ChocolateBar, NerdBomb

class Player(object):
    '''
    classdocs
    '''

    def __init__(self):
        self.attack = randint(10,20)
        self.hp = randint(100,125)
        self.weapons = [HersheyKiss]
        weaponChoices = [SourStraw, ChocolateBar, NerdBomb]
        for i in range(9):
            self.weapons.append(choice(weaponChoices))
        