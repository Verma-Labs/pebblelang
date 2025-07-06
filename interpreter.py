# interpreter.py

variables = {}

def resolve(value):
    # Try to interpret the value as an int, otherwise fetch from variables
    if value.isdigit() or (value[0] == '-' and value[1:].isdigit()):
        return int(value)
    elif value in variables:
        return variables[value]
    else:
        raise ValueError(f"'{value}' is not a number or a defined variable")

def interpret(command):
    cmd = command["command"]

    if cmd == "set":
        value = str(command["value"])
        variables[command["var"]] = resolve(value)

    elif cmd == "increase":
        var_name = command["var"]
        value = str(command["value"])

        if var_name in variables:
            variables[var_name] += resolve(value)
        else:
            raise ValueError(f"Variable '{var_name}' is not defined")

    elif cmd == "decrease":
        var_name = command["var"]
        value = str(command["value"])

        if var_name in variables:
            variables[var_name] -= resolve(value)
        else:
            raise ValueError(f"Variable '{var_name}' is not defined")

    elif cmd == "show":
        var_name = command["var"]
        if var_name in variables:
            print(variables[var_name])
        else:
            print(f"{var_name} is undefined")

    else:
        raise ValueError(f"Unknown command: {cmd}")
