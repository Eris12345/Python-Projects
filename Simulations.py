# -*- coding: utf-8 -*-

from Location import Location
from Drunk import *
from Field import Field
from RandomWalk import drunkTest, simWalks

import matplotlib.pyplot as plt
import random

def simAll(drunkKinds, walkLengths, numTrials):
    for dClass in drunkKinds:
        drunkTest(walkLengths, numTrials, dClass)


random.seed(0)
simAll((UsualDrunk, ColdDrunk, EWDrunk),
       (1000, 10000), 100)

#########################################################

class styleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles

    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result

def simDrunk(numTrials, dClass, walkLengths):
    meanDistances = []
    for numSteps in walkLengths:
        print('Starting simulation of', numSteps, 'steps')
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials)/len(trials)
        meanDistances.append(mean)
    return meanDistances

def simAll1(drunkKinds, walkLengths, numTrials):
    styleChoice = styleIterator(('m-', 'r:', 'k-.'))
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
        print('Starting simulation of', dClass.__name__)
        means = simDrunk(numTrials, dClass, walkLengths)
        plt.plot(walkLengths, means, curStyle,
                   label = dClass.__name__)
    plt.title('Mean Distance from Origin ('
                + str(numTrials) + ' trials)')
    plt.xlabel('Number of Steps')
    plt.ylabel('Distance from Origin')
    plt.legend(loc = 'best')
    plt.semilogx()
    plt.semilogy()

simAll1((UsualDrunk, ColdDrunk, EWDrunk),
        (10,100,1000,10000), 100)
#       (10,100,1000,10000,100000), 100)
 

#########################################################


def getFinalLocs(numSteps, numTrials, dClass):
    locs = []
    d = dClass()
    for t in range(numTrials):
        f = Field()
        f.addDrunk(d, Location(0, 0))
        for s in range(numSteps):
            f.moveDrunk(d)
        locs.append(f.getLoc(d))
    return locs

def plotLocs(drunkKinds, numSteps, numTrials):
    styleChoice = styleIterator(('k+', 'r^', 'mo'))
    for dClass in drunkKinds:
        locs = getFinalLocs(numSteps, numTrials, dClass)
        xVals, yVals = [], []
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
        meanX = sum(xVals)/len(xVals)
        meanY = sum(yVals)/len(yVals)
        curStyle = styleChoice.nextStyle()
        plt.plot(xVals, yVals, curStyle,
                      label = dClass.__name__ + ' mean loc. = <'
                      + str(meanX) + ', ' + str(meanY) + '>')
    plt.title('Location at End of Walks ('
                + str(numSteps) + ' steps)')
    plt.xlabel('Steps East/West of Origin')
    plt.ylabel('Steps North/South of Origin')
    # plt.legend(loc = 'lower left')
    plt.legend(loc = 'center')

plotLocs((UsualDrunk, ColdDrunk, EWDrunk), 100, 200)
plt.clf()
plotLocs((UsualDrunk, ColdDrunk), 10000, 200)


#########################################################


def traceWalk(drunkKinds, numSteps):
    styleChoice = styleIterator(('k+', 'r^', 'mo'))
    f = Field()
    for dClass in drunkKinds:
        d = dClass()
        f.addDrunk(d, Location(0, 0))
        locs = []
        for s in range(numSteps):
            f.moveDrunk(d)
            locs.append(f.getLoc(d))
        xVals, yVals = [], []
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
        curStyle = styleChoice.nextStyle()
        plt.plot(xVals, yVals, curStyle,
                   label = dClass.__name__)
    plt.title('Spots Visited on Walk ('
                + str(numSteps) + ' steps)')
    plt.xlabel('Steps East/West of Origin')
    plt.ylabel('Steps North/South of Origin')
    plt.legend(loc = 'best')

traceWalk((UsualDrunk, ColdDrunk, EWDrunk), 200)


