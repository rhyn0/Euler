import os, sys
from euler_funcs import *

functions = {
    "1": euler1,
    "2": euler2,
    "3": euler3,
    "4": euler4,
    "5": euler5,
    "6": euler6,
    "7": euler7,
    "8": euler8,
    "9": euler9,
    "10": euler10,
    "11": euler11,
    "12": euler12,
    "13": euler13,
    "14": euler14,
    "15": euler15,
    "16": euler16,
    "17": euler17,
    "18": euler18,
    "19":euler19,
}
# https://projecteuler.net/


def main():
    for arg in sys.argv[1:]:
        print("Euler Problem " + str(arg) + "- Result: " + str(functions[arg]()))


if __name__ == "__main__":
    main()
