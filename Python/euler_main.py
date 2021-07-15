import os, sys
import euler_funcs as eu

functions = {
    "1": eu.euler1,
    "2": eu.euler2,
    "3": eu.euler3,
    "4": eu.euler4,
    "5": eu.euler5,
    "6": eu.euler6,
    "7": eu.euler7,
    "8": eu.euler8,
    "9": eu.euler9,
    "10": eu.euler10,
    "11": eu.euler11,
    "12": eu.euler12,
    "13": eu.euler13,
    "14": eu.euler14,
    "15": eu.euler15,
    "16": eu.euler16,
    "17": eu.euler17,
    "18": eu.euler18,
    "19": eu.euler19,
    "20": eu.euler20,
    "21": eu.euler21,
    "22": eu.euler22,
    "23": eu.euler23,
    "24": eu.euler24,
}
# https://projecteuler.net/


def main():
    for arg in sys.argv[1:]:
        print("Euler Problem " + str(arg) + "- Result: " + str(functions[arg]()))


if __name__ == "__main__":
    main()
