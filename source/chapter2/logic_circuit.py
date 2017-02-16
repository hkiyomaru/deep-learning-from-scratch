"""Implementation of Logic Circuits."""
import numpy as np


def AND(x1, x2):
    """Calculate AND."""
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp < 0:
        return 0
    else:
        return 1


def NAND(x1, x2):
    """Calculate NAND."""
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.9
    tmp = np.sum(w * x) + b
    if tmp < 0:
        return 0
    else:
        return 1


def OR(x1, x2):
    """Calculate OR."""
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp < 0:
        return 0
    else:
        return 1


def XOR(x1, x2):
    """Calculate XOR."""
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


def main():
    """Entry point."""
    print("AND TEST")
    print("# (0, 0): {}".format(AND(0, 0)))
    print("# (0, 1): {}".format(AND(0, 1)))
    print("# (1, 0): {}".format(AND(1, 0)))
    print("# (1, 1): {}".format(AND(1, 1)))
    print("NAND TEST")
    print("# (0, 0): {}".format(NAND(0, 0)))
    print("# (0, 1): {}".format(NAND(0, 1)))
    print("# (1, 0): {}".format(NAND(1, 0)))
    print("# (1, 1): {}".format(NAND(1, 1)))
    print("OR TEST")
    print("# (0, 0): {}".format(OR(0, 0)))
    print("# (0, 1): {}".format(OR(0, 1)))
    print("# (1, 0): {}".format(OR(1, 0)))
    print("# (1, 1): {}".format(OR(1, 1)))
    print("XOR TEST")
    print("# (0, 0): {}".format(XOR(0, 0)))
    print("# (0, 1): {}".format(XOR(0, 1)))
    print("# (1, 0): {}".format(XOR(1, 0)))
    print("# (1, 1): {}".format(XOR(1, 1)))


if __name__ == '__main__':
    main()
