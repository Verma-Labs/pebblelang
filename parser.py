# parser.py

def parse_line(line):
    line = line.strip()

    if not line or line.startswith("comment:"):
        return None

    tokens = line.split()

    if tokens[0] == "set" and tokens[2] == "to":
        return {"command": "set", "var": tokens[1], "value": tokens[3]}

    if tokens[0] == "increase" and tokens[2] == "by":
        return {"command": "increase", "var": tokens[1], "value": tokens[3]}

    if tokens[0] == "decrease" and tokens[2] == "by":
        return {"command": "decrease", "var": tokens[1], "value": tokens[3]}

    if tokens[0] == "show":
        return {"command": "show", "var": tokens[1]}

    if tokens[0] == "if" and "then" in tokens:
        var1 = tokens[1]
        condition = " ".join(tokens[2:5])
        var2 = tokens[5]
        return {
            "command": "if",
            "left": var1,
            "op": condition,
            "right": var2,
            "body": []
        }

    if tokens[0] == "repeat" and tokens[2] == "times:":
        return {
            "command": "repeat",
            "times": int(tokens[1]),
            "body": []
        }

    if tokens[0] == "end":
        return {"command": "end"}

    raise ValueError(f"Invalid syntax: {line}")


def parse_script(lines):
    program = []
    stack = []

    for line in lines:
        parsed = parse_line(line)
        if parsed is None:
            continue

        if parsed["command"] in ("repeat", "if"):
            stack.append(parsed)
        elif parsed["command"] == "end":
            completed = stack.pop()
            if stack:
                stack[-1]["body"].append(completed)
            else:
                program.append(completed)
        else:
            if stack:
                stack[-1]["body"].append(parsed)
            else:
                program.append(parsed)

    if stack:
        raise ValueError("Missing 'end' for block")

    return program
