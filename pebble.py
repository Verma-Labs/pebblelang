from parser import parse_line
from interpreter import interpret
import sys

def run_script(filename):
    with open(filename) as f:
        for line_number, line in enumerate(f, 1):
            try:
                parsed = parse_line(line)
                if parsed:
                    interpret(parsed)
            except Exception as e:
                print(f"[Line {line_number}] Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pebble.py script.peb")
    else:
        run_script(sys.argv[1])
