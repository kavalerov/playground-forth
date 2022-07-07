import sys
from typing import Optional, List

last: Optional[float] = None

ops = {
    "+": lambda p1, p2: p1 + p2,
    "-": lambda p1, p2: p1 - p2,
    "*": lambda p1, p2: p1 * p2,
    "/": lambda p1, p2: p1 / p2
}


def process_line(line: str):
    elems = line.split()
    stack: List[float] = []
    for el in elems:
        if el.isnumeric():
            stack.append(float(el))
        elif el in ops:
            if len(stack) >= 2:
                p2 = stack.pop()
                p1 = stack.pop()
                stack.append(ops[el](p1, p2))
            else:
                raise Exception("Not complete expression (not enough elements for operation)")
        else:
            raise Exception("Unsupported elements in the input")
    if len(stack) == 1:
        global last
        last = stack.pop()
        return last
    else:
        raise Exception("Expression cannot be evaluated (stack has > 1 elements at the end of evaluation)")


if __name__ == '__main__':
    while True:
        uinput = sys.stdin.readline()
        output = process_line(uinput)
        print(output)
