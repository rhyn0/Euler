import os,sys
from euler_funcs import *

functions = {"1": euler1, "2": euler2, "3": euler3, "4": euler4, "5": euler5, "6": euler6, "7": euler7,
    "8":euler8, "9":euler9, "10":euler10}
#https://projecteuler.net/


def main():
    for arg in sys.argv[1:]:
        print("Euler Problem " + str(arg) + "- Result: " + str(functions[arg]()))

if __name__ == "__main__":
    main()