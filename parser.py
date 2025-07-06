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

    raise ValueError(f"Invalid syntax: {line}")
