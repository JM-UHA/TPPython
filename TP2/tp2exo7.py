from random import randint

lance = randint(0, 100)

if lance < (100 * 2/3):
    print("C'est pile !")
else:
    print("C'est face !")
