import solver as solver
import TuringMachine as TM

x = int(input("Input x= "))
y = int(input("Input y= "))
f = 0
bin = solver.solver(x, y, f)  # отримаємо бінарний стрінг після виконання рівняння

R = 1
L = -1
S = 0

CHANGE_TO = 0
MOVE_TO = 1
NEXT_STATE = 2

output = TM.turing_machine({
    "A": ((0, R, "A"), (1, R, "B")),  # ліво 0, право 1
    "B": ((1, S, "C"), (1, R, "B")),
    "C": ((0, S, "C"), (1, S, "C"))},
    list(bin),  # input
    "A",  # first one
    0)  # first element

print("Input:", bin)
print("Output:", output)
