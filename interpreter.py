# interpreter.py

variables = {}

def resolve(value):
    if value.isdigit() or (value.startswith("-") and value[1:].isdigit()):
        return int(value)
    elif value in variables:
        return variables[value]
    else:
        raise ValueError(f"'{value}' is not a number or defined variable")


def evaluate_condition(left, op, right):
    a = resolve(left)
    b = resolve(right)

    if op == "is greater than":
        return a > b
    if op == "is less than":
        return a < b
    if op == "equals":
        return a == b
    raise ValueError(f"Unsupported condition: {op}")


def interpret(command):
    cmd = command["command"]

    if cmd == "set":
        variables[command["var"]] = resolve(command["value"])

    elif cmd == "increase":
        variables[command["var"]] += resolve(command["value"])

    elif cmd == "decrease":
        variables[command["var"]] -= resolve(command["value"])

    elif cmd == "show":
        print(variables.get(command["var"], f"{command['var']} is undefined"))

    elif cmd == "if":
        if evaluate_condition(command["left"], command["op"], command["right"]):
            for stmt in command["body"]:
                interpret(stmt)

    elif cmd == "repeat":
        for _ in range(command["times"]):
            for stmt in command["body"]:
                interpret(stmt)
