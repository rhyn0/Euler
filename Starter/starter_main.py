import sys
import starter_funcs as sf

functions = {
    "1": sf.euler1,
    "2": sf.euler2,
    "3": sf.euler3,
    "4": sf.euler4,
    "5": sf.euler5,
    "6": sf.euler6,
    "7": sf.euler7,
    "8": sf.euler8,
    "9": sf.euler9,
    "10": sf.euler10,
    "11": sf.euler11,
    "12": sf.euler12,
    "13": sf.euler13,
    "14": sf.euler14,
    "15": sf.euler15,
    "16": sf.euler16,
    "17": sf.euler17,
    "18": sf.euler18,
    "19": sf.euler19,
}
# https://projecteuler.net/


def main():
    for arg in sys.argv[1:]:
        print("Euler Problem " + str(arg) + "- Result: " + str(functions[arg]()))


if __name__ == "__main__":
    main()
