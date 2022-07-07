import sys


def process_line(line: str):
    return "You said: " + line


if __name__ == '__main__':
    while True:
        uinput = sys.stdin.readline()
        output = process_line(uinput)
        print(output)
