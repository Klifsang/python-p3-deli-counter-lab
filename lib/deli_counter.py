# deli_counter.py

def line(deli):
    if not deli:
        print("The line is currently empty.")
    else:
        line_str = "The line is currently:"
        for i, person in enumerate(deli, start=1):
            line_str += f" {i}. {person}"
        print(line_str)

def take_a_number(deli, name):
    deli.append(name)
    print(f"Welcome, {name}. You are number {len(deli)} in line.")

def now_serving(deli):
    if not deli:
        print("There is nobody waiting to be served!")
    else:
        serving = deli.pop(0)
        print(f"Currently serving {serving}.")
