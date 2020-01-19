"""
Solution to Exercice 05
"""
# License: see, LICENSE

import os
import sys

if __name__ == "__main__":
    MA_LISTE = [1, 3, 1, 1, 6, 31, 5, 8, 20, 6, 9, 2, 3]
    # 1
    print("ilk yontem:\n")
    pairs = filter(lambda x: x % 2 == 0, MA_LISTE)
    list(map(lambda x: print(str(x)), pairs))
    print("")

    # 2
    print("ikinci yontem:\n")
    list(map(lambda x: print(str(x)) if ((x % 2) == 0) else x, MA_LISTE))
    print("")

    # 3
    print("ucuncu yontem:\n")
    for x in MA_LISTE:
        residu = x % 2
        if residu == 0:
            print(x)
    #
    print("")
    print("Bitti")
