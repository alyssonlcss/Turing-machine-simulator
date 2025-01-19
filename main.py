import time
import os
from typing import List, Tuple

def turing_machine(script: str) -> Tuple[str, bool]:
    lines = [line.strip() for line in script.split("\n") if line.strip() and not line.startswith("#")]

    
    tape: List[str] = []
    initial_state: str = ""
    accept_state: str = ""
    transitions: List[Tuple[str, str, str, str, str]] = []

    for line in lines:
        if line.startswith("tape"):
            tape = list(line.split()[1])
        elif line.startswith("init"):
            initial_state = line.split()[1]
        elif line.startswith("accept"):
            accept_state = line.split()[1]
        elif "," in line:
            transitions.append(tuple(line.split(",")))

    tape.insert(0, "_")
    tape.append("_")

    current_state = initial_state
    head_position = 1

    def show_tape():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Estado atual:", current_state)
        print("tape:", "".join(tape))
        print(" " * (head_position * 2 + 6) + "^ (Cabeça)")
        time.sleep(0.3)

    show_tape()

    while True:
        current_symbol = tape[head_position]
        transition_found = False

        for transition in transitions:
            state, simbolo, next_state, new_symbol, direction = transition
            if current_state == state and current_symbol == simbolo:
                if new_symbol != '':
                    tape[head_position] = new_symbol
                current_state = next_state
                head_position += 1 if direction == ">" else -1
                transition_found = True

                show_tape()
                break

        if not transition_found:
            break

    tape_final = "".join(tape).strip("_")
    input_accept = current_state == accept_state
    show_tape()
    print("\nExecução finalizada.")
    return tape_final, input_accept


script = """
@Programa Fonte UFC
tape 101
init q0
accept qf
reject qr

q0,1,q1,_,>
q0,0,q2,_,>
q0,_,qf,_,>
q1,1,q1,1,>
q1,0,q1,0,>
q1,_,q3,_,<
q2,1,q2,1,>
q2,0,q2,0,>
q2,_,q4,_,<
q3,1,q0,_,<
q3,_,qf,_,>
q3,0,qr,_,>
q4,0,q0,_,<
q4,_,qf,_,>
q4,1,qr,_,>
"""

tape_final, input_accept = turing_machine(script)
print("Fita final:", tape_final)
print("Cadeia aceita?", input_accept)
