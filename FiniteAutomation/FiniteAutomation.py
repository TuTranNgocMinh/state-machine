
from MooreMachine import *
from MooreState import state_a
def FSM(input):
    print(Inputs)
    a=state_a()
    Mealy=MealyMachine(state_a())
    Mealy.transition(input[0])
    Mealy.getOutput(input[0])
    for i in range(1,len(input)):
        Mealy.updateCurrentState()
        Mealy.transition(input[i])
        Mealy.getOutput(input[i])
    return
def FSM_Moore(input):
    print(Inputs)
    a=state_a()
    Moore=MooreMachine(state_a())
    Moore.transition(input[0])
    Moore.getOutput()
    for i in range(1,len(input)):
        Moore.updateCurrentState()
        Moore.transition(input[i])
        Moore.getOutput()
    return
Inputs=("1 0 0 1 0 1")
Inputs=Inputs.split(" ")
Inputs=[bool(int(i)) for i in Inputs]
FSM_Moore(Inputs)
