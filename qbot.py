from random import random
import json
import math

class QBot(object):

    def __init__(self):
        self.count = 0
        self.tableLocation = "data/qvalues.json"
        self.learningRate = 0.7
        self.discountRate = 1.0
        self.loadQValues()
        self.initialState = "(0)(0)(0)"
        self.lastState = self.initialState
        self.lastAction = 0
        self.initStateIfNull(self.lastState)
        self.record = 0

    def loadQValues(self):
        self.QValues = {}
        try:
            with open(self.tableLocation, 'r') as j:
                x = json.load(j)
                self.count = x["i"]
                self.QValues = x["qv"]
                self.record = x["r"]
        except:
            return
    def reset(self):
        self.QValues = {}
        self.count = 0
        self.record = 0
        self.initStateIfNull(self.lastState)

    def addAgent(self, birb):
        self.birb = birb

    def initStateIfNull(self, state):
        if self.QValues.get(state) == None:
            self.QValues[state] = [0,0]

    def get_current_state(self):
        states = {
            ## v = birbs current velocity
            "v" : self.birb.vel,
            ## x = horizontal distance to next pipe
            "x" : math.floor((self.birb.nextPipe.x - self.birb.x) /3),
            ## y = vertical distance to bottom of next top pipe
            "y" : math.floor((self.birb.nextPipe.top_b_y - self.birb.y) /3)
        }
        x =  "({0})({1})({2})".format(states["v"], states["x"], states["y"])
        return x

    def saveQValues(self):
        with open(self.tableLocation, 'w') as out:
            json.dump({"qv" : self.QValues, "i" : self.count, "r" : self.record}, out)

    def rewardFunction(self, val):
        dtp_y = abs((self.birb.nextPipe.top_b_y + 200) - self.birb.y) / 100
        if val == True:
            ## dynamic reward, slightly higher value for being closer to middle of pipe Y 
            return (7 - dtp_y) / 7
        else:
            return -1000

    def reward(self):
        r = self.rewardFunction(self.birb.alive)

        self.initStateIfNull(self.get_current_state())

        self.QValues[self.lastState][self.lastAction] = (1-self.learningRate) * self.QValues[self.lastState][self.lastAction] + \
            self.learningRate * (r + self.discountRate * max(self.QValues[self.get_current_state()]))


    def action(self):
        action = 0
        if self.birb.nextPipe != None:
            state_t = self.get_current_state()
            
            self.initStateIfNull(state_t)
            
            action = 0 if self.QValues[state_t][0] >= self.QValues[state_t][1] else 1

            self.lastAction = action
            self.lastState = state_t

            
        return action






        