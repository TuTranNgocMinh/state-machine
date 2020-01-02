from AbstractBaseState import state

class state_a(state):
    def __init__(self):
        super().__init__()
        self._name=1
    @property
    def name(self):
        return self._name
    def Output(self,input):
        if(input==True):
            print("a1")
        else:
            print("a2")
    def setup(self):
        pass
class state_b(state):
    def __init__(self):
        super().__init__()
        self._name=2
    @property
    def name(self):
        return self._name
    def Output(self,input):
        print("b")
    def setup(self):
        pass
class state_c(state):
    def __init__(self):
        super().__init__()
        self._name=3
    @property
    def name(self):
        return self._name
    def Output(self,input):
        print("c")
    def setup(self):
        pass
