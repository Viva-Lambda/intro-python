"""
Solution to Exercice 04
"""
# License: see, LICENSE

import os


if __name__ == "__main__":
    asset_path = os.path.join("assets", "ex04.txt")
    with open(asset_path, "r", encoding="utf-8", newline="\n") as fd:
        satirlar = fd.readlines()
        kontrol = False
        for satir in satirlar:
            if not kontrol:
                kontrol = True
                print(satir)
            else:
                kontrol = False
