from AbstractBaseMachine import Machine, state
from MealyState import *
class MealyMachine(Machine):
    def __init__(self, initState):
        super().__init__(initState)
        self._currentState=initState
        self._nextState=None
        return
    def transition(self, input: bool):
        """transition function for Moore Machine
           if(type(self._currentState)==state_a):
                if(input==True):
                    return state_a()
                if(input==False):
                    return state_b()
           if(type(self._currentState)==state_b):
                if(input==True):
                    return state_c()
                if(input==False):
                    return state_b()
           if(type(self._currentState)==state_c):
                if(input==True):
                    return state_c()
                if(input==False):
                    return state_a()
           """
        if(type(self._currentState)==state_a):
            if(input==True):
                self._nextState = state_a()
            if(input==False):
                self._nextState = state_b()
        if(type(self._currentState)==state_b):
            if(input==True):
                self._nextState = state_c()
            if(input==False):
                self._nextState = state_b()
        if(type(self._currentState)==state_c):
            if(input==True):
                self._nextState = state_c()
            if(input==False):
                self._nextState = state_a()
        return
    def getCurrentStateName(self):
        """get current state name"""
        return self._currentState.name
    def getOutput(self,input):
        """get output of next state"""
        return self._nextState.Output(input)
    def updateCurrentState(self):
        """update current state function"""
        self._currentState=self._nextState
        return
    @property
    def currentState(self):
        return self._currentState
    @property
    def nextState(self):
        return self._nextState