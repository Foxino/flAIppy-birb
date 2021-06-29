from random import random
import json

class QBot(object):

    def __init__(self):
        self.count = 0
        self.learningRate = 0.7
        self.discountRate = 1.0
        self.loadQValues()
        self.moves = []
        self.initialState = "(0)(0)(0)"
        self.lastState = self.initialState
        self.lastAction = 0

    def loadQValues(self):
        self.QValues = {}
        try:
            j = open("data/qvalues.json", "r")
        except:
            return
        self.QValues = json.load(j)
        j.close()


    def addAgent(self, birb):
        self.birb = birb

    def get_current_state(self):
        states = {
            ## v = birbs current velocity
            "v" : self.birb.vel,
            ## x = horizontal distance to next pipe
            "x" : (self.birb.nextPipe.x - self.birb.x),
            ## y = vertical distance to bottom of next top pipe
            "y" : (self.birb.nextPipe.top_b_y - self.birb.y)
        }
        return "({0})({1})({2})".format(states["v"], states["x"], states["y"])

    def saveQValues(self):
        print(len(self.moves))


    def action(self):
        action = 0
        if self.birb.nextPipe != None and self.birb.alive == True:
            state_t = self.get_current_state()

            self.moves.append((self.lastState, self.lastAction, state_t))

            self.lastAction = action
            self.lastState = state_t

        return action






        