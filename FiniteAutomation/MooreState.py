from AbstractBaseState import state

class state_a(state):
    def __init__(self):
        super().__init__()
        self._name=1
    @property
    def name(self):
        return self._name
    def Output(self):
        print("a")
    def setup(self):
        pass
class state_b(state):
    def __init__(self):
        super().__init__()
        self._name=2
    @property
    def name(self):
        return self._name
    def Output(self):
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
    def Output(self):
        print("c")
    def setup(self):
        pass
class test_state(state):
    def __init__(self):
        super().__init__()
        self._name=10
    @property
    def name(self):
        return self._name
    def Output(self):
        print("c")
    def setup(self):
        print("setup")