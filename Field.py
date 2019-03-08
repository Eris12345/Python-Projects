# -*- coding: utf-8 -*-

class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, d, loc):
        self.drunks[d] = loc
   
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            print('Drunk not in field')
        else:
            xDist, yDist = drunk.takeStep()
            currentLocation = self.drunks[drunk]
            #use move method of Location to get new location
            self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            print('Drunk not in field')
        else:
            return self.drunks[drunk]
