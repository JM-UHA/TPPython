import sys


def main():
    args = sys.argv[1:]

    if len(args) >= 1:
        print(f"Les arguments sont :")
        for arg_pos, arg in enumerate(args, 1):
            print(f"\tArg. {arg_pos} => {arg}")
    else:
        print("Pas assez d'arguments pour le script 'argument.py'.")


if __name__ == "__main__":
    main()
