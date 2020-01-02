import abc
from abc import ABC, abstractmethod

from AbstractBaseState import state
class Machine(ABC):
    def __init__(self,initState: state):
        """initialize function"""
        return
    @abstractmethod
    def transition(self,input: bool):
        """this is an abstract function of the transition function"""
        pass
    @abstractmethod
    def getOutput(self):
        """this is an abstract function of the Get output function. 
           for Moore machine, this function returns the output of the current state
           example: self._currentState.Output()

           for Mealy machine, this function returns the output of the next state
           example: self._nextState.Output()"""
        pass
    @abstractmethod
    def getCurrentStateName(self):
        """get current state name"""
        pass
    @abstractmethod
    def updateCurrentState(self):
        pass
    @property
    @abstractmethod
    def currentState(self):
        ...

    @property
    @abstractmethod
    def nextState(self):
        ...


    