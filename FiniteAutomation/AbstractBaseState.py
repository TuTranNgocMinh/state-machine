import abc
from abc import ABC, abstractmethod
class state(ABC):
    """abstract class state"""
    def __init__(self):
        return
    @abstractmethod
    def Output(self):
        """this is an abstract output"""
        pass
    @abstractmethod
    def setup(self):
        """this is an abstract setup"""
        pass
    @property
    @abstractmethod
    def name(self):
        pass
