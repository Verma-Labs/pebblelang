# pebble.py

from parser import parse_script
from interpreter import interpret
import sys

def run_script(filename):
    with open(filename) as f:
        lines = f.readlines()
        try:
            program = parse_script(lines)
            for cmd in program:
                interpret(cmd)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pebble.py filename.peb")
    else:
        run_script(sys.argv[1])
