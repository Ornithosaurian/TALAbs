R = 1
L = -1
S = 0

CHANGE_TO = 0
MOVE_TO = 1
NEXT_STATE = 2


def turing_machine(program, tape, start_state, current_cell):
    current_state = start_state

    while (True):
        rows = program[current_state]
        current_row = rows[int(tape[current_cell])]
        tape[current_cell] = current_row[CHANGE_TO]
        if not current_row[MOVE_TO]:
            break
        current_cell += current_row[MOVE_TO]
        current_state = current_row[NEXT_STATE]
    return tape
