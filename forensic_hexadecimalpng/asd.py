import os

with open("asdfg", "rb") as f:
    lines = f.readlines()
    for i, line in enumerate(lines[63:66]):
        print(63+i, line.hex())
    print()
    for i, line in enumerate(lines[98:101]):
        print(98+i, line.hex())
    for i, line in enumerate(lines[63:66]):
        print(63+i, line)
    print()
    for i, line in enumerate(lines[98:101]):
        print(98+i, line)
