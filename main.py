import time
import os
from typing import List, Tuple

def turing_machine(script: str) -> Tuple[str, bool]:
    lines = [line.strip() for line in script.split("\n") if line.strip() and not line.startswith("#")]

    fita: List[str] = []
    initial_state: str = ""
    accept_state: str = ""
    transitions: List[Tuple[str, str, str, str, str]] = []

    for line in lines:
        if line.startswith("fita"):
            fita = list(line.split()[1])
        elif line.startswith("init"):
            initial_state = line.split()[1]
        elif line.startswith("accept"):
            accept_state = line.split()[1]
        elif line.startswith("#"): # Ignora comentários
            continue
        elif "," in line:
            transitions.append(tuple(line.split(",")))

    fita.insert(0, "_")
    fita.append("_")

    current_state = initial_state
    head_position = 1

    def show_tape():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Estado atual:", current_state)
        print("tape:", "".join(fita))
        print(" " * (head_position * 2 + 6) + "^ (Cabeça)")
        time.sleep(0.3)

    show_tape()

    while True:
        current_symbol = fita[head_position]
        transition_found = False

        for transition in transitions:
            state, simbolo, next_state, new_symbol, direction = transition
            if current_state == state and current_symbol == simbolo:
                if new_symbol != '':
                    fita[head_position] = new_symbol
                current_state = next_state
                head_position += 1 if direction == ">" else -1
                transition_found = True

                show_tape()
                break

        if not transition_found:
            break

    fita_final = "".join(fita).strip("_")
    input_accept = current_state == accept_state
    show_tape()
    print("\nExecução finalizada.")
    return fita_final, input_accept

if __name__ == "__main__":
    arquivo = open("palindromo.txt", "r")

    fita_final, input_accept = turing_machine(arquivo)
    print("Fita final:", fita_final)
    print("Cadeia aceita?", input_accept)
